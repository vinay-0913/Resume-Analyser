export default function Tabs({ currentTab, setCurrentTab }) {
  const tabs = ["Upload & Analyze", "Analysis Results",];

  return (
    <div className="flex border-b mt-4">
      {tabs.map((tab, i) => (
        <button
          key={i}
          onClick={() => setCurrentTab(tab)}
          className={`px-4 py-2 ${
            currentTab === tab
              ? "border-b-2 border-blue-500 font-semibold text-blue-600"
              : "text-gray-500"
          }`}
        >
          {tab}
        </button>
      ))}
    </div>
  );
}
