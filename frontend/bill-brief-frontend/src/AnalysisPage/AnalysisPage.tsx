import React from "react";
import SummarySection from "./AnalysisPageComponents/SummarySection";
import BillTable from "./AnalysisPageComponents/BillTable";
import { useLocation } from "react-router";


type llm_response = {
  paper_title: string,
  summary: string,
  benefits: string,
  concerns: string
}

const mock_response : llm_response = {
    "paper_title": "Paper Title",
    "summary" : "This is the default summary",
    "benefits": "This is the default main benefits",
    "concerns": "This is the default main concerns",
}

export default function AnalysisPage() {

  const location = useLocation();
  const response = location.state?.data;

  console.log("Recieved a response from the other page", response)

  if (response===undefined) {     
    return  <div className="bg-[#f8f9fa] h-screen">
    <div className="flex">
      <div className="flex-1 p-8">
      <SummarySection summary_text={mock_response} />
      <BillTable response={mock_response} />
      </div>
    </div>
  </div>

  }

    return (
      <div className="bg-[#f8f9fa] h-screen">
        <div className="flex">
          <div className="flex-1 p-8">
          <SummarySection response={response} />
          <BillTable response={response} />
          </div>
        </div>
      </div>
);
  }

