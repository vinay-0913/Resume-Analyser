export default function Navbar() {
  return (
    <header className="bg-white shadow-sm px-14 py-6 flex justify-between items-center">
      <div>
        <h1 className="text-2xl font-bold text-blue-900">AI Resume Analyzer</h1>
        <p className="text-sm text-gray-600">Optimize your resume with AI-powered insights</p>
      </div>
      <span className="text-sm bg-blue-100 text-blue-700 px-3 py-1 rounded-full">
        Powered by BERT & NLP
      </span>
    </header>
  );
}
