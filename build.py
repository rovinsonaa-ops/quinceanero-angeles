import os

output_path = r"C:\Users\Rovinson\.gemini\antigravity\scratch\quinceanero-angeles\index.html"

html_code = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover" />
  <title>Mis XV Años - Angeles | Disco Party 2026</title>
  
  <!-- Tipografías de Alta Costura: Bodoni Moda, Cinzel y Montserrat -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,700;0,6..96,900;1,6..96,700;1,6..96,900&family=Cinzel:wght@600;700;800;900&family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- Three.js para la Bola Disco 3D Real -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

  <style>
    /* =======================================================
       TOKENS CROMÁTICOS DISCO: AZUL ELÉCTRICO + VIOLETA + CIAN
       (60% Negro/Azul Profundo, 25% Azul, 10% Violeta/Magenta, 5% Cian/Blanco)
       ======================================================= */
    :root {
      --bg-black: #000000;
      --bg-deep: #020510;
      --bg-midnight: #050a18;
      --card-bg: rgba(5, 12, 28, 0.92);
      --card-border: rgba(37, 139, 255, 0.4);
      --card-inner-box: rgba(7, 18, 43, 0.85);

      /* Azules dominantes */
      --disco-blue-dark: #071b5c;
      --disco-blue-electric: #0a2fff;
      --disco-blue-vivid: #164dff;
      --disco-blue-bright: #258bff;

      /* Ciano como luz */
      --disco-cyan: #00d9ff;
      --disco-cyan-bright: #5cebff;

      /* Violeta y Magenta como elegancia */
      --disco-violet: #5b1fff;
      --disco-violet-bright: #7a2cff;
      --disco-purple: #a855f7;
      --disco-magenta: #d21fff;
      --disco-pink-neon: #ff35d1;

      /* Highlights y Blanco puro */
      --white-pure: #ffffff;
      --white-ice: #eaf7ff;
      --silver-mid: #cbd5e1;
      --gold-accent: #f59e0b;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html, body {
      width: 100%;
      min-height: 100vh;
      min-height: 100dvh;
      background-color: var(--bg-black);
      color: var(--white-pure);
      font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      overflow-x: hidden;
      position: relative;
    }

    /* =======================================================
       FONDO DISCO GLOBAL CON PROFUNDIDAD AZUL & NEÓN
       ======================================================= */
    #ambient-bg {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      height: 100dvh;
      pointer-events: none;
      z-index: 0;
      background: 
        radial-gradient(circle at 50% 12%, rgba(22, 77, 255, 0.32) 0%, transparent 60%),
        radial-gradient(circle at 10% 70%, rgba(122, 44, 255, 0.22) 0%, transparent 50%),
        radial-gradient(circle at 90% 75%, rgba(0, 217, 255, 0.2) 0%, transparent 50%),
        radial-gradient(circle at 50% 88%, rgba(210, 31, 255, 0.15) 0%, transparent 45%),
        var(--bg-deep);
    }

    /* Rayos volumétricos ambientales en azul y cian */
    .volumetric-rays {
      position: fixed;
      top: 0;
      left: 50%;
      transform: translateX(-50%);
      width: 100%;
      max-width: 550px;
      height: 100%;
      pointer-events: none;
      z-index: 1;
      overflow: hidden;
      opacity: 0.65;
    }

    .v-ray {
      position: absolute;
      top: -120px;
      width: 2.5px;
      height: 130vh;
      background: linear-gradient(180deg, rgba(234, 247, 255, 0.9) 0%, rgba(37, 139, 255, 0.45) 40%, rgba(0, 217, 255, 0.2) 70%, transparent 90%);
      filter: blur(2px);
      transform-origin: top center;
    }

    .v-ray-1 { left: 20%; transform: rotate(-25deg); animation: sweepRay1 7s ease-in-out infinite alternate; }
    .v-ray-2 { left: 50%; transform: rotate(0deg); animation: sweepRay2 5.5s ease-in-out infinite alternate; }
    .v-ray-3 { left: 80%; transform: rotate(25deg); animation: sweepRay3 8s ease-in-out infinite alternate; }

    @keyframes sweepRay1 { 0% { transform: rotate(-35deg); } 100% { transform: rotate(-10deg); } }
    @keyframes sweepRay2 { 0% { transform: rotate(-15deg); } 100% { transform: rotate(15deg); } }
    @keyframes sweepRay3 { 0% { transform: rotate(10deg); } 100% { transform: rotate(35deg); } }

    /* Canvas global de partículas y cascada */
    #particles-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 2;
    }

    /* Flash de pantalla cinematográfico */
    #cinematic-flash {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 99999;
      background: radial-gradient(circle at center, #ffffff 15%, rgba(0, 217, 255, 0.85) 60%, rgba(22, 77, 255, 0.6) 100%);
      opacity: 0;
      transition: opacity 0.35s ease-out;
    }

    #cinematic-flash.active {
      opacity: 1;
      transition: opacity 0.12s ease-in;
    }

    /* VIEWPORT CONTAINER MOBILE FIRST */
    .app-viewport {
      width: 100%;
      max-width: 440px;
      margin: 0 auto;
      min-height: 100vh;
      min-height: 100dvh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: max(16px, env(safe-area-inset-top));
      padding-bottom: max(32px, env(safe-area-inset-bottom));
      padding-left: max(16px, env(safe-area-inset-left));
      padding-right: max(16px, env(safe-area-inset-right));
      position: relative;
      z-index: 10;
    }

    /* =======================================================
       BOTÓN FLOTANTE DE MÚSICA — DISCO DE VINILO GIRATORIO
       ======================================================= */
    .music-floating-ctrl {
      position: fixed;
      top: max(14px, env(safe-area-inset-top));
      right: max(14px, env(safe-area-inset-right));
      z-index: 1000;
      min-height: 48px;
      background: rgba(5, 12, 28, 0.94);
      border: 1.5px solid var(--disco-cyan);
      border-radius: 50px;
      padding: 6px 16px 6px 6px;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      box-shadow: 0 4px 22px rgba(0, 217, 255, 0.4), inset 0 0 12px rgba(0,0,0,0.85);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .music-floating-ctrl:active {
      transform: scale(0.93);
    }

    .vinyl-disc {
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: 
        conic-gradient(
          from 0deg,
          rgba(255, 255, 255, 0.26) 0deg,
          transparent 45deg,
          rgba(255, 255, 255, 0.26) 90deg,
          transparent 135deg,
          rgba(255, 255, 255, 0.26) 180deg,
          transparent 225deg,
          rgba(255, 255, 255, 0.26) 270deg,
          transparent 315deg,
          rgba(255, 255, 255, 0.26) 360deg
        ),
        repeating-radial-gradient(
          circle at center,
          #0b0d14 0px,
          #0b0d14 1.5px,
          #1a2236 2px,
          #06080e 3px
        );
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.9), 0 0 12px rgba(0, 217, 255, 0.4);
      border: 1px solid #1e293b;
      animation: spinVinylDisc 2.8s linear infinite;
      animation-play-state: paused;
    }

    .music-floating-ctrl.playing .vinyl-disc {
      animation-play-state: running;
    }

    .vinyl-center-label {
      width: 14px;
      height: 14px;
      border-radius: 50%;
      background: radial-gradient(circle, var(--disco-cyan) 30%, var(--disco-blue-vivid) 100%);
      border: 1px solid rgba(255, 255, 255, 0.8);
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: inset 0 0 3px rgba(0,0,0,0.8);
    }

    .vinyl-spindle-hole {
      width: 3.5px;
      height: 3.5px;
      border-radius: 50%;
      background: #020510;
      border: 0.8px solid #cbd5e1;
    }

    @keyframes spinVinylDisc {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    .music-label-tag {
      font-size: 0.8rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      text-shadow: 0 0 10px rgba(0, 217, 255, 0.8);
    }

    /* =======================================================
       PANTALLA 1: PORTADA DISCO GLAM AZUL & VIOLETA
       ======================================================= */
    #screen-welcome {
      width: 100%;
      background: var(--card-bg);
      border-radius: 28px;
      padding: 32px 20px 36px 20px;
      text-align: center;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(37, 139, 255, 0.25), 0 0 45px rgba(22, 77, 255, 0.3);
      border: 1.5px solid var(--card-border);
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      transition: opacity 0.5s ease-out, transform 0.5s ease-out;
    }

    #screen-welcome.fading-out {
      opacity: 0;
      transform: scale(0.96) translateY(-20px);
      pointer-events: none;
    }

    /* Corona Plateada Diamante con destello azulado */
    .silver-crown-vector {
      width: 52px;
      height: auto;
      margin-bottom: 8px;
      filter: drop-shadow(0 0 10px rgba(234, 247, 255, 0.9)) drop-shadow(0 0 22px rgba(0, 217, 255, 0.7));
      animation: crownShine 3.5s ease-in-out infinite alternate;
    }

    @keyframes crownShine {
      0% { filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.8)) drop-shadow(0 0 15px rgba(0, 217, 255, 0.5)); }
      100% { filter: drop-shadow(0 0 15px rgba(255, 255, 255, 1)) drop-shadow(0 0 30px rgba(37, 139, 255, 0.85)); }
    }

    .heading-xv {
      font-family: 'Cinzel', serif;
      font-size: 0.96rem;
      font-weight: 700;
      letter-spacing: 8px;
      color: var(--white-ice);
      text-transform: uppercase;
      margin-bottom: 2px;
      text-shadow: 0 0 15px rgba(255, 255, 255, 0.75), 0 0 25px rgba(37, 139, 255, 0.6);
    }

    /* Nombre ANGELES en Bodoni Moda 900 con Degradado de Luz Azul-Cian-Violeta */
    .heading-angeles {
      font-family: 'Bodoni Moda', 'Playfair Display', serif;
      font-size: 3.4rem;
      font-weight: 900;
      letter-spacing: 4px;
      line-height: 1.25;
      padding-top: 6px;
      padding-bottom: 4px;
      text-transform: uppercase;
      background: linear-gradient(180deg, #ffffff 0%, #eaf7ff 22%, #5cebff 50%, #258bff 75%, #a855f7 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 20px rgba(0, 217, 255, 0.85)) drop-shadow(0 4px 8px rgba(0, 0, 0, 0.9));
      margin-bottom: 4px;
      display: inline-block;
    }

    .sub-badge-party {
      display: inline-block;
      font-family: 'Cinzel', serif;
      font-size: 0.84rem;
      font-weight: 800;
      letter-spacing: 3px;
      color: var(--disco-cyan-bright);
      text-transform: uppercase;
      margin-bottom: 14px;
      text-shadow: 0 0 12px rgba(0, 217, 255, 0.75);
    }

    /* ESCENARIO BOLA DISCO 3D (THREE.JS) */
    .disco-3d-stage {
      position: relative;
      width: 100%;
      max-width: 360px;
      height: 380px;
      margin-bottom: 18px;
      display: flex;
      justify-content: center;
      align-items: center;
      cursor: grab;
      touch-action: pan-y; /* Permite scroll vertical en móvil sin interferir */
    }

    .disco-3d-stage:active {
      cursor: grabbing;
    }

    #disco-three-canvas {
      width: 100% !important;
      height: 100% !important;
      display: block;
      pointer-events: auto;
    }

    .disco-drag-hint {
      position: absolute;
      bottom: 8px;
      left: 50%;
      transform: translateX(-50%);
      font-size: 0.68rem;
      color: rgba(234, 247, 255, 0.75);
      letter-spacing: 1.5px;
      text-transform: uppercase;
      pointer-events: none;
      background: rgba(2, 5, 16, 0.65);
      padding: 3px 14px;
      border-radius: 20px;
      border: 1px solid rgba(0, 217, 255, 0.25);
      backdrop-filter: blur(4px);
    }

    /* CALENDARIO ELEGANTE EN AZUL MEDIANOCHE */
    .calendar-wrapper {
      background: var(--card-inner-box);
      border: 1px solid rgba(37, 139, 255, 0.25);
      border-radius: 20px;
      padding: 18px 16px;
      width: 100%;
      margin-bottom: 22px;
      box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.6);
    }

    .calendar-month-title {
      font-family: 'Cinzel', serif;
      font-size: 0.9rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 3px;
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .calendar-grid-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      margin-bottom: 16px;
    }

    .calendar-grid-table th {
      color: #64748b;
      font-weight: 600;
      padding: 4px 0;
    }

    .calendar-grid-table td {
      padding: 6px 0;
      color: #94a3b8;
      font-weight: 500;
    }

    .day-oct-19 {
      color: #ffffff !important;
      font-weight: 800;
    }

    .day-oct-19-badge {
      display: inline-flex;
      justify-content: center;
      align-items: center;
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, var(--disco-blue-vivid), var(--disco-cyan));
      border-radius: 50%;
      box-shadow: 0 0 16px var(--disco-cyan);
      animation: pulseDayBadge 1.6s infinite alternate;
      border: 1.5px solid #ffffff;
    }

    @keyframes pulseDayBadge {
      0% { transform: scale(0.95); box-shadow: 0 0 8px var(--disco-blue-vivid); }
      100% { transform: scale(1.1); box-shadow: 0 0 22px var(--disco-cyan); }
    }

    /* CONTEO REGRESIVO */
    .countdown-title-bar {
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 4px;
      margin-bottom: 10px;
    }

    .countdown-boxes-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
    }

    .time-box {
      background: rgba(2, 5, 16, 0.95);
      border: 1px solid rgba(0, 217, 255, 0.35);
      border-radius: 14px;
      padding: 10px 4px;
      text-align: center;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.7);
    }

    .time-box-num {
      font-family: 'Montserrat', sans-serif;
      font-size: 1.55rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.1;
      text-shadow: 0 0 12px rgba(0, 217, 255, 0.75);
    }

    .time-box-lbl {
      font-size: 0.68rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* BOTÓN PRINCIPAL ABRIR INVITACIÓN (ÁREA TÁCTIL GRANDE Y CÓMODA) */
    .btn-open-invitation {
      min-height: 54px;
      width: 100%;
      max-width: 320px;
      background: linear-gradient(135deg, var(--disco-blue-vivid) 0%, var(--disco-violet-bright) 50%, var(--disco-cyan) 100%);
      background-size: 200% 200%;
      animation: pulseOpenBtn 2.4s infinite alternate;
      color: #ffffff;
      border: none;
      padding: 16px 36px;
      font-family: 'Cinzel', serif;
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: 2.5px;
      border-radius: 50px;
      cursor: pointer;
      box-shadow: 0 8px 32px rgba(0, 217, 255, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.6);
      transition: transform 0.2s, box-shadow 0.2s;
      text-transform: uppercase;
      border: 1px solid rgba(255, 255, 255, 0.4);
      position: relative;
    }

    .btn-open-invitation:active {
      transform: scale(0.96);
    }

    @keyframes pulseOpenBtn {
      0% { transform: scale(1); background-position: 0% 50%; box-shadow: 0 6px 25px rgba(22, 77, 255, 0.5); }
      100% { transform: scale(1.03); background-position: 100% 50%; box-shadow: 0 10px 35px rgba(0, 217, 255, 0.65); }
    }

    /* =======================================================
       PANTALLA 2: CONTENIDO DE LA FIESTA DISCO
       ======================================================= */
    #screen-invitation {
      display: none;
      width: 100%;
      background: var(--card-bg);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(37, 139, 255, 0.25), 0 0 45px rgba(22, 77, 255, 0.3);
      border: 1.5px solid var(--card-border);
      position: relative;
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.8s ease-out, transform 0.8s ease-out;
    }

    #screen-invitation.visible {
      opacity: 1;
      transform: translateY(0);
    }

    .invitation-top-laser {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 6px;
      background: linear-gradient(90deg, var(--disco-cyan), var(--disco-blue-vivid), var(--disco-violet-bright), var(--disco-magenta), var(--disco-cyan));
      background-size: 200% 100%;
      animation: moveLaserBar 4s linear infinite;
    }

    @keyframes moveLaserBar {
      0% { background-position: 0% 0%; }
      100% { background-position: 200% 0%; }
    }

    .invitation-inner-flow {
      padding: 32px 20px 40px 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    /* SECCIÓN DE PADRES Y DEDICATORIA EDITORIAL */
    .editorial-parents-card {
      background: var(--card-inner-box);
      border: 1px solid rgba(37, 139, 255, 0.25);
      border-radius: 20px;
      padding: 22px 18px;
      width: 100%;
      margin-bottom: 22px;
      box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
    }

    .parents-intro-tag {
      font-family: 'Cinzel', serif;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 2px;
      color: var(--disco-cyan-bright);
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .parents-couple-names {
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.45;
      margin-bottom: 14px;
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.3);
    }

    .dedication-poetic-quote {
      font-style: italic;
      font-size: 0.86rem;
      color: #cbd5e1;
      line-height: 1.5;
      margin-bottom: 16px;
    }

    .godparents-sub-box {
      border-top: 1px dashed rgba(37, 139, 255, 0.25);
      padding-top: 14px;
      margin-top: 10px;
    }

    .godparents-tag {
      font-family: 'Cinzel', serif;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 2px;
      color: var(--disco-violet-bright);
      text-transform: uppercase;
      margin-bottom: 6px;
    }

    .godparents-names-list {
      font-size: 0.95rem;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.4;
    }

    /* DETALLES DE FECHA, HORA Y DIRECCIÓN */
    .event-coords-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 24px;
    }

    .coord-card-item {
      background: var(--card-inner-box);
      border: 1px solid rgba(37, 139, 255, 0.25);
      border-radius: 16px;
      padding: 14px 16px;
      display: flex;
      align-items: center;
      gap: 14px;
      text-align: left;
    }

    .coord-icon-orb {
      width: 46px;
      height: 46px;
      min-width: 46px;
      border-radius: 50%;
      background: linear-gradient(135deg, rgba(22, 77, 255, 0.3), rgba(0, 217, 255, 0.2));
      border: 1.5px solid var(--disco-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .coord-data-block {
      display: flex;
      flex-direction: column;
    }

    .coord-type-lbl {
      font-family: 'Cinzel', serif;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      color: var(--disco-cyan);
      text-transform: uppercase;
    }

    .coord-val-txt {
      font-size: 0.95rem;
      font-weight: 700;
      color: #ffffff;
      margin-top: 2px;
    }

    .btn-maps-action {
      min-height: 50px;
      background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%);
      color: #ffffff;
      border: none;
      padding: 15px 24px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.92rem;
      font-weight: 700;
      letter-spacing: 1px;
      border-radius: 50px;
      cursor: pointer;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 20px rgba(0, 180, 216, 0.4);
      text-decoration: none;
      transition: transform 0.2s;
    }

    .btn-maps-action:active {
      transform: scale(0.96);
    }

    /* PROTOCOLO VIP Y REGLAS */
    .vip-protocol-card {
      background: var(--card-inner-box);
      border: 1px solid rgba(37, 139, 255, 0.25);
      border-radius: 20px;
      padding: 22px 18px;
      width: 100%;
      margin-bottom: 24px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }

    .vip-access-pill {
      background: rgba(0, 217, 255, 0.15);
      border: 1.5px solid var(--disco-cyan);
      color: #ffffff;
      font-family: 'Cinzel', serif;
      font-size: 0.9rem;
      font-weight: 800;
      letter-spacing: 2px;
      padding: 8px 22px;
      border-radius: 50px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      box-shadow: 0 0 16px rgba(0, 217, 255, 0.35);
    }

    /* RESTRICCIÓN DE EDAD (JÓVENES Y ADULTOS) */
    .adults-only-badge {
      background: rgba(2, 5, 16, 0.9);
      border-left: 3px solid var(--gold-accent);
      border-radius: 12px;
      padding: 12px 14px;
      width: 100%;
      text-align: left;
    }

    .adults-only-header {
      font-size: 0.84rem;
      font-weight: 800;
      color: var(--gold-accent);
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .adults-only-body {
      font-size: 0.82rem;
      color: #cbd5e1;
      line-height: 1.4;
    }

    /* DRESS CODE CON MUESTRAS CIRCULARES */
    .dress-code-box {
      width: 100%;
      text-align: center;
      border-top: 1px dashed rgba(37, 139, 255, 0.25);
      border-bottom: 1px dashed rgba(37, 139, 255, 0.25);
      padding: 14px 0;
    }

    .dress-code-lbl {
      font-family: 'Cinzel', serif;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 3px;
      color: var(--disco-cyan);
      text-transform: uppercase;
    }

    .dress-code-val {
      font-family: 'Cinzel', serif;
      font-size: 1.25rem;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 2px;
      margin: 4px 0 10px 0;
    }

    .reserved-colors-title {
      font-size: 0.72rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 8px;
    }

    .swatches-row {
      display: flex;
      justify-content: center;
      gap: 14px;
      margin-bottom: 8px;
    }

    .color-swatch-circle {
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 2px solid #ffffff;
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
    }

    .swatch-fuchsia { background: #ff007f; }
    .swatch-pink { background: #ff758f; }
    .swatch-silver { background: #cbd5e1; }

    .reserved-colors-footer {
      font-size: 0.72rem;
      color: #64748b;
      font-style: italic;
    }

    /* =======================================================
       SECCIÓN AMBIENTE & DJ ANIMADO (PRODUCCIÓN PREMIUM)
       ======================================================= */
    .ambiente-disco-card {
      background: var(--card-inner-box);
      border: 1.5px solid rgba(0, 217, 255, 0.4);
      border-radius: 22px;
      padding: 24px 18px;
      width: 100%;
      margin-bottom: 24px;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 25px rgba(22, 77, 255, 0.25);
      display: flex;
      flex-direction: column;
      align-items: center;
      position: relative;
      overflow: hidden;
    }

    .ambiente-live-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(0, 217, 255, 0.12);
      border: 1px solid var(--disco-cyan);
      padding: 4px 14px;
      border-radius: 50px;
      font-size: 0.72rem;
      font-weight: 800;
      color: var(--disco-cyan-bright);
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 12px;
    }

    .live-dot-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #00d9ff;
      box-shadow: 0 0 8px #00d9ff;
      animation: liveDotBlink 1.2s infinite ease-in-out;
    }

    @keyframes liveDotBlink {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.7); }
    }

    .ambiente-title {
      font-family: 'Cinzel', serif;
      font-size: 1.25rem;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 3px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    .ambiente-vibe-tag {
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 900;
      color: var(--disco-cyan);
      letter-spacing: 2px;
      text-shadow: 0 0 14px rgba(0, 217, 255, 0.7);
      margin-bottom: 6px;
    }

    .ambiente-attitude-txt {
      font-size: 0.88rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 16px;
    }

    /* DJ SETUP & EQUALIZER CONTAINER */
    .dj-setup-container {
      width: 100%;
      max-width: 320px;
      background: rgba(2, 5, 16, 0.95);
      border: 1px solid rgba(37, 139, 255, 0.35);
      border-radius: 18px;
      padding: 16px 14px;
      margin-bottom: 16px;
      box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8), 0 4px 15px rgba(0, 217, 255, 0.15);
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .dj-deck-visual {
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: space-around;
      margin-bottom: 14px;
    }

    .dj-turntable {
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: radial-gradient(circle, #0a0e1a 0%, #1a233a 50%, #050a18 100%);
      border: 2px solid rgba(0, 217, 255, 0.5);
      box-shadow: 0 0 12px rgba(22, 77, 255, 0.4);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      animation: spinTurntable 3s linear infinite;
    }

    .dj-turntable.deck-b {
      animation: spinTurntable 2.6s linear infinite reverse;
    }

    @keyframes spinTurntable {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    .dj-turntable-core {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--disco-cyan) 0%, var(--disco-blue-vivid) 100%);
      border: 1.5px solid #ffffff;
      box-shadow: 0 0 6px var(--disco-cyan);
    }

    .dj-mixer-center {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 5px;
    }

    .dj-fader-slot {
      width: 32px;
      height: 6px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 3px;
      position: relative;
    }

    .dj-fader-knob {
      width: 10px;
      height: 12px;
      background: var(--disco-cyan);
      border-radius: 2px;
      position: absolute;
      top: -3px;
      left: 11px;
      animation: slideFader 2s ease-in-out infinite alternate;
    }

    @keyframes slideFader {
      0% { left: 2px; }
      100% { left: 20px; }
    }

    /* ECUALIZADOR ANIMADO LED */
    .equalizer-spectrum-bar {
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 4px;
      height: 46px;
      width: 100%;
      padding: 0 8px;
    }

    .eq-column {
      flex: 1;
      max-width: 10px;
      background: linear-gradient(180deg, var(--disco-pink-neon) 0%, var(--disco-violet-bright) 35%, var(--disco-cyan) 75%, var(--disco-blue-vivid) 100%);
      border-radius: 3px 3px 1px 1px;
      box-shadow: 0 0 6px rgba(0, 217, 255, 0.4);
      transform-origin: bottom;
      animation: eqBounce 1.2s ease-in-out infinite alternate;
    }

    .eq-col-1  { height: 40%; animation-delay: 0.1s; animation-duration: 0.8s; }
    .eq-col-2  { height: 75%; animation-delay: 0.3s; animation-duration: 1.1s; }
    .eq-col-3  { height: 50%; animation-delay: 0.0s; animation-duration: 0.9s; }
    .eq-col-4  { height: 90%; animation-delay: 0.4s; animation-duration: 1.3s; }
    .eq-col-5  { height: 60%; animation-delay: 0.2s; animation-duration: 0.7s; }
    .eq-col-6  { height: 95%; animation-delay: 0.5s; animation-duration: 1.0s; }
    .eq-col-7  { height: 45%; animation-delay: 0.15s; animation-duration: 1.2s; }
    .eq-col-8  { height: 85%; animation-delay: 0.35s; animation-duration: 0.85s; }
    .eq-col-9  { height: 70%; animation-delay: 0.25s; animation-duration: 1.15s; }
    .eq-col-10 { height: 90%; animation-delay: 0.45s; animation-duration: 0.95s; }
    .eq-col-11 { height: 55%; animation-delay: 0.1s; animation-duration: 1.05s; }
    .eq-col-12 { height: 80%; animation-delay: 0.3s; animation-duration: 0.8s; }

    @keyframes eqBounce {
      0% { transform: scaleY(0.25); filter: brightness(0.85); }
      50% { transform: scaleY(0.95); filter: brightness(1.2); }
      100% { transform: scaleY(0.4); filter: brightness(1.0); }
    }

    .ambiente-host-note {
      font-size: 0.82rem;
      color: var(--disco-cyan-bright);
      line-height: 1.45;
      background: rgba(22, 77, 255, 0.15);
      border: 1px dashed rgba(0, 217, 255, 0.35);
      border-radius: 12px;
      padding: 10px 14px;
      width: 100%;
    }

    /* =======================================================
       SECCIÓN REGALITOS (LLUVIA DE SOBRES)
       ======================================================= */
    .regalitos-card {
      background: var(--card-inner-box);
      border: 1px solid rgba(37, 139, 255, 0.3);
      border-radius: 20px;
      padding: 22px 18px;
      width: 100%;
      margin-bottom: 24px;
      box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.5);
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
    }

    .regalitos-icon-halo {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: linear-gradient(135deg, rgba(22, 77, 255, 0.3), rgba(0, 217, 255, 0.2));
      border: 1.5px solid var(--disco-cyan);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 12px;
      box-shadow: 0 0 16px rgba(0, 217, 255, 0.35);
    }

    .regalitos-title {
      font-family: 'Cinzel', serif;
      font-size: 1.15rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    .regalitos-subtitle {
      font-family: 'Cinzel', serif;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--disco-cyan);
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 10px;
    }

    .regalitos-message {
      font-size: 0.86rem;
      color: #cbd5e1;
      line-height: 1.5;
      font-style: italic;
    }

    /* FORMULARIO DE CONFIRMACIÓN VIP (WHATSAPP BUSINESS) */
    .rsvp-vip-section {
      background: var(--card-inner-box);
      border: 1.5px solid var(--disco-cyan);
      border-radius: 22px;
      padding: 24px 18px;
      width: 100%;
      margin-bottom: 14px;
      box-shadow: 0 0 30px rgba(0, 217, 255, 0.2);
    }

    .rsvp-sec-title {
      font-family: 'Cinzel', serif;
      font-size: 1.2rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 6px;
    }

    .rsvp-sec-limit {
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--gold-accent);
      margin-bottom: 18px;
    }

    .input-field-custom {
      width: 100%;
      min-height: 48px;
      background: rgba(2, 5, 16, 0.9);
      border: 1px solid rgba(37, 139, 255, 0.35);
      border-radius: 12px;
      padding: 12px 16px;
      color: #ffffff;
      font-family: 'Montserrat', sans-serif;
      font-size: 16px; /* Evita auto-zoom en iOS Safari */
      outline: none;
      margin-bottom: 12px;
      transition: border 0.2s, box-shadow 0.2s;
    }

    .input-field-custom:focus {
      border-color: var(--disco-cyan);
      box-shadow: 0 0 12px rgba(0, 217, 255, 0.5);
    }

    .btn-wp-confirm {
      min-height: 52px;
      background: linear-gradient(135deg, #25d366 0%, #128c7e 100%);
      color: #ffffff;
      border: none;
      padding: 16px;
      font-size: 1.05rem;
      font-weight: 800;
      letter-spacing: 1px;
      border-radius: 50px;
      cursor: pointer;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      box-shadow: 0 6px 25px rgba(37, 211, 102, 0.45);
      transition: transform 0.2s;
      text-transform: uppercase;
    }

    .btn-wp-confirm:active {
      transform: scale(0.96);
    }

    /* PLAYLIST INTERACTIVA VIP (MÁXIMO 2 TEMAS POR INVITADO) */
    .playlist-vip-section {
      background: var(--card-inner-box);
      border: 1px solid rgba(37, 139, 255, 0.25);
      border-radius: 22px;
      padding: 24px 18px;
      width: 100%;
      margin-bottom: 24px;
      box-shadow: inset 0 0 25px rgba(0, 0, 0, 0.6);
    }

    .playlist-vip-heading {
      font-family: 'Cinzel', serif;
      font-size: 1.05rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      line-height: 1.35;
      margin-bottom: 6px;
    }

    .playlist-vip-subtext {
      font-size: 0.86rem;
      color: #cbd5e1;
      line-height: 1.45;
      margin-bottom: 16px;
    }

    .playlist-inputs-box {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 16px;
    }

    .btn-elegir-tema {
      min-height: 48px;
      background: linear-gradient(180deg, #ffffff 0%, #e2e8f0 40%, #94a3b8 100%);
      color: #020510;
      border: 1px solid #ffffff;
      padding: 14px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.98rem;
      font-weight: 800;
      letter-spacing: 1px;
      border-radius: 50px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      box-shadow: 0 4px 18px rgba(255, 255, 255, 0.3);
      transition: transform 0.2s;
    }

    .btn-elegir-tema:active {
      transform: scale(0.96);
    }

    .songs-added-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      width: 100%;
      text-align: left;
    }

    .song-item-pill {
      background: rgba(2, 5, 16, 0.95);
      border: 1px solid rgba(0, 217, 255, 0.4);
      border-radius: 12px;
      padding: 10px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      animation: popSongPill 0.4s ease-out;
    }

    @keyframes popSongPill {
      0% { opacity: 0; transform: scale(0.9); }
      100% { opacity: 1; transform: scale(1); }
    }

    .song-pill-data {
      display: flex;
      flex-direction: column;
    }

    .song-title-str {
      font-size: 0.92rem;
      font-weight: 700;
      color: #ffffff;
    }

    .song-artist-str {
      font-size: 0.78rem;
      color: var(--disco-cyan-bright);
    }

    .song-badge-status {
      font-size: 0.72rem;
      background: rgba(34, 197, 94, 0.2);
      color: #4ade80;
      padding: 3px 8px;
      border-radius: 6px;
      font-weight: 700;
      border: 1px solid rgba(74, 222, 128, 0.3);
    }

    .btn-share-playlist-wp {
      min-height: 48px;
      background: rgba(37, 211, 102, 0.15);
      border: 1px solid #25d366;
      color: #25d366;
      padding: 12px 18px;
      font-size: 0.88rem;
      font-weight: 700;
      border-radius: 50px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      margin-top: 14px;
      width: 100%;
    }

    /* TOAST DE SISTEMA */
    .toast-system-alert {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: rgba(220, 38, 38, 0.95);
      color: #ffffff;
      padding: 14px 22px;
      border-radius: 50px;
      font-size: 0.88rem;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
      z-index: 99999;
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
      pointer-events: none;
      text-align: center;
      max-width: 90%;
    }

    .toast-system-alert.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    .event-footer-tag {
      margin-top: 24px;
      font-size: 0.75rem;
      color: #64748b;
      letter-spacing: 2px;
      text-transform: uppercase;
    }

    /* REDUCED MOTION SUPPORT */
    @media (prefers-reduced-motion: reduce) {
      *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
      }
    }
  </style>
</head>
<body>

  <!-- Elemento de audio con fallback en formatos compatibles -->
  <audio id="bg-audio" loop preload="auto">
    <source src="musica.m4a" type="audio/mp4">
    <source src="musica.mp4" type="audio/mp4">
  </audio>

  <!-- CONTROL FLOTANTE DE MÚSICA CON DISCO DE VINILO GIRATORIO -->
  <div class="music-floating-ctrl" id="ctrl-music" title="Control de Música">
    <div class="vinyl-disc">
      <div class="vinyl-center-label">
        <div class="vinyl-spindle-hole"></div>
      </div>
    </div>
    <span class="music-label-tag">Música</span>
  </div>

  <!-- FONDO DISCO AMBIENTAL EN AZUL NOCTURNO -->
  <div id="ambient-bg"></div>

  <!-- RAYOS VOLUMÉTRICOS DE LUZ AZUL Y CIAN -->
  <div class="volumetric-rays">
    <div class="v-ray v-ray-1"></div>
    <div class="v-ray v-ray-2"></div>
    <div class="v-ray v-ray-3"></div>
  </div>

  <!-- LIENZO GLOBAL DE PARTÍCULAS / CASCADA DE LUCES DISCO -->
  <canvas id="particles-canvas"></canvas>

  <!-- FLASH CINEMATOGRÁFICO DE TRANSICIÓN -->
  <div id="cinematic-flash"></div>

  <!-- CONTENEDOR PRINCIPAL DE LA APLICACIÓN -->
  <div class="app-viewport">

    <!-- =======================================================
         PANTALLA 1: PORTADA VIP DISCO PARTY
         ======================================================= -->
    <div id="screen-welcome">

      <!-- Corona Plateada Vectorial con destello -->
      <svg class="silver-crown-vector" viewBox="0 0 100 65" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 52 L22 24 L42 38 L50 14 L58 38 L78 24 L88 52 Z" fill="url(#crown-metal-grad)" stroke="#ffffff" stroke-width="1.8"/>
        <circle cx="50" cy="11" r="5" fill="#ffffff" filter="drop-shadow(0 0 6px #00d9ff)"/>
        <circle cx="22" cy="21" r="4" fill="#ffffff" filter="drop-shadow(0 0 4px #00d9ff)"/>
        <circle cx="78" cy="21" r="4" fill="#ffffff" filter="drop-shadow(0 0 4px #00d9ff)"/>
        <circle cx="50" cy="33" r="3" fill="#00d9ff"/>
        <rect x="14" y="52" width="72" height="6" rx="3" fill="url(#crown-metal-grad)" stroke="#ffffff" stroke-width="1.5"/>
        <defs>
          <linearGradient id="crown-metal-grad" x1="0" y1="0" x2="100" y2="65" gradientUnits="userSpaceOnUse">
            <stop stop-color="#ffffff"/>
            <stop offset="0.5" stop-color="#eaf7ff"/>
            <stop offset="1" stop-color="#94a3b8"/>
          </linearGradient>
        </defs>
      </svg>

      <div class="heading-xv">MIS XV AÑOS</div>
      <h1 class="heading-angeles">ANGELES</h1>
      <div class="sub-badge-party">TE INVITA A SU DISCO PARTY</div>

      <!-- BOLA DISCO 3D REAL CON REFLEJOS EN TIEMPO REAL (THREE.JS) -->
      <div class="disco-3d-stage" id="disco-3d-stage">
        <canvas id="disco-three-canvas"></canvas>
        <div class="disco-drag-hint">Gira la esfera ✦</div>
      </div>

      <!-- CALENDARIO DE OCTUBRE 2026 -->
      <div class="calendar-wrapper">
        <div class="calendar-month-title">OCTUBRE 2026</div>
        <table class="calendar-grid-table">
          <thead>
            <tr>
              <th>D</th><th>L</th><th>M</th><th>M</th><th>J</th><th>V</th><th>S</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td></td><td></td><td></td><td></td><td>1</td><td>2</td><td>3</td>
            </tr>
            <tr>
              <td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td>
            </tr>
            <tr>
              <td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td>
            </tr>
            <tr>
              <td>18</td>
              <!-- DÍA 19 RESALTADO -->
              <td class="day-oct-19">
                <div class="day-oct-19-badge">19</div>
              </td>
              <td>20</td><td>21</td><td>22</td><td>23</td><td>24</td>
            </tr>
            <tr>
              <td>25</td><td>26</td><td>27</td><td>28</td><td>29</td><td>30</td><td>31</td>
            </tr>
          </tbody>
        </table>

        <!-- CUENTA REGRESIVA EN VIVO -->
        <div class="countdown-title-bar">¡FALTAN!</div>
        <div class="countdown-boxes-row">
          <div class="time-box">
            <div class="time-box-num" id="val-days">00</div>
            <div class="time-box-lbl">Días</div>
          </div>
          <div class="time-box">
            <div class="time-box-num" id="val-hours">00</div>
            <div class="time-box-lbl">Horas</div>
          </div>
          <div class="time-box">
            <div class="time-box-num" id="val-mins">00</div>
            <div class="time-box-lbl">Min</div>
          </div>
          <div class="time-box">
            <div class="time-box-num" id="val-secs">00</div>
            <div class="time-box-lbl">Seg</div>
          </div>
        </div>
      </div>

      <!-- BOTÓN PRINCIPAL ABRIR INVITACIÓN -->
      <button class="btn-open-invitation" id="btn-trigger-open">
        Abrir Invitación
      </button>

    </div>

    <!-- =======================================================
         PANTALLA 2: CONTENIDO COMPLETO DE LA FIESTA DISCO
         ======================================================= -->
    <div id="screen-invitation">
      <div class="invitation-top-laser"></div>

      <div class="invitation-inner-flow">

        <!-- Corona y Encabezado Persistente -->
        <svg class="silver-crown-vector" viewBox="0 0 100 65" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 52 L22 24 L42 38 L50 14 L58 38 L78 24 L88 52 Z" fill="url(#crown-metal-grad2)" stroke="#ffffff" stroke-width="1.8"/>
          <circle cx="50" cy="11" r="5" fill="#ffffff"/>
          <circle cx="22" cy="21" r="4" fill="#ffffff"/>
          <circle cx="78" cy="21" r="4" fill="#ffffff"/>
          <circle cx="50" cy="33" r="3" fill="#00d9ff"/>
          <rect x="14" y="52" width="72" height="6" rx="3" fill="url(#crown-metal-grad2)" stroke="#ffffff" stroke-width="1.5"/>
          <defs>
            <linearGradient id="crown-metal-grad2" x1="0" y1="0" x2="100" y2="65" gradientUnits="userSpaceOnUse">
              <stop stop-color="#ffffff"/>
              <stop offset="0.5" stop-color="#eaf7ff"/>
              <stop offset="1" stop-color="#94a3b8"/>
            </linearGradient>
          </defs>
        </svg>

        <div class="heading-xv">MIS XV AÑOS</div>
        <h2 class="heading-angeles" style="font-size: 2.8rem;">ANGELES</h2>
        <div class="sub-badge-party" style="margin-bottom: 22px;">DISCO PARTY</div>

        <!-- DEDICATORIA: PADRES Y PADRINOS -->
        <div class="editorial-parents-card">
          <div class="parents-intro-tag">Hoy gracias a Dios y a mis padres</div>
          <div class="parents-couple-names">Jahaira Lara Mondragón<br>&<br>Hermis Ramos</div>
          <p class="dedication-poetic-quote">
            "Por regalarme la vida, el amor y la oportunidad de celebrar este sueño."
          </p>
          <div class="godparents-sub-box">
            <div class="godparents-tag">Mis Padrinos</div>
            <div class="godparents-names-list">
              Juan Carlos Nakasone Alvarado<br>&<br>Giulissa Lara Mondragón
            </div>
          </div>
        </div>

        <!-- COORDENADAS: FECHA, HORA Y DIRECCIÓN -->
        <div class="event-coords-list">
          <div class="coord-card-item">
            <div class="coord-icon-orb">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00d9ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
            </div>
            <div class="coord-data-block">
              <span class="coord-type-lbl">Fecha</span>
              <span class="coord-val-txt">Lunes, 19 de Octubre del 2026</span>
            </div>
          </div>

          <div class="coord-card-item">
            <div class="coord-icon-orb">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00d9ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div class="coord-data-block">
              <span class="coord-type-lbl">Hora</span>
              <span class="coord-val-txt">7:00 PM</span>
            </div>
          </div>

          <div class="coord-card-item">
            <div class="coord-icon-orb">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#00d9ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
            </div>
            <div class="coord-data-block">
              <span class="coord-type-lbl">Ubicación</span>
              <span class="coord-val-txt">Calle Héroes Nacionales N° 519</span>
            </div>
          </div>

          <a href="https://maps.google.com/?q=Calle+Heroes+Nacionales+519" target="_blank" rel="noopener noreferrer" class="btn-maps-action">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="3 11 22 2 13 21 11 13 3 11"></polygon>
            </svg>
            Ver Ubicación en Google Maps
          </a>
        </div>

        <!-- PROTOCOLO VIP Y REGLAS -->
        <div class="vip-protocol-card">
          <div class="vip-access-pill">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M2 9v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2zm18 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2zM4 11a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
            </svg>
            1 LUGAR RESERVADO
          </div>

          <!-- RESTRICCIÓN DE EDAD -->
          <div class="adults-only-badge">
            <div class="adults-only-header">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#f59e0b" stroke-width="2.5">
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="4.93" y1="4.93" x2="19.07" y2="19.07"></line>
              </svg>
              Evento Exclusivo: Jóvenes & Adultos
            </div>
            <div class="adults-only-body">
              En esta ocasión nuestra invitación está dirigida sólo a jóvenes y adultos (No niños). ¡Gracias por tu comprensión!
            </div>
          </div>

          <!-- DRESS CODE -->
          <div class="dress-code-box">
            <div class="dress-code-lbl">Dress Code</div>
            <div class="dress-code-val">ELEGANTE</div>
            <div class="reserved-colors-title">Colores Reservados para la Quinceañera:</div>
            <div class="swatches-row">
              <div class="color-swatch-circle swatch-fuchsia" title="Fucsia"></div>
              <div class="color-swatch-circle swatch-pink" title="Rosado"></div>
              <div class="color-swatch-circle swatch-silver" title="Plateado"></div>
            </div>
            <div class="reserved-colors-footer">
              (Fucsia, Rosado y Plateado en ninguna de sus tonalidades)
            </div>
          </div>

        </div>

        <!-- SECCIÓN AMBIENTE & DJ ANIMADO -->
        <div class="ambiente-disco-card">
          <div class="ambiente-live-badge">
            <span class="live-dot-pulse"></span>
            EN VIVO • DJ SESSION
          </div>
          <div class="ambiente-title">AMBIENTE</div>
          <div class="ambiente-vibe-tag">¡ALOCADO!</div>
          <div class="ambiente-attitude-txt">LLEVAR ACTITUD</div>

          <!-- DJ CONSOLE & EQUALIZER SPECTRUM -->
          <div class="dj-setup-container">
            <div class="dj-deck-visual">
              <div class="dj-turntable deck-a">
                <div class="dj-turntable-core"></div>
              </div>
              <div class="dj-mixer-center">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00d9ff" stroke-width="2">
                  <path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
                  <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
                </svg>
                <div class="dj-fader-slot">
                  <div class="dj-fader-knob"></div>
                </div>
              </div>
              <div class="dj-turntable deck-b">
                <div class="dj-turntable-core"></div>
              </div>
            </div>

            <!-- ECUALIZADOR ANIMADO DE AUDIO -->
            <div class="equalizer-spectrum-bar">
              <div class="eq-column eq-col-1"></div>
              <div class="eq-column eq-col-2"></div>
              <div class="eq-column eq-col-3"></div>
              <div class="eq-column eq-col-4"></div>
              <div class="eq-column eq-col-5"></div>
              <div class="eq-column eq-col-6"></div>
              <div class="eq-column eq-col-7"></div>
              <div class="eq-column eq-col-8"></div>
              <div class="eq-column eq-col-9"></div>
              <div class="eq-column eq-col-10"></div>
              <div class="eq-column eq-col-11"></div>
              <div class="eq-column eq-col-12"></div>
            </div>
          </div>

          <div class="ambiente-host-note">
            Si deseas aportar con algo, pregunta al anfitrión de la fiesta.
          </div>
        </div>

        <!-- SECCIÓN REGALITOS -->
        <div class="regalitos-card">
          <div class="regalitos-icon-halo">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#00d9ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M20 12V8H6a2 2 0 0 1-2-2c0-1.1.9-2 2-2h12v4"></path>
              <path d="M4 6v12c0 1.1.9 2 2 2h14v-4"></path>
              <path d="M18 12a2 2 0 0 0-2 2c0 1.1.9 2 2 2h4v-4h-4z"></path>
            </svg>
          </div>
          <div class="regalitos-title">REGALITOS</div>
          <div class="regalitos-subtitle">Lluvia de sobres ✉️</div>
          <p class="regalitos-message">
            "Tu presencia es mi mejor regalo, pero si deseas hacerme un presente: Lluvia de sobres."
          </p>
        </div>

        <!-- PLAYLIST INTERACTIVA (MÁXIMO 2 TEMAS POR INVITADO) -->
        <div class="playlist-vip-section">
          <div class="playlist-vip-heading">¿QUÉ CANCIÓN NO PUEDE FALTAR EN LA PLAYLIST?</div>
          <div class="playlist-vip-subtext">¡Ayúdame a armar los mejores temas para la fiesta!</div>

          <div class="playlist-inputs-box" id="playlist-inputs-box">
            <input type="text" id="playlist-title-in" class="input-field-custom" placeholder="Nombre de la Canción" />
            <input type="text" id="playlist-artist-in" class="input-field-custom" placeholder="Artista o Grupo" />
            
            <button class="btn-elegir-tema" id="btn-save-song">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 18V5l12-2v13"></path>
                <circle cx="6" cy="18" r="3"></circle>
                <circle cx="18" cy="16" r="3"></circle>
              </svg>
              Elegí tu tema
            </button>
          </div>

          <!-- LISTA DE CANCIONES GUARDADAS POR EL INVITADO -->
          <div class="songs-added-list" id="songs-added-list"></div>

          <!-- BOTÓN COMPARTIR PLAYLIST CON ANGELES -->
          <button class="btn-share-playlist-wp" id="btn-share-playlist-wp" style="display: none;">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <path d="M12.031 2C6.495 2 2 6.495 2 12.031c0 1.996.586 3.86 1.6 5.435L2 22l4.675-1.572a10.02 10.02 0 0 0 5.356 1.603h.005c5.536 0 10.031-4.495 10.031-10.031 0-5.536-4.495-10.031-10.031-10.031z"/>
            </svg>
            Compartir mis temas con Angeles por WhatsApp
          </button>
        </div>

        <!-- FORMULARIO DE CONFIRMACIÓN VIP (WHATSAPP BUSINESS) -->
        <div class="rsvp-vip-section">
          <div class="rsvp-sec-title">Confirmación de Asistencia</div>
          <div class="rsvp-sec-limit">Fecha límite de reserva: Hasta el 10 de Octubre</div>

          <form id="form-vip-rsvp">
            <input type="text" id="rsvp-input-name" class="input-field-custom" placeholder="Escribe tu Nombre y Apellido" required />
            
            <select id="rsvp-input-choice" class="input-field-custom">
              <option value="¡Sí, confirmo mi asistencia! (1 persona)">¡Sí, confirmo mi asistencia! (1 persona)</option>
              <option value="Lo siento, no podré asistir">Lo siento, no podré asistir</option>
            </select>

            <button type="submit" class="btn-wp-confirm">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12.031 2C6.495 2 2 6.495 2 12.031c0 1.996.586 3.86 1.6 5.435L2 22l4.675-1.572a10.02 10.02 0 0 0 5.356 1.603h.005c5.536 0 10.031-4.495 10.031-10.031 0-5.536-4.495-10.031-10.031-10.031zm0 18.232c-1.637 0-3.178-.46-4.502-1.258l-.323-.192-3.107 1.045 1.045-3.04-.21-.342a8.214 8.214 0 0 1-1.229-4.414c0-4.542 3.69-8.232 8.231-8.232 4.542 0 8.232 3.69 8.232 8.232 0 4.542-3.69 8.232-8.232 8.232zm4.512-6.17c-.247-.123-1.463-.722-1.69-.804-.227-.082-.392-.123-.557.123-.165.247-.639.804-.783.969-.144.165-.288.185-.535.062s-1.045-.385-1.99-1.228c-.736-.657-1.233-1.468-1.377-1.715-.144-.247-.015-.38.108-.503.111-.111.247-.288.371-.433.123-.144.165-.247.247-.412.082-.165.041-.309-.021-.433-.062-.123-.557-1.34-763-1.835-.201-.482-.405-.417-.557-.425l-.474-.008c-.165 0-.433.062-.659.309-.227.247-.866.845-.866 2.062s.887 2.392 1.01 2.557c.123.165 1.745 2.665 4.228 3.738.591.255 1.053.408 1.413.522.595.189 1.136.162 1.564.098.477-.071 1.463-.598 1.669-1.175.206-.577.206-1.072.144-1.175-.062-.103-.227-.165-.474-.288z"/>
              </svg>
              Confirmar por WhatsApp
            </button>
          </form>
        </div>

        <div class="event-footer-tag">
          ANGELES • DISCO PARTY • 2026
        </div>

      </div>
    </div>

  </div>

  <!-- NOTIFICACIÓN TOAST DEL SISTEMA -->
  <div class="toast-system-alert" id="toast-system-alert">
    <span id="toast-alert-msg">Solo puedes sugerir un máximo de 2 canciones por invitado</span>
  </div>

  <script>
    // =======================================================
    // NÚMERO DE TELÉFONO DE PRUEBAS (WHATSAPP BUSINESS)
    // =======================================================
    const WHATSAPP_PHONE = "51945221946";

    // =======================================================
    // REPRODUCTOR DE MÚSICA & DISCO DE VINILO
    // =======================================================
    const bgAudio = document.getElementById("bg-audio");
    const musicCtrl = document.getElementById("ctrl-music");
    let isMusicPlaying = false;

    function playDiscoAudio() {
      bgAudio.play().then(() => {
        isMusicPlaying = true;
        musicCtrl.classList.add("playing");
      }).catch(err => {
        console.log("Autoplay bloqueado hasta interacción:", err);
      });
    }

    function toggleMusicPlayback() {
      if (bgAudio.paused) {
        bgAudio.play();
        isMusicPlaying = true;
        musicCtrl.classList.add("playing");
      } else {
        bgAudio.pause();
        isMusicPlaying = false;
        musicCtrl.classList.remove("playing");
      }
    }

    musicCtrl.addEventListener("click", (e) => {
      e.stopPropagation();
      toggleMusicPlayback();
    });

    // Desbloqueo pasivo en el primer gesto del usuario
    function onFirstTouchGesture() {
      if (!isMusicPlaying) playDiscoAudio();
      document.removeEventListener("touchstart", onFirstTouchGesture);
      document.removeEventListener("click", onFirstTouchGesture);
    }
    document.addEventListener("touchstart", onFirstTouchGesture, { passive: true });
    document.addEventListener("click", onFirstTouchGesture, { passive: true });

    // =======================================================
    // BOLA DISCO 3D REAL CON THREE.JS (PALETA AZUL / CIAN / VIOLETA)
    // =======================================================
    let discoSphereRef = null;
    let discoSpotsRef = null;
    let discoBlueLightRef = null;
    let discoCyanLightRef = null;
    let discoVioletLightRef = null;
    let ballSpeedMultiplier = 1.0;

    function initDisco3D() {
      const stage = document.getElementById('disco-3d-stage');
      const canvas = document.getElementById('disco-three-canvas');
      if (!stage || !canvas || typeof THREE === 'undefined') return;

      const rect = stage.getBoundingClientRect();
      const w = rect.width || 350;
      const h = rect.height || 380;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, w / h, 0.1, 1000);
      camera.position.set(0, 0, 7.2);

      const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
      renderer.setSize(w, h);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.35;

      // Iluminación ambiental en azul profundo
      const ambLight = new THREE.AmbientLight(0x0a1845, 1.8);
      scene.add(ambLight);

      // Foco principal Azul Eléctrico
      const blueLight = new THREE.PointLight(0x164dff, 6.2, 24);
      blueLight.position.set(4, 3, 4);
      scene.add(blueLight);
      discoBlueLightRef = blueLight;

      // Foco Cian Eléctrico
      const cyanLight = new THREE.PointLight(0x00d9ff, 5.5, 24);
      cyanLight.position.set(-4, -2, 3);
      scene.add(cyanLight);
      discoCyanLightRef = cyanLight;

      // Foco Violeta / Magenta de acento
      const violetLight = new THREE.PointLight(0xd21fff, 4.8, 20);
      violetLight.position.set(0, -4, 2);
      scene.add(violetLight);
      discoVioletLightRef = violetLight;

      // Foco Blanco Hielo superior
      const whiteLight = new THREE.DirectionalLight(0xeaf7ff, 4.2);
      whiteLight.position.set(0, 6, 6);
      scene.add(whiteLight);

      const ballAssembly = new THREE.Group();
      scene.add(ballAssembly);

      // Cable de suspensión metálico
      const cableGeo = new THREE.CylinderGeometry(0.018, 0.018, 4.2, 8);
      const cableMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.95, roughness: 0.15 });
      const cable = new THREE.Mesh(cableGeo, cableMat);
      cable.position.y = 3.7;
      ballAssembly.add(cable);

      // Aro y tapa de sujeción cromada
      const ringGeo = new THREE.TorusGeometry(0.12, 0.03, 8, 24);
      const ringMat = new THREE.MeshStandardMaterial({ color: 0xffffff, metalness: 0.95, roughness: 0.1 });
      const ring = new THREE.Mesh(ringGeo, ringMat);
      ring.rotation.x = Math.PI / 2;
      ring.position.y = 1.68;
      ballAssembly.add(ring);

      const capGeo = new THREE.CylinderGeometry(0.24, 0.28, 0.18, 16);
      const cap = new THREE.Mesh(capGeo, ringMat);
      cap.position.y = 1.58;
      ballAssembly.add(cap);

      // Textura procedural de facetas de cristal con reflejos azul/cian/violeta/plata
      function buildMirrorTexture() {
        const c = document.createElement('canvas');
        c.width = 1024; c.height = 512;
        const ctx = c.getContext('2d');
        const cols = 64, rows = 32;
        const cellW = c.width / cols, cellH = c.height / rows;

        ctx.fillStyle = '#050a18';
        ctx.fillRect(0, 0, c.width, c.height);

        for (let y = 0; y < rows; y++) {
          for (let x = 0; x < cols; x++) {
            const rand = Math.random();
            let baseG = Math.floor(215 + rand * 40);
            let r = baseG, g = baseG, b = baseG;

            if (rand > 0.82) {
              r = 92; g = 235; b = 255; // Reflejo Cian Eléctrico
            } else if (rand > 0.68) {
              r = 37; g = 139; b = 255; // Reflejo Azul Brillante
            } else if (rand > 0.55) {
              r = 210; g = 31; b = 255; // Reflejo Violeta/Magenta
            }

            ctx.fillStyle = `rgb(${r},${g},${b})`;
            ctx.fillRect(x * cellW + 1, y * cellH + 1, cellW - 2, cellH - 2);

            ctx.strokeStyle = '#020510';
            ctx.lineWidth = 1;
            ctx.strokeRect(x * cellW, y * cellH, cellW, cellH);
          }
        }

        const tex = new THREE.CanvasTexture(c);
        tex.wrapS = THREE.RepeatWrapping;
        tex.wrapT = THREE.ClampToEdgeWrapping;
        return tex;
      }

      function buildNormalTexture() {
        const c = document.createElement('canvas');
        c.width = 1024; c.height = 512;
        const ctx = c.getContext('2d');
        const cols = 64, rows = 32;
        const cellW = c.width / cols, cellH = c.height / rows;

        ctx.fillStyle = 'rgb(128,128,255)';
        ctx.fillRect(0, 0, c.width, c.height);

        for (let y = 0; y < rows; y++) {
          for (let x = 0; x < cols; x++) {
            const tiltX = Math.floor(128 + (Math.random() - 0.5) * 50);
            const tiltY = Math.floor(128 + (Math.random() - 0.5) * 50);
            ctx.fillStyle = `rgb(${tiltX},${tiltY},255)`;
            ctx.fillRect(x * cellW + 1.5, y * cellH + 1.5, cellW - 3, cellH - 3);
          }
        }
        return new THREE.CanvasTexture(c);
      }

      const sphereGeo = new THREE.SphereGeometry(1.5, 48, 32);
      const sphereMat = new THREE.MeshStandardMaterial({
        map: buildMirrorTexture(),
        normalMap: buildNormalTexture(),
        metalness: 0.98,
        roughness: 0.08,
        flatShading: true,
        envMapIntensity: 2.5
      });

      const sphereMesh = new THREE.Mesh(sphereGeo, sphereMat);
      ballAssembly.add(sphereMesh);
      discoSphereRef = sphereMesh;

      // Reflejos danzantes proyectados (Azul, Cian, Violeta, Blanco)
      const spotsCount = 200;
      const spotsGeo = new THREE.BufferGeometry();
      const spotsPos = new Float32Array(spotsCount * 3);
      const spotsCols = new Float32Array(spotsCount * 3);

      const palette = [
        new THREE.Color(0xffffff),
        new THREE.Color(0x00d9ff),
        new THREE.Color(0x5cebff),
        new THREE.Color(0x164dff),
        new THREE.Color(0x258bff),
        new THREE.Color(0x7a2cff),
        new THREE.Color(0xd21fff),
        new THREE.Color(0xeaf7ff)
      ];

      for (let i = 0; i < spotsCount; i++) {
        const radius = 2.3 + Math.random() * 2.4;
        const theta = Math.random() * Math.PI * 2;
        const phi = (Math.random() - 0.5) * Math.PI * 0.95;

        spotsPos[i * 3] = radius * Math.cos(phi) * Math.cos(theta);
        spotsPos[i * 3 + 1] = radius * Math.sin(phi);
        spotsPos[i * 3 + 2] = radius * Math.cos(phi) * Math.sin(theta);

        const col = palette[Math.floor(Math.random() * palette.length)];
        spotsCols[i * 3] = col.r;
        spotsCols[i * 3 + 1] = col.g;
        spotsCols[i * 3 + 2] = col.b;
      }

      spotsGeo.setAttribute('position', new THREE.BufferAttribute(spotsPos, 3));
      spotsGeo.setAttribute('color', new THREE.BufferAttribute(spotsCols, 3));

      function createSpotTexture() {
        const c = document.createElement('canvas');
        c.width = 64; c.height = 64;
        const cx = c.getContext('2d');
        const grad = cx.createRadialGradient(32, 32, 0, 32, 32, 32);
        grad.addColorStop(0, 'rgba(255,255,255,1)');
        grad.addColorStop(0.3, 'rgba(234,247,255,0.9)');
        grad.addColorStop(0.6, 'rgba(0,217,255,0.45)');
        grad.addColorStop(1, 'rgba(0,0,0,0)');
        cx.fillStyle = grad;
        cx.fillRect(0, 0, 64, 64);
        return new THREE.CanvasTexture(c);
      }

      const spotsMat = new THREE.PointsMaterial({
        size: 0.32,
        vertexColors: true,
        map: createSpotTexture(),
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });

      const spotsMesh = new THREE.Points(spotsGeo, spotsMat);
      scene.add(spotsMesh);
      discoSpotsRef = spotsMesh;

      // Resplandor halo central en azul profundo y cian
      const glowGeo = new THREE.PlaneGeometry(5.4, 5.4);
      function createBackGlowTex() {
        const c = document.createElement('canvas');
        c.width = 256; c.height = 256;
        const ctx = c.getContext('2d');
        const grad = ctx.createRadialGradient(128, 128, 0, 128, 128, 128);
        grad.addColorStop(0, 'rgba(0, 217, 255, 0.45)');
        grad.addColorStop(0.4, 'rgba(22, 77, 255, 0.3)');
        grad.addColorStop(0.8, 'rgba(122, 44, 255, 0.15)');
        grad.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = grad;
        ctx.fillRect(0, 0, 256, 256);
        return new THREE.CanvasTexture(c);
      }
      const glowMat = new THREE.MeshBasicMaterial({
        map: createBackGlowTex(),
        transparent: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false
      });
      const backGlow = new THREE.Mesh(glowGeo, glowMat);
      backGlow.position.z = -0.5;
      scene.add(backGlow);

      // Control táctil con inercia
      let isTouching = false;
      let lastX = 0;
      let userSpinMomentum = 0;

      function onDragStart(e) {
        isTouching = true;
        lastX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      }

      function onDragMove(e) {
        if (!isTouching) return;
        const curX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
        const diffX = curX - lastX;
        lastX = curX;
        userSpinMomentum = diffX * 0.006;
        sphereMesh.rotation.y += userSpinMomentum;
        spotsMesh.rotation.y += userSpinMomentum;
      }

      function onDragEnd() {
        isTouching = false;
      }

      stage.addEventListener('mousedown', onDragStart);
      window.addEventListener('mousemove', onDragMove);
      window.addEventListener('mouseup', onDragEnd);

      stage.addEventListener('touchstart', onDragStart, { passive: true });
      window.addEventListener('touchmove', onDragMove, { passive: true });
      window.addEventListener('touchend', onDragEnd, { passive: true });

      let clock = new THREE.Clock();
      function renderLoop() {
        requestAnimationFrame(renderLoop);
        const elapsed = clock.getElapsedTime();

        if (!isTouching) {
          userSpinMomentum *= 0.95;
          const baseSpeed = 0.012 * ballSpeedMultiplier;
          sphereMesh.rotation.y += baseSpeed + userSpinMomentum;
          spotsMesh.rotation.y += baseSpeed * 1.2 + userSpinMomentum;
        }

        ballAssembly.rotation.y = Math.sin(elapsed * 0.8) * 0.04;
        ballAssembly.rotation.z = Math.sin(elapsed * 0.6) * 0.02;

        blueLight.position.x = Math.cos(elapsed * 1.3) * 4.6;
        blueLight.position.z = Math.sin(elapsed * 1.3) * 4.6;

        cyanLight.position.x = Math.cos(elapsed * 1.0 + Math.PI) * 4.6;
        cyanLight.position.z = Math.sin(elapsed * 1.0 + Math.PI) * 4.6;

        backGlow.scale.setScalar(1 + Math.sin(elapsed * 2.2) * 0.07);

        renderer.render(scene, camera);
      }

      renderLoop();

      window.addEventListener('resize', () => {
        const r = stage.getBoundingClientRect();
        if (r.width > 0 && r.height > 0) {
          camera.aspect = r.width / r.height;
          camera.updateProjectionMatrix();
          renderer.setSize(r.width, r.height);
        }
      });
    }

    window.addEventListener('DOMContentLoaded', initDisco3D);

    // =======================================================
    // MOTOR DE PARTÍCULAS CANVAS (PALETA DISCO AZUL-CIAN-VIOLETA)
    // =======================================================
    const pCanvas = document.getElementById("particles-canvas");
    const pCtx = pCanvas.getContext("2d");
    let pWidth = 0, pHeight = 0;
    let particlesList = [];
    let isWaterfallMode = false;

    function resizeParticlesCanvas() {
      pWidth = window.innerWidth;
      pHeight = window.innerHeight;
      pCanvas.width = pWidth;
      pCanvas.height = pHeight;
    }
    window.addEventListener("resize", resizeParticlesCanvas);
    resizeParticlesCanvas();

    class DiscoParticle {
      constructor(isWaterfall = false) {
        this.reset(isWaterfall);
      }

      reset(isWaterfall = false) {
        this.x = Math.random() * pWidth;
        this.y = isWaterfall ? -Math.random() * 200 : Math.random() * pHeight;
        this.type = Math.floor(Math.random() * 4);
        this.size = this.type === 3 ? (Math.random() * 6 + 4) : (Math.random() * 3 + 1.2);
        this.speedY = isWaterfall ? (Math.random() * 3.5 + 2.2) : (Math.random() * 0.6 + 0.2);
        this.speedX = (Math.random() - 0.5) * (isWaterfall ? 1.5 : 0.4);
        this.angle = Math.random() * Math.PI * 2;
        this.spinSpeed = (Math.random() - 0.5) * 0.06;
        this.alpha = isWaterfall ? (Math.random() * 0.6 + 0.4) : (Math.random() * 0.5 + 0.2);
        this.twinkleRate = Math.random() * 0.04 + 0.01;
        this.twinkleDir = 1;

        // Paleta oficial: Azul, Cian, Violeta, Magenta, Blanco Hielo
        const colors = [
          '#ffffff', '#00d9ff', '#5cebff', '#164dff', '#258bff', '#7a2cff', '#d21fff', '#eaf7ff'
        ];
        this.color = colors[Math.floor(Math.random() * colors.length)];
      }

      update() {
        this.y += this.speedY;
        this.x += this.speedX;
        this.angle += this.spinSpeed;

        this.alpha += this.twinkleRate * this.twinkleDir;
        if (this.alpha > 0.9) this.twinkleDir = -1;
        if (this.alpha < 0.15) this.twinkleDir = 1;

        if (this.y > pHeight + 20) {
          if (isWaterfallMode) {
            this.reset(true);
          } else {
            this.y = -10;
            this.x = Math.random() * pWidth;
          }
        }
      }

      draw(ctx) {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(this.angle);
        ctx.globalAlpha = Math.max(0, Math.min(1, this.alpha));

        if (this.type === 0) {
          // Tipo A: Punto luminoso
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.arc(0, 0, this.size, 0, Math.PI * 2);
          ctx.fill();
        } else if (this.type === 1) {
          // Tipo B: Fragmento de espejo
          ctx.fillStyle = this.color;
          ctx.fillRect(-this.size, -this.size * 0.6, this.size * 2, this.size * 1.2);
        } else if (this.type === 2) {
          // Tipo C: Estrella de 4 puntas
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(-this.size * 2.2, -0.8, this.size * 4.4, 1.6);
          ctx.fillRect(-0.8, -this.size * 2.2, 1.6, this.size * 4.4);
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.arc(0, 0, this.size * 0.8, 0, Math.PI * 2);
          ctx.fill();
        } else {
          // Tipo D: Bokeh suave
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.arc(0, 0, this.size, 0, Math.PI * 2);
          ctx.fill();
        }

        ctx.restore();
      }
    }

    // Inicializar 65 partículas ambientales
    for (let i = 0; i < 65; i++) {
      particlesList.push(new DiscoParticle(false));
    }

    function renderParticlesEngine() {
      requestAnimationFrame(renderParticlesEngine);
      pCtx.clearRect(0, 0, pWidth, pHeight);

      for (let p of particlesList) {
        p.update();
        p.draw(pCtx);
      }
    }
    renderParticlesEngine();

    function triggerDiscoWaterfall() {
      isWaterfallMode = true;
      for (let i = 0; i < 120; i++) {
        particlesList.push(new DiscoParticle(true));
      }
      setTimeout(() => {
        isWaterfallMode = false;
        setTimeout(() => {
          particlesList = particlesList.slice(0, 75);
        }, 4000);
      }, 3500);
    }

    // =======================================================
    // TRANSICIÓN CINEMATOGRÁFICA
    // =======================================================
    const btnOpen = document.getElementById("btn-trigger-open");
    const screenWelcome = document.getElementById("screen-welcome");
    const screenInvitation = document.getElementById("screen-invitation");
    const cinematicFlash = document.getElementById("cinematic-flash");

    btnOpen.addEventListener("click", () => {
      playDiscoAudio();

      ballSpeedMultiplier = 3.5;
      if (discoBlueLightRef) discoBlueLightRef.intensity = 9.0;
      if (discoCyanLightRef) discoCyanLightRef.intensity = 8.5;
      if (discoVioletLightRef) discoVioletLightRef.intensity = 7.0;

      cinematicFlash.classList.add("active");
      triggerDiscoWaterfall();

      setTimeout(() => {
        cinematicFlash.classList.remove("active");
        screenWelcome.classList.add("fading-out");

        setTimeout(() => {
          screenWelcome.style.display = "none";
          screenInvitation.style.display = "block";

          setTimeout(() => {
            screenInvitation.classList.add("visible");
            window.scrollTo({ top: 0, behavior: 'smooth' });

            ballSpeedMultiplier = 1.0;
            if (discoBlueLightRef) discoBlueLightRef.intensity = 6.2;
            if (discoCyanLightRef) discoCyanLightRef.intensity = 5.5;
            if (discoVioletLightRef) discoVioletLightRef.intensity = 4.8;
          }, 60);

        }, 450);
      }, 260);
    });

    // =======================================================
    // CONFIRMACIÓN DE ASISTENCIA — WHATSAPP BUSINESS
    // =======================================================
    const rsvpForm = document.getElementById("form-vip-rsvp");
    rsvpForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const guestName = document.getElementById("rsvp-input-name").value.trim();
      const guestChoice = document.getElementById("rsvp-input-choice").value;

      if (!guestName) {
        showSystemToast("Por favor escribe tu Nombre y Apellido");
        return;
      }

      const textMsg = `¡Hola Angeles! 🪩✨\\nSoy *${guestName}* y confirmo mi asistencia a tu fiesta de 15 años Disco Party (19 de Octubre):\\n👉 *${guestChoice}*`;
      const wpUrl = `https://api.whatsapp.com/send?phone=${WHATSAPP_PHONE}&text=${encodeURIComponent(textMsg)}`;
      
      window.open(wpUrl, "_blank");
    });

    // =======================================================
    // PLAYLIST INTERACTIVA (LÓGICA ESTRICTA: MÁXIMO 2 CANCIONES)
    // =======================================================
    const pTitleIn = document.getElementById("playlist-title-in");
    const pArtistIn = document.getElementById("playlist-artist-in");
    const btnSaveSong = document.getElementById("btn-save-song");
    const songsAddedList = document.getElementById("songs-added-list");
    const btnSharePlaylistWp = document.getElementById("btn-share-playlist-wp");
    const toastAlert = document.getElementById("toast-system-alert");
    const toastMsgSpan = document.getElementById("toast-alert-msg");

    const STORAGE_KEY = "angeles_xv_disco_playlist";

    function getGuestSongs() {
      try {
        const raw = localStorage.getItem(STORAGE_KEY);
        return raw ? JSON.parse(raw) : [];
      } catch(e) {
        return [];
      }
    }

    function storeGuestSongs(songs) {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(songs));
      } catch(e) {}
    }

    function showSystemToast(msg) {
      toastMsgSpan.innerText = msg;
      toastAlert.classList.add("show");
      setTimeout(() => {
        toastAlert.classList.remove("show");
      }, 3500);
    }

    function renderGuestPlaylist() {
      const songs = getGuestSongs();
      songsAddedList.innerHTML = "";

      if (songs.length > 0) {
        btnSharePlaylistWp.style.display = "flex";
      } else {
        btnSharePlaylistWp.style.display = "none";
      }

      songs.forEach((s) => {
        const pill = document.createElement("div");
        pill.className = "song-item-pill";
        pill.innerHTML = `
          <div class="song-pill-data">
            <span class="song-title-str">🎵 ${escapeSafeHtml(s.title)}</span>
            <span class="song-artist-str">${escapeSafeHtml(s.artist)}</span>
          </div>
          <span class="song-badge-status">Agregada ✓</span>
        `;
        songsAddedList.appendChild(pill);
      });

      if (songs.length >= 2) {
        pTitleIn.disabled = true;
        pArtistIn.disabled = true;
        pTitleIn.placeholder = "Límite alcanzado (2 temas guardados)";
        pArtistIn.placeholder = "¡Gracias por tus canciones!";
      } else {
        pTitleIn.disabled = false;
        pArtistIn.disabled = false;
        pTitleIn.placeholder = "Nombre de la Canción";
        pArtistIn.placeholder = "Artista o Grupo";
      }
    }

    function escapeSafeHtml(str) {
      return (str || '').replace(/[&<>"']/g, function(m) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m];
      });
    }

    btnSaveSong.addEventListener("click", () => {
      const currentSongs = getGuestSongs();

      if (currentSongs.length >= 2) {
        showSystemToast("Solo puedes sugerir un máximo de 2 canciones por invitado");
        return;
      }

      const title = pTitleIn.value.trim();
      const artist = pArtistIn.value.trim();

      if (!title) {
        showSystemToast("Por favor escribe el nombre de la canción");
        pTitleIn.focus();
        return;
      }

      currentSongs.push({
        title: title,
        artist: artist || "Sin artista especificado"
      });

      storeGuestSongs(currentSongs);

      pTitleIn.value = "";
      pArtistIn.value = "";

      renderGuestPlaylist();
      triggerDiscoWaterfall();
    });

    btnSharePlaylistWp.addEventListener("click", () => {
      const currentSongs = getGuestSongs();
      if (currentSongs.length === 0) return;

      let msg = "¡Hola Angeles! 🪩🎶 Mis canciones sugeridas para tu fiesta de 15 años son:\\n";
      currentSongs.forEach((s, idx) => {
        msg += `${idx + 1}. *${s.title}* - ${s.artist}\\n`;
      });

      const wpUrl = `https://api.whatsapp.com/send?phone=${WHATSAPP_PHONE}&text=${encodeURIComponent(msg)}`;
      window.open(wpUrl, "_blank");
    });

    renderGuestPlaylist();

    // =======================================================
    // CUENTA REGRESIVA EN VIVO (19 DE OCTUBRE 2026 - 19:00 UTC-5)
    // =======================================================
    const eventTimeMs = new Date("2026-10-19T19:00:00-05:00").getTime();

    function updateCountdownTimer() {
      const now = new Date().getTime();
      const dist = eventTimeMs - now;

      if (dist < 0) {
        document.getElementById("val-days").innerText = "00";
        document.getElementById("val-hours").innerText = "00";
        document.getElementById("val-mins").innerText = "00";
        document.getElementById("val-secs").innerText = "00";
        return;
      }

      const days = Math.floor(dist / (1000 * 60 * 60 * 24));
      const hours = Math.floor((dist % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const mins = Math.floor((dist % (1000 * 60 * 60)) / (1000 * 60));
      const secs = Math.floor((dist % (1000 * 60)) / 1000);

      document.getElementById("val-days").innerText = String(days).padStart(2, '0');
      document.getElementById("val-hours").innerText = String(hours).padStart(2, '0');
      document.getElementById("val-mins").innerText = String(mins).padStart(2, '0');
      document.getElementById("val-secs").innerText = String(secs).padStart(2, '0');
    }

    setInterval(updateCountdownTimer, 1000);
    updateCountdownTimer();

  </script>
</body>
</html>
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_code)

print(f"index.html quirúrgicamente adaptado a la nueva paleta Azul/Cian/Violeta. Tamaño: {len(html_code)} bytes")
