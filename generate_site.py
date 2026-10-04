#!/usr/bin/env python3
"""Genera las páginas HTML del sitio FIC Xilitla."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def header(prefix: str, current: str) -> str:
    def href(path: str) -> str:
        return prefix + path

    def cur(name: str) -> str:
        return ' aria-current="page"' if current == name else ""

    return f"""  <a class="skip" href="#contenido">Saltar al contenido</a>
  <header class="site-header">
    <div class="header-inner">
      <a class="logo" href="{href("index.html")}"><img src="{href("assets/logo.png")}" alt="FIC Xilitla"></a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menú</button>
      <nav class="nav" id="menu">
        <a href="{href("quienes-somos.html")}"{cur("quienes")}>Quiénes somos</a>
        <a href="{href("convocatoria.html")}"{cur("convocatoria")}>Convocatoria</a>
        <a href="{href("sedes.html")}"{cur("sedes")}>Sedes</a>
        <a href="{href("programa.html")}"{cur("programa")}>Programa</a>
        <a href="{href("noticias.html")}"{cur("noticias")}>Noticias</a>
        <div class="nav-drop">
          <button type="button" aria-expanded="false">Galería</button>
          <div class="nav-drop-menu">
            <a href="{href("edicion-2024.html")}"{cur("g2024")}>Edición 2024</a>
            <a href="{href("edicion-2025.html")}"{cur("g2025")}>Edición 2025</a>
          </div>
        </div>
      </nav>
    </div>
  </header>"""


def footer(prefix: str) -> str:
    return f"""  <footer class="site-footer">
    <h2>Festival Internacional de Cine de Xilitla</h2>
    <p><a href="mailto:ficxilitlaslp@gmail.com">ficxilitlaslp@gmail.com</a></p>
    <div class="social">
      <a href="https://www.instagram.com/ficxilitla" rel="noopener noreferrer">Instagram</a>
      <a href="https://www.facebook.com/share/yHXfnhhzN3xK53yJ/" rel="noopener noreferrer">Facebook</a>
    </div>
    <p class="credit">Desarrollado por Jorge S. Saldaña</p>
  </footer>
  <script src="{prefix}js/main.js"></script>"""


def page(title: str, prefix: str, current: str, body: str, extra_head: str = "") -> str:
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="icon" href="{prefix}favicon.ico">
  <link rel="stylesheet" href="{prefix}css/styles.css">
  {extra_head}
</head>
<body>
{header(prefix, current)}
  <main id="contenido">
{body}
  </main>
{footer(prefix)}
</body>
</html>
"""


pages = {}

pages["index.html"] = page(
    "FIC Xilitla",
    "",
    "home",
    """    <section class="hero" style="background-image:url('assets/home/hero.jpg')">
      <div class="hero-copy">
        <p>2 al 6 de diciembre</p>
        <h1>FICXILITLA 2025</h1>
      </div>
    </section>
    <section class="video-wrap">
      <div class="video-frame">
        <iframe src="https://www.youtube-nocookie.com/embed/qYeIt9abn_0" title="Video promocional FICXILITLA" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
      </div>
    </section>
    <section class="section split">
      <div>
        <h2>Experimenta el cine en la selva</h2>
        <p class="lede">El FICXILITLA es una experiencia cinematográfica cuyo objetivo es llevar historias a públicos diversos, generando disertaciones en un espacio seguro y surrealista.</p>
      </div>
      <img src="assets/home/logo-wordmark.png" alt="Logotipo del Festival Internacional de Cine de Xilitla">
    </section>
    <section class="section split">
      <img src="assets/home/community.jpg" alt="Público y realizadores durante el festival">
      <div>
        <h2>Conecta con tu comunidad</h2>
        <p>El FICXILITLA es un espacio de interacción entre el público, realizadores y especialistas de la industria cinematográfica. Organizamos talleres, conferencias, recorridos y sesiones de preguntas y respuestas tras la proyección de cortometrajes y largometrajes en nuestras distintas sedes.</p>
        <p>Nuestra ventana de exhibición también es un punto de encuentro para el networking entre el gremio cinematográfico.</p>
        <p>El Festival Internacional de Cine de Xilitla (Xilitla Film Fest) acepta inscripciones por FilmFreeway:</p>
        <div class="cta-row">
          <a class="btn btn-solid" href="https://filmfreeway.com/festivals/81189" rel="noopener noreferrer">Inscribirse en FilmFreeway</a>
        </div>
      </div>
    </section>
""",
)

pages["quienes-somos.html"] = page(
    "Quiénes somos — FIC Xilitla",
    "",
    "quienes",
    """    <section class="page-hero" style="background-image:url('assets/quienes/01.jpg')">
      <h1>Quiénes somos</h1>
    </section>
    <section class="section prose">
      <p>El FICXILITLA nació en el 2023 gracias a la iniciativa del empresario mexicano Mario César Ramírez, quien propuso este encuentro en el pueblo mágico de Xilitla, con el objetivo de ser una ventana de exhibición de la cinematografía nacional e internacional.</p>
      <p>Xilitla, ubicado en el Estado de San Luis Potosí, es el escenario ideal para esta propuesta ya que dentro de sus paisajes selváticos, se encuentra el Jardín Escultórico de Edward James, por lo que el surrealismo y la magia, se respiran en cada uno de estos rincones de la Huasteca Potosina.</p>
      <p>Hemos sido plataforma de nuevas y nuevos talentos al cobijar sus proyectos junto a los de cineastas consagrados, para hacer del FICXILITLA un escenario de creación de industria.</p>
      <p>Durante el festival, en nuestra programación contamos con pitchings, conferencias, master clases y talleres impartidos por figuras con trayectoria en el ámbito cinematográfico.</p>
      <p>El también llamado “Xilitla Film Fest”, cuenta con competencias nacionales e internacionales para cortometrajes y largometrajes de distintos géneros dentro de la fantasía, los cuales son reconocidos con la Presea James.</p>
      <p>Las preseas son otorgadas por un equipo de jurados nacionales e internacionales en los que destacan los nombres de Lena Vurma, Thor Klein, Fernando Delgado, Olivia Portillo y Gabriel Gutiérrez.</p>
      <p>Este año, estrenamos una residencia para consolidar proyectos en donde profesionales de la industria, darán seguimiento y asesoría para materializar esos sueños en la pantalla grande.</p>
      <p>Apoyados por nuestras sedes, ofrecemos experiencias turísticas, holísticas y gastronómicas a nuestras y nuestros realizadores de forma gratuita para hacer más grata su experiencia dentro de Xilitla.</p>
      <p>El FICXILITLA está arropado por la Red Iberoamericana de Festivales de Cine Iberoamericano (REDIBEROFEST) y por UNIFEST. Por los que nuestros proyectos ganadores son exhibidos en otros espacios y festivales durante un año, dando así, una continuidad al apoyo de exhibición del cine mexicano.</p>
    </section>
    <section class="section photo-grid venue-grid">
      <img src="assets/quienes/02.jpg" alt="Público en una función del festival">
      <img src="assets/quienes/03.jpg" alt="Invitados del festival">
      <img src="assets/quienes/04.jpg" alt="Actividades de FICXILITLA">
      <img src="assets/quienes/05.jpg" alt="Proyección al aire libre">
      <img src="assets/quienes/06.jpg" alt="Xilitla durante el festival">
    </section>
""",
)

pages["convocatoria.html"] = page(
    "Convocatoria — FIC Xilitla",
    "",
    "convocatoria",
    """    <section class="page-hero" style="background-image:url('assets/home/convocatoria-hero.jpg')">
      <h1>Convocatoria</h1>
    </section>
    <section class="section prose">
      <h2>Cortometraje Xilitlense</h2>
      <h3>Concurso de cortometraje con celular de Centro James y FICXILITLA</h3>
      <p>El Centro James y el Festival Internacional de Cine de Xilitla (FICXILITLA), convoca a jóvenes de Xilitla y comunidades de la región a participar en el:</p>
      <p><strong>Premio audiovisual Juvenil Centro James 2026</strong></p>
      <p><strong>“Edward James: ¿Qué representa para ti?”</strong></p>
      <p>Con el objetivo de incentivar la expresión audiovisual de las juventudes, promover el trabajo en equipo, fortalecer las narrativas locales y generar espacios para contar historias desde el propio entorno, el Centro James abre esta convocatoria dirigida a jóvenes creadoras y creadores interesados en realizar un cortometraje utilizando un teléfono celular o videocámara.</p>
      <p>La iniciativa busca generar espacios para imaginar, narrar, documentar y reflexionar sobre el legado de Edward James desde experiencias personales, comunitarias y creativas, dando voz a las juventudes de la región mediante el lenguaje audiovisual.</p>
      <h2>1. Participantes</h2>
      <p>Podrán participar jóvenes de entre 14 y 22 años residentes de Xilitla y municipios o comunidades cercanas, de manera individual o en equipo.</p>
      <p>En caso de participación grupal, deberá designarse una persona representante del proyecto.</p>
      <p>Las personas menores de edad deberán contar con autorización firmada de madre, padre o tutor para participar.</p>
      <h2>2. Tema</h2>
      <p>Los cortometrajes deberán responder al tema:</p>
      <p><strong>“Edward James: ¿Qué representa para ti y cómo influye en tu vida?”</strong></p>
      <p>Las obras podrán abordar el tema desde perspectivas personales, comunitarias, históricas, simbólicas, sociales, artísticas o imaginativas.</p>
      <p>Se podrán contar historias inspiradas en experiencias reales, recuerdos, reflexiones, leyendas, transformaciones del entorno o interpretaciones libres vinculadas al legado de Edward James.</p>
      <p>Las propuestas podrán explorar preguntas como:</p>
      <ul>
        <li>¿Qué representa Edward James para tu comunidad?</li>
        <li>¿Cómo ha influido en tu vida, entorno o manera de imaginar el mundo?</li>
        <li>¿Qué cambios culturales, sociales o simbólicos ha dejado su presencia en Xilitla?</li>
        <li>¿Cómo dialoga su legado con la juventud actual?</li>
      </ul>
      <h2>3. Formato de realización</h2>
      <p>Los cortometrajes deberán:</p>
      <ul>
        <li>Ser realizados con teléfono celular o videocámara.</li>
        <li>Tener una duración máxima de 10 minutos, incluyendo créditos.</li>
        <li>Haberse realizado específicamente para esta convocatoria.</li>
        <li>Presentarse en ficción, documental o híbrido.</li>
      </ul>
      <p>Se permite el uso de entrevistas, actuaciones, recreaciones, animación, archivo familiar, música y cualquier recurso creativo que fortalezca la narrativa audiovisual.</p>
      <h2>4. Criterios de evaluación</h2>
      <ul>
        <li>Relación y pertinencia con el tema de la convocatoria.</li>
        <li>Creatividad y propuesta narrativa.</li>
        <li>Calidad técnica de acuerdo con los recursos disponibles.</li>
        <li>Uso audiovisual del lenguaje cinematográfico.</li>
        <li>Originalidad.</li>
        <li>Capacidad para comunicar una historia o idea.</li>
        <li>Trabajo colectivo, apropiación del entorno y valor expresivo de la propuesta.</li>
      </ul>
      <h2>5. Reconocimientos y estímulos</h2>
      <p>Centro James otorgará apoyos económicos a los proyectos seleccionados.</p>
      <ul>
        <li>Primer lugar: hasta $10,000 MXN</li>
        <li>Segundo lugar: hasta $5,000 MXN</li>
        <li>Tercer lugar: hasta $2,500 MXN</li>
      </ul>
      <p>Los apoyos podrán consistir en estímulos económicos, en especie o en beneficios equivalentes, como mentorías, asesorías y experiencias formativas. El comité evaluador podrá determinar la naturaleza, modalidad y valor de cada apoyo, o declarar desierto cualquiera de los estímulos.</p>
      <h2>6. Selección y exhibición</h2>
      <p>Los cortometrajes con mejor evaluación formarán parte de una selección especial presentada en el marco de FICXILITLA 4, a celebrarse del 2 al 6 de diciembre de 2026.</p>
      <p>La presente convocatoria forma parte de las actividades culturales vinculadas a FICXILITLA; sin embargo, constituye una iniciativa independiente impulsada por el Centro James.</p>
      <h2>7. Bases de participación</h2>
      <p>La convocatoria estará abierta del 31 de julio al 17 de septiembre de 2026 a las 23:59 h.</p>
      <p>Los proyectos deberán enviarse a <a href="mailto:ficxilitlaslp@gmail.com">ficxilitlaslp@gmail.com</a> mediante un enlace de Google Drive con permisos de visualización o descarga.</p>
      <p>El correo deberá incluir: nombre del proyecto, duración, nombre completo de la persona representante, edad, correo, teléfono, nombres de participantes, municipio o comunidad de procedencia, y carta de autorización de madre, padre o tutor en caso de menores de edad.</p>
      <p>Cada participante o equipo podrá registrar únicamente un proyecto. Los proyectos seleccionados serán notificados vía correo electrónico previo al festival.</p>
      <h2>8. Consideraciones finales</h2>
      <p>La participación implica la aceptación de las presentes bases. Cualquier situación no prevista será resuelta por el comité organizador del Centro James y FICXILITLA.</p>
    </section>
""",
)

pages["sedes.html"] = page(
    "Sedes — FIC Xilitla",
    "",
    "sedes",
    """    <section class="section">
      <h1>Sedes</h1>
      <p class="lede">El FICXILITLA se llevará a cabo en distintas sedes emblemáticas del Pueblo Mágico de Xilitla, entre las que destacan el Jardín Escultórico Edward James, la Plaza Principal de Xilitla, Cervecería James, el Museo Leonora Carrington Xilitla y el Museo Edward James.</p>
      <p>El festival dará inicio el 2 de diciembre en Cervecería James con la presencia de realizadores e invitados especiales de la cinta inaugural.</p>
      <p>Posteriormente, a partir del 3 de diciembre, se realizarán proyecciones de muestras y competencias oficiales en todas las sedes participantes. Asimismo, se presentarán premieres y funciones especiales acompañadas por sus realizadores.</p>
      <p>Comprometidos con la formación y el intercambio cultural, el festival contará con talleres, conferencias y enlaces virtuales con cineastas internacionales.</p>
      <p>La ceremonia de premiación se llevará a cabo el 5 de diciembre en Cervecería James, y la clausura el 6 de diciembre en la plaza principal de Xilitla, acompañada por la gran pantalla itinerante de la Cineteca Alameda.</p>
    </section>
    <section class="section">
      <h2>Nuestras sedes</h2>
      <div class="venue-grid">
        <article class="venue-card">
          <img src="assets/sedes/museo-edward-james.jpg" alt="Museo Edward James">
          <h2>Museo Edward James</h2>
          <p>Primer museo dedicado a Edward James, figura clave del arte moderno, inaugurado en el 2022.</p>
        </article>
        <article class="venue-card">
          <img src="assets/sedes/cerveceria-james.jpg" alt="Cervecería James">
          <h2>Cervecería James</h2>
          <p>Cervecería de bebidas artesanales ubicada frente al Jardín Escultórico de Edward James.</p>
        </article>
        <article class="venue-card">
          <img src="assets/sedes/jardin-edward-james.jpg" alt="Jardín Escultórico de Edward James">
          <h2>Jardín Escultórico de Edward James</h2>
          <p>Creado por Edward James, excéntrico poeta, artista británico y mecenas del movimiento surrealista. Entre cascadas y pozas, un laberinto surrealista se abre paso.</p>
        </article>
        <article class="venue-card">
          <img src="assets/sedes/museo-leonora-carrington.jpg" alt="Museo Leonora Carrington Xilitla">
          <h2>Museo Leonora Carrington Xilitla</h2>
          <p>Dedicado a Leonora Carrington. El recinto alberga una colección de escultura, litografía y dibujo. Fue íntima amiga del poeta y coleccionista Edward James.</p>
        </article>
        <article class="venue-card">
          <img src="assets/sedes/cineteca-alameda.jpg" alt="Cineteca Alameda itinerante">
          <h2>Cineteca Alameda (Itinerante)</h2>
          <p>Exhibición itinerante de la Cineteca Alameda de la capital de S.L.P.</p>
        </article>
      </div>
    </section>
""",
)

pages["programa.html"] = page(
    "Programa — FIC Xilitla",
    "",
    "programa",
    """    <section class="section" style="text-align:center">
      <h1>Descarga nuestro programa</h1>
      <p class="lede">Entérate de todas las actividades del festival y planifica tu experiencia.</p>
      <div class="cta-row" style="justify-content:center">
        <a class="btn btn-solid" href="assets/ProgFicXilComp.pdf">Descargar PDF</a>
      </div>
    </section>
""",
)

noticias = [
    (
        "esta-es-la-pelicula-mas-taquillera-de-rusia",
        "Esta es la película más taquillera de Rusia que hizo enojar a Vladimir Putin; entrevista con su director, Michael Lockshin",
        "ficxilitla SLP · 10/07/25",
        "noticias/01.png",
        "https://www.eluniversal.com.mx/espectaculos/esta-es-la-pelicula-mas-taquillera-de-rusia-que-hizo-enojar-a-vladimir-putin-llega-a-mexico/",
    ),
    (
        "homenajearan-a-silvia-pinal",
        "Homenajearán a Silvia Pinal en 2ª edición de FICXILITLA",
        "ficxilitla SLP · 11/03/19",
        "noticias/02.png",
        "https://24-horas.mx/principales/homenajearan-a-silvia-pinal-en-2a-edicion-de-ficxilitla/",
    ),
    (
        "inaugura-el-ficxilitla-2024",
        "Inaugura el FICXILITLA 2024",
        "ficxilitla SLP · 11/03/19",
        "noticias/03.png",
        "https://oem.com.mx/elsoldesanluis/cultura/inaugura-el-ficxilitla-2024-18439659",
    ),
    (
        "cine-y-surrealismo-ficxilitla-2024",
        "Cine y surrealismo: El FICXILITLA 2024 celebra su 2a. edición",
        "ficxilitla SLP · 11/03/19",
        "noticias/04.png",
        "https://escandala.com/cine-y-surrealismo-el-ficxilitla-2024-celebra-su-2a-edicion/",
    ),
    (
        "festival-reconocera-a-silvia-pinal",
        'Festival de Cine de Xilitla reconocerá a "la dama del cine surrealista" Silvia Pinal',
        "ficxilitla SLP · 11/03/19",
        "noticias/05.png",
        "https://www.milenio.com/cultura/rendira-homenaje-festival-internacional-cine-xilitla-silvia-pinal",
    ),
]

cards = []
for slug, title, date, img, url in noticias:
    cards.append(
        f"""        <article class="news-card">
          <a href="{url}" rel="noopener noreferrer"><img src="assets/{img}" alt="{title}"></a>
          <div>
            <p class="credit">{date}</p>
            <h2><a href="{url}" rel="noopener noreferrer">{title}</a></h2>
            <p>Haz clic en la imagen para ir a la noticia.</p>
            <a class="btn" href="{url}" rel="noopener noreferrer">Leer más</a>
          </div>
        </article>"""
    )

pages["noticias.html"] = page(
    "Noticias — FIC Xilitla",
    "",
    "noticias",
    f"""    <section class="section">
      <h1>Noticias</h1>
      <div class="news-grid">
{chr(10).join(cards)}
      </div>
    </section>
""",
)

gallery_btns = "\n".join(
    f"""        <button type="button" data-full="assets/galeria/{i:02d}.jpg">
          <img src="assets/galeria/{i:02d}.jpg" alt="FICXILITLA edición 2024, foto {i}">
        </button>"""
    for i in range(1, 27)
)

pages["edicion-2024.html"] = page(
    "Edición 2024 — FIC Xilitla",
    "",
    "g2024",
    f"""    <section class="section">
      <h1>Edición 2024</h1>
      <div class="gallery-grid">
{gallery_btns}
      </div>
    </section>
    <div class="lightbox" role="dialog" aria-modal="true">
      <button class="lightbox-close" type="button" aria-label="Cerrar">&times;</button>
      <img alt="">
    </div>
""",
)

pages["edicion-2025.html"] = page(
    "Edición 2025 — FIC Xilitla",
    "",
    "g2025",
    """    <section class="section">
      <h1>Edición 2025</h1>
      <p class="empty">La galería de esta edición se publicará pronto.</p>
    </section>
""",
)

pages["404.html"] = page(
    "No encontrada — FIC Xilitla",
    "",
    "",
    """    <section class="section" style="text-align:center">
      <h1>Página no encontrada</h1>
      <p><a class="btn" href="index.html">Volver al inicio</a></p>
    </section>
""",
)

for name, html in pages.items():
    (ROOT / name).write_text(html, encoding="utf-8")
    print("wrote", name)

(ROOT / "edicion2024.html").write_text(
    """<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=edicion-2024.html"><link rel="canonical" href="/edicion-2024.html"><title>Redirigiendo</title></head><body><p><a href="edicion-2024.html">Edición 2024</a></p></body></html>
""",
    encoding="utf-8",
)

(ROOT / "_redirects").write_text(
    """/ /index.html 200
/quienes-somos /quienes-somos.html 200
/convocatoria /convocatoria.html 200
/sedes /sedes.html 200
/programa /programa.html 200
/noticias /noticias.html 200
/edicion-2024 /edicion-2024.html 200
/edicion2024 /edicion-2024.html 200
/edicion-2025 /edicion-2025.html 200
/galera /edicion-2024.html 200
/s/ProgFicXilComp-hatc.pdf /assets/ProgFicXilComp.pdf 200
""",
    encoding="utf-8",
)
print("done")
