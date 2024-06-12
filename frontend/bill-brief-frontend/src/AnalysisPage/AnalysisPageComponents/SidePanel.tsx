import React from "react";

interface SidePanelProps {
    paper_title: string;
  }

export default function SidePanel({ paper_title }: SidePanelProps) {
    return (
        <div className="bg-[#ffffff] w-[250px] h-screen border-r-[1px] border-[#e0e0e0]">
            <div className="p-4">
                <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md w-full border-[1px] border-[#007bff]">+ New Bill</button>
            </div>
            <div className="p-4">
                <h2 className="text-[#6c757d] text-sm mb-2">Library</h2>
                <ul>
                    <li className="text-[#007bff] text-sm mb-2">{paper_title}</li>
                </ul>
            </div>
            <div className="absolute bottom-0 p-4 w-full">
            <div className="flex items-center mb-4">
                <div className="bg-[#e9ecef] rounded-full w-8 h-8 flex items-center justify-center mr-2">
                <i className="fas fa-question text-[#6c757d]"></i>
                </div>
                <span className="text-[#6c757d] text-sm">Help and guides</span>
            </div>
            <div className="flex items-center mb-4">
                <div className="bg-[#e9ecef] rounded-full w-8 h-8 flex items-center justify-center mr-2">
                <i className="fas fa-envelope text-[#6c757d]"></i>
                </div>
                <span className="text-[#6c757d] text-sm">Contact Us</span>
            </div>
            <div className="flex items-center mb-4">
                <div className="bg-[#e9ecef] rounded-full w-8 h-8 flex items-center justify-center mr-2">
                <i className="fas fa-user text-[#6c757d]"></i>
                </div>
                <span className="text-[#6c757d] text-sm">parthitm...@gmail.com</span>
            </div>
            </div>
      </div>
    )
}