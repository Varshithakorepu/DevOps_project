import { useState } from "react";

function App() {
  const [headlines, setHeadlines] = useState([]);
  const [status, setStatus] = useState("");

  const fetchNews = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/news");
    const data = await res.json();
    setHeadlines(data.headlines);
  };

  const sendSMS = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/send", { method: "POST" });
    const data = await res.json();
    setStatus(`✅ SMS Sent! SID: ${data.sid}`);
    setHeadlines(data.headlines);
  };

  return (
    <div className="p-6 font-sans">
      <h1 className="text-2xl font-bold mb-4">📱 Telugu News SMS Bot</h1>
      <button onClick={fetchNews} className="px-4 py-2 bg-blue-500 text-white rounded">Fetch News</button>
      <button onClick={sendSMS} className="ml-2 px-4 py-2 bg-green-500 text-white rounded">Send SMS</button>
      {status && <p className="mt-4">{status}</p>}
      <ul className="mt-4 list-disc pl-5">
        {headlines.map((h, i) => <li key={i}>{h}</li>)}
      </ul>
    </div>
  );
}

export default App;
