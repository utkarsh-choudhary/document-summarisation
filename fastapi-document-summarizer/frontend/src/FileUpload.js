// src/FileUpload.js
import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a file first.");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/upload/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setSummary(response.data.summary);
    } catch (error) {
      console.error("Error uploading file:", error.response ? error.response.data : error.message);
      alert("An error occurred while uploading the file. Check console for details.");
    }
  };

  return (
    <div className="relative min-h-screen">
  <img
    src="https://images.pexels.com/photos/261763/pexels-photo-261763.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"
    alt="Background"
    className="absolute top-0 left-0 w-full h-full object-cover -z-10"
  />
  <div className="relative z-10">
    <h1 className="text-3xl text-gray-700 text-center leading-10 font-semibold py-2">
      Upload PDF and Get <span className='className="text-5xl font-bold text-cyan-500"'> Summary</span> 
    </h1>
    <div className="flex justify-center">
  <input 
    type="file" 
    accept=".pdf" 
    onChange={handleFileChange} 
    className="block w-full md:w-[650px] rounded-md border 
               p-2 text-sm shadow-lg font-medium text-gray-700
               focus:border-gray-500 focus:outline-none focus:ring-0" 
  />
</div>
    <div className="flex justify-center">
  <button 
    className="mt-5 bg-blue-700 px-5 text-white text-2xl font-semibold cursor-pointer rounded-lg
               hover:bg-blue-400"
    onClick={handleUpload}
  >
    Upload
  </button>
</div>
    <div className="flex flex-col items-center mt-8">
  <h2 className="text-3xl font-bold mb-4 text-gray-700">Summary:</h2>
  <div className="w-full max-w-[800px] bg-gray-100 bg-opacity-50 p-4 rounded-lg shadow-lg overflow-auto">
    <p className="text-lg leading-relaxed text-black break-words">
      {summary}
    </p>
  </div>
</div>

</div>

  </div>


  ); 
};

export default FileUpload;
