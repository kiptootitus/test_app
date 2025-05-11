// src/App.js
import { useState } from "react";
import axios from "axios";

function App() {
  const [form, setForm] = useState({ username: "", password: "", action: "login" });

  const handleSubmit = async () => {
    try {
      const res = await axios.post("http://localhost:8000/auth/", form);
      alert(JSON.stringify(res.data));
    } catch (err) {
      console.error("💥 Auth error:", err.response?.data || err.message);
      alert("Error: " + (err.response?.data?.error || "Something went wrong"));
    }
  };
  

  return (
    <div>
      <h1>{form.action.toUpperCase()}</h1>
      <input placeholder="Username" onChange={e => setForm({...form, username: e.target.value})} />
      <input type="password" placeholder="Password" onChange={e => setForm({...form, password: e.target.value})} />
      <button onClick={handleSubmit}>Submit</button>
      <button onClick={() => setForm({...form, action: form.action === 'login' ? 'signup' : 'login'})}>
        Switch to {form.action === 'login' ? 'Signup' : 'Login'}
      </button>
    </div>
  );
}

export default App;
