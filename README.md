# Core Material JSC — Website

Website tĩnh cho www.corematerial.vn (HTML/CSS thuần, không cần build).

- `public/index.html` — toàn bộ trang
- `public/img/` — hình ảnh và logo (core-mark.svg, core-mark-white.svg)
- `wrangler.jsonc` — cấu hình Cloudflare Workers (static assets)

Triển khai: Cloudflare Workers kết nối repo này. Build command để trống, deploy command `npx wrangler deploy`.
