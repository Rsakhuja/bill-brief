import React, {useState} from "react";

export default function UploadPDFCard() {

    const [loading, setLoading] = useState(true);
    
    const [dragging, setDragging] = useState(false);
    const [fileUploaded, setFileUploaded] = useState(false);
    const [fileName, setFileName] = useState(null);

    const handleDragEnter = (e) => {
      e.preventDefault();
      e.stopPropagation();
      setDragging(true);
    };
  
    const handleDragLeave = (e) => {
      e.preventDefault();
      e.stopPropagation();
      setDragging(false);
    };
  
    const handleDragOver = (e) => {
      e.preventDefault();
      e.stopPropagation();
    };

    const handleBrowseClick = (e) => {
        // Programmatically trigger the file input click
        const fileInput = document.getElementById('fileInput');
        if (fileInput) {
          fileInput.click();
        }
      };

    const handleFileInputChange = (e) => {
        const files = e.target.files;
        console.log(files); // This logs an array of File objects
        setFileUploaded(true);
        Array.from(files).forEach(file => {
          console.log('Uploaded file:', file.name);
          setFileName(file.name);
        });
      };
  
    const handleDrop = (e) => {
      e.preventDefault();
      e.stopPropagation();
      setDragging(false);
  
      const files = [...e.dataTransfer.files];
      console.log(files); // This logs an array of File objects
  
      // You can access the file details like name, type, etc.
      files.forEach(file => {
        console.log('Uploaded file:', file.name);
        const fileName = file.name;
        setFileUploaded(true);
        setFileName(fileName);
      });
    };

    return (
        <div className="flex items-center justify-center min-h-screen bg-[#f8f9fa]">
            <div className=" min-h-screen p-8 w-1/2">
                <h2 className="text-[#6c757d] text-lg mb-4">Select a bill to analyse</h2>
                <div className="bg-white rounded-[12px] shadow-md p-6">
                <div className="bg-[#f8f9fa] rounded-[12px] p-4 mb-4">
                    <div className="flex items-center mb-4">
                    <i className="fas fa-upload text-[#6c757d] mr-2"></i>
                    <span className="text-[#6c757d]">Extract data from PDF</span>
                    </div>
                    {
                    fileUploaded ?
                     <>
                        <h3>File {fileName} recieved</h3>
                     </> : <>
                        <h3 className="text-[#6c757d] text-lg mb-4">Upload legislative document</h3>
                        <div className="border-dashed border-2 border-[#6c757d] rounded-[12px] p-10 text-center m-8"       
                            onDragEnter={handleDragEnter}
                            onDragOver={handleDragOver}
                            onDragLeave={handleDragLeave}
                            onDrop={handleDrop}
                            onClick={handleBrowseClick}
                            >
                            <i className="fas fa-cloud-upload-alt text-[#6c757d] text-4xl mb-4"></i>
                            <p className="text-[#6c757d]">Drag and drop PDFs<br />Or click to browse files</p>
                            
                        </div>
                        <input id="fileInput" type="file" accept=".pdf" className="hidden" onChange={handleFileInputChange} />
                        </>
                    }
                    
                </div>
                <button       
                className={`py-2 px-4 rounded-[8px] ${fileUploaded ? 'bg-[#92de95] hover:bg-[#89c98b] cursor-pointer' : 'bg-[#adb5bd] opacity-40 cursor-not-allowed'}`}
                disabled={!fileUploaded}>
                    Analyse Bill</button>
                <div className="flex items-center">
                    <i className="fas fa-list text-[#6c757d] mr-2"></i>
                </div>
                </div>
                <button className="bg-[#6c757d] text-white p-4 rounded-full fixed bottom-8 right-8">
                <i className="fas fa-arrow-right"></i>
                </button>
            
            </div>
        </div>
);
  }