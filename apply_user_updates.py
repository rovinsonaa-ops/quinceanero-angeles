import re

file_path = r"C:\Users\Rovinson\.gemini\antigravity\scratch\quinceanero-angeles\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Eliminar .disco-drag-hint de CSS y de HTML
content = re.sub(r'\s*\.disco-drag-hint\s*\{[^}]*\}', '', content)
content = re.sub(r'\s*<div class="disco-drag-hint">[^<]*<\/div>', '', content)

# 2. Reducir a menos espacio las coordenadas en CSS
old_coords_css = """    /* DETALLES DE FECHA, HORA Y DIRECCIÓN */
    .event-coords-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 14px;
      margin-bottom: 24px;
    }

    .coord-card-item {
      background: var(--card-inner-box);
      border: 1px solid rgba(255, 0, 127, 0.25);
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
      background: linear-gradient(135deg, rgba(255, 0, 127, 0.3), rgba(157, 78, 221, 0.2));
      border: 1.5px solid var(--neon-fuchsia);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 10px rgba(255, 0, 127, 0.35);
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
      color: var(--neon-pink-light);
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
    }"""

new_coords_css = """    /* DETALLES DE FECHA, HORA Y DIRECCIÓN (COMPACTO Y ELEGANTE) */
    .event-coords-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-bottom: 15px;
    }

    .coord-card-item {
      background: var(--card-inner-box);
      border: 1px solid rgba(255, 0, 127, 0.22);
      border-radius: 12px;
      padding: 8px 12px;
      display: flex;
      align-items: center;
      gap: 10px;
      text-align: left;
    }

    .coord-icon-orb {
      width: 32px;
      height: 32px;
      min-width: 32px;
      border-radius: 50%;
      background: linear-gradient(135deg, rgba(255, 0, 127, 0.3), rgba(157, 78, 221, 0.2));
      border: 1.2px solid var(--neon-fuchsia);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 8px rgba(255, 0, 127, 0.3);
    }

    .coord-data-block {
      display: flex;
      flex-direction: column;
    }

    .coord-type-lbl {
      font-family: 'Cinzel', serif;
      font-size: 0.65rem;
      font-weight: 700;
      letter-spacing: 1.2px;
      color: var(--neon-pink-light);
      text-transform: uppercase;
      line-height: 1.1;
    }

    .coord-val-txt {
      font-size: 0.86rem;
      font-weight: 700;
      color: #ffffff;
      margin-top: 1px;
      line-height: 1.2;
    }

    .btn-maps-action {
      min-height: 40px;
      background: linear-gradient(135deg, #00b4d8 0%, #0077b6 100%);
      color: #ffffff;
      border: none;
      padding: 9px 16px;
      font-family: 'Montserrat', sans-serif;
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.8px;
      border-radius: 50px;
      cursor: pointer;
      width: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      box-shadow: 0 4px 16px rgba(0, 180, 216, 0.35);
      text-decoration: none;
      transition: transform 0.2s;
      margin-top: 2px;
    }"""

if old_coords_css in content:
    content = content.replace(old_coords_css, new_coords_css)
    print("Coords CSS updated to compact!")
else:
    print("Warning: old_coords_css not found directly, checking partial replacement...")

# Reducir tamaño de iconos svg en las coordenadas (de 22 a 17)
content = re.sub(r'(<div class="coord-icon-orb">\s*<svg width=")22(" height=")22(")', r'\g<1>17\g<2>17\g<3>', content)

# 3. Badge Ambiente: solo 'MÚSICA EN VIVO' y punto rojo parpadeando
old_badge_html = """          <div class="ambiente-live-badge">
            <span class="live-dot-pulse"></span>
            EN VIVO • DJ SESSION
          </div>"""

new_badge_html = """          <div class="ambiente-live-badge">
            <span class="live-dot-pulse-red"></span>
            MÚSICA EN VIVO
          </div>"""

content = content.replace(old_badge_html, new_badge_html)

# CSS del badge con punto rojo parpadeando
old_badge_css = """.ambiente-live-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 0, 127, 0.15);
      border: 1px solid var(--neon-fuchsia);
      padding: 4px 14px;
      border-radius: 50px;
      font-size: 0.72rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 12px;
      box-shadow: 0 0 10px rgba(255, 0, 127, 0.4);
    }

    .live-dot-pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #ff007f;
      box-shadow: 0 0 8px #ff007f;
      animation: liveDotBlink 1.2s infinite ease-in-out;
    }

    @keyframes liveDotBlink {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.3; transform: scale(0.7); }
    }"""

new_badge_css = """.ambiente-live-badge {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      background: rgba(255, 0, 51, 0.12);
      border: 1px solid rgba(255, 0, 51, 0.65);
      padding: 4px 14px;
      border-radius: 50px;
      font-size: 0.72rem;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-bottom: 12px;
      box-shadow: 0 0 14px rgba(255, 0, 51, 0.35);
    }

    .live-dot-pulse-red {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #ff0033;
      box-shadow: 0 0 10px #ff0033, 0 0 18px rgba(255, 0, 51, 0.9);
      animation: redDotBlink 1.1s infinite ease-in-out;
    }

    @keyframes redDotBlink {
      0%, 100% { opacity: 1; transform: scale(1.2); box-shadow: 0 0 12px #ff0033, 0 0 20px #ff0033; }
      50% { opacity: 0.2; transform: scale(0.7); box-shadow: 0 0 2px #ff0033; }
    }"""

if old_badge_css in content:
    content = content.replace(old_badge_css, new_badge_css)
    print("Badge CSS updated to red dot + MUSICA EN VIVO!")

# 4. Ecualizador Ochentero Multicolor (Años 80)
old_eq_css = """    /* ECUALIZADOR ANIMADO LED NEÓN */
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
      background: linear-gradient(180deg, #ffffff 0%, var(--neon-pink) 30%, var(--neon-fuchsia) 60%, var(--neon-violet) 100%);
      border-radius: 3px 3px 1px 1px;
      box-shadow: 0 0 6px rgba(255, 0, 127, 0.45);
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
      50% { transform: scaleY(0.95); filter: brightness(1.25); }
      100% { transform: scaleY(0.4); filter: brightness(1.0); }
    }"""

new_eq_css = """    /* ECUALIZADOR ANIMADO ESTILO DISCO AÑOS 80 (MULTICOLOR RETRO) */
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

if old_eq_css in content:
    content = content.replace(old_eq_css, new_eq_css)
    print("Equalizer CSS updated to 80s Disco!")

# En el HTML del ecualizador, asegurar 14 barras
old_eq_html = """            <!-- ECUALIZADOR ANIMADO DE AUDIO NEÓN -->
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
            </div>"""

new_eq_html = """            <!-- ECUALIZADOR ANIMADO DISCO AÑOS 80 (MULTICOLOR RETRO) -->
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

if old_eq_html in content:
    content = content.replace(old_eq_html, new_eq_html)
    print("Equalizer HTML updated to 14 bars!")

# 5. Más chispas de brillo plateadas y claras que se noten más
# En Three.js: más spots y mayor intensidad plateada
content = content.replace("const spotCount = 180;", "const spotCount = 280;")
content = content.replace("size: 0.32,", "size: 0.38,")
content = content.replace("whiteLight = new THREE.DirectionalLight(0xffffff, 4.2);", "whiteLight = new THREE.DirectionalLight(0xffffff, 5.8);")

old_3d_colors = """      const colorPalette = [
        new THREE.Color(0xff007f), // Fucsia
        new THREE.Color(0xff3399), // Rosa
        new THREE.Color(0x9d4edd), // Violeta
        new THREE.Color(0x00d4ff), // Cian
        new THREE.Color(0xffffff)  // Blanco
      ];"""

new_3d_colors = """      const colorPalette = [
        new THREE.Color(0xffffff), // Blanco diamante
        new THREE.Color(0xffffff), // Plata pura
        new THREE.Color(0xe2e8f0), // Plata clara
        new THREE.Color(0xff007f), // Fucsia neón
        new THREE.Color(0x00e5ff), // Cian eléctrico
        new THREE.Color(0xffffff)  // Blanco
      ];"""

if old_3d_colors in content:
    content = content.replace(old_3d_colors, new_3d_colors)
    print("Three.js reflections updated to diamond silver/white!")

# En el motor de partículas canvas: chispas plateadas/claras más abundantes y nítidas
content = content.replace("for (let i = 0; i < 65; i++)", "for (let i = 0; i < 95; i++)")

old_particle_colors = """        const colors = [
          '#ffffff', '#ff007f', '#ff3399', '#9d4edd', '#00d4ff', '#fbcfe8', '#fcd34d'
        ];"""

new_particle_colors = """        // Chispas de brillo plateadas y claras notorias
        const colors = [
          '#ffffff', '#ffffff', '#eaf7ff', '#f8fafc', '#ffffff', '#ff007f', '#ff75b5', '#cbd5e1'
        ];"""

if old_particle_colors in content:
    content = content.replace(old_particle_colors, new_particle_colors)

# Mejorar el dibujo de chispas tipo estrella de 4 puntas y destellos de espejo para que brillen intensamente
old_draw_code = """        if (this.type === 0) {
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
        }"""

new_draw_code = """        if (this.type === 0) {
          // Tipo A: Chispa de cristal brillante plateada
          ctx.shadowColor = '#ffffff';
          ctx.shadowBlur = 6;
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.arc(0, 0, this.size * 1.1, 0, Math.PI * 2);
          ctx.fill();
          ctx.shadowBlur = 0;
        } else if (this.type === 1) {
          // Tipo B: Fragmento de espejo plateado brillante
          ctx.shadowColor = '#ffffff';
          ctx.shadowBlur = 8;
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(-this.size, -this.size * 0.7, this.size * 2, this.size * 1.4);
          ctx.shadowBlur = 0;
        } else if (this.type === 2) {
          // Tipo C: Estrella de brillo plateado de 4 puntas de alta visibilidad
          ctx.shadowColor = '#ffffff';
          ctx.shadowBlur = 10;
          ctx.fillStyle = '#ffffff';
          ctx.fillRect(-this.size * 2.8, -1.0, this.size * 5.6, 2.0);
          ctx.fillRect(-1.0, -this.size * 2.8, 2.0, this.size * 5.6);
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.arc(0, 0, this.size * 1.1, 0, Math.PI * 2);
          ctx.fill();
          ctx.shadowBlur = 0;
        } else {
          // Tipo D: Bokeh suave
          ctx.fillStyle = this.color;
          ctx.beginPath();
          ctx.arc(0, 0, this.size, 0, Math.PI * 2);
          ctx.fill();
        }"""

if old_draw_code in content:
    content = content.replace(old_draw_code, new_draw_code)
    print("Particle drawing updated to glowing diamond silver sparkles!")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"index.html updated successfully! Total bytes: {len(content)}")
