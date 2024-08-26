from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader  # Updated import
import torch
import shutil
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up Hugging Face token as an environment variable
os.environ["HUGGINGFACE_TOKEN"] = "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"
huggingface_token = os.environ["HUGGINGFACE_TOKEN"]

# Load tokenizer and model with the new `token` argument
checkpoint = "MBZUAI/LaMini-Flan-T5-248M"
tokenizer = T5Tokenizer.from_pretrained(checkpoint, token=huggingface_token, legacy=False)
base_model = T5ForConditionalGeneration.from_pretrained(checkpoint, token=huggingface_token, device_map='auto', torch_dtype=torch.float32)

# File upload directory
UPLOAD_DIR = "uploaded_files/"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Function to preprocess and summarize text
def file_preprocessing(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    texts = text_splitter.split_documents(pages)

    final_texts = ""
    for text in texts:
        final_texts += text.page_content
    return final_texts

def llm_pipeline(input_text):
    pipe_sum = pipeline(
        'summarization',
        model=base_model,
        tokenizer=tokenizer,
        max_length=500,
        min_length=50,
        clean_up_tokenization_spaces=False  # This line prevents the deprecation warning
    )
    result = pipe_sum(input_text)
    result = result[0]['summary_text']
    return result

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)

    input_text = file_preprocessing(file_location)
    summary = llm_pipeline(input_text)
    return {"summary": summary}
