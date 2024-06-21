import React from "react";

export default function SummarySection({response}: any) {
    return (
        <>
            <div className="flex justify-between items-center mb-4">
                <h1 className="text-[#343a40] text-2xl font-semibold">{response.paper_title} Analysed</h1>
                <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md border-[1px] border-[#007bff]">+ New Bill</button>
            </div><div className="bg-[#ffffff] p-6 rounded-md shadow-sm border-[1px] border-[#e0e0e0]">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-[#343a40] text-xl font-semibold">Summary of the Bill</h2>
                    </div>
                    <p className="text-[#6c757d] text-sm mb-4">
                        {response.summary}
                    </p>
                    <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md border-[1px] border-[#007bff]">Copy</button>
                </div>
        </>
    )
}