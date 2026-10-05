import re

file_path = r"C:\Users\Rovinson\.gemini\antigravity\scratch\quinceanero-angeles\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. ACTUALIZAR LETRAS ALOCADAS EN CSS
old_alocado_css = """    .ambiente-title {
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
      color: var(--neon-fuchsia);
      letter-spacing: 2px;
      text-shadow: 0 0 14px rgba(255, 0, 127, 0.7);
      margin-bottom: 6px;
    }

    .ambiente-attitude-txt {
      font-size: 0.88rem;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 16px;
    }"""

new_alocado_css = """    .ambiente-title {
      font-family: 'Cinzel', serif;
      font-size: 1.1rem;
      font-weight: 900;
      color: #ffffff;
      letter-spacing: 3px;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    .ambiente-vibe-tag {
      font-family: 'Montserrat', 'Cinzel', sans-serif;
      font-size: 1.6rem;
      font-weight: 900;
      letter-spacing: 4px;
      text-transform: uppercase;
      display: inline-block;
      margin: 4px 0 6px 0;
      /* Gradiente neón alocado y festivo: Fucsia -> Amarillo Sol -> Cian */
      background: linear-gradient(90deg, #ff007f 0%, #ffee00 50%, #00e5ff 100%);
      background-size: 200% auto;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 14px rgba(255, 0, 127, 0.8)) drop-shadow(0 0 8px rgba(255, 238, 0, 0.6));
      animation: crazyAlocadoMotion 2.2s ease-in-out infinite alternate, crazyShineGrad 3s linear infinite;
    }

    @keyframes crazyAlocadoMotion {
      0% {
        transform: rotate(-3.5deg) scale(0.98);
        filter: drop-shadow(0 0 12px rgba(255, 0, 127, 0.85));
      }
      50% {
        transform: rotate(2.5deg) scale(1.06) skewX(-2deg);
        filter: drop-shadow(0 0 20px rgba(0, 229, 255, 0.9));
      }
      100% {
        transform: rotate(-2.5deg) scale(1.02) skewX(2deg);
        filter: drop-shadow(0 0 16px rgba(255, 238, 0, 0.85));
      }
    }

    @keyframes crazyShineGrad {
      0% { background-position: 0% center; }
      100% { background-position: 200% center; }
    }

    .ambiente-attitude-txt {
      font-size: 0.88rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 16px;
      animation: pulseAttitude 1.8s infinite alternate;
    }

    @keyframes pulseAttitude {
      0% { opacity: 0.85; transform: scale(0.98); }
      100% { opacity: 1; transform: scale(1.02); text-shadow: 0 0 10px rgba(255, 0, 127, 0.8); }
    }"""

if old_alocado_css in content:
    content = content.replace(old_alocado_css, new_alocado_css)
    print("Alocado title & animated letters updated!")
else:
    print("Warning: old_alocado_css not found directly, checking partial replacement...")

# 2. ACTUALIZAR TORNAMESAS A DISCOS DE VINILO QUE GIRAN Y GIRAN Y GIRAN
old_vinyl_css = """    .dj-turntable {
      width: 58px;
      height: 58px;
      border-radius: 50%;
      background: radial-gradient(circle, #1a1020 0%, #251030 50%, #0d0612 100%);
      border: 2px solid rgba(255, 0, 127, 0.5);
      box-shadow: 0 0 12px rgba(255, 0, 127, 0.4);
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
      background: linear-gradient(135deg, var(--neon-fuchsia) 0%, var(--neon-violet) 100%);
      border: 1.5px solid #ffffff;
      box-shadow: 0 0 6px var(--neon-fuchsia);
    }"""

new_vinyl_css = """    .dj-turntable {
      width: 66px;
      height: 66px;
      border-radius: 50%;
      /* Surcos concéntricos de acetato negro de disco de vinilo real */
      background: 
        radial-gradient(circle, #2a2a2a 0%, #151515 18%, #080808 36%, #1c1c1c 54%, #0a0a0a 72%, #181818 88%, #020202 100%);
      border: 2px solid #333344;
      box-shadow: 0 0 16px rgba(255, 0, 127, 0.35), inset 0 0 8px rgba(0, 0, 0, 0.95);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      animation: spinDeckVinylA 3s linear infinite;
    }

    .dj-turntable.deck-b {
      animation: spinDeckVinylB 2.4s linear infinite reverse;
    }

    @keyframes spinDeckVinylA {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    @keyframes spinDeckVinylB {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }

    /* Brillo de reflejo de luz radial en el vinilo al girar */
    .dj-turntable::before {
      content: '';
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      border-radius: 50%;
      background: conic-gradient(from 0deg, transparent 0deg, rgba(255, 255, 255, 0.16) 45deg, transparent 90deg, transparent 180deg, rgba(255, 255, 255, 0.16) 225deg, transparent 270deg);
      pointer-events: none;
    }

    /* Galleta / Etiqueta central del vinilo de discoteca */
    .dj-turntable-core {
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--neon-fuchsia) 0%, var(--neon-violet) 100%);
      border: 1.5px solid #ffffff;
      box-shadow: 0 0 8px rgba(255, 0, 127, 0.8);
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 2;
    }

    .dj-turntable.deck-b .dj-turntable-core {
      background: linear-gradient(135deg, #00e5ff 0%, #7a2cff 100%);
      box-shadow: 0 0 8px rgba(0, 229, 255, 0.8);
    }

    .dj-spindle-hole {
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background: #030305;
      border: 1px solid rgba(255, 255, 255, 0.8);
    }"""

if old_vinyl_css in content:
    content = content.replace(old_vinyl_css, new_vinyl_css)
    print("DJ turntables updated to real spinning vinyl records!")
else:
    print("Warning: old_vinyl_css not found directly...")

# Agregar spindle-hole en el HTML de las tornamesas
old_decks_html = """            <div class="dj-deck-visual">
              <div class="dj-turntable deck-a">
                <div class="dj-turntable-core"></div>
              </div>
              <div class="dj-mixer-center">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ff007f" stroke-width="2">
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
            </div>"""

new_decks_html = """            <div class="dj-deck-visual">
              <!-- DISCO DE VINILO A GIRANDO EN VIVO -->
              <div class="dj-turntable deck-a" title="Disco de Vinilo A">
                <div class="dj-turntable-core">
                  <div class="dj-spindle-hole"></div>
                </div>
              </div>
              <div class="dj-mixer-center">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#ff007f" stroke-width="2">
                  <path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
                  <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
                </svg>
                <div class="dj-fader-slot">
                  <div class="dj-fader-knob"></div>
                </div>
              </div>
              <!-- DISCO DE VINILO B GIRANDO EN VIVO -->
              <div class="dj-turntable deck-b" title="Disco de Vinilo B">
                <div class="dj-turntable-core">
                  <div class="dj-spindle-hole"></div>
                </div>
              </div>
            </div>"""

if old_decks_html in content:
    content = content.replace(old_decks_html, new_decks_html)
    print("DJ turntables HTML updated with spindle holes!")

# 3. ACTUALIZAR BARRA DE MÚSICA CON EL ESPECTRO ARCOÍRIS DISCO DE LAS IMÁGENES REFERENCIALES
# Eliminar el ecualizador actual y sustituir por el espectro de 18 columnas arcoíris
old_eq_section_css = """    /* ECUALIZADOR ANIMADO ESTILO DISCO AÑOS 80 (MULTICOLOR RETRO) */
    .equalizer-spectrum-bar {
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 3px;
      height: 52px;
      width: 100%;
      padding: 0 6px 4px 6px;
      background: rgba(4, 3, 8, 0.85);
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.95);
    }

    .eq-column {
      flex: 1;
      max-width: 12px;
      border-radius: 2px 2px 0 0;
      transform-origin: bottom;
      animation: eqBounce80s 1.2s ease-in-out infinite alternate;
      /* Segmentación LED clásica ochentera (Verde neón -> Amarillo neón -> Naranja -> Rojo/Fucsia) */
      background: 
        repeating-linear-gradient(180deg, transparent 0px, transparent 2px, rgba(0, 0, 0, 0.55) 2px, rgba(0, 0, 0, 0.55) 4px),
        linear-gradient(to top, #00ff66 0%, #00ff66 32%, #ffee00 58%, #ff6600 78%, #ff0044 100%);
      box-shadow: 0 0 8px rgba(0, 255, 102, 0.4), 0 0 14px rgba(255, 0, 68, 0.35);
    }

    .eq-col-1  { height: 42%; animation-delay: 0.1s; animation-duration: 0.8s; }
    .eq-col-2  { height: 80%; animation-delay: 0.3s; animation-duration: 1.1s; }
    .eq-col-3  { height: 55%; animation-delay: 0.05s; animation-duration: 0.9s; }
    .eq-col-4  { height: 95%; animation-delay: 0.4s; animation-duration: 1.3s; }
    .eq-col-5  { height: 65%; animation-delay: 0.2s; animation-duration: 0.75s; }
    .eq-col-6  { height: 100%; animation-delay: 0.5s; animation-duration: 1.05s; }
    .eq-col-7  { height: 50%; animation-delay: 0.15s; animation-duration: 1.2s; }
    .eq-col-8  { height: 90%; animation-delay: 0.35s; animation-duration: 0.85s; }
    .eq-col-9  { height: 75%; animation-delay: 0.25s; animation-duration: 1.15s; }
    .eq-col-10 { height: 95%; animation-delay: 0.45s; animation-duration: 0.95s; }
    .eq-col-11 { height: 60%; animation-delay: 0.1s; animation-duration: 1.05s; }
    .eq-col-12 { height: 85%; animation-delay: 0.3s; animation-duration: 0.8s; }
    .eq-col-13 { height: 70%; animation-delay: 0.2s; animation-duration: 1.1s; }
    .eq-col-14 { height: 90%; animation-delay: 0.4s; animation-duration: 0.9s; }

    @keyframes eqBounce80s {
      0% { transform: scaleY(0.2); filter: brightness(0.9); }
      50% { transform: scaleY(0.98); filter: brightness(1.35); }
      100% { transform: scaleY(0.38); filter: brightness(1.0); }
    }"""

new_eq_section_css = """    /* ECUALIZADOR ANIMADO DISCO MULTICOLOR RETRO (SEGÚN REFERENCIAS OCHENTERAS) */
    .equalizer-spectrum-bar {
      display: flex;
      align-items: flex-end;
      justify-content: center;
      gap: 3px;
      height: 54px;
      width: 100%;
      padding: 0 6px 4px 6px;
      background: rgba(3, 2, 7, 0.92);
      border-radius: 10px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: inset 0 0 16px rgba(0, 0, 0, 0.98), 0 2px 10px rgba(0, 0, 0, 0.6);
      overflow: hidden;
      position: relative;
    }

    .eq-column {
      flex: 1;
      max-width: 11px;
      border-radius: 2px 2px 0 0;
      transform-origin: bottom;
      animation: eqBounceRainbow 1.2s ease-in-out infinite alternate;
      /* Bloques LED segmentados característicos de los ecualizadores ochenteros */
      background-image: repeating-linear-gradient(180deg, transparent 0px, transparent 2px, rgba(0, 0, 0, 0.6) 2px, rgba(0, 0, 0, 0.6) 4px);
    }

    /* Cada barra con su color del espectro arcoíris disco (como en las imágenes referenciales) */
    .eq-c-1  { background-color: #ff0033; box-shadow: 0 0 8px #ff0033; height: 38%; animation-delay: 0.1s;  animation-duration: 0.8s; }
    .eq-c-2  { background-color: #ff3d00; box-shadow: 0 0 8px #ff3d00; height: 65%; animation-delay: 0.25s; animation-duration: 1.05s; }
    .eq-c-3  { background-color: #ff6d00; box-shadow: 0 0 8px #ff6d00; height: 48%; animation-delay: 0.05s; animation-duration: 0.9s; }
    .eq-c-4  { background-color: #ff9100; box-shadow: 0 0 8px #ff9100; height: 82%; animation-delay: 0.35s; animation-duration: 1.2s; }
    .eq-c-5  { background-color: #ffea00; box-shadow: 0 0 8px #ffea00; height: 60%; animation-delay: 0.15s; animation-duration: 0.75s; }
    .eq-c-6  { background-color: #c6ff00; box-shadow: 0 0 8px #c6ff00; height: 95%; animation-delay: 0.45s; animation-duration: 1.05s; }
    .eq-c-7  { background-color: #76ff03; box-shadow: 0 0 8px #76ff03; height: 52%; animation-delay: 0.1s;  animation-duration: 1.15s; }
    .eq-c-8  { background-color: #00e676; box-shadow: 0 0 8px #00e676; height: 90%; animation-delay: 0.3s;  animation-duration: 0.85s; }
    .eq-c-9  { background-color: #00bfa5; box-shadow: 0 0 8px #00bfa5; height: 72%; animation-delay: 0.2s;  animation-duration: 1.1s; }
    .eq-c-10 { background-color: #00e5ff; box-shadow: 0 0 8px #00e5ff; height: 98%; animation-delay: 0.4s;  animation-duration: 0.95s; }
    .eq-c-11 { background-color: #00b0ff; box-shadow: 0 0 8px #00b0ff; height: 58%; animation-delay: 0.12s; animation-duration: 1.05s; }
    .eq-c-12 { background-color: #2979ff; box-shadow: 0 0 8px #2979ff; height: 85%; animation-delay: 0.32s; animation-duration: 0.8s; }
    .eq-c-13 { background-color: #651fff; box-shadow: 0 0 8px #651fff; height: 68%; animation-delay: 0.22s; animation-duration: 1.15s; }
    .eq-c-14 { background-color: #aa00ff; box-shadow: 0 0 8px #aa00ff; height: 92%; animation-delay: 0.42s; animation-duration: 0.9s; }
    .eq-c-15 { background-color: #d500f9; box-shadow: 0 0 8px #d500f9; height: 64%; animation-delay: 0.18s; animation-duration: 1.0s; }
    .eq-c-16 { background-color: #ff007f; box-shadow: 0 0 8px #ff007f; height: 88%; animation-delay: 0.38s; animation-duration: 0.85s; }
    .eq-c-17 { background-color: #ff1744; box-shadow: 0 0 8px #ff1744; height: 74%; animation-delay: 0.28s; animation-duration: 1.1s; }
    .eq-c-18 { background-color: #ff5252; box-shadow: 0 0 8px #ff5252; height: 45%; animation-delay: 0.08s; animation-duration: 0.9s; }

    @keyframes eqBounceRainbow {
      0% { transform: scaleY(0.18); filter: brightness(0.85); }
      50% { transform: scaleY(0.98); filter: brightness(1.4); }
      100% { transform: scaleY(0.35); filter: brightness(0.95); }
    }"""

if old_eq_section_css in content:
    content = content.replace(old_eq_section_css, new_eq_section_css)
    print("Equalizer CSS updated to full Rainbow Spectrum!")
else:
    print("Warning: old_eq_section_css not found directly...")

# Actualizar el HTML del ecualizador a las 18 barras del arcoíris
old_bars_html = """            <!-- ECUALIZADOR ANIMADO DISCO AÑOS 80 (MULTICOLOR RETRO) -->
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
              <div class="eq-column eq-col-13"></div>
              <div class="eq-column eq-col-14"></div>
            </div>"""

new_bars_html = """            <!-- ECUALIZADOR ANIMADO DISCO MULTICOLOR RETRO (SEGÚN REFERENCIAS OCHENTERAS) -->
            <div class="equalizer-spectrum-bar">
              <div class="eq-column eq-c-1"></div>
              <div class="eq-column eq-c-2"></div>
              <div class="eq-column eq-c-3"></div>
              <div class="eq-column eq-c-4"></div>
              <div class="eq-column eq-c-5"></div>
              <div class="eq-column eq-c-6"></div>
              <div class="eq-column eq-c-7"></div>
              <div class="eq-column eq-c-8"></div>
              <div class="eq-column eq-c-9"></div>
              <div class="eq-column eq-c-10"></div>
              <div class="eq-column eq-c-11"></div>
              <div class="eq-column eq-c-12"></div>
              <div class="eq-column eq-c-13"></div>
              <div class="eq-column eq-c-14"></div>
              <div class="eq-column eq-c-15"></div>
              <div class="eq-column eq-c-16"></div>
              <div class="eq-column eq-c-17"></div>
              <div class="eq-column eq-c-18"></div>
            </div>"""

if old_bars_html in content:
    content = content.replace(old_bars_html, new_bars_html)
    print("Equalizer HTML updated to 18 Rainbow bars!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"index.html successfully updated! Length: {len(content)}")
