// Định tuyến theo tên miền:
//  - corematerial.info (và www)  -> nội dung trong public/info/
//  - corematerial.vn và các tên miền khác -> website chính trong public/
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();
    const isInfo = host === "corematerial.info" || host === "www.corematerial.info";

    // Gộp www.corematerial.info về corematerial.info
    if (host === "www.corematerial.info") {
      url.hostname = "corematerial.info";
      return Response.redirect(url.toString(), 301);
    }

    let path = url.pathname;

    if (isInfo) {
      path = "/info" + path;
    } else if (path === "/info" || path.startsWith("/info/")) {
      // Nội dung Insights chỉ phục vụ trên corematerial.info
      const target = new URL(path.replace(/^\/info/, "") || "/", "https://corematerial.info");
      target.search = url.search;
      return Response.redirect(target.toString(), 301);
    }

    if (path.endsWith("/")) path += "index.html";

    const assetUrl = new URL(url);
    assetUrl.pathname = path;
    let res = await env.ASSETS.fetch(new Request(assetUrl, request));

    // Cho phép đường dẫn không có đuôi .html
    if (res.status === 404 && !/\.[a-z0-9]+$/i.test(path)) {
      assetUrl.pathname = path + ".html";
      const alt = await env.ASSETS.fetch(new Request(assetUrl, request));
      if (alt.ok) res = alt;
    }
    return res;
  },
};
