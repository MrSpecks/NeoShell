// src/components/Terminal.tsx
"use client";

import { useState } from "react";

const Terminal = () => {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState<string[]>([]);

  const handleCommand = async () => {
    if (!input.trim()) return;
    // Inside handleCommand()
    if (data.result === "__CLEAR__") {
      setOutput([]);
    } else {
      setOutput([...output, `> ${input}`, data.result]);
    }
    const response = await fetch("/api/shell", {
      method: "POST",
      body: JSON.stringify({ cmd: input }),
      headers: { "Content-Type": "application/json" },
    });
    const data = await response.json();
    setOutput([...output, `> ${input}`, data.result]);
    setInput("");
  };

  return (
    <div className="h-[400px] overflow-y-auto rounded-xl bg-black p-4 font-mono text-green-400 shadow-inner">
      {output.map((line, index) => (
        <div key={index}>{line}</div>
      ))}
      <input
        className="mt-2 w-full border-none bg-black text-white outline-none"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleCommand();
        }}
        placeholder="Type a command..."
        autoFocus
      />
    </div>
  );
};

export default Terminal;
