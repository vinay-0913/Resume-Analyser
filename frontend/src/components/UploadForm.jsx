import { useState } from "react";
import { Upload, FileText, Briefcase, Loader2 } from "lucide-react";

export default function UploadForm({ setResult, setCurrentTab })  {
  const [file, setFile] = useState(null);
  const [jobDesc, setJobDesc] = useState("");
  const [loading, setLoading] = useState(false);
  const [analysisProgress, setAnalysisProgress] = useState(0);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  

  const handleSubmit = async () => {
    if (!file || !jobDesc.trim()) {
      alert("Please upload a resume and paste the job description.");
      return;
    }
  
   setIsAnalyzing(true);
   setAnalysisProgress(0);
    setLoading(true);
    const formData = new FormData();
    formData.append("resume", file);
    formData.append("job_description", jobDesc);

     const stages = [15, 35, 60, 90, 100];
     stages.forEach((value, idx) =>
     setTimeout(() => setAnalysisProgress(value), idx * 800)
    );
    let data = null;
    try {
      const res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
      setCurrentTab("Analysis Results");             
    } catch (err) {
      console.error("Error:", err);
      alert("Something went wrong while uploading.");
    } setTimeout(() => {
    setAnalysisProgress(100);
    setTimeout(() => {
      setIsAnalyzing(false);
      if (data) setResult(data);
    }, 400); 
  }, 3200); 
};
  return (
    <div className="p-6 flex flex-col gap-6">
      <div className="flex gap-6">
        {/* Resume Upload */}
        <div className="w-1/2 border hover:shadow-lg transition-shadow duration-300 rounded-lg p-6 bg-white shadow-sm">
          <h2 className="text-xl font-semibold mb-2 flex items-center gap-2">
            <FileText className="h-5 w-5 text-blue-600" />
            Upload Resume
          </h2>
          <div className="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center hover:border-blue-400 transition-colors cursor-pointer">
            <input
              type="file"
              accept=".txt,.pdf,.doc,.docx"
              onChange={(e) => setFile(e.target.files[0])}
              className="hidden"
              id="resume-upload"
            />
            <Upload className="h-12 w-12 text-gray-400 mx-auto mb-4" />
            <p className="text-gray-600 mb-2">
              Drag and drop your resume here, or click to browse
            </p>
            <label
              htmlFor="resume-upload"
              className="inline-block bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors cursor-pointer"
            >
              Choose File
            </label>
            {file && (
              <p className="mt-2 text-sm text-green-600">
                ✓ {file.name} uploaded
              </p>
            )}
          </div>
        </div>

        {/* Job Description */}
        <div className="w-1/2 border rounded-lg p-6 hover:shadow-lg transition-shadow duration-300 bg-white shadow-sm">
          <h2 className="text-xl font-semibold mb-2 flex items-center gap-2">
            <Briefcase className="h-5 w-5 text-green-600" />
            Paste Job Description
          </h2>
          <p className="text-sm text-gray-500 mb-2">
            Copy and paste the job description you want to match your resume against:
          </p>
          <textarea
            value={jobDesc}
            onChange={(e) => setJobDesc(e.target.value)}
            rows={10}
            className="w-full border rounded p-2"
            placeholder="Paste the job description here..."
          ></textarea>
        </div>
      </div>
      
      {isAnalyzing && (
  <div className="bg-blue-50 border border-blue-200 rounded-md p-4 mb-4 w-full">
    <div className="flex items-center justify-between mb-2">
      <h3 className="font-semibold text-blue-900 text-sm">Analyzing Your Resume</h3>
      <span className="text-sm text-blue-700">{Math.round(analysisProgress)}%</span>
    </div>
    
    {/* Progress Bar */}
    <div className="relative w-full bg-blue-100 rounded-full h-3 overflow-hidden mb-2">
      <div
        className="bg-gradient-to-r from-blue-500 to-green-200 h-full rounded-full transition-all duration-500 ease-in-out"
        style={{ width: `${analysisProgress}%` }}
      ></div>
    </div>

    {/* Status Message */}
    <div className="flex items-center gap-2 text-sm text-blue-700">
      <Loader2 className="h-4 w-4 animate-spin" />
      {analysisProgress < 30 && "Processing resume content..."}
      {analysisProgress >= 30 && analysisProgress < 60 && "Extracting keywords..."}
      {analysisProgress >= 60 && analysisProgress < 90 && "Matching with job description..."}
      {analysisProgress >= 90 && "Generating insights..."}
    </div>
  </div>
)}

      {/* Submit Button */}
      <div className="flex justify-center mt-4">
        <button
          onClick={handleSubmit}
          disabled={loading}
          className="bg-gradient-to-r from-blue-500 to-green-200 text-white px-6 py-2 rounded-lg font-semibold shadow-md"
        >
          {loading ? (
            <>
              <Loader2 className="animate-spin h-5 w-5" /> Analyzing...
            </>
          ) : (
            "Analyse Resume"
          )}
        </button>
      </div>
    </div>
  );
}
