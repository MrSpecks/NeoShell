export function simulateShellCommand(cmd: string): string {
  const lower = cmd.trim().toLowerCase();

  switch (lower) {
    case "help":
      return "Available commands: help, whoami, date, clear";
    case "whoami":
      return "You are Neo.";
    case "date":
      return new Date().toString();
    case "clear":
      return "__CLEAR__";
    default:
      return `Unknown command: ${cmd}`;
  }
}
