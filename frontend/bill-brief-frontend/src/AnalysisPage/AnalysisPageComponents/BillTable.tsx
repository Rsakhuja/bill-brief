import React from "react";

export default function BillTable({response}: any) {
    return (
        <><div className="flex justify-between items-center mt-4">
            <div className="bg-[#308a22] text-white py-2 px-4 rounded-md">Bill addresses your needs</div>
            <div className="flex items-center">
                <button className="bg-[#f8f9fa] text-[#343a40] py-2 px-4 rounded-md border-[1px] border-[#e0e0e0] mr-2">Filters</button>
            </div>
        </div><div className="mt-4">
                <table className="w-full bg-[#ffffff] border-[1px] border-[#e0e0e0] rounded-md">
                    <thead>
                        <tr className="bg-[#f8f9fa]">
                            <th className="text-left text-[#6c757d] text-sm py-2 px-4">Paper</th>
                            <th className="text-left text-[#6c757d] text-sm py-2 px-4">Main findings</th>
                            <th className="text-left text-[#6c757d] text-sm py-2 px-4">Benefits</th>
                            <th className="text-left text-[#6c757d] text-sm py-2 px-4">Concerns</th>


                        </tr>
                    </thead>
                    <tbody>
                        <tr className="border-t-[1px] border-[#e0e0e0]">
                            <td className="text-left content-start text-[#343a40] text-sm py-2 px-4">
                                <input type="checkbox" className="mr-2" />
                                <span>{response.paper_title}</span>
                                <div className="text-[#6c757d] text-xs">{response.paper_title}</div>
                            </td>
                            <td className="text-left content-start text-[#343a40] text-sm py-2 px-4">{response.main_findings}</td>
                            <td className="text-left content-start text-[#343a40] text-sm py-2 px-4">{response.benefits}</td>
                            <td className="text-left content-start text-[#343a40] text-sm py-2 px-4">{response.concerns}</td>
                        </tr>
                    </tbody>
                </table>
            </div></>
    )
}