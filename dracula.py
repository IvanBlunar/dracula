<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="color-scheme" content="dark" />
  <title>Drácula — Hero Parallax</title>

  <!-- Tailwind (CDN) -->
  <script src="https://cdn.tailwindcss.com"></script>

  <style>
    /* Viñeta sutil solo para el hero */
    .vignette::after {
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      box-shadow: inset 0 0 160px rgba(0, 0, 0, .8);
    }
    .willchange-transform { will-change: transform; }

    /* Estado activo del nav: muestra ON y oculta OFF */
    .nav-item.is-active .off { opacity: 0 !important; }
    .nav-item.is-active .on  { opacity: 1 !important; }
  </style>
</head>
<body class="bg-black text-white overflow-x-hidden antialiased">

<!-- ===== Header (blur, logo grande, hover ON/OFF, activo por clic) ===== -->
<header class="fixed inset-x-0 top-0 z-[100]">
  <div class="relative mx-auto mt-4 w-[94%] max-w-[1400px]">
    <div class="flex flex-col sm:flex-row items-center justify-center sm:justify-between px-4 md:px-6 py-2 bg-black/40 backdrop-blur-md rounded-3xl">
      
      <div class="flex items-center justify-center sm:justify-between w-full gap-12 sm:gap-0">
        
        <!-- Logo -->
        <img src="assets/header/Logo Dracula.webp" alt="Drácula"
             class="h-[50px] sm:h-[42px] md:h-[50px] w-auto select-none">

        <!-- Navegación -->
        <nav class="flex items-center gap-10 sm:gap-14">
          
          <!-- Bestiario -->
          <a href="#bestiario" class="group relative inline-block nav-item" data-nav="bestiario" aria-label="El Bestiario">
            <img src="assets/header/OFF EL BESTIARIO.webp" alt="El Bestiario"
                 class="off h-[22px] sm:h-[26px] md:h-[28px] w-auto select-none transition-opacity duration-200 ease-out group-hover:opacity-0">
            <img src="assets/header/ON EL BESTIARIO.webp" alt=""
                 class="on pointer-events-none absolute inset-0 h-[22px] sm:h-[26px] md:h-[28px] w-auto select-none opacity-0 transition-opacity duration-200 ease-out group-hover:opacity-100">
          </a>

          <!-- Castillo (más grande, y un poco más abajo con mt-[2px]) -->
          <a href="#castillo" class="group relative inline-block nav-item mt-[2px]" data-nav="castillo" aria-label="El Castillo">
            <img src="assets/header/OFF El Castilo.webp" alt="El Castillo"
                 class="off h-[30px] sm:h-[36px] md:h-[42px] w-auto select-none transition-opacity duration-200 ease-out group-hover:opacity-0">
            <img src="assets/header/ON El Castilo.webp" alt=""
                 class="on pointer-events-none absolute inset-0 h-[30px] sm:h-[36px] md:h-[42px] w-auto select-none opacity-0 transition-opacity duration-200 ease-out group-hover:opacity-100">
          </a>

        </nav>
      </div>
    </div>
  </div>
</header>


  <!-- ===== Wrapper relativo: aquí ponemos el fondo que debe llegar hasta el final de Bestiario ===== -->
  <main class="relative z-0">

    <!-- FONDO del bosque (NO fijo). Altura dinámica hasta el inicio de #castillo -->
    <div class="bg-wrap absolute inset-x-0 top-0 -z-10 overflow-hidden" style="height: 100vh;">
      <img src="assets/Background Primera Sección.webp" alt="Fondo del bosque"
           class="bg-bosque w-full h-full object-cover object-center opacity-95 select-none willchange-transform">
    </div>

    <!-- ===== HERO Parallax ===== -->
    <section class="hero relative min-h-[100vh] md:h-[140vh] w-full overflow-visible z-10"></section>
      <!-- Luna grande recortada al borde izquierdo -->
      <div class="moon absolute left-0 top-[calc(6vh-20px)] sm:top-[calc(8vh-20px)] md:top-[calc(6vh-50px)]
                  w-[54vw] sm:w-[50vw] md:w-[46vw] max-w-[880px] aspect-square overflow-hidden z-[1] willchange-transform">
        <img src="assets/Luna Normal.webp" alt="Luna"
             class="w-full h-full object-cover pointer-events-none select-none">
      </div>     

      <!-- ===== TRAILER (sección tipo hero, con video) ===== -->
<section id="trailer" class="relative min-h-[100vh] md:h-[140vh] w-full overflow-visible z-10">
  <!-- Fondo opcional (puedes cambiar la imagen o quitarlo) -->
  <img src="assets/Background Primera Sección.webp" alt="" 
       class="absolute inset-0 w-full h-full object-cover opacity-0 pointer-events-none select-none -z-10">

       

  <!-- Contenedor del reproductor con marco verde -->
  <div class="mx-auto mt-24 md:mt-28 w-[92%] max-w-[1100px]">
    <div class="relative rounded-3xl border-4 border-lime-500/90 bg-black/40 backdrop-blur-sm overflow-hidden shadow-[0_0_40px_rgba(132,255,0,0.2)]">
      
      <!-- VIDEO -->
      <video id="draculaTrailer"
             class="block w-full aspect-video object-cover"
             preload="metadata"
             playsinline
             muted
             controlslist="nodownload noplaybackrate"
             poster="assets/posters/trailer-poster.jpg">
        <source src="assets/video/dracula-trailer.mp4" type="video/mp4">
        Tu navegador no soporta video HTML5.
      </video>

      

      

      <!-- Botón Play grande (overlay) -->
      <button id="trailerPlay"
              class="group absolute inset-0 grid place-items-center transition-opacity duration-300">
        <span class="inline-grid place-items-center w-20 h-20 md:w-24 md:h-24 rounded-full bg-black/60 backdrop-blur text-white border-2 border-white/70 shadow-lg">
          <!-- triángulo play -->
          <svg class="w-10 h-10 md:w-12 md:h-12 translate-x-[2px] group-hover:scale-110 transition"
               viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M8 5v14l11-7z" />
          </svg>
        </span>
      </button>
    </div>

    <!-- CTA y flecha (opcional) -->
    <div class="mt-6 text-center">
      <a href="#captura-bestias"
         class="inline-block px-6 py-3 border-2 border-lime-500 bg-black text-white font-black tracking-wider text-lg hover:bg-lime-500 hover:text-black transition-colors">
        EXPLORA UNA NUEVA AVENTURA
      </a>
      <div class="mt-3 animate-bounce text-lime-500">
        <svg class="w-6 h-6 mx-auto" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z" clip-rule="evenodd" />
        </svg>
      </div>
    </div>
  </div>
</section>

<!-- Nube derecha (pegada) -->
<div class="cloud-right-wrap absolute right-0 top-[60vh] sm:top-[62vh] md:top-[66vh] w-[32vw] sm:w-[28vw] md:w-[24vw] overflow-hidden z-[3] willchange-transform">
  <div
    class="cloud-right relative w-[66vw] sm:w-[50vw] md:w-[36vw] aspect-[2/1] willchange-transform"
    style="-webkit-mask-image:linear-gradient(to left, rgba(0,0,0,0.1), rgba(0,0,0,1) 22%, rgba(0,0,0,1)); mask-image:linear-gradient(to left, rgba(0,0,0,0.1), rgba(0,0,0,1) 22%, rgba(0,0,0,0.1));">
    <img src="assets/Nube Morada A.webp" alt="Nube derecha"
         class="w-full h-full object-cover pointer-events-none select-none transform -scale-x-100">
  </div>
</div>

<!-- Nube izquierda (pegada) -->
<div class="cloud-left-wrap absolute left-[-5vw] top-[55vh] sm:top-[58vh] md:top-[50vh] w-[40vw] sm:w-[35vw] md:w-[30vw] overflow-hidden z-[3] willchange-transform">
  <div class="cloud-left relative w-full aspect-[2/1] willchange-transform">
    <img src="assets/Nube Morada A.webp" alt="Nube izquierda grande"
         class="w-full h-full object-cover pointer-events-none select-none">
  </div>
</div>


<!-- Nube inferior derecha (muy abajo, pero aún visible) -->
<div class="cloud-low absolute right-[-11vh]  top-[92vh] sm:top-[91vh] md:top-[90vh]
            w-[80vw] sm:w-[60vw] md:w-[46vw] max-w-[900px] aspect-[2/1] opacity-80 z-[90] willchange-transform">
  <img src="assets/Nube Morada Blurr B.webp" alt="Nube baja derecha"
       class="w-full h-full object-cover pointer-events-none select-none">
</div>


<!-- Nube inferior izquierda (más abajo que la derecha, reflejada) -->
<div class="cloud-low-left absolute left-[-11vh] top-[96vh] sm:top-[95vh] md:top-[99vh]
            w-[80vw] sm:w-[60vw] md:w-[46vw] max-w-[900px] aspect-[2/1] opacity-80 z-[90] willchange-transform">
  <img src="assets/Nube Morada Blurr B.webp" alt="Nube baja izquierda"
       class="w-full h-full object-cover pointer-events-none select-none transform -scale-x-100">
</div>

<!-- NIEBLA FINAL: ancho completo, sin opacidad ni recortes -->
<div class="fixed top-[60vh] left-0 right-0 w-full h-[40vh] z-[50] pointer-events-none">
  <img src="assets/Niebla General (1).webp" alt="Niebla general"
       class="w-full h-full object-fill select-none pointer-events-none" />
</div>


      <!-- Sello/Título centrado -->
      <div class="title absolute left-1/2 -translate-x-1/2 top-[20vh] sm:top-[24vh] md:top-[30vh]
                  w-[72vw] sm:w-[52vw] md:w-[44vw] max-w-[900px] z-[60] willchange-transform">
        <img src="assets/Sello A.webp" alt="Secretos del Bosque Prohibido"
             class="w-full h-full object-contain mx-auto pointer-events-none select-none">
      </div>
      

      <!-- Sello/Título centrado -->
<div class="title absolute left-1/2 -translate-x-1/2 top-[20vh] sm:top-[24vh] md:top-[30vh]
            w-[72vw] sm:w-[52vw] md:w-[44vw] max-w-[900px] z-[60] willchange-transform flex flex-col items-center">
  
  <!-- Imagen del sello -->
  <img src="assets/Sello A.webp" alt="Secretos del Bosque Prohibido"
       class="w-full h-full object-contain mx-auto pointer-events-none select-none">

  <!-- Botón y texto debajo del sello -->
  <div class="mt-6 flex flex-col items-center">
    <a href="#trailer"
       class="px-6 py-3 border-2 border-lime-500 text-white font-black tracking-wider text-lg sm:text-xl bg-black hover:bg-lime-500 hover:text-black transition-colors duration-300">
      CONOCE LA HISTORIA
    </a>

    <!-- Flecha verde hacia abajo -->
    <div class="mt-3 animate-bounce">
      <svg class="w-6 h-6 text-lime-500" fill="currentColor" viewBox="0 0 20 20">
        <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z" clip-rule="evenodd" />
      </svg>
    </div>

    <!-- Texto de instrucción -->
    <p class="mt-2 text-sm sm:text-base text-gray-300 text-center leading-snug max-w-xs">Haz scroll con la barra del mouse para comenzar la aventura</p>
  </div>
</div>


      <!-- Fade inferior para transición suave -->
      <div class="pointer-events-none absolute inset-x-0 -bottom-1 h-16 sm:h-20 md:h-24 z-[45]"
           style="background:linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.35) 55%, rgba(0,0,0,0.85) 100%);"></div>
    </section>

    

        
    <!-- ===== BESTIARIO ===== -->
<section id="captura-bestias" class="relative z-10 min-h-[100vh] md:min-h-[110vh] flex flex-col md:flex-row-reverse items-center justify-center p-6 overflow-visible">

  <!-- Nube Verde B - esquina superior derecha -->
  <div class="absolute top-10 right-[-1rem] w-40 sm:w-48 md:w-64 lg:w-80 opacity-90 -z-10 pointer-events-none">
    <img src="assets/Nube Verde B.webp" alt="Nube Verde B" class="w-full h-auto object-contain select-none" />
  </div>

  <!-- Nube Verde B - esquina inferior izquierda -->
  <div class="absolute -bottom-16 sm:-bottom-20 md:-bottom-24 lg:-bottom-40 left-6 sm:left-8 md:left-12 w-56 sm:w-72 md:w-96 lg:w-[28rem] opacity-90 -z-10 pointer-events-none">
    <img src="assets/Nube Verde B.webp" alt="Nube Verde B" class="w-full h-auto object-contain select-none" />
  </div>

  <!-- Nube Verde C - parte superior izquierda -->
  <div class="absolute top-[-8vh] sm:top-[-20vh] left-[-4vw] sm:left-[-5vw] w-56 sm:w-72 md:w-96 lg:w-[28rem] opacity-90 -z-10 pointer-events-none" id="nube-c">
    <img src="assets/Nube Verde B.webp" alt="Nube Verde B" class="w-full h-auto object-contain select-none" />
  </div>
    
  <!-- Castillo Maqueta -->
  <div class="relative -z-30 mt-8 md:mt-0 md:mr-12 w-[80vw] sm:w-[70vw] md:w-[60vw] max-w-[600px]">
    <img src="assets/Castillo Maqueta.webp" alt="Castillo Maqueta" class="w-full h-auto select-none pointer-events-none" />
    
    <!-- Luna Verde detrás del castillo -->
<img src="assets/Luna Verde.webp" alt="Luna Verde" 
     class="absolute top-[calc(-40vh-20px)] 
            max-[639px]:top-[-20vh] 
            sm:top-[calc(-35vh-20px)] 
            left-[-3vw] 
            w-[54vw] max-w-[880px] aspect-square 
            opacity-80 select-none pointer-events-none -z-40 object-cover" />
  </div>

  <!-- Texto descriptivo -->
  <div class="relative z-30 max-w-xl text-white text-center md:text-left p-4 md:p-8 flex flex-col items-center md:items-start">

    <!-- Título -->
    <h2 class="text-xl sm:text-2xl md:text-3xl font-black uppercase leading-tight mb-4 text-center md:text-">
      Conviértete en el<br />
      <span class="text-white">Señor del Castillo Drácula</span>
    </h2>

    <!-- Caja de texto -->
    <div class="border-2 border-lime-500 bg-black text-white p-4 md:p-6 rounded-lg max-w-md text-sm sm:text-base leading-relaxed text-center md:text-left mb-6">
      Lorem ipsum dolor sit amet consectetur. Id tortor ipsum nisl duis massa. In non amet urna at in proin sed. Tellus facilisis
      ipsum iaculis mauris eget nisl in laoreet et. Eget tincidunt amet donec fringilla nisi diam augue. Blandit suspendisse
      elementum cras a molestie vivamus pulvinar enim sed.
    </div>

    <!-- CTA -->
    <div class="text-center mt-2">
      <p class="text-xs sm:text-sm uppercase tracking-widest text-gray-300 mb-1">Tienes el castillo. Ahora</p>
      <p class="text-2xl sm:text-3xl md:text-4xl font-extrabold text-white uppercase tracking-wide mb-2">Captura a las bestias</p>

      <!-- Flecha -->
      <div class="mt-2 animate-bounce">
        <svg class="w-6 h-6 text-lime-500 mx-auto" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 10.94l3.71-3.71a.75.75 0 111.06 1.06l-4.24 4.24a.75.75 0 01-1.06 0L5.21 8.29a.75.75 0 01.02-1.08z" clip-rule="evenodd" />
        </svg>
      </div>
    </div>
  </div>

<!-- Corte de Nubes MÁS ABAJO, al borde inferior del castillo -->
<div class="absolute 
            bottom-[19rem]                 <!-- 📱 en móvil: más arriba -->
            sm:bottom-[-24rem] 
            md:bottom-[-26rem] 
            lg:bottom-[-30rem] 
            left-0 right-0 w-full -z-20 pointer-events-none">
  <img src="assets/Corte Nubes.webp" alt="Corte Nubes"
       class="w-full h-auto object-cover select-none pointer-events-none" />
</div>



</section>



<!-- ===== CASTILLO ===== -->



 
<section id="castillo" class="relative z-10 overflow-visible">
  <div class="relative w-full h-[calc(100vw*2.0833)] min-h-screen">

    <!-- Corte de Nubes encima de la unión con Bestiario -->
<div class="absolute
            -top-[11rem]      /* móvil */
            sm:-top-[14rem]
            md:-top-[16rem]
            lg:-top-[27rem]
            left-0 right-0 w-full
            z-[30] pointer-events-none">
  <img src="assets/Corte Nubes.webp" alt="Corte Nubes"
       class="w-full h-auto object-cover select-none pointer-events-none" />
</div>


    <img src="assets/Background Cielo Castillo.webp" 
     alt="Fondo Cielo Castillo"
     class="absolute inset-0 w-full h-full object-cover pointer-events-none select-none"
     style="top:-10px; z-index:-100;" />



    

    <!-- 1) Fondo (cielo+suelo) -->
    <img src="assets/Background Castillo Full.webp" alt="Castillo fondo"
         class="absolute inset-0 -z-10 w-full h-full object-contain pointer-events-none select-none"
         style="object-position:center top;" />



         

<div id="castillo-moon-slot"
  class="absolute z-[-20] w-[60vw] aspect-square pointer-events-none select-none overflow-visible"
  style="top: 30svh; left: 10vw;">
  <img src="assets/Luna Verde.webp" alt="Luna Verde Castillo"
       class="castillo-green-moon absolute inset-0 w-full h-full object-contain opacity-0 willchange-transform pointer-events-none select-none" />
</div>

<style>
  @media (min-width: 1024px) {
    #castillo-moon-slot {
      top: 80svh !important; /* más abajo en desktop */
      left: 8vw !important;  /* más hacia la izquierda en desktop */
    }
  }
</style>



    <!-- 4) Ramas y enredaderas (encima del castillo) -->
    <!-- Rama morada derecha (media altura, responsive) -->
<img src="assets/Rama Arbol Morado Alejandose.webp" alt="Rama morada"
     class="branch-purple-far absolute
            right-[-10vw] top-[30%] w-[100vw]              <!-- 📱 móvil -->
            sm:right-[-12vw] sm:top-[58%] sm:w-[115vw]     <!-- tablet -->
            md:right-[-10vw] md:top-[70%] md:w-[92vw]      <!-- desktop mediano -->
            lg:right-[-8vw]  lg:top-[43%] lg:w-[74vw]      <!-- desktop grande -->
            xl:right-[-6vw]  xl:top-[40%] xl:w-[68vw]      <!-- pantallas XL -->
            max-w-none object-contain pointer-events-none select-none z-[35]" />


    <!-- Rama verde (medio–baja) -->
    <img src="assets/Corte Rama Arbol Verde.webp" alt="Rama verde"
         class="branch-green-cut absolute
                left-[-16vw] bottom-[-20vh] w-[190vw]
                sm:left-[-14vw] sm:bottom-[-14vh] sm:w-[165vw]
                md:left-[-10vw] md:bottom-[-8vh]  md:w-[135vw]
                lg:left-[-8vw]  lg:bottom-[-6vh]  lg:w-[118vw]
                xl:left-[-6vw]  xl:bottom-[-4vh]  xl:w-[110vw]
                max-w-none object-contain pointer-events-none select-none z-[30]" />

    <!-- Rama libro morada (primer plano) -->
    <img src="assets/Rama del Libro Morado.webp" alt="Rama libro morada"
         class="branch-book-purple absolute
                right-[-22vw] bottom-[-24vh] w-[210vw]
                sm:right-[-20vw] sm:bottom-[-22vh] sm:w-[185vw]
                md:right-[-18vw] md:bottom-[-20vh] md:w-[150vw]
                lg:right-[-16vw] lg:bottom-[-18vh] lg:w-[120vw]
                xl:right-[-14vw] xl:bottom-[-16vh] xl:w-[108vw]
                max-w-none object-contain pointer-events-none select-none z-[50]" />

    <!-- Enredaderas base -->
    <img src="assets/Corte Enredaderas.webp" alt="Enredaderas"
         class="vine-cut absolute left-1/2 -translate-x-1/2
                bottom-[-36vh] w-[185vw]
                sm:bottom-[-38vh] sm:w-[165vw]
                md:bottom-[-40vh] md:w-[145vw]
                lg:bottom-[-38vh] lg:w-[128vw]
                xl:bottom-[-36vh] xl:w-[120vw]
                max-w-none object-cover pointer-events-none select-none z-[45]" />

    <!-- Enredaderas blurr (más abajo, profundidad) -->
<img src="assets/Corte Enredadera Blurr.webp" alt="Enredaderas desenfocadas"
     class="vine-blurr absolute left-1/2 -translate-x-1/2
            bottom-[-40vh] w-[100vw]               <!-- 📱 móvil -->
            sm:bottom-[-62vh] sm:w-[188vw]         <!-- tablet -->
            md:bottom-[-66vh] md:w-[50vw]         <!-- desktop mediano -->
            lg:bottom-[-80vh] lg:w-[100vw]         <!-- desktop grande -->
            xl:bottom-[-58vh] xl:w-[130vw]         <!-- pantallas XL -->
            max-w-none object-cover pointer-events-none select-none z-[44]" />
  </div>

  
</section>


   

  </main>

  <!-- GSAP + ScrollTrigger -->
 <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script>
  gsap.registerPlugin(ScrollTrigger);

  /* ===== Ajusta la ALTURA del fondo para que llegue EXACTO
     hasta el INICIO de #castillo (o sea, final de Bestiario) ===== */
  function fitBgToBestiarioEnd() {
    const castillo = document.querySelector('#castillo');
    const bgWrap   = document.querySelector('.bg-wrap');
    if (!castillo || !bgWrap) return;

    const topCastillo = castillo.getBoundingClientRect().top + window.scrollY;
    bgWrap.style.height = topCastillo + 'px';
  }

  window.addEventListener('load', fitBgToBestiarioEnd);
  window.addEventListener('resize', fitBgToBestiarioEnd);
  window.addEventListener('orientationchange', fitBgToBestiarioEnd);

  /* ===== Parallax del FONDO desde que entra BESTIARIO hasta su FINAL ===== */
  function mountBgParallax() {
    ScrollTrigger.killTweensOf('.bg-bosque');
    ScrollTrigger.getAll().forEach(st => {
      if (st.vars?.id === 'bg-parallax') st.kill();
    });

    gsap.to(".bg-bosque", {
      y: () => (window.innerWidth >= 768 ? -240 : -120),
      ease: "none",
      scrollTrigger: {
        id: "bg-parallax",
        trigger: "#bestiario",
        start: "top bottom",
        end: "bottom top",
        scrub: true
      }
    });
  }
  window.addEventListener('load', mountBgParallax);
  window.addEventListener('resize', () => {
    fitBgToBestiarioEnd();
    mountBgParallax();
  });

  /* ===== Respiración / flotación suave de elementos ===== */
  gsap.to(".moon",            { y: 18, scale: 1.025, duration: 6,  yoyo: true, repeat: -1, ease: "sine.inOut" });
  gsap.to(".cloud-left",      { x: 24, y: -8,  duration: 10, repeat: -1, yoyo: true, ease: "sine.inOut" });
  gsap.to(".cloud-right",     { x: -22, y: 6,  duration: 12, repeat: -1, yoyo: true, ease: "sine.inOut" });
  gsap.to(".cloud-low",       { x: 16, y: 12, duration: 14, repeat: -1, yoyo: true, ease: "sine.inOut" });
  gsap.to(".cloud-low-left",  { x: -16, y: 12, duration: 14, repeat: -1, yoyo: true, ease: "sine.inOut" });

  /* ===== Parallax en scroll del hero ===== */
  gsap.timeline({
    scrollTrigger: { trigger: ".hero", start: "top top", end: "bottom top", scrub: true }
  })
    .to(".moon",            { y: -60 }, 0)
    .to(".cloud-left",      { y: -40 }, 0)
    .to(".cloud-right",     { y: -30 }, 0)
    .to(".cloud-low",       { y: -18 }, 0)
    .to(".cloud-low-left",  { y: -18 }, 0)
    .to(".title",           { y: -32, opacity: 0.98 }, 0);

  /* ===== Nav activo por clic ===== */
  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('is-active'));
      item.classList.add('is-active');
    });
  });

  /* ============================================================
     ONE-SCROLL JUMP (Hero) -> ahora baja a #trailer (NO a bestiario)
     ============================================================ */
  (function setupOneScrollJump() {
    const hero   = document.querySelector('.hero');
    const target = document.querySelector('#trailer'); // 👈 cambio clave
    if (!hero || !target) return;

    let locking = false;
    let touchStartY = null;

    function scrollToTarget() {
      if (locking) return;
      locking = true;
      const top = target.getBoundingClientRect().top + window.scrollY;
      window.scrollTo({ top, behavior: 'smooth' });
      setTimeout(() => { locking = false; }, 1200);
    }

    function inHeroViewport() {
      const r = hero.getBoundingClientRect();
      return r.top < window.innerHeight && r.bottom > 0;
    }

    function onWheel(e) {
      if (!inHeroViewport()) return;
      if (e.deltaY > 15) {
        e.preventDefault();
        scrollToTarget();
      }
    }
    function onTouchStart(e) {
      if (!inHeroViewport()) return;
      if (e.touches && e.touches.length === 1) touchStartY = e.touches[0].clientY;
    }
    function onTouchEnd(e) {
      if (!inHeroViewport() || touchStartY == null) return;
      const endY = (e.changedTouches && e.changedTouches[0]?.clientY) ?? touchStartY;
      const dy = touchStartY - endY;
      touchStartY = null;
      if (dy > 30) scrollToTarget();
    }

    hero.addEventListener('wheel', onWheel, { passive: false });
    hero.addEventListener('touchstart', onTouchStart, { passive: true });
    hero.addEventListener('touchend', onTouchEnd, { passive: true });
  })();

  /* ============================================================
     ONE-SCROLL en #trailer → salta a #captura-bestias
     ============================================================ */
  (function setupTrailerToBestiarioJump() {
    const trailer  = document.querySelector('#trailer');
    const bestiario = document.querySelector('#captura-bestias');
    if (!trailer || !bestiario) return;

    let locking = false;
    let touchStartY = null;

    const inViewport = el => {
      const r = el.getBoundingClientRect();
      return r.top < window.innerHeight && r.bottom > 0;
    };
    const jumpTo = (el) => {
      const top = el.getBoundingClientRect().top + window.scrollY;
      window.scrollTo({ top, behavior: 'smooth' });
      setTimeout(() => { locking = false; }, 1200);
    };

    function onWheel(e) {
      if (!inViewport(trailer) || locking) return;
      if (e.deltaY > 15) {
        e.preventDefault();
        locking = true;
        jumpTo(bestiario);
      }
    }
    function onTouchStart(e) {
      if (!inViewport(trailer)) return;
      if (e.touches && e.touches.length === 1) touchStartY = e.touches[0].clientY;
    }
    function onTouchEnd(e) {
      if (!inViewport(trailer) || touchStartY == null || locking) return;
      const endY = (e.changedTouches && e.changedTouches[0]?.clientY) ?? touchStartY;
      const dy = touchStartY - endY; // swipe up
      touchStartY = null;
      if (dy > 30) {
        locking = true;
        jumpTo(bestiario);
      }
    }

    trailer.addEventListener('wheel', onWheel, { passive: false });
    trailer.addEventListener('touchstart', onTouchStart, { passive: true });
    trailer.addEventListener('touchend', onTouchEnd, { passive: true });
  })();

  /* ============================================================
     MORPHING DE LUNA (solo luna) + ONE-SCROLL JUMP bidireccional
     (con regreso primero a #trailer al subir desde bestiario)
     ============================================================ */
  let moonMorphST;

  function centerOf(el) {
    const r = el.getBoundingClientRect();
    return {
      x: r.left + r.width / 2 + window.scrollX,
      y: r.top  + r.height/ 2 + window.scrollY
    };
  }

  function mountMoonMorph() {
    if (moonMorphST) { moonMorphST.kill(); moonMorphST = null; }

    const moon     = document.querySelector('.moon');
    const moonImg  = moon?.querySelector('img');
    const green    = document.querySelector('#captura-bestias img[alt="Luna Verde"]');
    const triggerS = document.querySelector('#captura-bestias');
    const hero     = document.querySelector('.hero');
    const trailer  = document.querySelector('#trailer'); // 👈 nuevo

    if (!moon || !moonImg || !green || !triggerS || !hero) return;

    const greenTargetOpacity = parseFloat(getComputedStyle(green).opacity) || 0.8;

    gsap.set(moon,    { clearProps: "x,y,opacity,scale" });
    gsap.set(moonImg, { filter: "hue-rotate(0deg) saturate(1) brightness(1)" });
    gsap.set(green,   { opacity: 0 });

    const cMoon  = centerOf(moon);
    const cGreen = centerOf(green);
    const dx = cGreen.x - cMoon.x;
    const dy = cGreen.y - cMoon.y;

    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: triggerS,
        start: "top bottom",
        end: "center center",
        scrub: 2.5
      }
    });

    tl.to(moon,   { x: dx, y: dy, scale: 0.92, ease: "power1.out" }, 0)
      .to(moonImg,{ filter: "hue-rotate(95deg) saturate(1.35) brightness(1.05)", ease: "power1.out" }, 0)
      .to(green,  { opacity: greenTargetOpacity, ease: "power1.out" }, 0.65)
      .to(moon,   { opacity: 0, ease: "power1.out" }, 0.8);

    moonMorphST = tl.scrollTrigger;

    /* ===== one-scroll up/down entre secciones (redirecciones) ===== */
    const JUMP_LOCK_MS   = 1600;
    const WHEEL_THRESH   = 12;
    const SWIPE_THRESH   = 28;
    const HIDE_DELAY_MS  = 350;

    let lockingDown = false;
    let lockingUp   = false;
    let tStartHero  = null;
    let tStartBest  = null;

    const inViewport = el => {
      const r = el.getBoundingClientRect();
      return r.top < window.innerHeight && r.bottom > 0;
    };
    const jumpTo = (el) => {
      const top = el.getBoundingClientRect().top + window.scrollY;
      window.scrollTo({ top, behavior: 'smooth' });
    };

    // --- Hero: salto hacia abajo (ahora a trailer si existe) ---
    if (!hero.dataset.jumpDownAttached) {
      function onWheelDown(e) {
        if (!inViewport(hero)) return;
        if (e.deltaY > WHEEL_THRESH && !lockingDown) {
          e.preventDefault();
          lockingDown = true;
          jumpTo(trailer || triggerS); // 👈 cambio
          setTimeout(() => { lockingDown = false; }, JUMP_LOCK_MS);
        }
      }
      function onTouchStartHero(e) {
        if (!inViewport(hero)) return;
        if (e.touches?.length === 1) tStartHero = e.touches[0].clientY;
      }
      function onTouchEndHero(e) {
        if (!inViewport(hero) || tStartHero == null) return;
        const endY = e.changedTouches?.[0]?.clientY ?? tStartHero;
        const dy = tStartHero - endY;
        tStartHero = null;
        if (dy > SWIPE_THRESH && !lockingDown) {
          lockingDown = true;
          jumpTo(trailer || triggerS); // 👈 cambio
          setTimeout(() => { lockingDown = false; }, JUMP_LOCK_MS);
        }
      }

      hero.addEventListener('wheel', onWheelDown, { passive: false });
      hero.addEventListener('touchstart', onTouchStartHero, { passive: true });
      hero.addEventListener('touchend', onTouchEndHero, { passive: true });
      hero.dataset.jumpDownAttached = '1';
    }

    // --- Bestiario: salto hacia arriba (vuelve primero a trailer) ---
    if (!triggerS.dataset.jumpUpAttached) {
      function onWheelUp(e) {
        if (!inViewport(triggerS)) return;
        if (e.deltaY < -WHEEL_THRESH && !lockingUp) {
          e.preventDefault();
          lockingUp = true;
          jumpTo(trailer || hero); // 👈 cambio
          setTimeout(() => {
            const m  = document.querySelector('.moon');
            const mi = m?.querySelector('img');
            const g  = document.querySelector('#captura-bestias img[alt="Luna Verde"]');
            if (m && mi && g) {
              gsap.set(m,  { x: 0, y: 0, scale: 1, opacity: 1 });
              gsap.set(mi, { filter: "hue-rotate(0deg) saturate(1) brightness(1)" });
              gsap.set(g,  { opacity: 0 });
              ScrollTrigger.refresh();
            }
          }, HIDE_DELAY_MS);
          setTimeout(() => { lockingUp = false; }, JUMP_LOCK_MS);
        }
      }
      function onTouchStartBest(e) {
        if (!inViewport(triggerS)) return;
        if (e.touches?.length === 1) tStartBest = e.touches[0].clientY;
      }
      function onTouchEndBest(e) {
        if (!inViewport(triggerS) || tStartBest == null) return;
        const endY = e.changedTouches?.[0]?.clientY ?? tStartBest;
        const dy = tStartBest - endY;
        tStartBest = null;
        if (dy < -SWIPE_THRESH && !lockingUp) {
          lockingUp = true;
          jumpTo(trailer || hero); // 👈 cambio
          setTimeout(() => {
            const m  = document.querySelector('.moon');
            const mi = m?.querySelector('img');
            const g  = document.querySelector('#captura-bestias img[alt="Luna Verde"]');
            if (m && mi && g) {
              gsap.set(m,  { x: 0, y: 0, scale: 1, opacity: 1 });
              gsap.set(mi, { filter: "hue-rotate(0deg) saturate(1) brightness(1)" });
              gsap.set(g,  { opacity: 0 });
              ScrollTrigger.refresh();
            }
          }, HIDE_DELAY_MS);
          setTimeout(() => { lockingUp = false; }, JUMP_LOCK_MS);
        }
      }

      triggerS.addEventListener('wheel', onWheelUp, { passive: false });
      triggerS.addEventListener('touchstart', onTouchStartBest, { passive: true });
      triggerS.addEventListener('touchend', onTouchEndBest, { passive: true });
      triggerS.dataset.jumpUpAttached = '1';
    }
  }

  // Inicializa/recalcula (solo para la luna)
  window.addEventListener('load',  mountMoonMorph);
  window.addEventListener('resize', () => { mountMoonMorph(); ScrollTrigger.refresh(); });
  window.addEventListener('orientationchange', () => { mountMoonMorph(); ScrollTrigger.refresh(); });


  /* === NUBES: descenso desde HERO hasta #trailer (scrub) === */
function mountCloudDropToTrailer() {
  ScrollTrigger.getAll().forEach(st => {
    if (st.vars?.id === 'cloud-drop-left' || st.vars?.id === 'cloud-drop-right') st.kill();
  });

  const hero     = document.querySelector('.hero');
  const trailer  = document.querySelector('#trailer');
  const leftW    = document.querySelector('.cloud-left-wrap');
  const rightW   = document.querySelector('.cloud-right-wrap');
  if (!hero || !trailer || !leftW || !rightW) return;

  // Ayudantes para calcular delta Y dinámico (se reevalúan en refresh)
  const deltaToTrailer = (el, offset = 0) => {
    const elTop      = el.getBoundingClientRect().top + window.scrollY;
    const trailerTop = trailer.getBoundingClientRect().top + window.scrollY;
    return (trailerTop + offset) - elTop;
  };

  const isDesktop = () => window.innerWidth >= 768;

  // Nube izquierda
  gsap.to(leftW, {
    id: 'cloud-drop-left',
    y: () => deltaToTrailer(leftW, isDesktop() ? 40 : 24), // pequeño ajuste para que “aterrice” lindo
    ease: 'none',
    scrollTrigger: {
      id: 'cloud-drop-left',
      trigger: hero,
      start: 'bottom bottom',   // cuando el bottom del hero toca el bottom de la ventana
      endTrigger: '#trailer',
      end: 'top top',           // hasta que el top del trailer toca el top de la ventana
      scrub: true,
      invalidateOnRefresh: true
    }
  });

  // Nube derecha
  gsap.to(rightW, {
    id: 'cloud-drop-right',
    y: () => deltaToTrailer(rightW, isDesktop() ? 20 : 12),
    ease: 'none',
    scrollTrigger: {
      id: 'cloud-drop-right',
      trigger: hero,
      start: 'bottom bottom',
      endTrigger: '#trailer',
      end: 'top top',
      scrub: true,
      invalidateOnRefresh: true
    }
  });
}

window.addEventListener('load',  () => { mountCloudDropToTrailer(); ScrollTrigger.refresh(); });
window.addEventListener('resize', () => { mountCloudDropToTrailer(); ScrollTrigger.refresh(); });
window.addEventListener('orientationchange', () => { mountCloudDropToTrailer(); ScrollTrigger.refresh(); });

  /* ===== Parallax de continuidad en #trailer (luna + nubes bajan) ===== */
  function mountTrailerCarryParallax() {
    ScrollTrigger.getAll().forEach(st => {
      if (st.vars?.id === 'trailer-carry') st.kill();
    });

    const isDesktop = () => window.innerWidth >= 768;

    gsap.timeline({
      scrollTrigger: {
        id: 'trailer-carry',
        trigger: '#trailer',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      },
      defaults: { ease: 'none' }
    })
    .to('.moon', {
        y: () => isDesktop() ? '+=220' : '+=150',
        x: () => isDesktop() ? '+=20'  : '+=12',
        immediateRender: false
    }, 0)
    .to('.cloud-left', {
        y: () => isDesktop() ? '+=130' : '+=95',
        x: () => isDesktop() ? '-=24'  : '-=16',
        immediateRender: false
    }, 0)
    .to('.cloud-right', {
        y: () => isDesktop() ? '+=120' : '+=90',
        x: () => isDesktop() ? '+=22'  : '+=14',
        immediateRender: false
    }, 0)
    .to('.cloud-low', {
        y: () => isDesktop() ? '+=60' : '+=42',
        x: () => isDesktop() ? '+=10' : '+=6',
        immediateRender: false
    }, 0)
    .to('.cloud-low-left', {
        y: () => isDesktop() ? '+=60' : '+=42',
        x: () => isDesktop() ? '-=10' : '-=6',
        immediateRender: false
    }, 0);
  }
  window.addEventListener('load',  mountTrailerCarryParallax);
  window.addEventListener('resize', mountTrailerCarryParallax);
  window.addEventListener('orientationchange', mountTrailerCarryParallax);

  /* ===== Video overlay y autoplay inteligente ===== */
  (() => {
    const video = document.getElementById('draculaTrailer');
    const playBtn = document.getElementById('trailerPlay');
    if (!video || !playBtn) return;

    playBtn.addEventListener('click', async () => {
      try { video.muted = false; await video.play(); } catch(e) {}
      playBtn.style.opacity = '0';
      playBtn.style.pointerEvents = 'none';
    });
    video.addEventListener('play', () => {
      playBtn.style.opacity = '0';
      playBtn.style.pointerEvents = 'none';
    });
    video.addEventListener('pause', () => {
      playBtn.style.opacity = '1';
      playBtn.style.pointerEvents = 'auto';
    });

    const io = new IntersectionObserver(entries => {
      entries.forEach(async e => {
        if (e.isIntersecting) {
          try { await video.play(); } catch(_) {}
        } else {
          video.pause();
        }
      });
    }, { threshold: 0.4 });
    io.observe(video);
  })();


document.querySelectorAll('a[href="#trailer"]').forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const t = document.querySelector('#trailer');
      if (t) window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY, behavior: 'smooth' });
    });
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

  // 🌿 Ramas laterales → MÁS hacia los lados
  tl.from(q('.branch-green-cut'), {
    x: -600, opacity: 0, duration: 1.6, immediateRender: false
  }, 0);

  tl.from(q('.branch-purple-far'), {
    x: 600, opacity: 0, duration: 1.6, immediateRender: false
  }, 0);

  tl.from(q('.branch-book-purple'), {
    x: 700, opacity: 0, duration: 1.8, immediateRender: false
  }, 0.1);

  // 🌱 Enredaderas desde MÁS abajo
  tl.from(q('.vine-cut'), {
    y: 460, opacity: 0, duration: 1.8, immediateRender: false
  }, 0.2);
}

window.addEventListener('load',  () => { mountCastilloReveal(); ScrollTrigger.refresh(); });
window.addEventListener('resize', () => { mountCastilloReveal(); ScrollTrigger.refresh(); });
window.addEventListener('orientationchange', () => { mountCastilloReveal(); ScrollTrigger.refresh(); });

/* ===== LUNA: viaja al castillo, queda detrás y hace cross-fade a la luna verde ===== */
function mountMoonToCastillo() {
  const castillo = Array.from(document.querySelectorAll('section#castillo')).at(-1);
  const slot     = castillo?.querySelector('#castillo-moon-slot');
  const green    = castillo?.querySelector('.castillo-green-moon');
  const heroMoon = document.querySelector('.moon');

  if (!castillo || !slot || !green || !heroMoon) return;

  // helper centro + medidas
  const centerOf = (el) => {
    const r = el.getBoundingClientRect();
    return {
      x: r.left + r.width / 2 + window.scrollX,
      y: r.top  + r.height/ 2 + window.scrollY,
      w: r.width, h: r.height
    };
  };

  // matar instancias previas
  ScrollTrigger.getAll().forEach(st => {
    if (st.vars?.id === 'moon-to-castillo' || st.vars?.id === 'moon-z-swap') st.kill();
  });

  // z-index swap para que quede DETRÁS del recorte (z 25) y delante del fondo
  ScrollTrigger.create({
    id: 'moon-z-swap',
    trigger: castillo,
    start: 'top 75%',
    end:   'bottom top',
    onEnter:     () => gsap.set(heroMoon, { zIndex: 20 }),
    onLeaveBack: () => gsap.set(heroMoon, { zIndex: 60 }) // vuelve a su z alto en el hero
  });

  // timeline de viaje + cross-fade a luna verde
  const tl = gsap.timeline({
    defaults: { ease: 'none' },
    scrollTrigger: {
      id: 'moon-to-castillo',
      trigger: castillo,
      start: 'top bottom',   // cuando aparece el castillo por abajo
      end:   'top 45%',      // hasta llegar a la mitad aprox.
      scrub: true,
      invalidateOnRefresh: true
      // markers: true
    }
  });

  tl.to(heroMoon, {
    x: () => {
      const cM = centerOf(heroMoon);
      const cS = centerOf(slot);
      return cS.x - cM.x;
    },
    y: () => {
      const cM = centerOf(heroMoon);
      const cS = centerOf(slot);
      return cS.y - cM.y;
    },
    scale: () => {
      const rM = heroMoon.getBoundingClientRect();
      const rS = slot.getBoundingClientRect();
      return rS.width / rM.width;
    },
    transformOrigin: 'center center',
    immediateRender: false
  }, 0)
  // cross-fade: aparece la luna verde grande del slot
  .to(green, { opacity: 1 }, 0.55);
}

window.addEventListener('load',  () => { mountMoonToCastillo(); ScrollTrigger.refresh(); });
window.addEventListener('resize', () => { mountMoonToCastillo(); ScrollTrigger.refresh(); });
window.addEventListener('orientationchange', () => { mountMoonToCastillo(); ScrollTrigger.refresh(); });
  
 
</script>

</body>
</html>
