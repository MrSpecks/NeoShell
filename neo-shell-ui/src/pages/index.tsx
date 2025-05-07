// src/pages/index.tsx
import Head from "next/head";
import Terminal from "@/components/Terminal";

export default function Home() {
  return (
    <>
      <Head>
        <title>NeoShell UI</title>
        <meta name="description" content="NeoShell frontend UI" />
      </Head>
      <main className="flex min-h-screen flex-col items-center justify-center bg-gray-900 text-white">
        <h1 className="mb-6 text-3xl font-bold">NeoShell UI</h1>
        <Terminal />
      </main>
    </>
  );
}
