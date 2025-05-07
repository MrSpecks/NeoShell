// src/components/Terminal.tsx
"use client";

import { useState } from "react";

const Terminal = () => {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState<string[]>([]);

  const handleCommand = async () => {
    if (!input.trim()) return;

    // Send the command to the server-side API ("/api/shell")
    const response = await fetch("/api/shell", {
      method: "POST",
      body: JSON.stringify({ cmd: input }),
      headers: { "Content-Type": "application/json" },
    });

    // Wait for the response and parse it as JSON
    const data = await response.json();

    // Check if the response indicates clearing the terminal
    if (data.result === "__CLEAR__") {
      setOutput([]); // Clear the terminal output
    } else {
      // Otherwise, append the command and its result to the output
      setOutput([...output, `> ${input}`, data.result]);
    }

    // Clear the input field
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