// Cloudflare Worker: forwards /api/* to the game for your GitHub Pages site only.
const TARGET = "https://lagoslife.eliysites.com";
const ALLOWED = "https://beastx2008.github.io"; // change if your Pages address is different

export default {
  async fetch(req) {
    const url = new URL(req.url);
    const cors = {
      "Access-Control-Allow-Origin": ALLOWED,
      "Access-Control-Allow-Headers": "Content-Type, X-Session",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Expose-Headers": "X-Session-Set",
      "Vary": "Origin",
    };

    if (req.headers.get("Origin") !== ALLOWED) {
      return new Response("Forbidden", { status: 403 });
    }
    if (req.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: cors });
    }
    if (!url.pathname.startsWith("/api/")) {
      return new Response("Not found", { status: 404, headers: cors });
    }

    const headers = new Headers();
    const type = req.headers.get("Content-Type");
    if (type) headers.set("Content-Type", type);
    const session = req.headers.get("X-Session");
    if (session) headers.set("Cookie", session);

    const r = await fetch(TARGET + url.pathname + url.search, {
      method: req.method,
      headers,
      body: req.method === "GET" ? undefined : await req.text(),
    });

    const out = new Headers(cors);
    out.set("Content-Type", r.headers.get("Content-Type") || "application/json");
    const cookies = r.headers.getSetCookie().map(c => c.split(";")[0]).join("; ");
    if (cookies) out.set("X-Session-Set", cookies);

    return new Response(await r.text(), { status: r.status, headers: out });
  },
};
