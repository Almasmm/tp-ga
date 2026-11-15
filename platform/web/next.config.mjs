const api = process.env.TPGA_API_ORIGIN || "http://127.0.0.1:8765";

export default {
  devIndicators: false,
  async rewrites() {
    return [{ source: "/api/:path*", destination: api + "/:path*" }];
  },
};

