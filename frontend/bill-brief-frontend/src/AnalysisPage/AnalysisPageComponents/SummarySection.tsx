import React from "react";

export default function SummarySection() {
    return (
        <>
            <div className="flex justify-between items-center mb-4">
                <h1 className="text-[#343a40] text-2xl font-semibold">Bill Number 123 Analysed</h1>
                <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md border-[1px] border-[#007bff]">+ New Bill</button>
            </div><div className="bg-[#ffffff] p-6 rounded-md shadow-sm border-[1px] border-[#e0e0e0]">
                    <div className="flex justify-between items-center mb-4">
                        <h2 className="text-[#343a40] text-xl font-semibold">Summary of the Bill</h2>
                        <div className="flex items-center">
                            <span className="text-[#343a40] text-sm mr-2">4 papers</span>
                            <i className="fas fa-chevron-down text-[#6c757d]"></i>
                        </div>
                    </div>
                    <p className="text-[#6c757d] text-sm mb-4">
                        Cardiomyocytes, the cells responsible for the contraction of the heart, are central to the understanding of various heart conditions. 
                        <a href="www.google.com" className="text-[#007bff]">Zamecznik (2014)</a> highlights the case of a 14-year-old boy with restrictive cardiomyopathy, a rare form of the disease characterized by diastolic dysfunction. This case underscores the importance of early diagnosis and treatment, as the condition can be fatal. 
                        <a href="www.google.com" className="text-[#007bff]">Emanuel (1972)</a> discusses the association of cardiomyopathy with heredofamilial neuromyopathic disorders, such as Friedreich's disease. 
                        <a href="www.google.com" className="text-[#007bff]">Yanjari (2018)</a> provides a comprehensive overview of the symptoms and clinical features of cardiomyopathy in adults, emphasizing the need for early recognition and management. 
                        <a href="www.google.com" className="text-[#007bff]">Ижкина (2012)</a> categorizes nonischemic cardiomyopathy into four main types, including dilated, hypertrophic, restrictive, and arrhythmogenic right ventricular, and underscores the high mortality rates in pediatric cases. These studies collectively underscore the importance of understanding and addressing cardiomyocyte-related conditions.
                    </p>
                    <button className="bg-[#f8f9fa] text-[#007bff] py-2 px-4 rounded-md border-[1px] border-[#007bff]">Copy</button>
                </div><div className="flex justify-between items-center mt-4">
                    <div className="bg-[#308a22] text-white py-2 px-4 rounded-md">Vote For</div>
                    <div className="flex items-center">
                        <button className="bg-[#f8f9fa] text-[#343a40] py-2 px-4 rounded-md border-[1px] border-[#e0e0e0] mr-2">Filters</button>
                        <button className="bg-[#f8f9fa] text-[#343a40] py-2 px-4 rounded-md border-[1px] border-[#e0e0e0] mr-2">Export as <span className="text-[#007bff]">Social Media Post</span></button>
                    </div>
                </div>
        </>
    )
}