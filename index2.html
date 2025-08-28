<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="color-scheme" content="dark" />
  <title>Drácula</title>
  <link rel="preload" as="font" href="assets/fonts/Berani.woff2" type="font/woff2" crossorigin>
  <link rel="preload" as="font" href="assets/fonts/JollyLodger-Regular.woff2" type="font/woff2" crossorigin>
  <link rel="preload" as="font" href="assets/fonts/Screature.woff2" type="font/woff2" crossorigin>


  <!-- Tailwind (CDN) -->
  <script src="https://cdn.tailwindcss.com"></script>

  <style>

    /* === Asignación de tipografías global === */
body{
  font-family: "Jolly Lodger", system-ui, sans-serif; /* Párrafos */
}
h1,h2,h3,h4,h5,h6,
.font-titulo{
  font-family: "Berani", system-ui, sans-serif;       /* Títulos */
  letter-spacing: .01em;
}
/* CTA: añade esta clase a los botones/enlaces de acción */
.font-cta, .cta, .btn-cta{
  font-family: "Screature", system-ui, sans-serif;    /* CTAs */
  letter-spacing: .04em;
  text-transform: uppercase;
}


    /* Títulos */
@font-face{
  font-family: "Berani";
  src: url("assets/fonts/Berani.woff2") format("woff2"),
       url("assets/fonts/Berani.woff") format("woff");
  font-weight: 200; /* peso */
  font-style: normal;
  font-display: swap;
  
}

/* Párrafos */
@font-face{
  font-family: "Jolly Lodger";
  src: url("assets/fonts/JollyLodger-Regular.woff2") format("woff2"),
       url("assets/fonts/JollyLodger-Regular.woff") format("woff");
  font-weight: 100;
  font-style: normal;
  font-display: swap;
}

/* CTAs */
@font-face{
  font-family: "Screature";
  src: url("assets/fonts/Screature.woff2") format("woff2"),
       url("assets/fonts/Screature.woff") format("woff");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

/* TITULOS: siempre Berani */
h1,h2,h3,h4,h5,h6, .font-titulo{
  font-family: "Berani", system-ui, sans-serif !important;
  line-height: 1.08;            
  letter-spacing: .02em;
}

/* PARRAFOS: Jolly Lodger más legible */
p, .font-parrafo{
  font-family: "Jolly Lodger", system-ui, sans-serif;
  font-size: clamp(15px, 1.65vw, 18px);
  line-height: 1.6;
  letter-spacing: .015em;
}

/* CTAs: limitar la fuente Screature SOLO a botones/enlaces de acción */
a.font-cta, button.font-cta, a.cta, button.cta, .btn-cta{
  font-family: "Screature", system-ui, sans-serif !important;
  letter-spacing: .04em;
  text-transform: uppercase;
}

/* Si algún contenedor .cta/.font-cta envuelve títulos, forzamos que los h1–h6 sigan en Berani */
.font-cta h1, .font-cta h2, .font-cta h3,
.cta h1, .cta h2, .cta h3{
  font-family: "Berani", system-ui, sans-serif !important;
  text-transform: none;
}


    .vignette::after { content:""; position:absolute; inset:0; pointer-events:none; box-shadow: inset 0 0 160px rgba(0,0,0,.8); }
    .willchange-transform { will-change: transform; }
    .nav-item.is-active .off { opacity: 0 !important; }
    .nav-item.is-active .on  { opacity: 1 !important; }
      html, body {
    width: 100%;
    max-width: 100%;
    overflow-x: hidden;            
    overscroll-behavior-x: none;   
    touch-action: pan-y;           
    position: relative;

    #libro {
  position: relative;
  overflow: hidden; 
}

    

    
  }
    
  </style>

<!-- === BEGIN estilos del LIBRO (importados de libro.html) === -->
<style>
    html, body { max-width:100%; overflow-x:hidden; touch-action:pan-y; }
    .hidden { display:none !important; }

    /* Botones ON/OFF (medallas, flechas, iconos) */
    .btn-swap { position: relative; width: 72px; height: 72px; }
    .btn-swap img { position:absolute; inset:0; width:100%; height:100%; object-fit:contain; transition:opacity .15s ease; }
    .btn-swap .on { opacity:0; }
    .btn-swap:hover .on, .btn-swap.is-active .on { opacity:1; }
    .btn-swap:hover .off, .btn-swap.is-active .off { opacity:0; }

    /* Barra de categorías (encima del libro) */
    .realm-bar { position:absolute; left:50%; transform:translateX(-50%); top:9%; z-index:30; display:flex; align-items:center; gap:.5rem; }
    @media (min-width:768px){ .realm-bar { gap:.75rem; } }
    .realm-tab { width:72px; height:72px; }
    @media (min-width:768px){ .realm-tab { width:80px; height:80px; } }

    /* Navegación lateral (flechas) */
    .side-nav { position:absolute; top:45%; transform:translateY(-50%); z-index:20; }
    @media (max-width:640px){
      .side-nav { top:48%; }
    }

    /* Área de páginas (ajustada a la imagen del libro) */
    .pages-area { position:absolute; top:18%; left:9.5%; width:81%; height:60%; }
    .page-left  { position:absolute; top:0; left:40px;   width:44.5%; height:100%; padding:1rem; }
    .page-right { position:absolute; top:0; right:23px; width:46.5%; height:100%; padding:1rem; }

    /* Ajustes responsive de páginas dentro del libro */
    @media (max-width:1024px){
      .pages-area { top:16%; left:8.5%; width:83%; height:60%; }
      .page-left { left:34px; }
      .page-right { right:18px; }
    }
    @media (max-width:640px){
      .pages-area { top:17%; left:6.5%; width:85%; height:58%; }
      .page-left { left:26px; padding:.75rem; }
      .page-right { right:13px; padding:.75rem; }
    }

    /* Fichas a doble página (subidas un poco respecto al atril) */
    .pages-area.ficha { top:20.5%; height:34%; }
    @media (min-width:1280px){ .pages-area.ficha { top:20%; height:35%; } }
    @media (max-width:1024px){ .pages-area.ficha { top:21%; height:33.5%; } }
    @media (max-width:640px){ .pages-area.ficha { top:20%; height:33%; } }

    /* Barra de acciones sobre la ficha (encima de la página izquierda) */
    .action-bar{
      position:absolute;
      z-index:28;
      top:1%;
      left:9.8%;
      width:34.2%;
      display:flex;
      justify-content:space-between;
      gap:1rem;
      pointer-events:auto;
      filter: drop-shadow(0 0 8px rgba(0,0,0,.35));
    }
    @media (max-width:1024px){
      .action-bar{ top:-2%; left:11.8%; width:31.8%; }
    }
    @media (max-width:640px){
      .action-bar{ top:-7%; left:15.5%; width:26.5%; }
      .btn-swap{ width:64px; height:64px; }
    }

    /* Tarjeta monstruo (cuadrícula de miniaturas) */
    .monster { background:rgba(120,53,15,.04); transition:transform .2s ease, background .2s ease; }
    .monster .thumb { width:100%; aspect-ratio:1/1; background:rgba(120,53,15,.12); object-fit:content; }
    .monster:hover { background: rgba(120,53,15,.15); transform: scale(1.02); }

    /* Toast simple */
    #toast{ position:fixed; left:50%; transform:translateX(-50%); bottom:1.75rem; z-index:60; background:rgba(16,185,129,.95); color:#fff; padding:.6rem 1rem; border-radius:.75rem; box-shadow:0 8px 30px rgba(0,0,0,.35); font-weight:600; letter-spacing:.02em; }

    /* Iconos del HOME (tamaño fluido) */
    .icon-btn { width:clamp(64px, 8.5vw, 96px); height:clamp(64px, 8.5vw, 96px); }

    /* --- Ajuste vertical del HOME (intro) --- */
    #pagina-home{
      top: 20.5%;
      height: 58%;
    }
    @media (min-width: 1280px){
      #pagina-home{ top: 21.5%; height: 56%; }
    }
    @media (max-width: 768px){
      #pagina-home{ top: 17%; height: 54%; }
    }
    #pagina-home .page-left{  padding-top: 1.25rem; }
    #pagina-home .page-right{ padding-top: 1.25rem; }

    /* Íconos de la HOME más pequeños en móvil */
    @media (max-width:640px){
      .icon-btn{
        width: clamp(39px, 13vw, 58px);
        height: clamp(39px, 13vw, 54px);
      }
      #grid-home{ gap: .5rem; }
    }

    /* Medallas (barra superior) también un poco más pequeñas en móvil */
    @media (max-width:640px){
      .realm-tab{
        width: 56px;
        height: 56px;
      }
    }

    /* --- CTA SALIR AL BOSQUE (imagen ON/OFF pegada al libro) --- */
    #cta-salir{
      position:absolute;
      left:50%; transform:translateX(-50%);
      bottom: 25.5%;
      z-index:22;
      filter: drop-shadow(0 8px 18px rgba(0,0,0,.45));
    }
    .cta-swap{
      width: clamp(220px, 36vw, 520px);
      aspect-ratio: 354 / 150;
      height:auto;
    }
    @media (min-width:1280px){
      #cta-salir{ bottom: 26.5%; }
    }
    @media (max-width:768px){
      #cta-salir{ bottom:25% !important; }
      .cta-swap{ width: clamp(200px, 50vw, 420px); }
    }

    /* Título de la home encima de los iconos */
    .home-heading{
      width: clamp(220px, 55%, 520px);
      filter: drop-shadow(0 4px 10px rgba(0,0,0,.35));
      margin-bottom: .3rem;
    }

    /* (pequeño fix) faltaba la unidad en móvil */
    @media (max-width:768px){
      #cta-salir{ bottom: 20px; } 
    }

    /* Desktop: empuja el título hacia la derecha */
    @media (min-width:1024px){
      .home-heading{
        margin-left: clamp(16px, 3vw, 56px);
      }
    }

    /* ==========================
       Destacados sobre la intro
       ========================== */
    .hero-monster{
      position:absolute;
      z-index:26;                  
      top:7%;
      left:10%;
      width: clamp(140px, 26%, 240px);
      height:auto;
      filter: drop-shadow(0 6px 18px rgba(0,0,0,.45));
      transition: transform .18s ease, filter .18s ease;
    }
    .hero-monster:hover{ transform: translateY(-2px) scale(1.02); }

    /* Ajustes responsivos */
    @media (max-width:1024px){
      .hero-monster{ top:6%; left:9%; width: clamp(120px, 28%, 210px); }
    }
    @media (max-width:640px){
      .hero-monster{ top:5%; left:8%; width: clamp(110px, 34%, 200px); }
    }

    /* Modificadores por reino (tócalos si quieres mover un poco) */
    .hero-monster--vamp{ left:11%; top:8%; }

    /* DRACUTÁNICOS — más pequeño */
.hero-monster--vamp{
  top: 45%;
  left: 26%;
  /* ↓ reduce tamaño en desktop */
  width: clamp(120px, 22%, 160px);
}
@media (max-width:1024px){
  .hero-monster--vamp{
    top: 14%; left: 24%;
    width: clamp(76px, 20%, 140px);
  }
}
@media (max-width:640px){
  .hero-monster--vamp{
    top: 50%; left: 35%;
    /* ↓ bastante más pequeño en móvil */
    width: clamp(50px, 22%, 110px);
  }
}

/* ZELVIRA — más pequeño */
.hero-monster--floral{
  top: 50%;
  left: 30%;
  width: clamp(90px, 22%, 160px);
}
@media (max-width:1024px){
  .hero-monster--floral{
    top: 14%; left: 24%;
    width: clamp(76px, 20%, 140px);
  }
}
@media (max-width:640px){
  .hero-monster--floral{
    top: 55%; left: 35%;
    width: clamp(45px, 22%, 110px);
  }
}

/* === Fusión MULTIPLY en iconos y fichas === */
/* Aísla el libro para que el blend no afecte fuera */
#libro .relative{ isolation:isolate; }

/* Aplica a: medallas/flechas/home (btn-swap), miniaturas de monstruo, fichas y destacados */
.btn-swap img,
.monster .thumb,
.pages-area.ficha > img,
.hero-monster img{
  mix-blend-mode: multiply;
}

/* (Opcional) si algún asset se ve demasiado oscuro, puedes suavizarlo con esta clase extra */
.blend-soft{ opacity:.9; }

/* === Fusión MULTIPLY en iconos, miniaturas, fichas, destacados e INTROS === */
#libro .relative{ isolation:isolate; }

.btn-swap img,               /* medallas, flechas, home */
.monster .thumb,             /* miniaturas */
.pages-area.ficha > img,     /* fichas a doble página */
.hero-monster img,           /* destacados sobre la intro */
.pages-area .page-left > img,/* INTROS (imagen grande de la página izquierda) */
.pages-area .page-right > img/* por si usas intros en la derecha */
{
  mix-blend-mode: multiply;
}


.blend-soft{ opacity:.9; }
.blend-normal{ mix-blend-mode: normal !important; }


  /* ============================
    MARCOS DEL LIBRO (por reino)
    ============================ */

  /* Aísla el libro para que el blend no “salga” del contenedor */
  #libro .relative{ isolation:isolate; }

  /* Base del overlay de marco sobre cada pages-area */
  .pages-area::after{
    content:"";
    position:absolute;
    /* un pelín más ancho/alto que el área para que quede pegado al papel */
    left:-0.5%;
    right:-0.5%;
    top:-35%;      /* ⬅️ sube el marco (más negativo = más arriba) */
    bottom:-1.2%;
    background-position:center;
    background-repeat:no-repeat;
    background-size:contain;   
    pointer-events:none;
    z-index:25;                
    mix-blend-mode:multiply;   
    display:none;              
  }

/* FICHA — marco más bajo (menos alto superior/inferior) */
.pages-area.ficha::after{
  background-size: 100% 100%;
  background-position: center;
  /*         top   right  bottom left  */
  inset:   -19%   -1.6%   -9%   -1.6%;
  mix-blend-mode: multiply;
  z-index: 25;
  pointer-events: none;
}

/* Ajustes por reino (todos aún más bajos que antes) */
#libro[data-realm="bestial"]   .pages-area.ficha::after{ inset: -17% -1.6% -10% -1.6%; }
#libro[data-realm="vampirico"] .pages-area.ficha::after{ inset: -17% -1.6% -10% -1.6%; }
#libro[data-realm="floral"]    .pages-area.ficha::after{ inset: -16% -1.6%  -9% -1.6%;  }
#libro[data-realm="pantano"]   .pages-area.ficha::after{ inset: -16% -1.6%  -9% -1.6%;  }
#libro[data-realm="rocoso"]    .pages-area.ficha::after{ inset: -16% -1.6%  -9% -1.6%;  }

/* Tablet */
@media (max-width:1024px){
  .pages-area.ficha::after{ inset: -17% -1.8% -10% -1.8%; }
}
/* Móvil */
@media (max-width:640px){
  .pages-area.ficha::after {
    inset: -10% -4% -15%  -1% !important;
  }
}






  

  /* Mostrar el marco solo en la página visible del reino actual */
  #libro[data-realm] .pages-area:not(.hidden)::after{ display:block; }

  /* ---- Marcos por reino (ajusta rutas si cambian) ---- */
  #libro[data-realm="pantano"]   .pages-area:not(.hidden)::after{
    background-image:url("assets/marcos/MARCO PANTANO.webp");
  }
  #libro[data-realm="bestial"]   .pages-area:not(.hidden)::after{
    background-image:url("assets/marcos/MARCO BESTIAL VERDE.webp");
  }
  #libro[data-realm="vampirico"] .pages-area:not(.hidden)::after{
    background-image:url("assets/marcos/MARCO VAMPIRICO NARANJA.webp");
  }
  #libro[data-realm="floral"]    .pages-area:not(.hidden)::after{
    background-image:url("assets/marcos/MARCO FLORAL ROSA.webp");
  }
  #libro[data-realm="rocoso"]    .pages-area:not(.hidden)::after{
    background-image:url("assets/marcos/MARCO ROCOSO PURPURA.webp");
  }

  /* ---- Ajustes responsivos (toca a gusto) ---- */
  @media (max-width:1024px){
    .pages-area::after{ top:-27.0%; bottom:-1.4%; }
    .pages-area.ficha::after{ top:-10.8%; bottom:-1.8%; }
  }
  @media (max-width:640px){
    .pages-area::after{ top:-30%; bottom:-1.6%; }
    .pages-area.ficha::after{ top:-9.2%; bottom:-2.0%; }
  }

  /* Utilidades opcionales */
  .pages-area--sin-marco::after{ display:none !important; }  /* por si quieres ocultarlo en alguna página */




  </style>
<!-- === END estilos del LIBRO === -->

</head>
<body class="bg-black text-white overflow-x-hidden antialiased">

<!-- ===== Header ===== -->
<header class="fixed inset-x-0 top-0 z-[100]">
  <div class="relative mx-auto mt-4 w-[94%] max-w-[1400px]">
    <div class="flex flex-col sm:flex-row items-center justify-center sm:justify-between px-4 md:px-6 py-2 bg-black/40 backdrop-blur-md rounded-3xl">
      <div class="flex items-center justify-center sm:justify-between w-full gap-12 sm:gap-0">
        <a href="#top" id="logo-home" aria-label="Ir al inicio" class="inline-block align-middle">
  <img src="assets/header/Logo Dracula.webp" alt="Drácula"
       class="h-[50px] sm:h-[42px] md:h-[50px] w-auto select-none pointer-events-none">
</a>

        <nav class="flex items-center gap-10 sm:gap-14">
          <!-- Corregido: href al id real del bestiario -->
          <!-- Bestiario → LIBRO -->
<a href="#libro" class="group relative inline-block nav-item" data-nav="bestiario" aria-label="El Bestiario">
  <img src="assets/header/OFF EL BESTIARIO.webp" alt="El Bestiario" class="off h-[40px] sm:h-[48px] md:h-[52px] w-auto select-none transition-opacity duration-200 ease-out group-hover:opacity-0">
  <img src="assets/header/ON EL BESTIARIO.webp" alt="" class="on pointer-events-none absolute inset-0 h-[40px] sm:h-[48px] md:h-[52px] w-auto select-none opacity-0 transition-opacity duration-200 ease-out group-hover:opacity-100">
</a>

<a href="#fortnite-cta" class="group relative inline-block nav-item mt-[2px]" data-nav="castillo" aria-label="El Castillo">
  <img src="assets/header/OFF El Castilo.webp" alt="El Castillo" class="off h-[50px] sm:h-[60px] md:h-[70px] w-auto select-none transition-opacity duration-200 ease-out group-hover:opacity-0">
  <img src="assets/header/ON El Castilo.webp" alt="" class="on pointer-events-none absolute inset-0 h-[50px] sm:h-[60px] md:h-[70px] w-auto select-none opacity-0 transition-opacity duration-200 ease-out group-hover:opacity-100">
</a>


          </a>
        </nav>
      </div>
    </div>
  </div>
</header>

<main class="relative z-0">
  <!-- Fondo bosque que llega hasta castillo -->
  <div class="bg-wrap absolute inset-x-0 top-0 -z-10 overflow-hidden" style="height: 100vh;">
    <img src="assets/Background Primera Sección.webp" alt="Fondo del bosque" class="bg-bosque w-full h-full object-cover object-center opacity-95 select-none willchange-transform">
  </div>

  <!-- ===== HERO ===== -->
  <section class="hero relative min-h-[100vh] md:h-[140vh] w-full overflow-visible z-10"></section>

  <!-- Luna HERO (z alto por defecto) -->
  <div class="moon absolute left-0 top-[calc(6vh-20px)] sm:top-[calc(8vh-20px)] md:top-[calc(6vh-50px)]
              w-[54vw] sm:w-[50vw] md:w-[46vw] max-w-[880px] aspect-square overflow-hidden z-[50] willchange-transform">
    <img src="assets/Luna Normal.webp" alt="Luna" class="w-full h-full object-cover pointer-events-none select-none">
  </div>

  <!-- ===== TRAILER ===== -->
  <section id="trailer" class="relative min-h-[100vh] md:h-[140vh] w-full overflow-visible z-10">
    <img src="assets/Background Primera Sección.webp" alt="" class="absolute inset-0 w-full h-full object-cover opacity-0 pointer-events-none select-none -z-10">
    <div class="mx-auto mt-24 md:mt-28 w-[92%] max-w-[1100px]">
      <div class="relative rounded-3xl border-4 border-lime-500/90 bg-black/40 backdrop-blur-sm overflow-hidden shadow-[0_0_40px_rgba(132,255,0,0.2)]">
        <video id="draculaTrailer" class="block w-full aspect-video object-cover" preload="metadata" playsinline muted controlslist="nodownload noplaybackrate" poster="assets/posters/trailer-poster.jpg">
          <source src="assets/video/dracula-trailer.mp4" type="video/mp4">
          Tu navegador no soporta video HTML5.
        </video>
        <button id="trailerPlay" class="group absolute inset-0 grid place-items-center transition-opacity duration-300">
          <span class="inline-grid place-items-center w-20 h-20 md:w-24 md:h-24 rounded-full bg-black/60 backdrop-blur text-white border-2 border-white/70 shadow-lg">
            <svg class="w-10 h-10 md:w-12 md:h-12 translate-x-[2px]" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
          </span>
        </button>
      </div>
      <div class="mt-6 text-center">
        <a href="#captura-bestias"
   class="font-titulo font-normal uppercase tracking-[.02em] inline-block
          text-xl sm:text-2xl md:text-[26px] leading-none
          px-6 md:px-7 py-3 md:py-3.5
          border-2 border-lime-500 text-white
          bg-black hover:bg-lime-500 hover:text-black
          transition-colors duration-300">
  EXPLORA UNA NUEVA AVENTURA
</a>

        <div class="mt-3 animate-bounce text-lime-500">
          <svg class="w-6 h-6 mx-auto" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z" clip-rule="evenodd"/></svg>
        </div>
      </div>
    </div>
  </section>

  <!-- Nubes hero/trailer -->
  <div class="cloud-right-wrap absolute right-0 top-[60vh] sm:top-[62vh] md:top-[66vh] w-[32vw] sm:w-[28vw] md:w-[24vw] overflow-hidden z-[3] willchange-transform">
    <div class="cloud-right relative w-[66vw] sm:w-[50vw] md:w-[36vw] aspect-[2/1] willchange-transform"
         style="-webkit-mask-image:linear-gradient(to left, rgba(0,0,0,0.1), rgba(0,0,0,1) 22%, rgba(0,0,0,1));
                mask-image:linear-gradient(to left, rgba(0,0,0,0.1), rgba(0,0,0,1) 22%, rgba(0,0,0,0.1));">
      <img src="assets/Nube Morada A.webp" alt="Nube derecha" class="w-full h-full object-cover pointer-events-none select-none transform -scale-x-100">
    </div>
  </div>
  <div class="cloud-left-wrap absolute left-[-5vw] top-[55vh] sm:top-[58vh] md:top-[50vh] w-[40vw] sm:w-[35vw] md:w-[30vw] overflow-hidden z-[50] willchange-transform">
    <div class="cloud-left relative w-full aspect-[2/1] willchange-transform">
      <img src="assets/Nube Morada A.webp" alt="Nube izquierda grande" class="w-full h-full object-cover pointer-events-none select-none">
    </div>
  </div>
  <div class="cloud-low absolute right-[-11vh] top-[92vh] sm:top-[91vh] md:top-[90vh] w-[80vw] sm:w-[60vw] md:w-[46vw] max-w-[900px] aspect-[2/1] opacity-80 z-[90] willchange-transform">
    <img src="assets/Nube Morada Blurr B.webp" alt="Nube baja derecha" class="w-full h-full object-cover pointer-events-none select-none">
  </div>
  <div class="cloud-low-left absolute left-[-11vh] top-[96vh] sm:top-[95vh] md:top-[99vh] w-[80vw] sm:w-[60vw] md:w-[46vw] max-w-[900px] aspect-[2/1] opacity-80 z-[90] willchange-transform">
    <img src="assets/Nube Morada Blurr B.webp" alt="Nube baja izquierda" class="w-full h-full object-cover pointer-events-none select-none transform -scale-x-100">
  </div>

  <!-- Niebla -->
  <div class="fixed top-[60vh] left-0 right-0 w-full h-[40vh] z-[50] pointer-events-none">
    <img src="assets/Niebla General (1).webp" alt="Niebla general" class="w-full h-full object-fill select-none pointer-events-none" />
  </div>

  <!-- Sello + CTA -->
  <div class="title absolute left-1/2 -translate-x-1/2 
            top-[20vh] sm:top-[24vh] md:top-[17vh] 
            max-[639px]:top-[28vh]
            w-[72vw] sm:w-[52vw] md:w-[44vw] max-w-[450px] 
            z-[60] willchange-transform flex flex-col items-center
            gap-0 sm:gap-3 md:gap-0">
    <img src="assets/Sello A.webp" alt="Secretos del Bosque Prohibido" class="w-full h-full object-contain mx-auto pointer-events-none select-none">
    <div class="mt-6 flex flex-col items-center">
      <a href="#trailer"
   class="font-titulo font-normal uppercase tracking-[.02em]
          text-xl sm:text-2xl md:text-[26px] leading-none
          px-6 md:px-7 py-3 md:py-3.5
          border-2 border-lime-500 text-white
          bg-black hover:bg-lime-500 hover:text-black
          transition-colors duration-300">
  CONOCE LA HISTORIA
</a>

      <div class="mt-3 animate-bounce">
        <svg class="w-6 h-6 text-lime-500" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z" clip-rule="evenodd"/></svg>
      </div>
      <p class="mt-10 sm:mt-3 md:mt-0 
          text-sm sm:text-base text-gray-300 text-center 
          leading-snug max-w-xs flex items-center justify-center gap-2">
          <p class="mt-10 sm:mt-3 md:mt-4 
          text-sm sm:text-base text-gray-300 text-center 
          leading-snug max-w-xs flex flex-col sm:flex-row items-center justify-center gap-2">
  <!-- Icono -->
 <img src="assets/icons/Icon Scroll.svg" alt="Icono Scroll"
     class="block mx-auto w-6 h-6 sm:w-5 sm:h-5 -mt-6 sm:mt-0 animate-soft-blink">


  
<p class="text-center -mt-20 sm:mt-0 text-[clamp(16px,3.6vw,24px)] leading-[1.3] opacity-90">
  Haz scroll con la barra del mouse para comenzar la aventura
</p>



<style>
/* Titileo suave */
@keyframes soft-blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; } 
}
.animate-soft-blink {
  animation: soft-blink 2.5s ease-in-out infinite; 
}
</style>


    </div>
  </div>

  <!-- ===== BESTIARIO ===== -->
  <section id="captura-bestias" class="relative z-10 min-h-[100vh] md:min-h-[110vh] flex flex-col md:flex-row-reverse items-center justify-center p-6 overflow-visible">
    <!-- nubes verdes decorativas -->
    <div class="absolute top-10 right-[-1rem] w-40 sm:w-48 md:w-64 lg:w-80 opacity-90 -z-10 pointer-events-none">
      <img src="assets/Nube Verde B.webp" alt="Nube Verde B" class="w-full h-auto object-contain select-none" />
    </div>
    <div class="absolute -bottom-16 sm:-bottom-20 md:-bottom-24 lg:-bottom-40 left-6 sm:left-8 md:left-12 w-56 sm:w-72 md:w-96 lg:w-[28rem] opacity-90 -z-10 pointer-events-none">
      <img src="assets/Nube Verde B.webp" alt="Nube Verde B" class="w-full h-auto object-contain select-none" />
    </div>
    <div class="absolute top-[-8vh] sm:top-[-34vh] left-[-4vw] sm:left-[-5vw] w-56 sm:w-72 md:w-96 lg:w-[28rem] opacity-90 -z-10 pointer-events-none" id="nube-c">
      <img src="assets/Nube Verde B.webp" alt="Nube Verde B" class="w-full h-auto object-contain select-none" />
    </div>

    <!-- Castillo maqueta + LUNA VERDE -->
    <div class="relative -z-30 mt-8 md:mt-0 md:mr-12 w-[80vw] sm:w-[70vw] md:w-[60vw] max-w-[600px]">
      <img
  src="assets/Castillo Maqueta.webp"
  alt="Castillo Maqueta"
  class="w-full h-auto select-none pointer-events-none"
  style="
    -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
            mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 50%, rgba(0,0,0,0) 100%);
    mask-repeat: no-repeat; -webkit-mask-repeat: no-repeat;
    mask-size: 100% 100%; -webkit-mask-size: 100% 100%;
  "
/>

      <img src="assets/Luna Verde.webp" alt="Luna Verde"
           class="absolute top-[calc(-40vh-20px)]
                  max-[639px]:top-[-20vh]
                  sm:top-[calc(-35vh-20px)]
                  left-[-3vw]
                  w-[54vw] max-w-[880px] aspect-square
                  opacity-80 select-none pointer-events-none
                  -z-40 object-cover" />
    </div>

    <!-- Texto -->
<div class="relative z-30 max-w-xl text-white text-center p-4 md:p-8 flex flex-col items-center md:items-center mx-auto -mt-7 sm:mt-0">

<h2 class="font-titulo text-center uppercase tracking-[.02em] leading-[1.08] text-3xl md:text-5xl mb-0">
  CONVIÉRTETE EN EL<br>SEÑOR DEL CASTILLO DRÁCULA
</h2>

<div class="border-2 border-lime-500 bg-black text-white p-4 md:p-6 rounded-lg max-w-md mx-auto text-[15px] sm:text-[17px] md:text-[18px] lg:text-[19px] leading-[1.45] tracking-[.01em] text-center md:text-left mt-3 sm:mt-4 md:mt-5 mb-6">
  Lorem ipsum dolor sit amet consectetur. Id tortor ipsum nisl duis massa. In non amet urna at in proin sed. Tellus facilisis ipsum iaculis mauris eget nisl in laoreet et.
</div>



  <div class="text-center mt-2 mx-auto">
    <p class="text-xs sm:text-sm uppercase tracking-widest text-gray-300 mb-1">Tienes el castillo. Ahora</p>

    <h2 class="font-titulo font-normal text-center text-2xl sm:text-3xl md:text-4xl text-white uppercase tracking-[.02em] leading-[1.08] mb-2">
      Captura a las bestias
    </h2>

    <div class="mt-2 animate-bounce">
      <svg class="w-6 h-6 text-lime-500 mx-auto" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z" clip-rule="evenodd" />
      </svg>
    </div>
  </div>
</div>

<!-- Corte nubes borde inferior (oculto en móvil) -->
<div class="hidden sm:block absolute bottom-[14rem] sm:bottom-[-24rem] md:bottom-[-26rem] lg:bottom-[-30rem] left-0 right-0 w-full -z-20 pointer-events-none">
  <img src="assets/Corte Nubes.webp" alt="Corte Nubes" class="w-full h-auto object-cover select-none pointer-events-none" />
</div>
</section>


  <!-- ===== CASTILLO ===== -->
  <section id="castillo" class="relative z-10 overflow-visible">
    <div class="relative w-full h-[calc(100vw*2.0833)] min-h-screen">
      <div class="absolute -top-[11rem] sm:-top-[14rem] md:-top-[16rem] lg:-top-[27rem] left-0 right-0 w-full z-[30] pointer-events-none">
        <img src="assets/Corte Nubes.webp" alt="Corte Nubes" class="w-full h-auto object-cover select-none pointer-events-none" />
      </div>

      <img src="assets/Background Cielo Castillo.webp" alt="Fondo Cielo Castillo" class="absolute inset-0 w-full h-full object-cover pointer-events-none select-none" style="top:-10px; z-index:-100;" />
      <!-- Imagen del castillo -->
<img src="assets/Background Castillo Full.webp" alt="Castillo fondo"
     class="absolute inset-0 z-[10] w-full h-full object-contain pointer-events-none select-none"
     style="object-position:center top;" />

<!-- Overlay oscuro más fuerte y más corto -->
<div class="absolute inset-0 z-[15] pointer-events-none select-none"
     style="background: linear-gradient(to top, rgba(0,0,0,0.9) 10%, transparent 25%);"></div>


      <!-- Slot de luna en castillo -->
      <div id="castillo-moon-slot" class="absolute z-[-20] w-[60vw] aspect-square pointer-events-none select-none overflow-visible" style="top: 30svh; left: 10vw;">
        <img src="assets/Luna Verde.webp" alt="Luna Verde Castillo" class="castillo-green-moon absolute inset-0 w-full h-full object-contain opacity-0 willchange-transform pointer-events-none select-none" />
      </div>
      <style>@media (min-width:1024px){#castillo-moon-slot{top:80svh!important; left:8vw!important;}}</style>

      <!-- Ramas / enredaderas -->
      <img src="assets/Rama Arbol Morado Alejandose.webp" alt="Rama morada" class="branch-purple-far absolute right-[-10vw] top-[20%] w-[100vw] sm:right-[-12vw] sm:top-[58%] sm:w-[115vw] md:right-[-10vw] md:top-[70%] md:w-[92vw] lg:right-[-8vw]  lg:top-[43%] lg:w-[74vw] xl:right-[-6vw]  xl:top-[40%] xl:w-[68vw] max-w-none object-contain pointer-events-none select-none z-[35]" />
      <img src="assets/Corte Rama Arbol Verde.webp" alt="Rama verde" class="branch-green-cut absolute left-[-16vw] bottom-[-20vh] w-[190vw] sm:left-[-14vw] sm:bottom-[-14vh] sm:w-[165vw] md:left-[-10vw] md:bottom-[-8vh] md:w-[135vw] lg:left-[-8vw] lg:bottom-[-6vh] lg:w-[118vw] xl:left-[-6vw] xl:bottom-[-4vh] xl:w-[110vw] max-w-none object-contain pointer-events-none select-none z-[30]" />
      <img src="assets/Rama del Libro Morado.webp" alt="Rama libro morada" class="branch-book-purple absolute right-[-22vw] bottom-[-24vh] w-[210vw] sm:right-[-20vw] sm:bottom-[-22vh] sm:w-[185vw] md:right-[-18vw] md:bottom-[-20vh] md:w-[150vw] lg:right-[-16vw] lg:bottom-[-18vh] lg:w-[120vw] xl:right-[-14vw] xl:bottom-[-16vh] xl:w-[108vw] max-w-none object-contain pointer-events-none select-none z-[50]" />
      <img src="assets/Corte Enredadera Blurr.webp" alt="Enredaderas desenfocadas" class="vine-blurr absolute left-1/2 -translate-x-1/2 bottom-[-62vh] w-[180vw] sm:bottom-[-64vh] sm:w-[170vw] md:bottom-[-66vh] md:w-[160vw] lg:bottom-[-62vh] lg:w-[145vw] xl:bottom-[-58vh] xl:w-[135vw] max-w-none object-cover pointer-events-none select-none z-[44]" />
      <img src="assets/Corte Enredaderas.webp" alt="Enredaderas" class="vine-cut absolute left-1/2 -translate-x-1/2 bottom-[-36vh] w-[185vw] sm:bottom-[-38vh] sm:w-[165vw] md:bottom-[-40vh] md:w-[145vw] lg:bottom-[-38vh] lg:w-[128vw] xl:bottom-[-36vh] xl:w-[120vw] max-w-none object-cover pointer-events-none select-none z-[45]" />
    </div> 

    <!-- Overrides SOLO móvil dentro de #castillo y #podio -->
<style>

  /* Scroll suave para anclas */
html { scroll-behavior: auto; }
#libro, #fortnite-cta { scroll-margin-top: clamp(72px, 12vh, 128px); }



@media (max-width: 639.98px) {
  /* --- CASTILLO: subir ramas/enredaderas en móvil --- */
  #castillo .branch-purple-far  { top: 10%  !important; }  
  #castillo .branch-green-cut   { bottom: -8vh  !important; } 
  #castillo .branch-book-purple { bottom: -12vh !important; } 
  #castillo .vine-blurr         { bottom: -46vh !important; } 
  #castillo .vine-cut           { bottom: -24vh !important; } 

  /* --- PODIO: subir elementos (mismo bloque/área) --- */
  #podio .rama-verde  { top: 14% !important; }  
  #podio .rama-morada { top: 36% !important; }  

  /* Los que usan BOTTOM: mayor valor = más arriba */
  #podio .espinas-verdes  { bottom: 14% !important; } 
  #podio .rama-libro      { bottom: 18% !important; } 
  #podio .espinas-moradas { bottom: 4%  !important; } 
}
</style>


<!-- ===== PODIO ===== -->
<section id="podio" class="relative z-10 overflow-visible">
  <div class="relative w-full min-h-[180svh] md:min-h-[200vh]" style="perspective:1000px;">
    <!-- Punto focal invisible del libro -->
    <div class="podio-focus absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                h-0 w-0 pointer-events-none select-none"></div>

    <!-- Imagen de fondo del bosque -->
    <img src="assets/Background Bosque - Podio.webp" alt="Bosque Podio"
         class="podio-bg absolute inset-0 w-full h-full object-cover pointer-events-none select-none -z-20 willchange-transform" />

    <!-- Overlay oscuro en la parte superior -->
    <div class="absolute inset-0 z-[-19] pointer-events-none select-none"
         style="background: linear-gradient(to bottom, rgba(0,0,0,0.8) 5%, transparent 30%);"></div>

    <!-- Podios (lejos → cerca → muy cerca) -->
    <img src="assets/(01) Podio Lejos.webp" alt="Podio lejos"
         class="podio-lejos absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                w-[100vw] sm:w-[76vw] md:w-[70vw] max-w-[1000px]
                opacity-100 pointer-events-none select-none z-[10] willchange-transform"
         style="transform-origin:center top;" />

    <img src="assets/(02) Podio Cerca.webp" alt="Podio cerca"
         class="podio-cerca absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                w-[110vw] sm:w-[84vw] md:w-[80vw] max-w-[1100px]
                opacity-0 pointer-events-none select-none z-[11] willchange-transform"
         style="transform-origin:center top;" />

    <img src="assets/(02) Podio Muy cerca.webp" alt="Podio muy cerca"
         class="podio-muycerca absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                w-[120vw] sm:w-[92vw] md:w-[90vw] max-w-[1200px]
                opacity-0 pointer-events-none select-none z-[12] willchange-transform"
         style="transform-origin:center top;" />

    <!-- Ramas / espinas -->
    <img src="assets/Corte Espinas Verdes.webp" alt="Espinas verdes"
         class="espinas-verdes absolute left-[-4vw] bottom-[10%]
                w-[140vw] sm:w-[125vw] md:w-[120vw]
                opacity-0 pointer-events-none select-none z-[20] willchange-transform" />

    <img src="assets/Corte Rama Arbol Verde.webp" alt="Rama verde"
         class="rama-verde absolute right-[6vw] top-[18%]
                w-[120vw] sm:w-[108vw] md:w-[100vw]
                opacity-0 pointer-events-none select-none z-[21] willchange-transform" />

    <img src="assets/Rama Arbol Morado Alejandose.webp" alt="Rama morada"
         class="rama-morada absolute left-[0vw] top-[42%]
                w-[130vw] sm:w-[118vw] md:w-[110vw]
                opacity-0 pointer-events-none select-none z-[22] willchange-transform" />

    <img src="assets/Corte Ramas Libro.webp" alt="Ramas libro"
         class="rama-libro absolute right-[-10vw] bottom-[12%]
                w-[150vw] sm:w-[138vw] md:w-[130vw]
                opacity-0 pointer-events-none select-none z-[23] willchange-transform" />

    <img src="assets/Corte Espinas Moradas.webp" alt="Espinas moradas"
         class="espinas-moradas absolute left-[0vw] bottom-0 
                w-[160vw] sm:w-[148vw] md:w-[140vw]
                opacity-0 pointer-events-none select-none z-[60] willchange-transform" />

    
</section>

<!-- ===== LIBRO (ESCENA) — DESLIGADO Y SIN PIN ===== -->
<section id="libro" class="relative min-h-[120svh] py-16 sm:py-20 md:py-24">
  <!-- === Decoraciones heredadas del index original (fondo/ramas) === -->
  <img src="assets/Background Libro.webp" alt="Fondo Libro"
         class="libro-bg absolute inset-0 -z-20 w-full h-full object-cover pointer-events-none select-none" />

         <!-- Ramas -->


    <img src="assets/Rama Arbol Morado Alejandose.webp" alt="Rama morada alejándose"
         class="libro-rama-morada absolute left-1/2 -translate-x-1/2
                top-[50%] w-[160vw] sm:w-[140vw] md:w-[130vw]
                opacity-0 pointer-events-none select-none z-[22] willchange-transform" />

    <!-- Enredaderas -->
    <img src="assets/Corte Enredaderas Final.webp" alt="Enredaderas finales"
         class="libro-enredaderas absolute left-1/2 -translate-x-1/2
                bottom-[-20vh] sm:bottom-[-24vh] md:bottom-[-28vh] lg:bottom-[-36vh]
                w-[180vw] sm:w-[160vw] md:w-[140vw]
                opacity-0 pointer-events-none select-none z-[24] willchange-transform" />
  </div>

  

  <!-- === Fin decoraciones heredadas === -->

    <div class="mx-auto w-[95%] max-w-[1200px]">
      <div class="relative mx-auto w-[100%] sm:w-[92%] md:w-[82%] lg:w-[74%]">

        <!-- Barra superior: Home + categorías -->
        <div class="realm-bar">
          <!-- HOME -->
          <button id="btnHome" class="btn-swap" aria-label="Inicio">
            <img class="off" src="assets/BT HOME OFF.webp" alt="Home OFF">
            <img class="on"  src="assets/BT HOME ON.webp"  alt="Home ON">
          </button>

          <!-- PANTANO -->
          <button id="tab-pantano" class="btn-swap realm-tab" data-goto="pantano" aria-label="Reino Pantano">
            <img class="off" src="assets/BT REINO PANTANO OFF.webp" alt="Pantano OFF">
            <img class="on"  src="assets/BT REINO PANTANO ON.webp"  alt="Pantano ON">
          </button>

          <!-- FLORAL -->
          <button id="tab-floral" class="btn-swap realm-tab" data-goto="floral" aria-label="Reino Floral">
            <img class="off" src="assets/BT REINO FLORAL OFF.webp" alt="Floral OFF">
            <img class="on"  src="assets/BT REINO FLORAL ON.webp"  alt="Floral ON">
          </button>

          <!-- BESTIAL -->
          <button id="tab-bestial" class="btn-swap realm-tab" data-goto="bestial" aria-label="Reino Bestial">
            <img class="off" src="assets/BT REINO BESTIAL OFF.webp" alt="Bestial OFF">
            <img class="on"  src="assets/BT REINO BESTIAL ON.webp"  alt="Bestial ON">
          </button>

          <!-- ROCOSO -->
          <button id="tab-rocoso" class="btn-swap realm-tab" data-goto="rocoso" aria-label="Reino Rocoso">
            <img class="off" src="assets/BT REINO ROCOSO OFF.webp" alt="Rocoso OFF">
            <img class="on"  src="assets/BT REINO ROCOSO ON.webp"  alt="Rocoso ON">
          </button>

          <!-- VAMPÍRICO -->
          <button id="tab-vampirico" class="btn-swap realm-tab" data-goto="vampirico" aria-label="Reino Vampírico">
            <img class="off" src="assets/BT REINO VAMPIRICO OFF.webp" alt="Vampírico OFF">
            <img class="on"  src="assets/BT REINO VAMPIRICO ON.webp"  alt="Vampírico ON">
          </button>
        </div>

        <!-- Libro+atril -->
        <img src="assets/Libro Abierto Escena.webp" alt="Libro y atril"
             class="block w-full h-auto pointer-events-none select-none drop-shadow-2xl" />

        <!-- Flechas laterales -->
        <button id="btnBack" class="btn-swap side-nav left-[-5%]" aria-label="Anterior">
          <img class="off" src="assets/BT BACK OFF.webp" alt="Back OFF">
          <img class="on"  src="assets/BT BACK ON.webp"  alt="Back ON">
        </button>
        <button id="btnNext" class="btn-swap side-nav right-[-5%]" aria-label="Siguiente">
          <img class="off" src="assets/BT NEXT OFF.webp" alt="Next OFF">
          <img class="on"  src="assets/BT NEXT ON.webp"  alt="Next ON">
        </button>

<!-- =========================
     P0: INTRO / HOME (dos columnas, responsive)
========================== -->
<div id="pagina-home" class="pages-area" data-page="home">
  <div class="page-left grid items-start pt-5">
    <img src="assets/Sello Intro Libro.webp"
         alt="Las Bestias del Bosque Prohibido"
         class="w-full object-contain">
  </div>

  <div class="page-right">
    <!-- Título arriba -->
    <img class="home-heading"
         src="assets/selecciona un reino.png"
         alt="Selecciona un reino">

    <!-- Iconos -->
    <div id="grid-home" class="grid grid-cols-2 gap-3 md:gap-4 place-items-center">
      <!-- PANTANO -->
      <button class="btn-swap icon-btn" data-goto="pantano" aria-label="Ir al Reino Pantano">
        <img class="off" src="assets/Icon Reino Pantano.webp" alt="Pantano">
        <img class="on"  src="assets/Icon Reino Pantano HOVER.webp" alt="">
      </button>
      <!-- FLORAL -->
      <button class="btn-swap icon-btn" data-goto="floral" aria-label="Ir al Reino Floral">
        <img class="off" src="assets/Icon Reino Floral.webp" alt="Floral">
        <img class="on"  src="assets/Icon Reino Floral HOVER.webp" alt="">
      </button>
      <!-- BESTIAL -->
      <button class="btn-swap icon-btn" data-goto="bestial" aria-label="Ir al Reino Bestial">
        <img class="off" src="assets/Icon Reino Bestial.webp" alt="Bestial">
        <img class="on"  src="assets/Icon Reino Bestial HOVER.webp" alt="">
      </button>
      <!-- ROCOSO -->
      <button class="btn-swap icon-btn" data-goto="rocoso" aria-label="Ir al Reino Rocoso">
        <img class="off" src="assets/Icon Reino Rocoso.webp" alt="Rocoso">
        <img class="on"  src="assets/Icon Reino Rocoso HOVER.webp" alt="">
      </button>
      <!-- VAMPÍRICO -->
      <button class="btn-swap icon-btn" data-goto="vampirico" aria-label="Ir al Reino Vampírico">
        <img class="off" src="assets/Icon Reino Vampirico.webp" alt="Vampírico">
        <img class="on"  src="assets/Icon Reino Vampirico HOVER.webp" alt="">
      </button>
    </div>
  </div>
</div>


        <!-- =========================
             P1: REINO PANTANO (grid)
        ========================== -->
        <div id="pagina-pantano" class="pages-area" data-page="pantano">
          <div class="page-left grid items-start pt-5">
            <img src="assets/INTRO PANTANO.webp" alt="Introducción Reino Pantano" class="w-full object-contain">
          </div>
          <div class="page-right">
            <div id="grid-pantano" class="grid grid-cols-2 gap-3 md:gap-4">
              <button class="monster" data-goto="plathom"><img class="thumb" src="assets/13 M-PLATHOM.webp" alt="Plathom"></button>
              <button class="monster" data-goto="venarth"><img class="thumb" src="assets/06 M-VENARTH.webp" alt="Venarth"></button>
              <button class="monster" data-goto="nebrashkarn"><img class="thumb" src="assets/14 M-NEBRASHKARN.webp" alt="Nebrashkarn"></button>
              <button class="monster" data-goto="noctalum"><img class="thumb" src="assets/21 M-NOCTALUM.webp" alt="Noctalum"></button>
              <button class="monster" data-goto="hexalga"><img class="thumb" src="assets/25 M-HEXALGA.webp" alt="Hexalga"></button>
              <button class="monster" data-goto="narthuun"><img class="thumb" src="assets/27 M-NARTHUUN.webp" alt="Narthuun"></button>
            </div>
          </div>
        </div>

        <!-- =========================
             P2..P7: FICHAS PANTANO (cada una con action-bar)
        ========================== -->
        <div id="pagina-plathom" class="pages-area ficha hidden" data-page="plathom">
          <img src="assets/13 F-PLATHOM.webp" alt="Plathom — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/13 F-PLATHOM.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-venarth" class="pages-area ficha hidden" data-page="venarth">
          <img src="assets/06 F-VENARTH.webp" alt="Venarth — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/06 F-VENARTH.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-nebrashkarn" class="pages-area ficha hidden" data-page="nebrashkarn">
          <img src="assets/14 F-NEBRASHKARN.webp" alt="Nebrashkarn — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/14 F-NEBRASHKARN.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-noctalum" class="pages-area ficha hidden" data-page="noctalum">
          <img src="assets/21 F-NOCTALUM.webp" alt="Noctalum — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/21 F-NOCTALUM.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-hexalga" class="pages-area ficha hidden" data-page="hexalga">
          <img src="assets/25 F-HEXALGA.webp" alt="Hexalga — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/25 F-HEXALGA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-narthuun" class="pages-area ficha hidden" data-page="narthuun">
          <img src="assets/27 F-NARTHUUN.webp" alt="Narthuun — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/27 F-NARTHUUN.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <!-- =========================
             P8: REINO BESTIAL (grid)
        ========================== -->
        <div id="pagina-bestial" class="pages-area" data-page="bestial">
          <div class="page-left grid items-start pt-5">
            <img src="assets/INTRO BESTIAL.webp" alt="Introducción Reino Bestial" class="w-full object-contain">
          </div>
          <div class="page-right">
            <div id="grid-bestial" class="grid grid-cols-2 gap-3 md:gap-4">
              <button class="monster" data-goto="cenethra"><img class="thumb" src="assets/bestial/10 M-CENETHRA.webp" alt="Cenethra"></button>
              <button class="monster" data-goto="taralith"><img class="thumb" src="assets/bestial/11 M-TARALITH.webp" alt="Taralith"></button>
              <button class="monster" data-goto="celtrion"><img class="thumb" src="assets/bestial/18 M-CELTRION.webp" alt="Celtrion"></button>
              <button class="monster" data-goto="mopheraidos"><img class="thumb" src="assets/bestial/23 M-MOHERAIDOS.webp" alt="Mopheraidos"></button>
              <button class="monster" data-goto="ardanox"><img class="thumb" src="assets/bestial/24 M-ARDANOX.webp" alt="Ardanox"></button>
            </div>
          </div>
        </div>

        <!-- =========================
             P9..P13: FICHAS BESTIAL
        ========================== -->
        <div id="pagina-cenethra" class="pages-area ficha hidden" data-page="cenethra">
          <img src="assets/10 F-CENETHRA.webp" alt="Cenethra — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/10 F-CENETHRA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-taralith" class="pages-area ficha hidden" data-page="taralith">
          <img src="assets/11 F-TARALITH.webp" alt="Taralith — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/11 F-TARALITH.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-celtrion" class="pages-area ficha hidden" data-page="celtrion">
          <img src="assets/18 F-CELTRION.webp" alt="Celtrion — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/18 F-CELTRION.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-mopheraidos" class="pages-area ficha hidden" data-page="mopheraidos">
          <img src="assets/23 F-MOPHERAIDOS.webp" alt="Mopheraidos — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/23 F-MOPHERAIDOS.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-ardanox" class="pages-area ficha hidden" data-page="ardanox">
          <img src="assets/24 F-ARDANOX.webp" alt="Ardanox — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/24 F-ARDANOX.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <!-- =========================
             P14: REINO VAMPÍRICO (grid)
        ========================== -->
        <div id="pagina-vampirico" class="pages-area" data-page="vampirico">
          <div class="page-left grid items-start pt-5">
            <img src="assets/vampirico/INTRO VAMPIRICO.webp" alt="Introducción Reino Vampírico" class="w-full object-contain">
            <!-- DESTACADO: DRACUTÁNICOS -->
            <button class="hero-monster hero-monster--vamp" data-goto="dracutanicos" aria-label="DRACUTÁNICOS">
              <img src="assets/vampirico/30 M-DRACUTANICUS.webp" alt="DRACUTÁNICOS">
            </button>
          </div>
          <div class="page-right">
            <div id="grid-vampirico" class="grid grid-cols-2 gap-3 md:gap-4">
              <button class="monster" data-goto="v1"><img class="thumb" src="assets/vampirico/08 M-NUBRAKAI.webp" alt="V1"></button>
              <button class="monster" data-goto="v2"><img class="thumb" src="assets/vampirico/09 M-INFERNELLE.webp" alt="V2"></button>
              <button class="monster" data-goto="v3"><img class="thumb" src="assets/vampirico/17 M-NOCTARIZ.webp" alt="V3"></button>
              <button class="monster" data-goto="v4"><img class="thumb" src="assets/vampirico/19 M-CAVERNUX.webp" alt="V4"></button>
              <button class="monster" data-goto="v5"><img class="thumb" src="assets/vampirico/28 M-DRAKYRA.webp" alt="V5"></button>
              <button class="monster" data-goto="v6"><img class="thumb" src="assets/vampirico/31 M-DRACULA.webp" alt="V6"></button>
            </div>
          </div>
        </div>

        <!-- =========================
             P15..P20: FICHAS VAMPÍRICO
        ========================== -->
        <div id="pagina-v1" class="pages-area ficha hidden" data-page="v1">
          <img src="assets/vampirico/08 F-NUBRAKAI.webp" alt="V1 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/08 F-NUBRAKAI.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-v2" class="pages-area ficha hidden" data-page="v2">
          <img src="assets/vampirico/09 F-INFERNELLE.webp" alt="V2 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/09 F-INFERNELLE.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-v3" class="pages-area ficha hidden" data-page="v3">
          <img src="assets/vampirico/17 F-NOCTARIZ.webp" alt="V3 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/17 F-NOCTARIZ.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-v4" class="pages-area ficha hidden" data-page="v4">
          <img src="assets/vampirico/19 F-CAVURNOX.webp" alt="V4 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/19 F-CAVURNOX.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-v5" class="pages-area ficha hidden" data-page="v5">
          <img src="assets/vampirico/28 F-DRAKYRA.webp" alt="V5 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/28 F-DRAKYRA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-v6" class="pages-area ficha hidden" data-page="v6">
          <img src="assets/vampirico/31 F-DRACULA.webp" alt="V6 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/31 F-DRACULA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <!-- =========================
             P21: REINO FLORAL (grid)
        ========================== -->
        <div id="pagina-floral" class="pages-area" data-page="floral">
          <div class="page-left grid items-start pt-5">
            <img src="assets/floral/INTRO FLORAL.webp" alt="Introducción Reino Floral" class="w-full object-contain">
            <!-- DESTACADO: ZELVIRA -->
            <button class="hero-monster hero-monster--floral" data-goto="zelvira" aria-label="ZELVIRA">
              <img src="assets/floral/01 M-ZELVIRA.webp" alt="ZELVIRA">
            </button>
          </div>
          <div class="page-right">
            <div id="grid-floral" class="grid grid-cols-2 gap-3 md:gap-4">
              <button class="monster" data-goto="fl1"><img class="thumb" src="assets/floral/04 M-HIEDRISS.webp" alt="FL1"></button>
              <button class="monster" data-goto="fl2"><img class="thumb" src="assets/floral/05 M-VOLTHERIA.webp" alt="FL2"></button>
              <button class="monster" data-goto="fl3"><img class="thumb" src="assets/floral/07 M-CARDANTAE.webp" alt="FL3"></button>
              <button class="monster" data-goto="fl4"><img class="thumb" src="assets/floral/12 M-LOTHARAK.webp" alt="FL4"></button>
              <button class="monster" data-goto="fl5"><img class="thumb" src="assets/floral/22 M-QUIRISDEA.webp" alt="FL5"></button>
              <button class="monster" data-goto="fl6"><img class="thumb" src="assets/floral/29 M-NEKROPHOS.webp" alt="FL6"></button>
              
            </div>
          </div>
        </div>

        <!-- =========================
             P22..P27: FICHAS FLORAL
        ========================== -->
        <div id="pagina-fl1" class="pages-area ficha hidden" data-page="fl1">
          <img src="assets/floral/04 F-HIEDRISS.webp" alt="FL1 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/04 F-HIEDRISS.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-fl2" class="pages-area ficha hidden" data-page="fl2">
          <img src="assets/floral/05 F-VOLTHERIA.webp" alt="FL2 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/05 F-VOLTHERIA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-fl3" class="pages-area ficha hidden" data-page="fl3">
          <img src="assets/floral/07 F-CARDANTAE.webp" alt="FL3 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/07 F-CARDANTAE.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-fl4" class="pages-area ficha hidden" data-page="fl4">
          <img src="assets/floral/12 F-LOTHARAX.webp" alt="FL4 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/12 F-LOTHARAX.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-fl5" class="pages-area ficha hidden" data-page="fl5">
          <img src="assets/floral/22 F-QUIRISDEA.webp" alt="FL5 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/22 F-QUIRISDEA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-fl6" class="pages-area ficha hidden" data-page="fl6">
          <img src="assets/floral/29 F-NEKROPHOS.webp" alt="FL6 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/29 F-NEKROPHOS.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <!-- =========================
             P28: REINO ROCOSO (grid)
        ========================== -->
        <div id="pagina-rocoso" class="pages-area" data-page="rocoso">
          <div class="page-left grid items-start pt-5">
            <img src="assets/rocoso/INTRO ROCOSO.webp" alt="Introducción Reino Rocoso" class="w-full object-contain">
          </div>
          <div class="page-right">
            <div id="grid-rocoso" class="grid grid-cols-2 gap-3 md:gap-4">
              <button class="monster" data-goto="r1"><img class="thumb" src="assets/rocoso/02 M-MULKAR.webp" alt="R1"></button>
              <button class="monster" data-goto="r2"><img class="thumb" src="assets/rocoso/03 M-IGNAROK.webp" alt="R2"></button>
              <button class="monster" data-goto="r3"><img class="thumb" src="assets/rocoso/15 M-OPTAROC.webp" alt="R3"></button>
              <button class="monster" data-goto="r4"><img class="thumb" src="assets/rocoso/16 M-LUTHERION.webp" alt="R4"></button>
              <button class="monster" data-goto="r5"><img class="thumb" src="assets/rocoso/20 M-MONOCRIT.webp" alt="R5"></button>
              <button class="monster" data-goto="r6"><img class="thumb" src="assets/rocoso/26 M-KARNIZUL.webp" alt="R6"></button>
            </div>
          </div>
        </div>

        <!-- =========================
             P29..P34: FICHAS ROCOSO
        ========================== -->
        <div id="pagina-r1" class="pages-area ficha hidden" data-page="r1">
          <img src="assets/rocoso/02 F-MULKAR.webp" alt="R1 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/rocoso/02 F-MULKAR.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-r2" class="pages-area ficha hidden" data-page="r2">
          <img src="assets/rocoso/03 F-IGNAROK.webp" alt="R2 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/rocoso/03 F-IGNAROK.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-r3" class="pages-area ficha hidden" data-page="r3">
          <img src="assets/rocoso/15 F-OPTAROC.webp" alt="R3 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/rocoso/15 F-OPTAROC.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-r4" class="pages-area ficha hidden" data-page="r4">
          <img src="assets/rocoso/16 F-LUTHERION.webp" alt="R4 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/rocoso/16 F-LUTHERION.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-r5" class="pages-area ficha hidden" data-page="r5">
          <img src="assets/rocoso/20 F-MONOCRIT.webp" alt="R5 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/rocoso/20 F-MONOCRIT.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-r6" class="pages-area ficha hidden" data-page="r6">
          <img src="assets/rocoso/26 F-KARNIZUL.webp" alt="R6 — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/rocoso/26 F-KARNIZUL.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <!-- NUEVAS FICHAS: ZELVIRA (Floral) y DRACUTÁNICOS (Vampírico) -->
        <div id="pagina-zelvira" class="pages-area ficha hidden" data-page="zelvira">
          <img src="assets/floral/01 F-ZELVIRA.webp" alt="ZELVIRA — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/floral/ZELVIRA FICHA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <div id="pagina-dracutanicos" class="pages-area ficha hidden" data-page="dracutanicos">
          <img src="assets/vampirico/30 F-DRACUTANICUS.webp" alt="DRACUTÁNICOS — ficha" class="absolute inset-0 w-full h-full object-contain">
          <div class="action-bar">
            <a class="btn-swap btn-download" href="assets/vampirico/DRACUTANICOS FICHA.webp" download aria-label="Descarga para colorear">
              <img class="off" src="assets/BT COLOREAR OFF.webp" alt="">
              <img class="on"  src="assets/BT COLOREAR ON.webp"  alt="">
            </a>
            <button class="btn-swap btn-upload" aria-label="Añádelo a tu Bestiario">
              <img class="off" src="assets/BT BESTIARIO OFF.webp" alt="">
              <img class="on"  src="assets/BT BESTIARIO ON.webp"  alt="">
            </button>
            <input type="file" class="file-input hidden" accept="application/pdf">
          </div>
        </div>

        <!-- CTA -->
   <!-- CTA (scroll hacia #podio-away) -->
<a id="cta-salir" href="#podio-away" class="btn-swap cta-swap" aria-label="Salir del bosque">
  <img class="off" src="assets/BT SALIR OFF.webp" alt="Salir del bosque">
  <img class="on"  src="assets/BT SALIR ON.webp"  alt="">
</a>

    </div>

    

    
  </section>

<!-- ===== PODIO (AWAY) — copia del podio, se aleja con scroll ===== -->
<section id="podio-away" class="relative z-10 overflow-visible">
  <div class="relative w-full min-h-[190svh] md:min-h-[200vh]" style="perspective:1000px;">
    <!-- Punto focal invisible del libro -->
    <div class="podio-focus absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                h-0 w-0 pointer-events-none select-none"></div>

                 <!-- Enredaderas que cubren la unión LIBRO ↔ PODIO -->
    <img src="assets/Corte Enredaderas Final.webp" alt="Enredaderas unión"
         class="seam-vines absolute left-1/2 -translate-x-1/2
                -top-[20svh] sm:-top-[24svh] md:-top-[28svh] lg:-top-[65svh]
                w-[190vw] sm:w-[170vw] md:w-[150vw]
                pointer-events-none select-none z-[80]" />

    <!-- Imagen de fondo del bosque -->
    <img src="assets/Background Bosque - Podio.webp" alt="Bosque Podio"
         class="podio-bg absolute inset-0 w-full h-full object-cover pointer-events-none select-none -z-20 willchange-transform" />

    <!-- Overlay oscuro en la parte superior -->
    <div class="absolute inset-0 z-[-1] pointer-events-none select-none"
         style="background: linear-gradient(to bottom, rgba(0,0,0,0.8) 10%, transparent 30%);"></div>

    <!-- Podios (lejos → cerca → muy cerca) -->
    <img src="assets/(01) Podio Lejos.webp" alt="Podio lejos"
         class="podio-lejos absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                w-[100vw] sm:w-[76vw] md:w-[70vw] max-w-[1000px]
                opacity-100 pointer-events-none select-none z-[10] willchange-transform"
         style="transform-origin:center top;" />

    <img src="assets/(02) Podio Cerca.webp" alt="Podio cerca"
         class="podio-cerca absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                w-[110vw] sm:w-[84vw] md:w-[80vw] max-w-[1100px]
                opacity-0 pointer-events-none select-none z-[11] willchange-transform"
         style="transform-origin:center top;" />

    <img src="assets/(02) Podio Muy cerca.webp" alt="Podio muy cerca"
         class="podio-muycerca absolute left-1/2 -translate-x-1/2 
                top-[34svh] sm:top-[38svh] md:top-[42vh] max-[639px]:top-[48svh]
                w-[120vw] sm:w-[92vw] md:w-[90vw] max-w-[1200px]
                opacity-0 pointer-events-none select-none z-[12] willchange-transform"
         style="transform-origin:center top;" />

    <!-- Ramas / espinas -->
    <img src="assets/Corte Espinas Verdes.webp" alt="Espinas verdes"
         class="espinas-verdes absolute left-[-4vw] bottom-[10%]
                w-[140vw] sm:w-[125vw] md:w-[120vw]
                opacity-0 pointer-events-none select-none z-[20] willchange-transform" />

    <img src="assets/Corte Rama Arbol Verde.webp" alt="Rama verde"
         class="rama-verde absolute right-[6vw] top-[18%]
                w-[120vw] sm:w-[108vw] md:w-[100vw]
                opacity-0 pointer-events-none select-none z-[21] willchange-transform" />

    <img src="assets/Rama Arbol Morado Alejandose.webp" alt="Rama morada"
         class="rama-morada absolute left-[0vw] top-[42%]
                w-[130vw] sm:w-[118vw] md:w-[110vw]
                opacity-0 pointer-events-none select-none z-[22] willchange-transform" />

    <img src="assets/Corte Ramas Libro.webp" alt="Ramas libro"
         class="rama-libro absolute right-[-10vw] bottom-[12%]
                w-[150vw] sm:w-[138vw] md:w-[130vw]
                opacity-0 pointer-events-none select-none z-[23] willchange-transform" />

    <img src="assets/Corte Espinas Moradas.webp" alt="Espinas moradas"
         class="espinas-moradas absolute left-[0vw] bottom-0 
                w-[160vw] sm:w-[148vw] md:w-[140vw]
                opacity-0 pointer-events-none select-none z-[60] willchange-transform" />

    <!-- Puente (fade) hacia LIBRO; altura controlada por --seam -->
    <div class="podio-fade pointer-events-none absolute inset-x-0 bottom-0 z-[30]"
         style="height:var(--seam,20svh);
                background:linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,.55) 60%, rgba(0,0,0,.9) 100%);"></div>
  </div>
</section>

<!-- ===== FORTNITE CTA — escena con scroll suave hacia abajo ===== -->
<section id="fortnite-cta"
  class="relative overflow-hidden
         z-[8] md:z-[90]
         md:-mt-[14svh] lg:-mt-[18svh]">

         

  <div class="relative w-full min-h-[100vh] md:min-h-[120vh]">

    
    

    

    
    <!-- Fondo -->
    <img src="assets/Background Castillo Cierre.webp" alt="Castillo y luna verde"
         class="fortnite-bg absolute inset-0 w-full h-full object-cover select-none pointer-events-none willchange-transform -z-10" />
    <!-- Vignette / oscurecer bordes -->
    <div class="absolute inset-0 pointer-events-none"
         style="box-shadow: inset 0 0 240px rgba(0,0,0,.85);"></div>

    <!-- Contenido centrado -->
    <div class="absolute top-[30%] left-0 right-0 flex justify-center text-center px-6">

      <div class="max-w-[480px] mx-auto">
        <img src="assets/Sello con Fortnite.webp" alt="Sello Fortnite Bosque Prohibido"
             class="fortnite-badge mx-auto w-[76%] sm:w-[64%] md:w-[520px] willchange-transform drop-shadow-[0_8px_30px_rgba(0,0,0,.6)]" />
        <div class="mt-6 md:mt-8 space-y-3 md:space-y-4 text-white">
          <h2 class="font-titulo font-normal tracking-[.02em] leading-[1.06] text-[clamp(18px,4vw,34px)]">
  ENTRA A FORTNITE Y EXPLORA<br>
  EL BOSQUE PROHIBIDO DE DRÁCULA.
</h2>

          <p class="text-[clamp(19px,3.4vw,24px)] opacity-90">
  Ingresa el código <span class="text-lime-400 font-bold">9456-8159-7833</span> en <span class="font-semibold">Código de Isla</span>… si te atreves.
</p>

        </div>
      </div>
    </div>
  </div>
</section>




<!-- ====== Estilos personalizados para control de espaciado ====== -->
<style>
.icon-grid-tight {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: -10px !important; 
  row-gap: 6px;
  justify-items: center; 
  align-items: center;
}

.stamp {
  padding: 0;
  margin: 0;
}

.stamp-icon {
  width: 72%;
  transition: all 0.3s ease;
}

/*móviles ancho */
@media (max-width: 640px) {
  .stamp-icon {
    width: 65%;
  }

  .icon-grid-tight {
    column-gap: -14px !important; 
  }
}

.stamp-icon:hover {
  transform: scale(1.05);
  filter: brightness(1.5) drop-shadow(0 0 8px limegreen);
}

/* espaciado entre columnas*/
.col-gap-tighter {
  column-gap: -60px !important;
}

/*móviles */
@media (max-width: 640px) {
  .col-gap-tighter {
    column-gap: -16px !important;
  }
}

/* Ayudas táctiles */
[data-goto] { cursor: pointer; touch-action: manipulation; }
[data-goto] img { pointer-events: none; -webkit-user-drag: none; user-select: none; }


/* iconos  */

@media (max-width: 767px) {
  #grid-home {
    margin-top: -11px; 
  }
}



</style>





 
</main>

<!-- GSAP + ScrollTrigger -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
  gsap.registerPlugin(ScrollTrigger);

  /* =====  fondo hasta el inicio de #castillo ===== */
  function fitBgToBestiarioEnd() {
    const castillo = document.querySelector('#castillo');
    const bgWrap   = document.querySelector('.bg-wrap');
    if (!castillo || !bgWrap) return;
    const topCastillo = castillo.getBoundingClientRect().top + window.scrollY;
    bgWrap.style.height = topCastillo + 'px';
  }
  addEventListener('load', fitBgToBestiarioEnd);
  addEventListener('resize', fitBgToBestiarioEnd);
  addEventListener('orientationchange', fitBgToBestiarioEnd);

  /* ===== Parallax del fondo en Bestiario  ===== */
  function mountBgParallax() {
    ScrollTrigger.killTweensOf('.bg-bosque');
    ScrollTrigger.getAll().forEach(st => { if (st.vars?.id === 'bg-parallax') st.kill(); });
    gsap.to(".bg-bosque", {
      y: () => (innerWidth >= 768 ? -240 : -120),
      ease: "none",
      scrollTrigger: {
        id: "bg-parallax",
        trigger: "#captura-bestias",
        start: "top bottom",
        end: "bottom top",
        scrub: 1.1
      }
    });
  }
  addEventListener('load', mountBgParallax);
  addEventListener('resize', () => { fitBgToBestiarioEnd(); mountBgParallax(); });

  /* ===== Flotación suave  ===== */
  gsap.to(".moon",            { y: 18,  scale: 1.025, duration: 6,  yoyo:true, repeat:-1, ease:"sine.inOut" });
  gsap.to(".cloud-left",      { x: 24,  y: -8, duration: 10, yoyo:true, repeat:-1, ease:"sine.inOut" });
  gsap.to(".cloud-right",     { x: -22, y: 6, duration: 12, yoyo:true, repeat:-1, ease:"sine.inOut" });
  gsap.to(".cloud-low",       { x: 16,  y: 12, duration: 14, yoyo:true, repeat:-1, ease:"sine.inOut" });
  gsap.to(".cloud-low-left",  { x: -16, y: 12, duration: 14, yoyo:true, repeat:-1, ease:"sine.inOut" });

  /* ===== Parallax en HERO  ===== */
  gsap.timeline({
    scrollTrigger:{ trigger: ".hero", start: "top top", end: "bottom top", scrub: 1.1 }
  })
  .to(".moon",           { y: -60 }, 0)
  .to(".cloud-left",     { y: -40 }, 0)
  .to(".cloud-right",    { y: -30 }, 0)
  .to(".cloud-low",      { y: -18 }, 0)
  .to(".cloud-low-left", { y: -18 }, 0)
  .to(".title",          { y: -32, opacity: .98, ease: "power1.inOut" }, 0);

  /* ===== Nav activo ===== */
  document.querySelectorAll('.nav-item').forEach(item=>{
    item.addEventListener('click', ()=>{
      document.querySelectorAll('.nav-item').forEach(i=>i.classList.remove('is-active'));
      item.classList.add('is-active');
    });
  });

  /* ===== One-scroll: hero -> trailer  ===== */
  (function(){
    const hero = document.querySelector('.hero'), target = document.querySelector('#trailer');
    if (!hero || !target) return;
    let locking=false, touchStartY=null;
    const inV = ()=>{ const r=hero.getBoundingClientRect(); return r.top<innerHeight && r.bottom>0; };
    const go = ()=>{ if (locking) return; locking=true; const top=target.getBoundingClientRect().top+scrollY; scrollTo({top,behavior:'smooth'}); setTimeout(()=>locking=false,1200);};
    hero.addEventListener('wheel', e=>{ if(!inV())return; if(e.deltaY>15){ e.preventDefault(); go(); }},{passive:false});
    hero.addEventListener('touchstart', e=>{ if(!inV())return; if(e.touches?.length===1) touchStartY=e.touches[0].clientY; },{passive:true});
    hero.addEventListener('touchend', e=>{ if(!inV()||touchStartY==null)return; const dy=touchStartY-(e.changedTouches?.[0]?.clientY??touchStartY); touchStartY=null; if(dy>30) go(); },{passive:true});
  })();

  /* ===== One-scroll: trailer -> bestiario ===== */
  (function(){
    const trailer=document.querySelector('#trailer'), bestiario=document.querySelector('#captura-bestias');
    if(!trailer||!bestiario) return;
    let locking=false, touchStartY=null;
    const inV=el=>{ const r=el.getBoundingClientRect(); return r.top<innerHeight && r.bottom>0; };
    const go=el=>{ const top=el.getBoundingClientRect().top+scrollY; scrollTo({top,behavior:'smooth'}); setTimeout(()=>locking=false,1200); };
    trailer.addEventListener('wheel', e=>{ if(!inV(trailer)||locking) return; if(e.deltaY>15){ e.preventDefault(); locking=true; go(bestiario);} },{passive:false});
    trailer.addEventListener('touchstart', e=>{ if(!inV(trailer))return; if(e.touches?.length===1) touchStartY=e.touches[0].clientY; },{passive:true});
    trailer.addEventListener('touchend', e=>{ if(!inV(trailer)||touchStartY==null||locking) return; const dy=touchStartY-(e.changedTouches?.[0]?.clientY??touchStartY); touchStartY=null; if(dy>30){ locking=true; go(bestiario);} },{passive:true});
  })();

  /* ===== Morph LUNA: Hero → Bestiario  ===== */
  let moonMorphST;
  function centerOf(el){ const r=el.getBoundingClientRect(); return {x:r.left+r.width/2+scrollX,y:r.top+r.height/2+scrollY}; }
  function mountMoonMorph(){
    if(moonMorphST){ moonMorphST.kill(); moonMorphST=null; }
    const moon=document.querySelector('.moon');
    const moonImg=moon?.querySelector('img');
    const green=document.querySelector('#captura-bestias img[alt="Luna Verde"]');
    const triggerS=document.querySelector('#captura-bestias');
    const hero=document.querySelector('.hero');
    if(!moon||!moonImg||!green||!triggerS||!hero) return;

    const greenTargetOpacity=parseFloat(getComputedStyle(green).opacity)||0.8;
    gsap.set(moon,{clearProps:"x,y,opacity,scale"}); gsap.set(moonImg,{filter:"hue-rotate(0deg) saturate(1) brightness(1)"}); gsap.set(green,{opacity:0});

    const cMoon=centerOf(moon), cGreen=centerOf(green); const dx=cGreen.x-cMoon.x, dy=cGreen.y-cMoon.y;

    const tl=gsap.timeline({ scrollTrigger:{ trigger:triggerS, start:"top bottom", end:"center center", scrub:3 }});
    tl.to(moon,{ x:dx, y:dy, scale:0.92, ease:"power1.inOut" },0)
      .to(moonImg,{ filter:"hue-rotate(95deg) saturate(1.35) brightness(1.05)", ease:"power1.inOut" },0)
      .to(green,{ opacity:greenTargetOpacity, ease:"power1.inOut" },0.65)
      .to(moon,{ opacity:0, ease:"power1.inOut" },0.8);

    moonMorphST=tl.scrollTrigger;
  }
  addEventListener('load',  mountMoonMorph);
  addEventListener('resize', ()=>{ mountMoonMorph(); ScrollTrigger.refresh(); });
  addEventListener('orientationchange', ()=>{ mountMoonMorph(); ScrollTrigger.refresh(); });

  /* ===== Z-SWAP luna (igual) ===== */
  (function mountHeroMoonZSwap(){
    const heroMoon=document.querySelector('.moon');
    const bestiario=document.querySelector('#captura-bestias');
    const castillo=document.querySelector('#castillo');
    if(!heroMoon||!bestiario||!castillo) return;
    ScrollTrigger.getAll().forEach(st=>{ if(st.vars?.id==='moon-z-swap-hero-best') st.kill(); });
    ScrollTrigger.create({
      id:'moon-z-swap-hero-best',
      trigger:bestiario,
      start:'top 95%',
      endTrigger: castillo,
      end:'top bottom',
      onEnter:     ()=> gsap.set(heroMoon,{ zIndex:-40 }),
      onEnterBack: ()=> gsap.set(heroMoon,{ zIndex:-40 }),
      onLeave:     ()=> gsap.set(heroMoon,{ zIndex:20  }),
      onLeaveBack: ()=> gsap.set(heroMoon,{ zIndex:60  })
    });
  })();

  /* ===== Nubes: descenso hero -> trailer ===== */
  function mountCloudDropToTrailer(){
    ScrollTrigger.getAll().forEach(st=>{ if(['cloud-drop-left','cloud-drop-right'].includes(st.vars?.id)) st.kill(); });
    const hero=document.querySelector('.hero'), trailer=document.querySelector('#trailer');
    const leftW=document.querySelector('.cloud-left-wrap'), rightW=document.querySelector('.cloud-right-wrap');
    if(!hero||!trailer||!leftW||!rightW) return;
    const dY=(el,off=0)=> (trailer.getBoundingClientRect().top+scrollY+off)-(el.getBoundingClientRect().top+scrollY);
    const desk=()=> innerWidth>=768;
    gsap.to(leftW,{ id:'cloud-drop-left', y:()=>dY(leftW, desk()?40:24), ease:'none',
      scrollTrigger:{ id:'cloud-drop-left', trigger:hero, start:'bottom bottom', endTrigger:'#trailer', end:'top top', scrub:1.2, invalidateOnRefresh:true }});
    gsap.to(rightW,{ id:'cloud-drop-right', y:()=>dY(rightW, desk()?20:12), ease:'none',
      scrollTrigger:{ id:'cloud-drop-right', trigger:hero, start:'bottom bottom', endTrigger:'#trailer', end:'top top', scrub:1.2, invalidateOnRefresh:true }});
  }
  addEventListener('load', ()=>{ mountCloudDropToTrailer(); ScrollTrigger.refresh(); });
  addEventListener('resize', ()=>{ mountCloudDropToTrailer(); ScrollTrigger.refresh(); });
  addEventListener('orientationchange', ()=>{ mountCloudDropToTrailer(); ScrollTrigger.refresh(); });

  /* ===== Parallax continuidad en #trailer ===== */
  function mountTrailerCarryParallax(){
    ScrollTrigger.getAll().forEach(st=>{ if(st.vars?.id==='trailer-carry') st.kill(); });
    const desk=()=> innerWidth>=768;
    gsap.timeline({ scrollTrigger:{ id:'trailer-carry', trigger:'#trailer', start:'top bottom', end:'bottom top', scrub:1.2 }, defaults:{ ease:'none' }})
      .to('.moon',           { y:()=>desk()?'+=220':'+=150', x:()=>desk()?'+=20':'+=12',  immediateRender:false },0)
      .to('.cloud-left',     { y:()=>desk()?'+=130':'+=95',  x:()=>desk()?'-=24':'-=16', immediateRender:false },0)
      .to('.cloud-right',    { y:()=>desk()?'+=120':'+=90',  x:()=>desk()?'+=22':'+=14', immediateRender:false },0)
      .to('.cloud-low',      { y:()=>desk()?'+=60':'+=42',   x:()=>desk()?'+=10':'+=6',  immediateRender:false },0)
      .to('.cloud-low-left', { y:()=>desk()?'+=60':'+=42',   x:()=>desk()?'-=10':'-=6',  immediateRender:false },0);
  }
  addEventListener('load',  mountTrailerCarryParallax);
  addEventListener('resize', mountTrailerCarryParallax);
  addEventListener('orientationchange', mountTrailerCarryParallax);

  /* ===== Video overlay + autoplay (igual) ===== */
  (function(){
    const video=document.getElementById('draculaTrailer'), playBtn=document.getElementById('trailerPlay');
    if(!video||!playBtn) return;
    playBtn.addEventListener('click', async ()=>{ try{ video.muted=false; await video.play(); }catch(e){} playBtn.style.opacity='0'; playBtn.style.pointerEvents='none'; });
    video.addEventListener('play',  ()=>{ playBtn.style.opacity='0'; playBtn.style.pointerEvents='none'; });
    video.addEventListener('pause', ()=>{ playBtn.style.opacity='1'; playBtn.style.pointerEvents='auto'; });
    const io=new IntersectionObserver(entries=>{ entries.forEach(async e=>{ if(e.isIntersecting){ try{ await video.play(); }catch(_){}} else { video.pause(); } }); }, {threshold:0.4});
    io.observe(video);
  })();

  document.querySelectorAll('a[href="#trailer"]').forEach(a=>{
    a.addEventListener('click', e=>{ e.preventDefault(); const t=document.querySelector('#trailer'); if(t) scrollTo({ top:t.getBoundingClientRect().top+scrollY, behavior:'smooth' }); });
  });

    /* ===== CASTILLO: ramas laterales + enredaderas desde abajo (scrub lento) ===== */
function mountCastilloReveal() {
  const castillos = Array.from(document.querySelectorAll('section#castillo'));
  const castillo = castillos.at(-1);
  if (!castillo) return;

  ScrollTrigger.getAll().forEach(st => {
    if (st.vars?.id === 'castillo-reveal') st.kill();
  });

  const q = gsap.utils.selector(castillo);

  const tl = gsap.timeline({
    defaults: { ease: 'power2.out' },
    scrollTrigger: {
      id: 'castillo-reveal',
      trigger: castillo,
      start: 'top 85%',
      end: 'bottom 40%',
      scrub: 0.9,
      invalidateOnRefresh: true,
      // markers: true,
    }
  });

  //Ramas laterales
  tl.from(q('.branch-green-cut'), {
    x: -600, opacity: 0, duration: 1.6, immediateRender: false
  }, 0);

  tl.from(q('.branch-purple-far'), {
    x: 600, opacity: 0, duration: 1.6, immediateRender: false
  }, 0);

  tl.from(q('.branch-book-purple'), {
    x: 700, opacity: 0, duration: 1.8, immediateRender: false
  }, 0.1);

  //Enredaderas
  tl.from(q('.vine-cut'), {
    y: 300, opacity: 0, duration: 1.8, immediateRender: false
  }, 0.2);
}

window.addEventListener('load',  () => { mountCastilloReveal(); ScrollTrigger.refresh(); });
window.addEventListener('resize', () => { mountCastilloReveal(); ScrollTrigger.refresh(); });
window.addEventListener('orientationchange', () => { mountCastilloReveal(); ScrollTrigger.refresh(); });

  /* ===== LUNA VERDE: Bestiario → Castillo (alineado con suavidad del morph) ===== */
  function mountMoonToCastillo(){
    const bestiario=document.querySelector('#captura-bestias');
    const castillo=document.querySelector('#castillo');
    const bestMoon=bestiario?.querySelector('img[alt="Luna Verde"]');
    const slot=castillo?.querySelector('#castillo-moon-slot');
    const castilloGreen=castillo?.querySelector('.castillo-green-moon');
    if(!bestiario||!castillo||!bestMoon||!slot||!castilloGreen) return;

    const centerOf=el=>{ const r=el.getBoundingClientRect(); return {x:r.left+r.width/2+scrollX, y:r.top+r.height/2+scrollY}; };

    ScrollTrigger.getAll().forEach(st=>{ if(st.vars?.id==='moon-best->cast'||st.vars?.id==='moon-best-zswap') st.kill(); });
    gsap.set(castilloGreen,{ opacity:0 });

    const tl=gsap.timeline({
      scrollTrigger:{
        id:'moon-best->cast',
        trigger:bestiario,
        start:'bottom bottom',
        endTrigger: castillo,
        end:'top 38%',
        scrub: 2.4,
        invalidateOnRefresh:true,
        onEnter:     ()=> gsap.set(bestMoon,{ zIndex:26 }),
        onLeaveBack: ()=> gsap.set(bestMoon,{ zIndex:''  })
      }
    });

    tl.to(bestMoon,{
      x:()=>{ const b=centerOf(bestMoon), s=centerOf(slot); return s.x-b.x; },
      y:()=>{ const b=centerOf(bestMoon), s=centerOf(slot); return s.y-b.y; },
      scale:()=>{ const rb=bestMoon.getBoundingClientRect(), rs=slot.getBoundingClientRect(); return rs.width/rb.width; },
      transformOrigin:'center center',
      ease:'power1.inOut',
      immediateRender:false
    },0)
    .to(castilloGreen,{ opacity:1, ease:'power1.inOut' },0.70)
    .to(bestMoon,     { opacity:0, ease:'power1.inOut' },0.88);

    ScrollTrigger.create({
      id:'moon-best-zswap',
      trigger: castillo,
      start: 'top bottom',
      onLeaveBack: ()=>{
        gsap.set(bestMoon,{ clearProps:'x,y,scale,opacity,zIndex' });
        gsap.set(castilloGreen,{ opacity:0 });
        ScrollTrigger.refresh();
      }
    });
  }
  addEventListener('load',  ()=>{ mountMoonToCastillo(); ScrollTrigger.refresh(); });
  addEventListener('resize', ()=>{ mountMoonToCastillo(); ScrollTrigger.refresh(); });
  addEventListener('orientationchange', ()=>{ mountMoonToCastillo(); ScrollTrigger.refresh(); });

  /* === BESTIARIO → CASTILLO: nubes verdes (scrub suave) === */
  function getGreenWrappers() {
    return Array.from(document.querySelectorAll('#captura-bestias img[alt="Nube Verde B"]')).map(img => img.closest('div')).filter(Boolean);
  }
  function mountGreenDropToCastillo() {
    const W = getGreenWrappers();
    const best = document.querySelector('#captura-bestias');
    const cast = document.querySelector('#castillo');
    const fondo = cast?.querySelector('img[alt="Castillo fondo"]');
    if (!W.length || !best || !cast || !fondo) return;

    ScrollTrigger.getAll().forEach(st => {
      if (['green-drop-a','green-drop-b','green-drop-c','green-drop-z'].includes(st.vars?.id)) st.kill();
    });

    const dY = (el, offset=0) => {
      const topStart = fondo.getBoundingClientRect().top + scrollY;
      const topEl    = el.getBoundingClientRect().top + scrollY;
      return (topStart - topEl) + offset;
    };
    const desk = () => innerWidth >= 768;

    ScrollTrigger.create({
      id: 'green-drop-z',
      trigger: best,
      start: 'bottom bottom',
      endTrigger: cast,
      end: 'top top',
      onEnter:     () => W.forEach(w => gsap.set(w, { zIndex: 200 })),
      onEnterBack: () => W.forEach(w => gsap.set(w, { zIndex: 200 })),
      onLeave:     () => W.forEach(w => gsap.set(w, { clearProps: 'zIndex' })),
      onLeaveBack: () => W.forEach(w => gsap.set(w, { clearProps: 'zIndex' }))
    });

    if (W[0]) gsap.to(W[0], { id:'green-drop-a', y:()=>dY(W[0], desk()?60:40), ease:'none',
      scrollTrigger:{ id:'green-drop-a', trigger:best, start:'bottom bottom', endTrigger:cast, end:'top top', scrub:1.1, invalidateOnRefresh:true }});
    if (W[1]) gsap.to(W[1], { id:'green-drop-b', y:()=>dY(W[1], desk()?80:60), ease:'none',
      scrollTrigger:{ id:'green-drop-b', trigger:best, start:'bottom bottom', endTrigger:cast, end:'top top', scrub:1.1, invalidateOnRefresh:true }});
    if (W[2]) gsap.to(W[2], { id:'green-drop-c', y:()=>dY(W[2], desk()?70:50), ease:'none',
      scrollTrigger:{ id:'green-drop-c', trigger:best, start:'bottom bottom', endTrigger:cast, end:'top top', scrub:1.1, invalidateOnRefresh:true }});
  }
  addEventListener('load', ()=>{ mountGreenDropToCastillo(); ScrollTrigger.refresh(); });
  addEventListener('resize', ()=>{ mountGreenDropToCastillo(); ScrollTrigger.refresh(); });
  addEventListener('orientationchange', ()=>{ mountGreenDropToCastillo(); ScrollTrigger.refresh(); });

  /* ===== PODIO: acercamiento (scrub + ease) ===== */
  let podioMM;

  function mountPodioSequence() {
    const podio = document.querySelector('#podio');
    if (!podio) return;

    const MOB_PODIO_UP_LAST = 83;   // móvil
    const DESK_RAISE_LAST   = 100;  // desktop

    const MOB_RAMAS_UP      = 150;   // móvil
    const DESK_RAMAS_DOWN   = 500;  // desktop

    ScrollTrigger.getAll().forEach(st => {
      if (st.vars?.id && (st.vars.id === 'podio-sequence' || st.vars.id.startsWith('podio-'))) st.kill();
    });
    if (podioMM) { podioMM.revert(); podioMM = null; }

    const q = gsap.utils.selector(podio);
    podioMM = gsap.matchMedia();

    const fitValues = (desk) => ({
      lejos: desk ? -6 : -4,
      cerca: desk ? -4 : -3,
      muy:   desk ? -2 : -1
    });

    /* ====== MOBILE (≤ 639px) ====== */
    podioMM.add("(max-width: 639px)", () => {
      const fit = fitValues(false);

      gsap.set(q('.podio-bg'),       { scale: 1, force3D: true });
      gsap.set(q('.podio-lejos'),    { opacity: 1, scale: 1.00, y: fit.lejos,   force3D: true });
      gsap.set(q('.podio-cerca'),    { opacity: 0, scale: 1.02, y: fit.cerca,   force3D: true });
      gsap.set(q('.podio-muycerca'), { opacity: 0, scale: 1.04, y: fit.muy,     force3D: true });
      gsap.set([q('.espinas-verdes'), q('.rama-verde'), q('.rama-morada'), q('.rama-libro'), q('.espinas-moradas')], { opacity: 0, force3D: true });

      const tl = gsap.timeline({
        defaults: { ease: 'power1.inOut' },
        scrollTrigger: {
          id: 'podio-sequence',
          trigger: podio,
          start: 'top 10%',
          end: '+=180%',
          scrub: 1.9,
          pin: true,
          anticipatePin: 2,
          invalidateOnRefresh: true
        }
      });

      // Fondo + dolly
      tl.to(q('.podio-bg'), { scale: 1.06, transformOrigin: 'center center' }, 0)
        .to(q('.podio-lejos'),    { scale: 0.985, y: fit.lejos +  6 }, 0.00)
        .to(q('.podio-cerca'),    { scale: 1.050, y: fit.cerca +  4 }, 0.18)
        .to(q('.podio-muycerca'), { scale: 1.100, y: fit.muy   +  0 }, 0.46)
        .to(q('.podio-lejos'),    { opacity: 0.00 }, 0.16)
        .to(q('.podio-cerca'),    { opacity: 1.00 }, 0.18)
        .to(q('.podio-cerca'),    { opacity: 0.00 }, 0.44)
        .to(q('.podio-muycerca'), { opacity: 1.00 }, 0.46)
        .to(q('.podio-muycerca'), { scale: 1.12,  y: `-=${MOB_PODIO_UP_LAST}` }, 0.68);

      // Ramas/espinas arriba
      tl.to(q('.espinas-verdes'),  { opacity: 1, y: -(30 + MOB_RAMAS_UP) }, 0.22)
        .to(q('.rama-verde'),      { opacity: 1, x: -32, y: -(6 + MOB_RAMAS_UP*0.8) }, 0.30)
        .to(q('.rama-morada'),     { opacity: 1, x:  26, y: -(6 + MOB_RAMAS_UP*0.8) }, 0.38)
        .to(q('.rama-libro'),      { opacity: 1, y: -(34 + MOB_RAMAS_UP) }, 0.46)
        .to(q('.espinas-moradas'), { opacity: 1, y: -(48 + MOB_RAMAS_UP), scale: 1.06,
                                     onStart: ()=> gsap.set(q('.espinas-moradas'), { zIndex: 60 }) }, 0.58);

      // Parallax 
      gsap.to(q('.rama-morada'), { y: -(10 + MOB_RAMAS_UP*0.4), ease: 'none',
        scrollTrigger: { id: 'podio-rm-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1 }});
      gsap.to(q('.rama-verde'), { y: -(8 + MOB_RAMAS_UP*0.4), ease: 'none',
        scrollTrigger: { id: 'podio-rv-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1 }});
    });

    /* ====== DESKTOP (≥ 640px) ====== */
    podioMM.add("(min-width: 640px)", () => {
      const fit = fitValues(true);

      gsap.set(q('.podio-bg'),       { scale: 1, force3D: true });
      gsap.set(q('.podio-lejos'),    { opacity: 1, scale: 1.00, y: fit.lejos,   force3D: true });
      gsap.set(q('.podio-cerca'),    { opacity: 0, scale: 1.02, y: fit.cerca,   force3D: true });
      gsap.set(q('.podio-muycerca'), { opacity: 0, scale: 1.04, y: fit.muy,     force3D: true });
      gsap.set([q('.espinas-verdes'), q('.rama-verde'), q('.rama-morada'), q('.rama-libro'), q('.espinas-moradas')], { opacity: 0, force3D: true });

      const tl = gsap.timeline({
        defaults: { ease: 'power1.inOut' },
        scrollTrigger: {
          id: 'podio-sequence',
          trigger: podio,
          start: 'top top',
          end: '+=220%',
          scrub: 2.0,
          pin: true,
          anticipatePin: 2,
          invalidateOnRefresh: true
        }
      });

      tl.to(q('.podio-bg'), { scale: 1.08, transformOrigin: 'center center' }, 0)
        .to(q('.podio-lejos'),    { scale: 0.97, y: fit.lejos + 10 }, 0.00)
        .to(q('.podio-cerca'),    { scale: 1.06, y: fit.cerca +  6 }, 0.20)
        .to(q('.podio-muycerca'), { scale: 1.12, y: fit.muy   -  4 }, 0.55)
        .to(q('.podio-lejos'),    { opacity: 0.00 }, 0.18)
        .to(q('.podio-cerca'),    { opacity: 1.00 }, 0.20)
        .to(q('.podio-cerca'),    { opacity: 0.00 }, 0.50)
        .to(q('.podio-muycerca'), { opacity: 1.00 }, 0.55)
        .to(q('.podio-muycerca'), { scale: 1.16, y: `-=${DESK_RAISE_LAST}` }, 0.78);

      tl.to(q('.espinas-verdes'),  { opacity: 1, y: (DESK_RAMAS_DOWN - 38) }, 0.22)
        .to(q('.rama-verde'),      { opacity: 1, x: -56, y: (DESK_RAMAS_DOWN*0.8 - 8) }, 0.30)
        .to(q('.rama-morada'),     { opacity: 1, x:  46, y: (DESK_RAMAS_DOWN*0.8 - 8) }, 0.38)
        .to(q('.rama-libro'),      { opacity: 1, y: (DESK_RAMAS_DOWN - 52) }, 0.46)
        .to(q('.espinas-moradas'), { opacity: 1, y: (DESK_RAMAS_DOWN - 64), scale: 1.08,
                                     onStart: ()=> gsap.set(q('.espinas-moradas'), { zIndex: 60 }) }, 0.60);

      gsap.to(q('.rama-morada'), { y: (DESK_RAMAS_DOWN*0.3 - 24), ease: 'none',
        scrollTrigger: { id: 'podio-rm-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1.1 }});
      gsap.to(q('.rama-verde'), { y: (DESK_RAMAS_DOWN*0.3 - 18), ease: 'none',
        scrollTrigger: { id: 'podio-rv-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1.1 }});
      gsap.to(q('.rama-libro'), { x: 10, ease: 'none',
        scrollTrigger: { id: 'podio-rl-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1.1 }});
    });
  }

  addEventListener('load',  ()=>{ mountPodioSequence(); ScrollTrigger.refresh(); });
  addEventListener('resize', ()=>{ mountPodioSequence(); ScrollTrigger.refresh(); });
  addEventListener('orientationchange', ()=>{ mountPodioSequence(); ScrollTrigger.refresh(); });

/* ===== LIBRO: entrada desde lejos y acercamiento (suave) ===== */
function mountLibroScene() {
  const section = document.querySelector('#libro');
  if (!section) return;

  // Limpieza re-montamos
  ScrollTrigger.getAll().forEach(st => { 
    if (st.vars?.id?.startsWith('libro-')) st.kill(); 
  });

  const q = gsap.utils.selector(section);
  const mm = gsap.matchMedia();

  /* ===== MOBILE (≤639px) ===== */
  mm.add("(max-width: 639px)", () => {
    gsap.set(q('.libro-bg'),          { scale: 1 });
    gsap.set(q('.libro-book'),        { scale: 0.78, y: 40,  opacity: 0 });
    gsap.set(q('.libro-rama-verde'),  { y: -40, x: -20, opacity: 0 });
    gsap.set(q('.libro-rama-morada'), { y:  30, x:  22, opacity: 0 });
    gsap.set(q('.libro-enredaderas'), { y: 160,        opacity: 0 });

    const tl = gsap.timeline({
      defaults: { ease: 'sine.inOut' },
      scrollTrigger: { 
        id:'libro-seq-mob', 
        trigger: section, 
        start:'top top',  
        end:'+=100%', 
        scrub: 2.2,
        pin: true, 
        anticipatePin: 1,
        invalidateOnRefresh: true
      }
    });

    // Libro (lejos → cerca)
    tl.to(q('.libro-book'), { 
      opacity:1, scale:0.92, y:-4, duration:1.6 
    }, 0.05)
    .to(q('.libro-book'), { 
      scale:1.12, y:-26, duration:2.2 
    }, 0.55);

    // Ramas y enredaderas
    tl.to(q('.libro-rama-verde'),  { opacity:1, x:0, y:-10, duration:1.6 }, 0.18);
    tl.to(q('.libro-rama-morada'), { opacity:1, x:0, y: 10, duration:1.6 }, 0.26);
    tl.to(q('.libro-enredaderas'), { opacity:1, y:0,   duration:1.8 }, 0.40);

    // Parallax suave
    gsap.to(q('.libro-rama-verde'),  { y:-30, ease:'none',
      scrollTrigger:{ id:'libro-parallax-verde', trigger:section, start:'top top', end:'bottom bottom', scrub:1, invalidateOnRefresh: true }});
    gsap.to(q('.libro-rama-morada'), { y: 22, ease:'none',
      scrollTrigger:{ id:'libro-parallax-morada', trigger:section, start:'top top', end:'bottom bottom', scrub:1, invalidateOnRefresh: true }});
  });

  /* ===== DESKTOP (≥640px) ===== */
  mm.add("(min-width: 640px)", () => {
    gsap.set(q('.libro-bg'),          { scale: 1 });
    gsap.set(q('.libro-book'),        { scale: 0.72, y: 26,  opacity: 0 });
    gsap.set(q('.libro-rama-verde'),  { y: -60, x: -30, opacity: 0 });
    gsap.set(q('.libro-rama-morada'), { y:  46, x:  36, opacity: 0 });
    gsap.set(q('.libro-enredaderas'), { y: 200,        opacity: 0 });

    const tl = gsap.timeline({
      defaults: { ease: 'sine.inOut' },
      scrollTrigger: { 
        id:'libro-seq-desk', 
        trigger: section, 
        start:'top top', 
        end:'+=120%',  // Reducido para menos scroll
        scrub: 2.5,
        pin: true, 
        anticipatePin: 2,
        invalidateOnRefresh: true
      }
    });

    // Eliminado el zoom del fondo

    // Libro (lejos → cerca)
    tl.to(q('.libro-book'), { 
      opacity:1, scale:0.86, y:-6, duration:1.8 
    }, 0.06)
    .to(q('.libro-book'), { 
      scale:1.16, y:-40, duration:2.4 
    }, 0.62);

    // Ramas y enredaderas
    tl.to(q('.libro-rama-verde'),  { opacity:1, x:0, y:-18, duration:1.8 }, 0.20);
    tl.to(q('.libro-rama-morada'), { opacity:1, x:0, y: 18, duration:1.8 }, 0.28);
    tl.to(q('.libro-enredaderas'), { opacity:1, y:0,   duration:2.0 }, 0.46);

    // Parallax suave
    gsap.to(q('.libro-rama-verde'),  { y:-40, ease:'none',
      scrollTrigger:{ id:'libro-parallax-verde', trigger:section, start:'top top', end:'bottom bottom', scrub:1.1, invalidateOnRefresh: true }});
    gsap.to(q('.libro-rama-morada'), { y: 34, ease:'none',
      scrollTrigger:{ id:'libro-parallax-morada', trigger:section, start:'top top', end:'bottom bottom', scrub:1.1, invalidateOnRefresh: true }});
  });
}

// Esperar imágenes antes de montar animaciones
function waitForImagesToLoad(callback) {
  const images = document.images;
  let loaded = 0;
  const total = images.length;

  if (total === 0) return callback();

  for (let i = 0; i < total; i++) {
    if (images[i].complete) {
      loaded++;
    } else {
      images[i].addEventListener('load', () => {
        loaded++;
        if (loaded === total) callback();
      });
      images[i].addEventListener('error', () => {
        loaded++;
        if (loaded === total) callback();
      });
    }
  }

  if (loaded === total) callback();
}

// Montaje / refresh seguro
window.addEventListener('load', () => {
  waitForImagesToLoad(() => {
    mountLibroScene();
    ScrollTrigger.refresh();

    // Extra seguridad: segundo refresh pequeño delay
    setTimeout(() => ScrollTrigger.refresh(), 300);
  });
});

window.addEventListener('resize', () => { 
  mountLibroScene(); 
  ScrollTrigger.refresh(); 
});

window.addEventListener('orientationchange', () => { 
  mountLibroScene(); 
  ScrollTrigger.refresh(); 
});




  

  
</script>


<!-- === BEGIN scripts del LIBRO (importados) === -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
  // Orden de navegación (Home → resto)
const order = [
  'home',

  // PANTANO
  'pantano','plathom','venarth','nebrashkarn','noctalum','hexalga','narthuun',

  // FLORAL (ZELVIRA destacado tras la intro)
  'floral','zelvira','fl1','fl2','fl3','fl4','fl5','fl6',

  // BESTIAL
  'bestial','cenethra','taralith','celtrion','mopheraidos','ardanox',

  // ROCOSO
  'rocoso','r1','r2','r3','r4','r5','r6',

  // VAMPÍRICO (DRACUTÁNICOS destacado tras la intro)
  'vampirico','dracutanicos','v1','v2','v3','v4','v5','v6'
];

  const pages = Object.fromEntries(order.map(id => [id, document.querySelector(`[data-page="${id}"]`)]) );

  const btnNext = document.getElementById('btnNext');
  const btnBack = document.getElementById('btnBack');
  const btnHome = document.getElementById('btnHome');
  const realmBar = document.querySelector('.realm-bar');

  // Pertenencia de páginas a cada reino (para activar medalla)
  const realms = {
    pantano: ['pantano','plathom','venarth','nebrashkarn','noctalum','hexalga','narthuun'],
    bestial: ['bestial','cenethra','taralith','celtrion','mopheraidos','ardanox'],
    vampirico: ['vampirico','dracutanicos','v1','v2','v3','v4','v5','v6'],
    floral:   ['floral','zelvira','fl1','fl2','fl3','fl4','fl5','fl6'],
    rocoso:   ['rocoso','r1','r2','r3','r4','r5','r6'],
  };
  const tabEls = {
    pantano: document.getElementById('tab-pantano'),
    bestial: document.getElementById('tab-bestial'),
    vampirico: document.getElementById('tab-vampirico'),
    floral:   document.getElementById('tab-floral'),
    rocoso:   document.getElementById('tab-rocoso'),
  };
  function realmOf(pageId){
    for (const [realm, list] of Object.entries(realms)) if (list.includes(pageId)) return realm;
    return null;
  }

  let current = 'home';

  function setActiveRealm(pageId){
    const active = realmOf(pageId);
    Object.entries(tabEls).forEach(([key, el])=>{
      el.classList.toggle('is-active', key === active);
    });
  }

  function show(id){
    Object.values(pages).forEach(el => el?.classList.add('hidden'));
    pages[id]?.classList.remove('hidden');
    current = id;

    const i = order.indexOf(current);
    const isHome = current === 'home';

    // flechas y barra de categorías visibles solo fuera del home
    [btnBack, btnNext].forEach(b => b.classList.toggle('hidden', isHome));
    realmBar.classList.toggle('hidden', isHome);

    // activar flechas (cuando no es home)
    if(!isHome){
      btnBack.classList.toggle('is-active', i > 0);
      btnNext.classList.toggle('is-active', i < order.length - 1);
    }

    // activar medalla del reino (no aplica en home)
    setActiveRealm(current);
  }

  // Click en grillas para abrir fichas o saltar desde HOME/intro
  ['grid-home','grid-pantano','grid-bestial','grid-vampirico','grid-floral','grid-rocoso'].forEach(id=>{
    const grid = document.getElementById(id);
    if(!grid) return;
    grid.addEventListener('click', (e)=>{
      const m = e.target.closest('[data-goto]');
      if(!m) return;
      show(m.dataset.goto);
    });
  });

  
  /* --- Tap inmediato en móvil para elementos con [data-goto] --- */
(() => {
  const containers = [
    'grid-home','grid-pantano','grid-bestial','grid-vampirico','grid-floral','grid-rocoso'
  ];

  const go = (e) => {
    const m = e.target.closest('[data-goto]');
    if (!m) return;
    e.preventDefault();     // evita el "ghost click" posterior
    e.stopPropagation();
    // navega ya
    show(m.dataset.goto);
  };

  containers.forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;

    // Tap inmediato en táctiles
    el.addEventListener('touchend', go, { passive: false });
    el.addEventListener('pointerup', (e) => {
      if (e.pointerType === 'touch' || e.pointerType === 'pen') go(e);
    });

    // Fallback desktop y navegadores viejos
    el.addEventListener('click', (e) => {
      // si viene de mouse, dejarlo; si vino inmediatamente tras touch, ya lo paramos en go()
      const m = e.target.closest('[data-goto]');
      if (!m) return;
      show(m.dataset.goto);
    });
  });

  // Realm bar si sus tabs usan data-goto
  const realmBarEl = document.querySelector('.realm-bar');
  if (realmBarEl) {
    const handle = (e) => {
      const m = e.target.closest('[data-goto]');
      if (!m) return;
      e.preventDefault();
      show(m.dataset.goto);
    };
    realmBarEl.addEventListener('touchend', handle, { passive: false });
    realmBarEl.addEventListener('pointerup', (e) => {
      if (e.pointerType === 'touch' || e.pointerType === 'pen') handle(e);
    });
    realmBarEl.addEventListener('click', handle);
  }
})();

  // Click en los “destacados” sobre la intro (ZELVIRA/DRACUTÁNICOS)
  document.querySelectorAll('.hero-monster').forEach(btn=>{
    btn.addEventListener('click', ()=> show(btn.dataset.goto));
  });

  // Flechas
  btnNext.addEventListener('click', ()=>{
    const i = order.indexOf(current);
    if (i < order.length - 1) show(order[i+1]);
  });
  btnBack.addEventListener('click', ()=>{
    const i = order.indexOf(current);
    if (i > 0) show(order[i-1]);
  });

  // Home → vuelve al home
  btnHome.addEventListener('click', (e)=>{ e.preventDefault(); show('home'); });

  // Medallas (tabs) → van a la intro del reino
  document.querySelectorAll('.realm-tab').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const target = btn.dataset.goto; // pantano | bestial | vampirico | floral | rocoso
      show(target);
    });
  });

  // Subida de PDFs (todas las fichas)
  function showToast(msg){
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.remove('hidden');
    setTimeout(()=>t.classList.add('hidden'), 1800);
  }
  document.querySelectorAll('.pages-area.ficha').forEach(ficha=>{
    const upBtn = ficha.querySelector('.btn-upload');
    const fileIn = ficha.querySelector('.file-input');
    if(upBtn && fileIn){
      upBtn.addEventListener('click', ()=> fileIn.click());
      fileIn.addEventListener('change', ()=>{
        if(fileIn.files?.length){
          showToast('¡PDF agregado a tu Bestiario!');
        }
      });
    }
  });

  // Teclado ← → y ESC
  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') btnNext.click();
    if (e.key === 'ArrowLeft')  btnBack.click();
    if (e.key === 'Escape')     btnHome.click();
  });

  // Estado inicial
  show(current);

  function setActiveRealm(pageId){
  const active = realmOf(pageId);
  Object.entries(tabEls).forEach(([key, el])=>{
    el.classList.toggle('is-active', key === active);
  });

  // ⬇️ NUEVO: indicamos el reino activo al contenedor del libro
  const libro = document.getElementById('libro');
  if (active) { libro.dataset.realm = active; }
  else { delete libro.dataset.realm; }  
}

</script>
<!-- === END scripts del LIBRO === -->

<!-- === Animación para PODIO (AWAY): se aleja al hacer scroll === -->
<script>
(function(){
  function mountPodioAwaySequence(){
    const podio = document.querySelector('#podio-away');
    if (!podio || typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    ScrollTrigger.getAll().forEach(st => {
      if (st.vars?.id && (st.vars.id === 'podio2-sequence' || String(st.vars.id).startsWith('podio2-'))) st.kill();
    });

    const q = gsap.utils.selector(podio);
    const mm = gsap.matchMedia();

    const fitValues = (desk) => ({
      lejos: desk ? -6 : -4,
      cerca: desk ? -4 : -3,
      muy:   desk ? -2 : -1
    });

    const MOB_PODIO_DOWN_LAST = 83;
    const DESK_LOWER_LAST     = 100;

    const MOB_RAMAS_DOWN      = 150;
    const DESK_RAMAS_UP       = 500;

    mm.add("(max-width: 639px)", () => {
      const fit = fitValues(false);
      gsap.set(q('.podio-bg'),       { scale: 1.08, force3D: true });
      gsap.set(q('.podio-lejos'),    { opacity: 0, scale: 0.99, y: fit.lejos,   force3D: true });
      gsap.set(q('.podio-cerca'),    { opacity: 0, scale: 1.04, y: fit.cerca,   force3D: true });
      gsap.set(q('.podio-muycerca'), { opacity: 1, scale: 1.10, y: fit.muy,     force3D: true });
      gsap.set([q('.espinas-verdes'), q('.rama-verde'), q('.rama-morada'), q('.rama-libro'), q('.espinas-moradas')], { opacity: 0, y: 0 });

      const tl = gsap.timeline({
        defaults: { ease: 'power1.inOut' },
        scrollTrigger: {
          id: 'podio2-sequence',
          trigger: podio,
          start: 'top 10%',
          end: '+=180%',
          scrub: 1.9,
          pin: true,
          anticipatePin: 2,
          invalidateOnRefresh: true
        }
      });

      tl.to(q('.podio-bg'), { scale: 1.00, transformOrigin: 'center center' }, 0)
        .to(q('.podio-muycerca'), { scale: 1.06, y: `+=${MOB_PODIO_DOWN_LAST*0.2}` }, 0.06)
        .to(q('.podio-cerca'),    { opacity: 1.00, scale: 1.02, y: `+=${MOB_PODIO_DOWN_LAST*0.3}` }, 0.18)
        .to(q('.podio-muycerca'), { opacity: 0.00 }, 0.22)
        .to(q('.podio-cerca'),    { opacity: 0.00 }, 0.44)
        .to(q('.podio-lejos'),    { opacity: 1.00, scale: 0.985, y: `+=${MOB_PODIO_DOWN_LAST}` }, 0.46)
        .to(q('.espinas-verdes'),  { opacity: 1, y: ( 30 + MOB_RAMAS_DOWN) }, 0.24)
        .to(q('.rama-verde'),      { opacity: 1, x: -22, y: ( 6 + MOB_RAMAS_DOWN*0.8) }, 0.30)
        .to(q('.rama-morada'),     { opacity: 1, x:  18, y: ( 6 + MOB_RAMAS_DOWN*0.8) }, 0.36)
        .to(q('.rama-libro'),      { opacity: 1, y: ( 34 + MOB_RAMAS_DOWN) }, 0.44)
        .to(q('.espinas-moradas'), { opacity: 1, y: ( 48 + MOB_RAMAS_DOWN), scale: 1.02,
                                     onStart: ()=> gsap.set(q('.espinas-moradas'), { zIndex: 60 }) }, 0.56);

      gsap.to(q('.rama-morada'), { y: (10 + MOB_RAMAS_DOWN*0.4), ease: 'none',
        scrollTrigger: { id: 'podio2-rm-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1 }});
      gsap.to(q('.rama-verde'), { y: (8 + MOB_RAMAS_DOWN*0.4), ease: 'none',
        scrollTrigger: { id: 'podio2-rv-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1 }});
    });

    mm.add("(min-width: 640px)", () => {
      const fit = fitValues(true);
      gsap.set(q('.podio-bg'),       { scale: 1.10, force3D: true });
      gsap.set(q('.podio-lejos'),    { opacity: 0, scale: 0.98, y: fit.lejos,   force3D: true });
      gsap.set(q('.podio-cerca'),    { opacity: 0, scale: 1.06, y: fit.cerca,   force3D: true });
      gsap.set(q('.podio-muycerca'), { opacity: 1, scale: 1.12, y: fit.muy,     force3D: true });
      gsap.set([q('.espinas-verdes'), q('.rama-verde'), q('.rama-morada'), q('.rama-libro'), q('.espinas-moradas')], { opacity: 0, y: 0 });

      const tl = gsap.timeline({
        defaults: { ease: 'power1.inOut' },
        scrollTrigger: {
          id: 'podio2-sequence',
          trigger: podio,
          start: 'top top',
          end: '+=220%',
          scrub: 2.0,
          pin: true,
          anticipatePin: 2,
          invalidateOnRefresh: true
        }
      });

      tl.to(q('.podio-bg'), { scale: 1.02, transformOrigin: 'center center' }, 0)
        .to(q('.podio-muycerca'), { scale: 1.08, y: `+=${DESK_LOWER_LAST*0.25}` }, 0.08)
        .to(q('.podio-cerca'),    { opacity: 1.00, scale: 1.04, y: `+=${DESK_LOWER_LAST*0.45}` }, 0.22)
        .to(q('.podio-muycerca'), { opacity: 0.00 }, 0.26)
        .to(q('.podio-cerca'),    { opacity: 0.00 }, 0.54)
        .to(q('.podio-lejos'),    { opacity: 1.00, scale: 0.97,  y: `+=${DESK_LOWER_LAST}` }, 0.58)
        .to(q('.espinas-verdes'),  { opacity: 1, y: (38 - DESK_RAMAS_UP) }, 0.24)
        .to(q('.rama-verde'),      { opacity: 1, x: -46, y: (8 - DESK_RAMAS_UP*0.8) }, 0.32)
        .to(q('.rama-morada'),     { opacity: 1, x:  36, y: (8 - DESK_RAMAS_UP*0.8) }, 0.40)
        .to(q('.rama-libro'),      { opacity: 1, y: (52 - DESK_RAMAS_UP) }, 0.48)
        .to(q('.espinas-moradas'), { opacity: 1, y: (64 - DESK_RAMAS_UP), scale: 1.04,
                                     onStart: ()=> gsap.set(q('.espinas-moradas'), { zIndex: 60 }) }, 0.62);

      gsap.to(q('.rama-morada'), { y: (24 - DESK_RAMAS_UP*0.3), ease: 'none',
        scrollTrigger: { id: 'podio2-rm-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1.1 }});
      gsap.to(q('.rama-verde'), { y: (18 - DESK_RAMAS_UP*0.3), ease: 'none',
        scrollTrigger: { id: 'podio2-rv-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1.1 }});
      gsap.to(q('.rama-libro'), { x: -10, ease: 'none',
        scrollTrigger: { id: 'podio2-rl-parallax', trigger: podio, start: 'top top', end: 'bottom bottom', scrub: 1.1 }});
    });
  }

  addEventListener('load', () => { mountPodioAwaySequence(); if (window.ScrollTrigger) ScrollTrigger.refresh(); });
  addEventListener('resize', () => { mountPodioAwaySequence(); if (window.ScrollTrigger) ScrollTrigger.refresh(); });
  addEventListener('orientationchange', () => { mountPodioAwaySequence(); if (window.ScrollTrigger) ScrollTrigger.refresh(); });
})();
</script>

<!-- Overrides SOLO móvil para #podio-away (copiados del #podio original) -->
<style>
@media (max-width: 639.98px) {
  #podio-away .rama-verde  { top: 14% !important; }
  #podio-away .rama-morada { top: 36% !important; }
  #podio-away .espinas-verdes  { bottom: 14% !important; }
  #podio-away .rama-libro      { bottom: 18% !important; }
  #podio-away .espinas-moradas { bottom: 4%  !important; }
}
</style>




<script>
(() => {
  // ====== Ajustes de velocidad ======
  // Aumenta MS_PER_PX para hacerlo más lento
  const MS_PER_PX = 2.2;       // milisegundos por píxel (1.8 = más lento)
  const MIN_DURATION = 1200;   // mínimo 1.2s
  const MAX_DURATION = 4000;   // máximo 4s

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function getHeaderOffset() {
    const header = document.querySelector('header');
    const h = header ? header.offsetHeight : 0;
    // colchón extra pequeño
    return h + 12;
  }

  function clamp(val, min, max) {
    return Math.max(min, Math.min(max, val));
  }

  function easeInOutCubic(t) {
    return t < 0.5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3) / 2;
  }

  function smoothScrollTo(targetY) {
    const startY = window.pageYOffset || document.documentElement.scrollTop;
    const delta = targetY - startY;
    const distance = Math.abs(delta);

    // Duración basada en distancia 
    const duration = prefersReduced
      ? 0
      : clamp(distance * MS_PER_PX, MIN_DURATION, MAX_DURATION);

    if (duration === 0 || distance < 2) {
      window.scrollTo(0, targetY);
      return;
    }

    let startTime = null;

    function step(ts) {
      if (!startTime) startTime = ts;
      const elapsed = ts - startTime;
      const t = clamp(elapsed / duration, 0, 1);
      const eased = easeInOutCubic(t);
      window.scrollTo(0, Math.round(startY + delta * eased));
      if (elapsed < duration) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  function getTargetTop(id) {
    const el = document.getElementById(id);
    if (!el) return null;
    const rect = el.getBoundingClientRect();
    const offsetTop = rect.top + (window.pageYOffset || document.documentElement.scrollTop);
    const target = offsetTop - getHeaderOffset();

    // Evitar rebasar el final del documento
    const maxY = document.documentElement.scrollHeight - window.innerHeight;
    return clamp(target, 0, maxY);
  }

  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const id = a.getAttribute('href').slice(1);
      const targetY = getTargetTop(id);
      if (targetY === null) return; 
      e.preventDefault();
      smoothScrollTo(targetY);

      // Actualiza la URL sin “brinco”
      history.replaceState(null, '', '#' + id);
    });
  });
})();
</script>

<script>
(() => {
  /* ===== Helper: fastTap (tap inmediato en táctiles, sin ghost-click) ===== */
  function fastTap(el, handler){
    if (!el) return;
    let ignoreClickUntil = 0;

    el.addEventListener('touchend', (e) => {
      if (e.touches && e.touches.length) return;  
      ignoreClickUntil = Date.now() + 450;
      e.preventDefault();                          
      e.stopPropagation();
      handler(e);
    }, { passive: false });

    el.addEventListener('pointerup', (e) => {
      if (e.pointerType === 'touch' || e.pointerType === 'pen') {
        ignoreClickUntil = Date.now() + 450;
        e.preventDefault();
        e.stopPropagation();
        handler(e);
      }
    });

    // Fallback desktop / navegadores sin touch
    el.addEventListener('click', (e) => {
      if (Date.now() < ignoreClickUntil) {        
        e.preventDefault();
        e.stopPropagation();
        return;
      }
      handler(e);
    });
  }

  /* ===== Smooth scroll helper (usa tu función si existe) ===== */
  function headerOffset(){
    const h = document.querySelector('header');
    return (h ? h.offsetHeight : 0) + 12;
  }
  function smoothToEl(el, hash){
    if (!el) return;
    const y = Math.min(
      document.documentElement.scrollHeight - window.innerHeight,
      el.getBoundingClientRect().top + (window.pageYOffset || document.documentElement.scrollTop) - headerOffset()
    );
    if (typeof window.smoothScrollTo === 'function') {
      window.smoothScrollTo(y);        
    } else {
      window.scrollTo({ top: y, behavior: 'smooth' });
    }
    if (hash) history.replaceState(null, '', hash);
  }

  /* ===== CTA SALIR  ===== */
  const ctaSalir = document.getElementById('cta-salir');
  fastTap(ctaSalir, () => {
    const dest = document.getElementById('podio-away');
    smoothToEl(dest, '#podio-away');
  });

  /* ===== HOME: abre fichas al primer toque ===== */
  const gridHome = document.getElementById('grid-home');
  fastTap(gridHome, (e) => {
    const m = e.target.closest('[data-goto]');
    if (!m) return;
    // Navega a la ficha inmediatamente
    if (typeof window.show === 'function') window.show(m.dataset.goto);
  });

  /* ===== Afinar botones con swap de imágenes en táctil ===== */
  const isTouch = window.matchMedia && window.matchMedia('(hover: none)').matches;
  if (isTouch) {
    // que las imágenes no intercepten el tap
    document.querySelectorAll('.btn-swap img').forEach(img => {
      img.style.pointerEvents = 'none';
      img.style.webkitUserDrag = 'none';
      img.style.userSelect = 'none';
    });
  }
})();
</script>

<script>
(() => {
  // ===== helpers de scroll suave (solo para este CTA) =====
  function easeInOutCubic(t){ return t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3)/2; }
  function animateScrollTo(targetY, durationMs){
    const startY = window.pageYOffset || document.documentElement.scrollTop;
    const delta = targetY - startY;
    if (Math.abs(delta) < 2) { window.scrollTo(0, targetY); return; }
    let t0 = null;
    function step(ts){
      if (!t0) t0 = ts;
      const t = Math.min(1, (ts - t0) / durationMs);
      const eased = easeInOutCubic(t);
      window.scrollTo(0, Math.round(startY + delta * eased));
      if (t < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  function headerOffset(){
    const h = document.querySelector('header');
    return (h ? h.offsetHeight : 0) + 12; 
  }
  function targetTop(el){
    const y = el.getBoundingClientRect().top + (window.pageYOffset || document.documentElement.scrollTop) - headerOffset();
    const maxY = document.documentElement.scrollHeight - window.innerHeight;
    return Math.max(0, Math.min(y, maxY));
  }

  // ===== CTA: salir del bosque con scroll más lento =====
  const ctaSalir = document.getElementById('cta-salir');
  if (ctaSalir) {
    const go = (e) => {
      e.preventDefault();
      const dest = document.getElementById('podio-away');
      if (!dest) return;
      animateScrollTo(targetTop(dest), 2400);  
      history.replaceState(null, '', '#podio-away');
    };

    // Tap inmediato en táctil (evita doble tap) + fallback click
    ctaSalir.addEventListener('touchend', (e)=>{ if(!e.touches?.length){ e.preventDefault(); go(e); } }, {passive:false});
    ctaSalir.addEventListener('pointerup', (e)=>{ if(e.pointerType==='touch'||e.pointerType==='pen'){ e.preventDefault(); go(e); }});
    ctaSalir.addEventListener('click', go);
  }
})();
</script>

<script>
(() => {
  const logo = document.getElementById('logo-home'); // <a id="logo-home">…</a>
  if (!logo) return;

  function easeInOutCubic(t){ return t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3)/2; }
  function scrollToTopSlow(ms){
    const start = window.pageYOffset || document.documentElement.scrollTop;
    if (start < 2) { window.scrollTo(0,0); return; }
    let t0 = null;
    function step(ts){
      if (!t0) t0 = ts;
      const p = Math.min(1, (ts - t0) / ms);
      const eased = easeInOutCubic(p);
      window.scrollTo(0, Math.round(start * (1 - eased)));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  const go = e => { e.preventDefault(); scrollToTopSlow(3400); }; 

  // Tap inmediato en táctil (evita doble-tap) + fallback click
  logo.addEventListener('touchend', e => { if(!e.touches?.length) go(e); }, { passive:false });
  logo.addEventListener('pointerup', e => { if(e.pointerType==='touch'||e.pointerType==='pen') go(e); });
  logo.addEventListener('click', go);
})();
</script>

<!-- React  -->
<script src="https://unpkg.com/preact@latest/dist/preact.umd.js"></script>




<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          titulo:  ['"Berani"', 'system-ui', 'sans-serif'],
          parrafo: ['"Jolly Lodger"', 'system-ui', 'sans-serif'],
          cta:     ['"Screature"', 'system-ui', 'sans-serif'],
        }
      }
    }
  }
</script>
<script src="https://cdn.tailwindcss.com"></script>



</body>
</html>
