import React, { useState } from "react";

export default function UploadComponent() {
  const [files, setFiles] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const sendToBackend = async () => {
    if (files.length === 0) return alert("Please upload images.");
    const form = new FormData();
    files.forEach(f => form.append("files", f));
    form.append("user_id", "web_user");
    setLoading(true);

    const res = await fetch("http://localhost:8000/api/analyze", {
      method: "POST",
      body: form
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div>
      <p>Select multiple face images</p>
      <input type="file" multiple accept="image/*" onChange={(e)=> setFiles([...e.target.files])} />
      <button onClick={sendToBackend} style={{ marginTop:10 }}>
        {loading ? "Processing..." : "Analyze Skin"}
      </button>

      {result && (
        <div style={{ marginTop:20 }}>
          <h3>Result</h3>
          <p><b>Conditions:</b> {result.predicted_conditions.join(", ")}</p>
          <p><b>Products:</b></p>
          <ul>{result.suggested_products.map((p,i)=><li key={i}>{p}</li>)}</ul>

          <h4>Images</h4>
          <div style={{display:"flex",gap:10, flexWrap:"wrap"}}>
            {result.images.map((img,i)=><img key={i} src={`http://localhost:8000${img}`} width={120} />)}
          </div>
        </div>
      )}
    </div>
  );
}
