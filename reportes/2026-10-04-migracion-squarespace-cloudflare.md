# Reporte: migración de FIC Xilitla (Squarespace → código + Cloudflare)

**Fecha:** 4 de octubre de 2026  
**Sitio en producción:** https://ficxilitlaonline.com  
**Réplica Cloudflare:** https://ficxilitlaweb.suarezsaldana.workers.dev  
**Repositorio:** https://github.com/SunnySuaSal/FICXilitlaWeb.git  
**Worker:** `ficxilitlaweb` (cuenta Cloudflare asociada al subdominio `suarezsaldana.workers.dev`)

Este documento resume el trabajo hecho para sacar el sitio del constructor WYSIWYG de Squarespace, publicarlo desde GitHub y dejar el dominio `ficxilitlaonline.com` apuntando al origen nuevo, sin perder el registro del dominio (pagado por un año a través de Squarespace).

---

## 1. Situación de partida

- El sitio público vivía en **Squarespace** (`server: Squarespace`). El DNS usaba nameservers de Google Cloud (`ns-cloud-a*.googledomains.com`), típicos de dominios que pasaron por Google Domains / Squarespace.
- El contenido era institucional y casi estático: inicio (hero, video, FilmFreeway, redes), quiénes somos, convocatoria, sedes, programa (PDF), noticias (enlaces a medios), galería 2024 y 2025 (vacía).
- El correo del festival es **Gmail** (`ficxilitlaslp@gmail.com`), no un buzón `@ficxilitlaonline.com`. No había registros MX; sí TXT de SPF (`v=spf1 -all`) y DMARC en `_dmarc`.
- El repo local `FicXilitla` empezó vacío. El objetivo era hosting por código fuente (más barato que el plan de sitio de Squarespace) y, más adelante, merch (fuera de este alcance).

Se planteó un camino didáctico (HTML → CSS → JS → React). Por falta de tiempo se **omitió React** y se entregó un sitio estático completo (HTML, CSS, JS, assets).

---

## 2. Qué se construyó

Sitio multi-página en la raíz del repo:

| Ruta pública | Archivo |
|---|---|
| `/` | `index.html` |
| `/quienes-somos` | `quienes-somos.html` |
| `/convocatoria` | `convocatoria.html` |
| `/sedes` | `sedes.html` |
| `/programa` | `programa.html` |
| `/noticias` | `noticias.html` |
| `/edicion-2024` | `edicion-2024.html` |
| `/edicion-2025` | `edicion-2025.html` |

- Estilos: `css/styles.css`. Interacción (menú, lightbox): `js/main.js`.
- Logos, fotos, favicon y PDF del programa: `assets/`.
- Alias de Squarespace: `_redirects` (`/edicion2024`, `/galera`, PDF antiguo `/s/ProgFicXilComp-hatc.pdf`).
- Generador opcional de HTML: `generate_site.py` (no se usa en el deploy).
- Desarrollo local: `npm start` (`serve`), Node instalado con Homebrew.

Identidad visual equivalente a Squarespace (fondo oscuro, mismas fotos y textos), no un clon pixel-perfect. En el inicio se conservó el texto **FICXILITLA 2025** tal como estaba en el sitio origen.

---

## 3. Video: de MP4 en Git a YouTube

El promo (~3:36, 1080p) se bajó del HLS cifrado de Squarespace y se guardó como `assets/home/promo.mp4` (~75 MB). Subirlo a GitHub fue una mala idea: Git no está pensado para vídeo; el `push` era lento y el clone inflaba el repo (~87 MB).

El vídeo se publicó en YouTube:

`https://youtu.be/qYeIt9abn_0`

El inicio usa embed (dominio `youtube-nocookie.com`):

`https://www.youtube-nocookie.com/embed/qYeIt9abn_0`

Se eliminó el MP4 del árbol de Git, se añadió a `.gitignore` y se **purgó de todo el historial** (`git filter-repo`, path `assets/home/promo.mp4`). Hubo **`git push --force-with-lease`** a `origin/main` (el historial remoto se reescribió). El empaque local bajó a ~12 MB. Clones **anteriores** al force-push no deben hacer `pull` a ciegas: conviene clonar de nuevo o alinear con `origin/main`.

GitHub puede tardar en borrar blobs inalcanzables de su caché interna; los clones nuevos no traen el MP4.

---

## 4. Publicación en Cloudflare

Se conectó el repo a Cloudflare. El proyecto se trata como **Worker con assets estáticos** (`npx wrangler deploy`), no como “Pages clásico” sin Wrangler.

### 4.1 Primer fallo: archivo demasiado grande

Wrangler tomó el directorio `.` entero, incluido `node_modules`. El binario `workerd` (~128 MB) supera el límite de 25 MiB por asset.

**Corrección:** `wrangler.jsonc` + `.assetsignore` (excluye `node_modules`, Git, `package.json`, el generador, etc.). Commit en `main`: *Evita que Cloudflare suba node_modules en el deploy.*

### 4.2 Segundo fallo: bucle en `_redirects`

La regla `/ /index.html 200` (y las rewrites a `*.html`) chocan con el comportamiento de Cloudflare: quita `.html` e `/index` y la regla se dispara otra vez (`Invalid _redirects` / infinite loop, código 100324).

**Corrección:** `html_handling: "auto-trailing-slash"` y `not_found_handling: "404-page"` en `wrangler.jsonc`. `_redirects` solo con alias reales (301/200), sin rewrites a `.html`.

### 4.3 Deploy correcto

Build exitoso. URL del Worker:

https://ficxilitlaweb.suarezsaldana.workers.dev

Cada `git push` a `main` vuelve a desplegar. Comando en el panel: `npx wrangler deploy`. Sin comando de build. `npm ci` sigue instalando `serve` (devDependency local); no se sube gracias a `.assetsignore`.

---

## 5. Dominio `ficxilitlaonline.com`

### Titularidad

El dominio se pagó en Squarespace. Squarespace (tras Google Domains) es el **registrador**: intermediario ante ICANN. El festival **es dueño del nombre**; no hacía falta transferirlo para publicar, y un traslado tan pronto tras el pago suele chocar con el bloqueo de ~60 días.

Se cambió solo el **DNS** (quién resuelve el nombre). El registrador y la renovación siguen en Squarespace hasta que se decida otra cosa.

No hay correo en el dominio; los TXT de SPF/DMARC se **conservaron**. No se tocaron al limpiar A/CNAME de Squarespace.

### Pasos que se siguieron

1. Añadir `ficxilitlaonline.com` como zona en la **misma** cuenta Cloudflare del Worker (plan Free).
2. En Squarespace, nameservers personalizados: `alberto.ns.cloudflare.com` y `ashley.ns.cloudflare.com` (los que asignó esta cuenta; no copiar estos a otro proyecto).
3. Esperar zona **Active**. Dejar de usar `ns-cloud-a*.googledomains.com`.
4. En DNS de Cloudflare, borrar orígenes de Squarespace:
   - A del apex a `198.49.23.*` / `198.185.159.*`
   - CNAME de `www` a `ext-sq.squarespace.com`  
   El nuble naranja **no** bastaba: el proxy seguía yendo a Squarespace.
5. Worker `ficxilitlaweb` → Settings → **Domains & Routes** → **Custom Domain** (no Route) para `ficxilitlaonline.com`.
6. `www` no se pudo añadir como segundo Custom Domain (CNAME/conflictos habituales). Solución: registro **A proxied** `www` → `192.0.2.0` (placeholder) y **Redirect Rule** 301 de `https://www.ficxilitlaonline.com` hacia `https://ficxilitlaonline.com` (conservando la ruta).

### Estado verificado (4 oct 2026)

- Apex: HTTPS 200, HTML del sitio nuevo, embed de YouTube, `/sedes` 200.
- `www`: 301 al apex y luego el mismo sitio.
- NS: Cloudflare.

**Add Route** no era el mecanismo correcto para publicar `www`: una Route no crea DNS ni sustituye al Custom Domain.

---

## 6. Qué no se hizo (a propósito)

- No hay React/Vite/Next; el merch futuro no depende de eso (Stripe, Mercado Pago, etc.).
- No se migraron páginas basura del tema Squarespace (`/diseo-blog-*`, `/tests`).
- No se canceló el **registro del dominio** en Squarespace. Cuando el sitio nuevo lleve unos días estable, conviene cancelar solo el **plan de hosting/web** de Squarespace, no el dominio.
- No se metió el Custom Domain de `www` en `wrangler.jsonc`; el apex y las reglas de redirect viven en el panel de Cloudflare.

---

## 7. Operación diaria

- Editar HTML/CSS/assets en local → `npm start` → http://localhost:3000  
- Commit y **push a `main`** → Cloudflare despliega.  
- Regenerar páginas con `python3 generate_site.py` solo si se usa ese flujo; hay que volver a no reintroducir reglas `_redirects` hacia `.html`.
- No volver a versionar vídeos grandes; YouTube (u otro CDN) es el origen del promo.

---

## 8. Archivos clave del repo

| Archivo | Rol |
|---|---|
| `wrangler.jsonc` | Nombre del Worker, HTML handling, 404 |
| `.assetsignore` | Qué no se sube como asset |
| `_redirects` | Alias Squarespace |
| `index.html` | Inicio + iframe YouTube |
| `css/styles.css`, `js/main.js` | Presentación y menú/galería |
| `assets/` | Imágenes y `ProgFicXilComp.pdf` |
| `package.json` | Solo `serve` para desarrollo |

---

## 9. Resultado

El Festival Internacional de Cine de Xilitla se sirve desde GitHub + Cloudflare Workers, con dominio propio, HTTPS, vídeo en YouTube y un repo liviano. Squarespace queda, como mucho, como registrador del nombre hasta que se elija moverlo o renovarlo ahí.
