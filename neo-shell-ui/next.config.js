/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    unoptimized: true, // Can remove if you plan to use Next/Image with optimization
  },
};

module.exports = nextConfig;
