# FIC Xilitla

Sitio estático del Festival Internacional de Cine de Xilitla, migrado desde Squarespace.

## Local

```bash
npm install
npm start
```

Abre http://localhost:3000

## Publicar

Cloudflare (Workers + assets estáticos) lee `wrangler.jsonc`. El archivo `.assetsignore` evita subir `node_modules` (si no, el deploy falla por el binario `workerd`).

Comando de deploy en el panel: `npx wrangler deploy`. No hace falta comando de build.

El archivo `_redirects` conserva las URLs de Squarespace (`/quienes-somos`, `/convocatoria`, etc.).
