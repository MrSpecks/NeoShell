import "@fontsource/fira-code";
import "@/src/styles/globals.css";
import type { AppProps } from "next/app";
import { useState } from "react";
import MatrixSplash from "../components/MatrixSplash";

function MyApp({ Component, pageProps }: AppProps) {
  const [loading, setLoading] = useState(true);

  return (
    <>
      {loading ? (
        <MatrixSplash onContinue={() => setLoading(false)} />
      ) : (
        <Component {...pageProps} />
      )}
    </>
  );
}
export default MyApp;