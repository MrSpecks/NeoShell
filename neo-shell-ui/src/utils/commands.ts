export function simulateShellCommand(cmd: string): string {
  const lower = cmd.trim().toLowerCase();

  switch (lower) {
    case "help":
      return `Available commands:
  help         Show this help message
  whoami       Reveal your identity
  date         Show current system date
  clear        Clear the screen
  ls           List accessible directories
  cd [dir]     Change (fake) directory
  sudo access  Attempt to gain root access
  hack the planet   Run elite exploit
  trace        Trace route to the mainframe
  ping matrix  Ping the Matrix core
  decode       Decrypt hidden message
  exit         Exit NeoShell`;

    case "whoami":
      return "guest@NeoShell: You are the anomaly.";

    case "date":
      return new Date().toString();

    case "clear":
      return "__CLEAR__";

    case "ls":
      return "README.md  /projects  /skills  /contact  /mainframe";

    case "cd projects":
    case "cd /projects":
      return "Entering /projects... (stand by)";

    case "cd skills":
    case "cd /skills":
      return "Displaying skill matrix...";

    case "cd contact":
    case "cd /contact":
      return "Engaging communication protocol...";

    case "sudo access":
      return "Access denied: You are not the chosen one... yet.";

    case "hack the planet":
      return "Launching zero-day exploit...\nBypassing firewalls...\nMainframe breached!";

    case "trace":
      return `Tracing route to The Source [42.42.42.42]...
  hop 1... 10ms
  hop 2... 8ms
  hop 3... Accessing hidden node...
  hop 4... Connection unstable.
  hop 5... Matrix core reached.`

    case "ping matrix":
      return `Pinging matrix.neoshell.net [101.101.101.1] with 32 bytes of data:
Reply from 101.101.101.1: bytes=32 time=5ms TTL=64
Reply from 101.101.101.1: bytes=32 time=5ms TTL=64
Reply from 101.101.101.1: bytes=32 time=5ms TTL=64
Matrix core stable.`;

    case "decode":
      return "01110100 01110010 01110101 01110100 01101000 = truth";

    case "exit":
      return "Exiting NeoShell... Goodbye.";

    case "nmap":
      return `Starting Nmap 7.93 ( https://nmap.org ) at ${new Date().toLocaleString()}
  Scanning localhost (127.0.0.1)...
  PORT     STATE SERVICE
  22/tcp   open  ssh
  80/tcp   open  http
  443/tcp  open  https
  1337/tcp open  elite`;

    case "banner":
      return `
        _   _                 ____  _          _ _
       | \\ | | ___  _ __ ___ / ___|| |__   ___| | |
       |  \\| |/ _ \\| '__/ _ \\\\___ \\| '_ \\ / _ \\ | |
       | |\\  | (_) | | | (_) |___) | | | |  __/ | |
       |_| \\_|\\___/|_|  \\___/____/|_| |_|\\___|_|_|
         Welcome to NeoShell — type 'help'
        `;

    case "cat secrets.txt":
      return "Accessing secrets.txt...\n\n[REDACTED] The Matrix has you...\nFollow the white rabbit.";

    case "rm -rf /":
      return "Nice try. NeoShell has safeguards. Self-destruct prevented.";

    case "sudo make me a sandwich":
      return "Okay. You're root. Here's your sandwich.";

    case "alias ll='ls -lah'":
      return "Alias created: now you're really pretending to know Linux.";

    case "reboot":
      return "System rebooting... [Matrix lines intensify]... Just kidding.";

    case "history":
      return `
  1  help
  2  whoami
  3  hack the planet
  4  decode
  5  ping matrix
  6  sudo access
  7  banner`;

    case "man hack":
      return `HACK(1)                NeoShell Manual                HACK(1)
  NAME
      hack - attempt to subvert systems with style
  
  SYNOPSIS
      hack [target]
  
  DESCRIPTION
      Executes a cinematic hacking sequence. Results not guaranteed.
  
  SEE ALSO
      sudo(8), nmap(1), matrix(6)`;

    case "matrix":
      return "Wake up, Neo...\nThe Matrix has you...\nFollow the white rabbit.";

    case "upgrade":
      return "NeoShell v2.0 detected... Initiating silent upgrade sequence... Done.";

    case "log":
      return `LOG [System Boot Time: ${new Date().toLocaleTimeString()}]
  - User authenticated.
  - Intrusion detection systems active.
  - No anomalies detected.
  - Awaiting input...`;

    default:
      return `Unknown command: ${cmd}\nType 'help' to see a list of available commands.`;
  }
}