import "@fontsource/fira-code";
import "@/src/styles/globals.css";
import type { AppProps } from "next/app";
// pages/_app.tsx or a specific page component
import { useState, useEffect } from 'react';
import MatrixSplash from '../components/MatrixSplash';

function MyApp({ Component, pageProps }: AppProps) {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false));
    return () => clearTimeout(timer);
  }, []);

  return (
    <>
      {loading && <MatrixSplash onContinue={function (): void {
        throw new Error("Function not implemented.");
      } } />}
      <Component {...pageProps} />
    </>
  );
}
export default MyApp;