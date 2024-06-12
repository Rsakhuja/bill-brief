import React from "react";

export default function BillTable({mock_response}: any) {
    return (
        <div className="mt-4">
          <table className="w-full bg-[#ffffff] border-[1px] border-[#e0e0e0] rounded-md">
            <thead>
              <tr className="bg-[#f8f9fa]">
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Paper</th>
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Summary</th>
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Main findings</th>
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Benefits</th>
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Concerns</th>
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Ammendments</th>
                <th className="text-left text-[#6c757d] text-sm py-2 px-4">Outcome for the people</th>
                
                
              </tr>
            </thead>
            <tbody>
              <tr className="border-t-[1px] border-[#e0e0e0]">
                <td className="text-left text-[#343a40] text-sm py-2 px-4">
                  <input type="checkbox" className="mr-2" />
                  <span>{mock_response.paper_title}</span>
                  <div className="text-[#6c757d] text-xs">{mock_response.paper_title}</div>
                </td>
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{mock_response.summary}</td>
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{mock_response.main_findings}</td> 
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{mock_response.benefits}</td>
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{mock_response.concerns}</td>              
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{mock_response.amendments}</td>             
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{mock_response.outcome_for_people}</td>              
                </tr>
            </tbody>
          </table>
        </div>
    )
}