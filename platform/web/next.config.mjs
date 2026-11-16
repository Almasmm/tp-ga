// The front end talks to the local FastAPI server through /api; set TPGA_API_ORIGIN before
// `next dev` or `next build` to use another address.
const api = process.env.TPGA_API_ORIGIN || "http://127.0.0.1:8000";

const config = {
  devIndicators: false,
  poweredByHeader: false,
  async rewrites() {
    return [{ source: "/api/:path*", destination: api + "/:path*" }];
  },
};

export default config;
