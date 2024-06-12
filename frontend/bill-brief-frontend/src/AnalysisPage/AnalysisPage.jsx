import React from "react";


const OpenAIResponse = {
    "paper_title": "Paper Title",
    "summary" : "Cardiomyocytes, the cells responsible for the contraction of the heart, are central to the understanding of various heart conditions. Zamecznik (2014) highlights the case of a 14-year-old boy with restrictive cardiomyopathy, a rare form of the disease characterized by diastolic dysfunction. This case underscores the importance of early diagnosis and treatment, as the condition can be fatal. Emanuel (1972) discusses the association of cardiomyopathy with heredofamilial neuromyopathic disorders, such as Friedreich's disease. Yanjari (2018) provides a comprehensive overview of the symptoms and clinical features of cardiomyopathy in adults, emphasizing the need for early recognition and management. Ижкина (2012) categorizes nonischemic cardiomyopathy into four main types, including dilated, hypertrophic, restrictive, and arrhythmogenic right ventricular, and underscores the high mortality rates in pediatric cases. These studies collectively underscore the importance of understanding and addressing cardiomyocyte-related conditions.",
    "main_findings": "Restrictive cardiomyopathy (RCM) is a rare type of cardiomyopathy, constituting only 2-5% of all cases. Pharmacotherapy helped stabilize the patient's condition, leading to a heart transplantation six months after diagnosis.",
    "benefits": "Restrictive cardiomyopathy (RCM) is a rare type of cardiomyopathy, constituting only 2-5% of all cases. Pharmacotherapy helped stabilize the patient's condition, leading to a heart transplantation six months after diagnosis.",
    "concerns": "Restrictive cardiomyopathy (RCM) is a rare type of cardiomyopathy, constituting only 2-5% of all cases. Pharmacotherapy helped stabilize the patient's condition, leading to a heart transplantation six months after diagnosis.",
    "amendments": "Restrictive cardiomyopathy (RCM) is a rare type of cardiomyopathy, constituting only 2-5% of all cases. Pharmacotherapy helped stabilize the patient's condition, leading to a heart transplantation six months after diagnosis.",
    "outcome_for_people": "Restrictive cardiomyopathy (RCM) is a rare type of cardiomyopathy, constituting only 2-5% of all cases. Pharmacotherapy helped stabilize the patient's condition, leading to a heart transplantation six months after diagnosis."
}
export default function AnalysisPage() {
    return (
  <div className="bg-[#f8f9fa] h-screen">
    <div className="flex">
      <div className="bg-[#ffffff] w-[250px] h-screen border-r-[1px] border-[#e0e0e0]">
        <div className="p-4">
          <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md w-full border-[1px] border-[#007bff]">+ New Bill</button>
        </div>
        <div className="p-4">
          <h2 className="text-[#6c757d] text-sm mb-2">Library</h2>
          <ul>
            <li className="text-[#007bff] text-sm mb-2">{OpenAIResponse.paper_title}</li>
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
      <div className="flex-1 p-8">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-[#343a40] text-2xl font-semibold">Bill Number 123 Analysed</h1>
          <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md border-[1px] border-[#007bff]">+ New Bill</button>
        </div>
        <div className="bg-[#ffffff] p-6 rounded-md shadow-sm border-[1px] border-[#e0e0e0]">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-[#343a40] text-xl font-semibold">Summary of the Bill</h2>
            <div className="flex items-center">
              <span className="text-[#343a40] text-sm mr-2">4 papers</span>
              <i className="fas fa-chevron-down text-[#6c757d]"></i>
            </div>
          </div>
          <p className="text-[#6c757d] text-sm mb-4">
            Cardiomyocytes, the cells responsible for the contraction of the heart, are central to the understanding of various heart conditions. <a href="#" className="text-[#007bff]">Zamecznik (2014)</a> highlights the case of a 14-year-old boy with restrictive cardiomyopathy, a rare form of the disease characterized by diastolic dysfunction. This case underscores the importance of early diagnosis and treatment, as the condition can be fatal. <a href="#" className="text-[#007bff]">Emanuel (1972)</a> discusses the association of cardiomyopathy with heredofamilial neuromyopathic disorders, such as Friedreich's disease. <a href="#" className="text-[#007bff]">Yanjari (2018)</a> provides a comprehensive overview of the symptoms and clinical features of cardiomyopathy in adults, emphasizing the need for early recognition and management. <a href="#" className="text-[#007bff]">Ижкина (2012)</a> categorizes nonischemic cardiomyopathy into four main types, including dilated, hypertrophic, restrictive, and arrhythmogenic right ventricular, and underscores the high mortality rates in pediatric cases. These studies collectively underscore the importance of understanding and addressing cardiomyocyte-related conditions.
          </p>
          <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md border-[1px] border-[#007bff]">Copy</button>
        </div>
        <div className="flex justify-between items-center mt-4">
          <div className="bg-[#308a22] text-white py-2 px-4 rounded-md">Vote For</div>
          <div className="flex items-center">
            <button className="bg-[#f8f9fa] text-[#343a40] py-2 px-4 rounded-md border-[1px] border-[#e0e0e0] mr-2">Filters</button>
            <button className="bg-[#f8f9fa] text-[#343a40] py-2 px-4 rounded-md border-[1px] border-[#e0e0e0] mr-2">Export as <span className="text-[#007bff]">Social Media Post</span></button>
          </div>
        </div>
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
                  <span>{OpenAIResponse.paper_title}</span>
                  <div className="text-[#6c757d] text-xs">{OpenAIResponse.paper_title}</div>
                </td>
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{OpenAIResponse.summary}</td>
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{OpenAIResponse.main_findings}</td> 
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{OpenAIResponse.benefits}</td>
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{OpenAIResponse.concerns}</td>              
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{OpenAIResponse.amendments}</td>             
                <td className="text-left text-[#343a40] text-sm py-2 px-4">{OpenAIResponse.outcome_for_people}</td>              
                </tr>
            </tbody>
          </table>
        </div>
        <div className="flex justify-center mt-4">
          <button className="bg-[#007bff] text-white py-2 px-4 rounded-md">Add new step</button>
        </div>
      </div>
    </div>
  </div>
);
  }

