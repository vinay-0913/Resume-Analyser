import { useState } from "react";
import Navbar from "./components/Navbar";
import Tabs from "./components/Tabs";
import UploadForm from "./components/UploadForm";
import AnalysisResult from "./components/AnalysisResult";

function App() {
  const [currentTab, setCurrentTab] = useState("Upload & Analyze");
  const [result, setResult] = useState(null); // 🟢 Moved here!

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50">
      <Navbar />
      <main className="px-10">
        <Tabs currentTab={currentTab} setCurrentTab={setCurrentTab} />
        
        {currentTab === "Upload & Analyze" && (
          <UploadForm setResult={setResult} setCurrentTab={setCurrentTab} />
        )}

        {currentTab === "Analysis Results" && result && (
          <AnalysisResult result={result} />
        )}
      </main>
    </div>
  );
}

export default App;
