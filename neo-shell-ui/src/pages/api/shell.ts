// src/pages/api/shell.ts
import type { NextApiRequest, NextApiResponse } from "next";
import { simulateShellCommand } from "@/utils/commands";

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  const { cmd } = req.body;
  const result = simulateShellCommand(cmd || "");
  res.status(200).json({ result });
}
