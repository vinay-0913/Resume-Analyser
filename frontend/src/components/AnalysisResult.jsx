import { useEffect, useState } from "react";

export default function AnalysisResult({ result }) {
  const {
    score_out_of_100,
    matched_keywords = [],
    matched_skills = [],
    keywords = [],
    recommendations = [],
    score_summary = {}
  } = result || {};

  const missingKeywords = keywords.filter(kw => !matched_keywords.includes(kw));

  return (
    <div className="p-6 space-y-6 ">
      {/* Match Score */}
      <div className="flex items-center gap-6 ">
     {/* Circular Score Ring */}
     <div
      className="relative w-28 h-28 rounded-full shadow-lg"
      style={{
        background: `conic-gradient(#f59e0b 0% ${score_out_of_100}%, #fef3c7 ${score_out_of_100}% 100%)`,
      }}
     >
      <div className="absolute inset-2 rounded-full  bg-white flex items-center justify-center ">
        <span className="text-orange-500 text-3xl font-bold">
          {score_out_of_100}
        </span>
      </div>
     </div>
        <p className="text-gray-600">
          Your resume matches {score_out_of_100}% with the job requirements
        </p>
        
        <span className={`text-sm shadow-sm px-2 py-1 rounded-full ${score_out_of_100 < 50 ? "bg-red-100 text-red-600" : "bg-green-100 text-green-600"}`}>
          {score_out_of_100 < 50 ? "Needs Improvement" : "Good Match"}
        </span>
      </div>

      
    <div className="grid grid-cols-2 gap-4">
        {/* ✅ Matched Keywords + Skills */}
        <div className="bg-green-50 shadow-md p-4 rounded-lg space-y-6">
        <h3 className="font-semibold text-lg text-green-700">✅ Matched Keywords & Skills</h3>

     {/* Matched Keywords */}
        <div>
      <h4 className="text-green-800 font-medium">Matched Keywords ({matched_keywords.length})</h4>
      <ul className="flex flex-wrap gap-2 mt-1">
        {matched_keywords.length > 0 ? (
          matched_keywords.map((kw, idx) => (
            <span
              key={idx}
              className="bg-green-100 text-green-700 text-sm px-3 py-1 rounded-full"
            >
              {kw}
            </span>
          ))
        ) : (
          <p className="text-sm text-gray-500 italic">No keywords matched</p>
        )}
        </ul>
    </div>

    {/* Matched Skills */}
    <div>
      <h4 className="text-green-800 font-medium mt-4">Matched Skills</h4>
      {["hard_skills", "soft_skills", "tools", "job_titles"].map((category) => (
        <div key={category}>
          <h5 className="text-green-700 capitalize mt-2">
            {category.replace("_", " ")}{" "}
            {score_summary?.[`${category.slice(0, -1)}_match`] &&
              `(${score_summary[`${category.slice(0, -1)}_match`]})`}
          </h5>
          <ul className="flex flex-wrap gap-2 mt-1">
            {matched_skills?.[category]?.length > 0 ? (
              matched_skills[category].map((skill, idx) => (
                <span
                  key={idx}
                  className="bg-green-100 text-green-700 text-sm px-3 py-1 rounded-full"
                >
                  {skill}
                </span>
              ))
            ) : (
              <p className="text-sm text-gray-500 italic">
                No {category.replace("_", " ")} matched
              </p>
            )}
          </ul>
        </div>
      ))}
    </div>
  </div>

  {/* ❌ Missing Keywords */}
  <div className="bg-red-50 shadow-md p-4 rounded-lg space-y-4">
    <h3 className="font-semibold text-lg text-red-700">❌ Missing Keywords ({missingKeywords.length})</h3>
    <ul className="flex flex-wrap gap-2">
      {missingKeywords.map((kw, idx) => (
        <span
          key={idx}
          className="bg-red-100 text-red-700 text-sm px-3 py-1 rounded-full"
        >
          {kw}
        </span>
      ))}
    </ul>
  </div>
 </div>


      {/* Suggestions */}
      <div className="bg-blue-50 shadow-md p-4 rounded-lg">
        <h3 className="text-lg font-semibold text-blue-700 mb-2">📌 Improvement Suggestions</h3>
        <ol className="list-decimal list-inside space-y-2 text-blue-800">
          {recommendations.map((tip, idx) => (
            <li key={idx}>{tip}</li>
          ))}
        </ol>
      </div>
    </div>
  );
}
