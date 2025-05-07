// components/MatrixSplash.tsx
"use client";

import React, { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";
import Typewriter from "typewriter-effect";

export default function MatrixSplash({ onContinue }: { onContinue: () => void }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [showButton, setShowButton] = useState(false);

  // Matrix Rain Effect
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const letters =
      "アァイィウヴエエェオカガキギクグケゲコゴサザシジスズセゼソゾタダチッヂヅテデトドナニヌネハバパヒビピフブプヘベペホボポマミムメモヤユヨラリルレロワヲンABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    const fontSize = 14;
    const columns = Math.floor(canvas.width / fontSize);
    const drops = Array(columns).fill(1);

    const draw = () => {
      ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.fillStyle = "#00FF00"; // Update to match GUI if needed
      ctx.font = `${fontSize}px monospace`;

      for (let i = 0; i < drops.length; i++) {
        const text = letters.charAt(Math.floor(Math.random() * letters.length));
        ctx.fillText(text, i * fontSize, drops[i] * fontSize);

        if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
          drops[i] = 0;
        }
        drops[i]++;
      }
    };

    const interval = setInterval(draw, 33);
    return () => clearInterval(interval);
  }, []);

  // Delay to show button after typing
  useEffect(() => {
    const timer = setTimeout(() => {
      setShowButton(true);
    }, 6000);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="relative flex h-screen w-full items-center 
    justify-center overflow-hidden bg-black">
      <canvas ref={canvasRef} className="absolute inset-0 z-0" />

      <motion.div
        className="z-10 max-w-2xl px-4 text-center text-green-400"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1, duration: 1 }}
      >
        <div className="font-mono text-xl leading-relaxed sm:text-3xl md:text-4xl">
          <Typewriter
            onInit={(typewriter) => {
              typewriter
                .typeString("Welcome to NeoShell")
                .pauseFor(2000)
                .typeString("<br /><br /> Are you ready to uncover the truth?")
                .start();
            }}
            options={{
              autoStart: true,
              delay: 40,
              loop: false,
            }}
          />
        </div>

        {showButton && (
          <motion.button
            onClick={onContinue}
            className="mt-8 rounded-md border border-green-500 px-6 py-3 
            font-mono text-green-300 transition-colors duration-300 
            hover:bg-green-500 hover:text-black"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 1 }}
          >
            Enter the Shell
          </motion.button>
        )}
      </motion.div>
    </div>
  );
}
