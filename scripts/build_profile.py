import os
import io
import base64
from PIL import Image

def get_crop_b64(img_path, col, row, size=512, target_size=(240, 240)):
    img = Image.open(img_path)
    crop = img.crop((col * size, row * size, (col + 1) * size, (row + 1) * size))
    if target_size:
        crop = crop.resize(target_size, Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    crop.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

def get_image_b64(img_path, target_size=None):
    img = Image.open(img_path)
    if target_size:
        img = img.resize(target_size, Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='PNG', optimize=True)
    return base64.b64encode(buf.getvalue()).decode('utf-8')

print("1. Extracting frames for Final Charcoal & Sapphire Suite...")
vw0 = get_crop_b64('Violet/violet-spritesheet.png', 0, 1, target_size=(260, 260))
vw1 = get_crop_b64('Violet/violet-spritesheet.png', 1, 1, target_size=(260, 260))
vw2 = get_crop_b64('Violet/violet-spritesheet.png', 2, 1, target_size=(260, 260))
vw3 = get_crop_b64('Violet/violet-spritesheet.png', 3, 1, target_size=(260, 260))

vt0 = get_crop_b64('Violet/violet-spritesheet.png', 0, 2, target_size=(190, 190))
vt1 = get_crop_b64('Violet/violet-spritesheet.png', 1, 2, target_size=(190, 190))
vt2 = get_crop_b64('Violet/violet-spritesheet.png', 2, 2, target_size=(190, 190))
vt3 = get_crop_b64('Violet/violet-spritesheet.png', 3, 2, target_size=(190, 190))

throne_b64 = get_image_b64('Queen/throne-fixed.png', target_size=(280, 240))

q_frames = []
for idx in range(14):
    r = idx // 4
    c = idx % 4
    q_frames.append(get_crop_b64('Queen/queen-spritesheet.png', c, r, target_size=(240, 240)))

ag_frames = []
for idx in [0, 2, 4, 7, 10, 13]:
    r = idx // 4
    c = idx % 4
    ag_frames.append(get_crop_b64('AntlerGirl/antler-girl-spritesheet.png', c, r, target_size=(230, 230)))

v_connect = get_crop_b64('Violet/violet-spritesheet.png', 2, 1, target_size=(210, 210))

# ==================== 1. HERO.SVG ====================
hero_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 375" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,600&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * {{ box-sizing: border-box; }}
      .font-sans {{ font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif; }}
      .font-serif {{ font-family: 'Playfair Display', Georgia, serif; }}
      .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
      @keyframes pulse-dot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}
      @keyframes rec-blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.2; }}
      }}
      @keyframes scrubber-move {{
        0% {{ width: 0%; }}
        80% {{ width: 95%; }}
        100% {{ width: 100%; }}
      }}
      @keyframes float-bubble {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-4px); }}
      }}
      @keyframes sapphire-glow {{
        0%, 100% {{ filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.4)); }}
        50% {{ filter: drop-shadow(0 0 20px rgba(37, 99, 235, 0.8)); }}
      }}
      .pulse-pill {{ animation: pulse-dot 2s ease-in-out infinite; }}
      .rec-dot {{ animation: rec-blink 1.2s ease-in-out infinite; }}
      .scrubber-fill {{ animation: scrubber-move 3.2s linear infinite; }}
      .speech-bubble {{ animation: float-bubble 3s ease-in-out infinite; }}
      .glow-sapphire {{ animation: sapphire-glow 4s ease-in-out infinite; }}
    </style>

    <linearGradient id="suit-charcoal-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141822" />
      <stop offset="45%" stop-color="#0f131b" />
      <stop offset="100%" stop-color="#0a0d13" />
    </linearGradient>

    <linearGradient id="suit-edge-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
      <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#1d4ed8" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#c49d63" stop-opacity="0.6" />
    </linearGradient>

    <radialGradient id="moonlight-aura" cx="22%" cy="28%" r="55%">
      <stop offset="0%" stop-color="#2563eb" stop-opacity="0.25" />
      <stop offset="60%" stop-color="#38bdf8" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#0f131b" stop-opacity="0" />
    </radialGradient>

    <pattern id="suit-weave" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#ffffff" fill-opacity="0.04" />
    </pattern>

    <linearGradient id="obsidian-panel" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#090d14" />
      <stop offset="100%" stop-color="#04060a" />
    </linearGradient>

    <linearGradient id="reality-glow-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#2563eb" />
    </linearGradient>
  </defs>

  <rect x="2" y="2" width="896" height="371" rx="20" fill="url(#suit-charcoal-bg)" stroke="url(#suit-edge-border)" stroke-width="1.6" />
  <rect x="2" y="2" width="896" height="371" rx="20" fill="url(#moonlight-aura)" />
  <rect x="2" y="2" width="896" height="371" rx="20" fill="url(#suit-weave)" />

  <g transform="translate(36, 30)">
    <polygon points="0,-7 2,-2 7,0 2,2 0,7 -2,2 -7,0 -2,-2" fill="#38bdf8" />
    <text x="14" y="4" class="font-mono" font-size="11" font-weight="700" fill="#ffffff" letter-spacing="1.5">HARSH</text>
    <text x="68" y="4" class="font-mono" font-size="11" fill="#64748b">/</text>
    <text x="80" y="4" class="font-mono" font-size="11" fill="#94a3b8">WELCOME TO MY SPACE</text>
  </g>

  <g transform="translate(36, 54)">
    <rect x="0" y="0" width="168" height="26" rx="13" fill="#090d15" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1" />
    <circle cx="16" cy="13" r="4" fill="#38bdf8" class="pulse-pill" />
    <text x="27" y="17" class="font-mono" font-size="10" font-weight="700" fill="#ffffff" letter-spacing="1">OPEN TO COLLABS</text>
  </g>

  <g transform="translate(36, 112)">
    <text x="0" y="0" class="font-sans" font-size="32" font-weight="800" fill="#ffffff" letter-spacing="-0.5">
      Turning Ideas
    </text>
    <text x="0" y="38" class="font-sans" font-size="32" font-weight="800" fill="#ffffff" letter-spacing="-0.5">
      Into <tspan fill="url(#reality-glow-grad)" class="glow-sapphire">Reality</tspan><tspan fill="#38bdf8" font-weight="400">|</tspan>
    </text>
  </g>

  <text x="36" y="180" class="font-sans" font-size="13" font-weight="500" fill="#cbd5e1">
    I'm a Computer Engineering student who loves building interactive,
  </text>
  <text x="36" y="198" class="font-sans" font-size="13" font-weight="500" fill="#cbd5e1">
    meaningful and aesthetic digital experiences with modern software.
  </text>

  <g transform="translate(36, 224)">
    <g transform="translate(0, 0)">
      <text x="0" y="18" class="font-sans" font-size="20" font-weight="800" fill="#ffffff">10+</text>
      <text x="0" y="32" class="font-mono" font-size="10" font-weight="600" fill="#94a3b8">Projects</text>
    </g>
    <g transform="translate(90, 0)">
      <text x="0" y="18" class="font-sans" font-size="20" font-weight="800" fill="#38bdf8">3+</text>
      <text x="0" y="32" class="font-mono" font-size="10" font-weight="600" fill="#94a3b8">Tech Stacks</text>
    </g>
    <g transform="translate(195, 0)">
      <text x="0" y="18" class="font-sans" font-size="20" font-weight="800" fill="#ffffff">100%</text>
      <text x="0" y="32" class="font-mono" font-size="10" font-weight="600" fill="#94a3b8">Passion</text>
    </g>
  </g>

  <g transform="translate(36, 285)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="168" height="28" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
      <text x="10" y="18" font-size="12">⚡</text>
      <text x="26" y="18" class="font-sans" font-size="11.5" font-weight="700" fill="#ffffff">Harsh Nilesh Patil</text>
    </g>
    <g transform="translate(176, 0)">
      <rect x="0" y="0" width="144" height="28" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
      <text x="10" y="18" font-size="12">📍</text>
      <text x="28" y="18" class="font-sans" font-size="11.5" font-weight="600" fill="#cbd5e1">Maharashtra, IN</text>
    </g>
    <g transform="translate(328, 0)">
      <rect x="0" y="0" width="148" height="28" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
      <text x="10" y="18" font-size="12">🎓</text>
      <text x="28" y="18" class="font-sans" font-size="11.5" font-weight="600" fill="#cbd5e1">Viva Tech ('29)</text>
    </g>
  </g>

  <g transform="translate(540, 24)">
    <rect x="0" y="0" width="324" height="324" rx="16" fill="url(#obsidian-panel)" stroke="#22334d" stroke-width="1.4" />
    <path d="M 14 30 L 14 14 L 30 14" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 294 14 L 310 14 L 310 30" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 14 294 L 14 310 L 30 310" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 294 310 L 310 310 L 310 294" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" />

    <g transform="translate(24, 28)">
      <circle cx="4" cy="0" r="4.5" fill="#38bdf8" class="rec-dot" />
      <text x="14" y="4" class="font-mono" font-size="10.5" font-weight="700" fill="#ffffff" letter-spacing="1">REC</text>
      <text x="46" y="4" class="font-mono" font-size="10" fill="#93c5fd">00:02:14</text>
      <text x="210" y="4" class="font-mono" font-size="9.5" fill="#64748b" text-anchor="end">HELLO_VIOLET.MP4</text>
    </g>

    <g class="speech-bubble" transform="translate(48, 54)">
      <rect x="0" y="0" width="62" height="24" rx="8" fill="#141c2c" stroke="#38bdf8" stroke-width="1.2" />
      <polygon points="12,24 16,30 20,24" fill="#141c2c" />
      <text x="31" y="16" class="font-sans" font-size="11.5" font-weight="800" fill="#ffffff" text-anchor="middle">hiii 👋</text>
    </g>

    <g transform="translate(32, 42)">
      <image href="data:image/png;base64,{vw0}" x="0" y="0" width="260" height="260">
        <animate attributeName="opacity" dur="3.2s" repeatCount="indefinite"
                 values="1;1;0;0;0;0" keyTimes="0;0.12;0.13;0.98;0.99;1" />
      </image>
      <image href="data:image/png;base64,{vw1}" x="0" y="0" width="260" height="260">
        <animate attributeName="opacity" dur="3.2s" repeatCount="indefinite"
                 values="0;0;1;1;0;0;0;0" keyTimes="0;0.12;0.13;0.25;0.26;0.98;0.99;1" />
      </image>
      <image href="data:image/png;base64,{vw2}" x="0" y="0" width="260" height="260">
        <animate attributeName="opacity" dur="3.2s" repeatCount="indefinite"
                 values="0;0;1;1;0;0;0;0" keyTimes="0;0.25;0.26;0.38;0.39;0.98;0.99;1" />
      </image>
      <image href="data:image/png;base64,{vw3}" x="0" y="0" width="260" height="260" opacity="1">
        <animate attributeName="opacity" dur="3.2s" repeatCount="indefinite"
                 values="0;0;1;1;1;0" keyTimes="0;0.38;0.39;0.88;0.96;1" />
      </image>
    </g>

    <g transform="translate(24, 300)">
      <rect x="0" y="0" width="276" height="4" rx="2" fill="#141c2c" />
      <rect x="0" y="0" height="4" rx="2" fill="url(#reality-glow-grad)">
        <animate attributeName="width" dur="3.2s" repeatCount="indefinite"
                 values="0;250;276;0" keyTimes="0;0.88;0.96;1" />
      </rect>
    </g>
  </g>
</svg>
'''
with open('hero.svg', 'w', encoding='utf-8') as f:
    f.write(hero_svg)

# ==================== 2. ABOUT-LIFE.SVG ====================
about_life_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 410" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * {{ box-sizing: border-box; }}
      .font-sans {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
      .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
      @keyframes blink-cursor {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0; }} }}
      .cursor-blink {{ animation: blink-cursor 1s infinite; }}
      @keyframes ring-dash {{ 0% {{ stroke-dashoffset: 260; }} 50% {{ stroke-dashoffset: 40; }} 100% {{ stroke-dashoffset: 260; }} }}
      .ring-anim-1 {{ animation: ring-dash 8s ease-in-out infinite; }}
      .ring-anim-2 {{ animation: ring-dash 8s ease-in-out infinite 0.5s; }}
      .ring-anim-3 {{ animation: ring-dash 8s ease-in-out infinite 1s; }}
    </style>
    <linearGradient id="suit-about-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
      <stop offset="45%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="80%" stop-color="#1d4ed8" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#c49d63" stop-opacity="0.5" />
    </linearGradient>
    <linearGradient id="suit-about-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141822" />
      <stop offset="45%" stop-color="#0f131b" />
      <stop offset="100%" stop-color="#0a0d13" />
    </linearGradient>
    <linearGradient id="ring-white" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="100%" stop-color="#cbd5e1" />
    </linearGradient>
    <linearGradient id="ring-sapphire" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#2563eb" />
    </linearGradient>
    <linearGradient id="ring-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fde68a" />
      <stop offset="100%" stop-color="#c49d63" />
    </linearGradient>
    <pattern id="card-suit-weave" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#ffffff" fill-opacity="0.04" />
    </pattern>
  </defs>

  <!-- Left Card: Developer -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="432" height="390" rx="18" fill="url(#suit-about-bg)" stroke="url(#suit-about-border)" stroke-width="1.5" />
    <rect x="0" y="0" width="432" height="390" rx="18" fill="url(#card-suit-weave)" />
    <text x="24" y="32" class="font-mono" font-size="11" font-weight="700" fill="#38bdf8" letter-spacing="1.5">// DEVELOPMENT</text>
    <text x="24" y="56" class="font-sans" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Interfaces &amp; Systems</text>

    <!-- Browser: Deep Obsidian on Charcoal -->
    <g transform="translate(24, 72)">
      <rect x="0" y="0" width="384" height="154" rx="12" fill="#05070c" stroke="#25354e" stroke-width="1.2" />
      <rect x="0" y="0" width="384" height="28" rx="12" fill="#0d121c" />
      <rect x="0" y="24" width="384" height="4" fill="#0d121c" />
      <circle cx="14" cy="14" r="4" fill="#64748b" />
      <circle cx="26" cy="14" r="4" fill="#38bdf8" />
      <circle cx="38" cy="14" r="4" fill="#ffffff" />
      <rect x="52" y="5" width="260" height="18" rx="6" fill="#131a27" stroke="#25354e" stroke-width="0.8" />
      <text x="64" y="18" class="font-mono" font-size="9" fill="#ffffff">localhost:3000/harsh/capabilities</text>
      <rect x="238" y="9" width="1.5" height="10" fill="#ffffff" class="cursor-blink" />

      <g transform="translate(14, 40)" opacity="0.85">
        <text x="0" y="14" class="font-mono" font-size="9" fill="#93c5fd">const <tspan fill="#ffffff">engineer</tspan> = {{</text>
        <text x="12" y="28" class="font-mono" font-size="9" fill="#ffffff">name: <tspan fill="#38bdf8">'Harsh Nilesh Patil'</tspan>,</text>
        <text x="12" y="42" class="font-mono" font-size="9" fill="#ffffff">role: <tspan fill="#38bdf8">'Comp Engg @ Mumbai'</tspan>,</text>
        <text x="12" y="56" class="font-mono" font-size="9" fill="#ffffff">passions: [<tspan fill="#ffffff">'AI'</tspan>, <tspan fill="#7dd3fc">'Web'</tspan>, <tspan fill="#93c5fd">'Sec'</tspan>]</text>
        <text x="0" y="70" class="font-mono" font-size="9" fill="#93c5fd">}};</text>
        <text x="0" y="86" class="font-mono" font-size="9" fill="#ffffff">engineer.<tspan fill="#38bdf8">buildFuture</tspan>();</text>
      </g>

      <g transform="translate(204, 12)">
        <image href="data:image/png;base64,{vt0}" x="0" y="0" width="170" height="170">
          <animate attributeName="opacity" dur="1.0s" repeatCount="indefinite"
                   values="1;1;0;0;0;0;0;0" keyTimes="0;0.23;0.25;0.73;0.75;0.98;0.99;1" />
        </image>
        <image href="data:image/png;base64,{vt1}" x="0" y="0" width="170" height="170">
          <animate attributeName="opacity" dur="1.0s" repeatCount="indefinite"
                   values="0;0;1;1;0;0;0;0" keyTimes="0;0.23;0.25;0.48;0.50;0.98;0.99;1" />
        </image>
        <image href="data:image/png;base64,{vt2}" x="0" y="0" width="170" height="170">
          <animate attributeName="opacity" dur="1.0s" repeatCount="indefinite"
                   values="0;0;1;1;0;0;0;0" keyTimes="0;0.48;0.50;0.73;0.75;0.98;0.99;1" />
        </image>
        <image href="data:image/png;base64,{vt3}" x="0" y="0" width="170" height="170" opacity="1">
          <animate attributeName="opacity" dur="1.0s" repeatCount="indefinite"
                   values="0;0;1;1" keyTimes="0;0.73;0.75;1" />
        </image>
      </g>
    </g>

    <!-- Capability Rows -->
    <g transform="translate(24, 238)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="384" height="42" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="42" rx="2" fill="#ffffff" />
        <text x="14" y="26" font-size="16">🧠</text>
        <text x="38" y="20" class="font-sans" font-size="12" font-weight="700" fill="#ffffff">AI / Machine Learning</text>
        <text x="38" y="34" class="font-sans" font-size="10.5" font-weight="500" fill="#cbd5e1">Model training, data exploration &amp; intelligent algorithms</text>
      </g>
      <g transform="translate(0, 48)">
        <rect x="0" y="0" width="384" height="42" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="42" rx="2" fill="#38bdf8" />
        <text x="14" y="26" font-size="16">💻</text>
        <text x="38" y="20" class="font-sans" font-size="12" font-weight="700" fill="#ffffff">Interactive UI &amp; Web Development</text>
        <text x="38" y="34" class="font-sans" font-size="10.5" font-weight="500" fill="#cbd5e1">Modern React interfaces, responsive design &amp; smooth UX</text>
      </g>
      <g transform="translate(0, 96)">
        <rect x="0" y="0" width="384" height="42" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="42" rx="2" fill="#c49d63" />
        <text x="14" y="26" font-size="16">🛡️</text>
        <text x="38" y="20" class="font-sans" font-size="12" font-weight="700" fill="#ffffff">Software Development &amp; Cybersecurity</text>
        <text x="38" y="34" class="font-sans" font-size="10.5" font-weight="500" fill="#cbd5e1">Robust architecture, Kali Linux, Nmap &amp; recon fundamentals</text>
      </g>
    </g>
  </g>

  <!-- Right Card: Hobbies -->
  <g transform="translate(458, 10)">
    <rect x="0" y="0" width="432" height="390" rx="18" fill="url(#suit-about-bg)" stroke="url(#suit-about-border)" stroke-width="1.5" />
    <rect x="0" y="0" width="432" height="390" rx="18" fill="url(#card-suit-weave)" />
    <text x="24" y="32" class="font-mono" font-size="11" font-weight="700" fill="#38bdf8" letter-spacing="1.5">// OFF THE CLOCK</text>
    <text x="24" y="56" class="font-sans" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Curious mind, continuous growth</text>

    <!-- Progress Bars -->
    <g transform="translate(24, 72)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="122" height="4" rx="2" fill="#05070c" />
        <rect x="0" y="0" height="4" rx="2" fill="#ffffff">
          <animate attributeName="width" dur="12s" repeatCount="indefinite" values="0;122;122;122;0" keyTimes="0;0.31;0.33;0.98;1" />
        </rect>
      </g>
      <g transform="translate(130, 0)">
        <rect x="0" y="0" width="122" height="4" rx="2" fill="#05070c" />
        <rect x="0" y="0" height="4" rx="2" fill="#38bdf8">
          <animate attributeName="width" dur="12s" repeatCount="indefinite" values="0;0;122;122;0" keyTimes="0;0.33;0.64;0.98;1" />
        </rect>
      </g>
      <g transform="translate(260, 0)">
        <rect x="0" y="0" width="122" height="4" rx="2" fill="#05070c" />
        <rect x="0" y="0" height="4" rx="2" fill="#c49d63">
          <animate attributeName="width" dur="12s" repeatCount="indefinite" values="0;0;122;0" keyTimes="0;0.66;0.98;1" />
        </rect>
      </g>
    </g>

    <g transform="translate(24, 92)">
      <g>
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="1;1;0;0;0;0" keyTimes="0;0.31;0.34;0.97;0.98;1" />
        <rect x="0" y="0" width="384" height="150" rx="14" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <text x="24" y="44" font-size="28">🎮</text>
        <text x="64" y="38" class="font-sans" font-size="18" font-weight="800" fill="#ffffff">Gaming</text>
        <text x="64" y="54" class="font-sans" font-size="11" font-weight="600" fill="#38bdf8">Competitive gaming &amp; experimenting with concepts</text>
        <text x="24" y="90" class="font-sans" font-size="12" font-weight="500" fill="#ffffff">Sharpening reaction time, game strategy, and analyzing</text>
        <text x="24" y="108" class="font-sans" font-size="12" font-weight="500" fill="#ffffff">game loops, mechanics &amp; real-time interactive physics.</text>
        <g transform="translate(24, 122)">
          <rect x="0" y="-12" width="76" height="20" rx="6" fill="#141c2c" stroke="#25354e" stroke-width="1" />
          <text x="8" y="2" class="font-mono" font-size="9" font-weight="700" fill="#ffffff">Competitive</text>
          <rect x="84" y="-12" width="86" height="20" rx="6" fill="#141c2c" stroke="#25354e" stroke-width="1" />
          <text x="92" y="2" class="font-mono" font-size="9" font-weight="700" fill="#ffffff">Strategy &amp; Logic</text>
        </g>
      </g>
      <g opacity="0">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.32;0.34;0.64;0.67;1" />
        <rect x="0" y="0" width="384" height="150" rx="14" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <text x="24" y="44" font-size="28">🔬</text>
        <text x="64" y="38" class="font-sans" font-size="18" font-weight="800" fill="#38bdf8">Technology</text>
        <text x="64" y="54" class="font-sans" font-size="11" font-weight="600" fill="#cbd5e1">Exploring new tech, AI models &amp; cybersecurity</text>
        <text x="24" y="90" class="font-sans" font-size="12" font-weight="500" fill="#ffffff">Diving into LLMs, neural networks, network reconnaissance</text>
        <text x="24" y="108" class="font-sans" font-size="12" font-weight="500" fill="#ffffff">and security defenses to build resilient modern software.</text>
        <g transform="translate(24, 122)">
          <rect x="0" y="-12" width="62" height="20" rx="6" fill="#141c2c" stroke="#25354e" stroke-width="1" />
          <text x="8" y="2" class="font-mono" font-size="9" font-weight="700" fill="#38bdf8">AI &amp; ML</text>
          <rect x="70" y="-12" width="84" height="20" rx="6" fill="#141c2c" stroke="#25354e" stroke-width="1" />
          <text x="78" y="2" class="font-mono" font-size="9" font-weight="700" fill="#38bdf8">Cybersecurity</text>
        </g>
      </g>
      <g opacity="0">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0" keyTimes="0;0.65;0.67;0.97;1" />
        <rect x="0" y="0" width="384" height="150" rx="14" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <text x="24" y="44" font-size="28">🎨</text>
        <text x="64" y="38" class="font-sans" font-size="18" font-weight="800" fill="#c49d63">Creative Design</text>
        <text x="64" y="54" class="font-sans" font-size="11" font-weight="600" fill="#cbd5e1">UI, visual concepts &amp; interactive experiences</text>
        <text x="24" y="90" class="font-sans" font-size="12" font-weight="500" fill="#ffffff">Designing luxury digital experiences, charcoal glass UI,</text>
        <text x="24" y="108" class="font-sans" font-size="12" font-weight="500" fill="#ffffff">micro-animations, and striking high-contrast aesthetics.</text>
        <g transform="translate(24, 122)">
          <rect x="0" y="-12" width="88" height="20" rx="6" fill="#141c2c" stroke="#25354e" stroke-width="1" />
          <text x="8" y="2" class="font-mono" font-size="9" font-weight="700" fill="#c49d63">Modern UI/UX</text>
        </g>
      </g>
    </g>

    <!-- Daily Rings -->
    <g transform="translate(24, 260)">
      <rect x="0" y="0" width="384" height="114" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
      <g transform="translate(68, 57)">
        <circle cx="0" cy="0" r="42" fill="none" stroke="#131a27" stroke-width="7" />
        <circle cx="0" cy="0" r="42" fill="none" stroke="url(#ring-white)" stroke-width="7" stroke-linecap="round" stroke-dasharray="264" class="ring-anim-1" transform="rotate(-90)" />
        <circle cx="0" cy="0" r="30" fill="none" stroke="#131a27" stroke-width="7" />
        <circle cx="0" cy="0" r="30" fill="none" stroke="url(#ring-sapphire)" stroke-width="7" stroke-linecap="round" stroke-dasharray="188" class="ring-anim-2" transform="rotate(-90)" />
        <circle cx="0" cy="0" r="18" fill="none" stroke="#131a27" stroke-width="7" />
        <circle cx="0" cy="0" r="18" fill="none" stroke="url(#ring-gold)" stroke-width="7" stroke-linecap="round" stroke-dasharray="113" class="ring-anim-3" transform="rotate(-90)" />
      </g>
      <g transform="translate(142, 22)">
        <text x="0" y="10" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" letter-spacing="1">DAILY FOCUS RINGS</text>
        <g transform="translate(0, 24)">
          <circle cx="5" cy="0" r="4" fill="#ffffff" />
          <text x="16" y="4" class="font-sans" font-size="11" font-weight="700" fill="#ffffff">Code &amp; Architecture</text>
          <text x="170" y="4" class="font-mono" font-size="10" font-weight="700" fill="#ffffff">92%</text>
        </g>
        <g transform="translate(0, 46)">
          <circle cx="5" cy="0" r="4" fill="#38bdf8" />
          <text x="16" y="4" class="font-sans" font-size="11" font-weight="700" fill="#ffffff">Research &amp; Security</text>
          <text x="170" y="4" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8">86%</text>
        </g>
        <g transform="translate(0, 68)">
          <circle cx="5" cy="0" r="4" fill="#c49d63" />
          <text x="16" y="4" class="font-sans" font-size="11" font-weight="700" fill="#ffffff">Design &amp; Creativity</text>
          <text x="170" y="4" class="font-mono" font-size="10" font-weight="700" fill="#c49d63">80%</text>
        </g>
      </g>
    </g>
  </g>
</svg>
'''
with open('about-life.svg', 'w', encoding='utf-8') as f:
    f.write(about_life_svg)

# ==================== 3. ROYAL-SCENE.SVG ====================
royal_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 420" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Playfair+Display:ital,wght@0,600;0,700;1,600&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * {{ box-sizing: border-box; }}
      .font-sans {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
      .font-serif {{ font-family: 'Playfair Display', Georgia, serif; }}
      .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
      @keyframes gold-shimmer {{ 0%, 100% {{ opacity: 0.8; }} 50% {{ opacity: 1; }} }}
      @keyframes star-twinkle {{ 0%, 100% {{ opacity: 0.2; transform: scale(0.8); }} 50% {{ opacity: 0.9; transform: scale(1.2); }} }}
      .shimmer {{ animation: gold-shimmer 4s ease-in-out infinite; }}
      .twinkle-1 {{ animation: star-twinkle 3s ease-in-out infinite; }}
      .twinkle-2 {{ animation: star-twinkle 4s ease-in-out infinite 1s; }}
      .twinkle-3 {{ animation: star-twinkle 3.5s ease-in-out infinite 1.8s; }}
    </style>

    <linearGradient id="suit-royal-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9" />
      <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="70%" stop-color="#1d4ed8" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#c49d63" stop-opacity="0.8" />
    </linearGradient>

    <linearGradient id="suit-royal-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141822" />
      <stop offset="45%" stop-color="#0f131b" />
      <stop offset="100%" stop-color="#0a0d13" />
    </linearGradient>

    <radialGradient id="royal-sapphire-glow" cx="28%" cy="52%" r="45%">
      <stop offset="0%" stop-color="#2563eb" stop-opacity="0.22" />
      <stop offset="100%" stop-color="#141822" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="royal-gold-glow" cx="72%" cy="52%" r="45%">
      <stop offset="0%" stop-color="#c49d63" stop-opacity="0.18" />
      <stop offset="100%" stop-color="#141822" stop-opacity="0" />
    </radialGradient>

    <pattern id="royal-suit-stars" width="40" height="40" patternUnits="userSpaceOnUse">
      <circle cx="10" cy="10" r="0.8" fill="#ffffff" fill-opacity="0.08" />
      <circle cx="30" cy="25" r="1.1" fill="#38bdf8" fill-opacity="0.12" />
      <circle cx="20" cy="35" r="0.7" fill="#ffffff" fill-opacity="0.06" />
    </pattern>
  </defs>

  <rect x="2" y="2" width="896" height="416" rx="20" fill="url(#suit-royal-bg)" stroke="url(#suit-royal-border)" stroke-width="1.6" />
  <rect x="2" y="2" width="896" height="416" rx="20" fill="url(#royal-sapphire-glow)" />
  <rect x="2" y="2" width="896" height="416" rx="20" fill="url(#royal-gold-glow)" />
  <rect x="2" y="2" width="896" height="416" rx="20" fill="url(#royal-suit-stars)" />

  <path d="M 120 416 L 120 190 Q 250 80 450 80 Q 650 80 780 190 L 780 416" fill="none" stroke="#38bdf8" stroke-opacity="0.16" stroke-width="1.5" stroke-dasharray="6,4" />
  <path d="M 160 416 L 160 210 Q 270 120 450 120 Q 630 120 740 210 L 740 416" fill="none" stroke="#c49d63" stroke-opacity="0.16" stroke-width="1" />

  <g class="twinkle-1" transform="translate(180, 68)">
    <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#ffffff" />
  </g>
  <g class="twinkle-2" transform="translate(710, 78)">
    <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#38bdf8" />
  </g>
  <g class="twinkle-3" transform="translate(450, 46)">
    <polygon points="0,-5 1.5,-1.5 5,0 1.5,1.5 0,5 -1.5,1.5 -5,0 -1.5,-1.5" fill="#fde68a" />
  </g>

  <g transform="translate(450, 40)" text-anchor="middle">
    <rect x="-120" y="-16" width="240" height="24" rx="12" fill="#070a10" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1.2" />
    <text x="0" y="0" class="font-mono" font-size="10.5" font-weight="700" fill="#38bdf8" letter-spacing="1.5">🎮 GAMING // AVATARS</text>
    <text x="0" y="32" class="font-serif" font-size="22" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Beyond the Code</text>
    <text x="0" y="52" class="font-sans" font-size="12.5" font-weight="500" fill="#cbd5e1">My in-game avatars: the Queen &amp; the Antler Companion</text>
  </g>

  <!-- Left: The Queen with full 14 frames -->
  <g transform="translate(60, 88)">
    <ellipse cx="170" cy="235" rx="120" ry="24" fill="#1d4ed8" fill-opacity="0.2" />
    <image href="data:image/png;base64,{throne_b64}" x="30" y="10" width="280" height="240" />

    <g transform="translate(50, 16)">
      <image href="data:image/png;base64,{q_frames[0]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="1;1;0;0;1;1;0;0" keyTimes="0;0.03;0.035;0.13;0.135;0.165;0.17;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[1]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;1;1;0;0" keyTimes="0;0.03;0.035;0.065;0.07;0.165;0.17;0.195;0.20;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[2]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;1;1;0;0" keyTimes="0;0.065;0.07;0.095;0.10;0.195;0.20;0.23;0.235;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[3]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;1;1;0;0" keyTimes="0;0.095;0.10;0.13;0.135;0.23;0.235;0.265;0.27;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[4]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.265;0.27;0.305;0.31;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[5]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.305;0.31;0.345;0.35;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[6]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.345;0.35;0.395;0.40;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[7]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.395;0.40;0.435;0.44;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[8]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.435;0.44;0.475;0.48;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[9]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.475;0.48;0.515;0.52;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[10]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.515;0.52;0.63;0.635;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[11]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.63;0.635;0.745;0.75;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[12]}" x="0" y="0" width="240" height="240">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.745;0.75;0.865;0.87;1" />
      </image>
      <image href="data:image/png;base64,{q_frames[13]}" x="0" y="0" width="240" height="240" opacity="1">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0" keyTimes="0;0.865;0.87;0.99;1" />
      </image>
    </g>

    <g transform="translate(68, 256)">
      <rect x="0" y="0" width="204" height="26" rx="13" fill="#070a10" stroke="#c49d63" stroke-width="1.2" />
      <text x="102" y="17" class="font-mono" font-size="10" font-weight="700" fill="#fde68a" text-anchor="middle" letter-spacing="1">👑 THE QUEEN // ARCHITECT</text>
    </g>
  </g>

  <!-- Center Crest -->
  <g transform="translate(450, 160)" text-anchor="middle">
    <circle cx="0" cy="20" r="28" fill="#070a10" stroke="#38bdf8" stroke-opacity="0.5" stroke-width="1.5" />
    <text x="0" y="27" font-size="20">✨</text>
    <line x1="0" y1="-30" x2="0" y2="-12" stroke="#38bdf8" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3,2" />
    <line x1="0" y1="52" x2="0" y2="76" stroke="#38bdf8" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3,2" />
    <text x="0" y="94" class="font-mono" font-size="9" font-weight="600" fill="#cbd5e1" letter-spacing="2">DUAL GUARDIANS</text>
  </g>

  <!-- Right: Antler Girl -->
  <g transform="translate(500, 88)">
    <ellipse cx="170" cy="235" rx="120" ry="24" fill="#38bdf8" fill-opacity="0.15" />
    <g transform="translate(55, 16)">
      <image href="data:image/png;base64,{ag_frames[0]}" x="0" y="0" width="230" height="230">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="1;1;0;0;0;0" keyTimes="0;0.28;0.29;0.98;0.99;1" />
      </image>
      <image href="data:image/png;base64,{ag_frames[1]}" x="0" y="0" width="230" height="230">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.28;0.29;0.41;0.42;1" />
      </image>
      <image href="data:image/png;base64,{ag_frames[2]}" x="0" y="0" width="230" height="230">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.41;0.42;0.62;0.63;1" />
      </image>
      <image href="data:image/png;base64,{ag_frames[3]}" x="0" y="0" width="230" height="230">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.62;0.63;0.81;0.82;1" />
      </image>
      <image href="data:image/png;base64,{ag_frames[5]}" x="0" y="0" width="230" height="230" opacity="1">
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1" keyTimes="0;0.81;0.82;1" />
      </image>
    </g>

    <g transform="translate(68, 256)">
      <rect x="0" y="0" width="204" height="26" rx="13" fill="#070a10" stroke="#38bdf8" stroke-width="1.2" />
      <text x="102" y="17" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="middle" letter-spacing="1">🦌 ANTLER GIRL &amp; KITTEN</text>
    </g>
  </g>

  <!-- Bottom Ribbon -->
  <g transform="translate(450, 386)" text-anchor="middle">
    <rect x="-240" y="-12" width="480" height="26" rx="13" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
    <text x="0" y="5" class="font-sans" font-size="11.5" font-weight="600" fill="#ffffff">
      <tspan fill="#c49d63">✦</tspan> Robust Logic &amp; Architecture &#160;&#160;|&#160;&#160; 
      <tspan fill="#38bdf8">✦</tspan> Cybersecurity Vigilance &#160;&#160;|&#160;&#160; 
      <tspan fill="#ffffff">✦</tspan> Modern Web Craft
    </text>
  </g>
</svg>
'''
with open('royal-scene.svg', 'w', encoding='utf-8') as f:
    f.write(royal_svg)

# ==================== 4. STACK.SVG (CHARCOAL & SAPPHIRE) ====================
stack_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 460" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * { box-sizing: border-box; }
      .font-sans { font-family: 'Plus Jakarta Sans', sans-serif; }
      .font-mono { font-family: 'JetBrains Mono', monospace; }
      @keyframes orbit-spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
      @keyframes orbit-spin-rev { from { transform: rotate(360deg); } to { transform: rotate(0deg); } }
      @keyframes core-pulse {
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 16px rgba(56, 189, 248, 0.6)); }
        50% { transform: scale(1.08); filter: drop-shadow(0 0 28px rgba(37, 99, 235, 0.9)); }
      }
      .orbit-path-1 { animation: orbit-spin 24s linear infinite; transform-origin: 450px 125px; }
      .orbit-path-2 { animation: orbit-spin-rev 32s linear infinite; transform-origin: 450px 125px; }
      .orbit-path-3 { animation: orbit-spin 40s linear infinite; transform-origin: 450px 125px; }
      .moon-orbit { animation: orbit-spin 6s linear infinite; transform-origin: 0px 0px; }
      .atom-center { animation: core-pulse 4s ease-in-out infinite; transform-origin: 450px 125px; }
    </style>

    <linearGradient id="suit-stack-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
      <stop offset="40%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="80%" stop-color="#1d4ed8" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#c49d63" stop-opacity="0.5" />
    </linearGradient>

    <linearGradient id="suit-stack-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141822" />
      <stop offset="45%" stop-color="#0f131b" />
      <stop offset="100%" stop-color="#0a0d13" />
    </linearGradient>

    <radialGradient id="stack-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#1d4ed8" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <pattern id="stack-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#ffffff" fill-opacity="0.04" />
    </pattern>
  </defs>

  <rect x="2" y="2" width="896" height="456" rx="20" fill="url(#suit-stack-bg)" stroke="url(#suit-stack-border)" stroke-width="1.6" />
  <rect x="2" y="2" width="896" height="456" rx="20" fill="url(#stack-dots)" />

  <g transform="translate(36, 32)">
    <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" fill="#38bdf8" letter-spacing="1.5">// TECH ORBIT &amp; CAPABILITIES</text>
    <text x="0" y="22" class="font-sans" font-size="19" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Interactive Planetary Tech Stack</text>
  </g>

  <g transform="translate(710, 32)">
    <rect x="0" y="-14" width="154" height="24" rx="12" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
    <circle cx="14" cy="-2" r="3.5" fill="#38bdf8" />
    <text x="26" y="2" class="font-mono" font-size="9.5" font-weight="600" fill="#ffffff">ATOMIC ORBITS</text>
  </g>

  <!-- Orbits -->
  <g transform="translate(0, 5)">
    <circle cx="450" cy="125" r="110" fill="url(#stack-core-glow)" />

    <ellipse cx="450" cy="125" rx="160" ry="58" fill="none" stroke="#38bdf8" stroke-opacity="0.25" stroke-width="1.2" stroke-dasharray="4,4" transform="rotate(-12 450 125)" />
    <ellipse cx="450" cy="125" rx="240" ry="68" fill="none" stroke="#ffffff" stroke-opacity="0.2" stroke-width="1.2" stroke-dasharray="5,4" transform="rotate(16 450 125)" />
    <ellipse cx="450" cy="125" rx="330" ry="82" fill="none" stroke="#c49d63" stroke-opacity="0.2" stroke-width="1.2" stroke-dasharray="6,4" transform="rotate(-22 450 125)" />

    <g class="orbit-path-1">
      <g transform="translate(605, 120)">
        <rect x="-16" y="-16" width="32" height="32" rx="8" fill="#070a10" stroke="#38bdf8" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="11" font-weight="700" fill="#38bdf8" text-anchor="middle">TS</text>
      </g>
      <g transform="translate(370, 75)">
        <rect x="-16" y="-16" width="32" height="32" rx="8" fill="#070a10" stroke="#ffffff" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle">NODE</text>
      </g>
      <g transform="translate(370, 175)">
        <rect x="-16" y="-16" width="32" height="32" rx="8" fill="#070a10" stroke="#38bdf8" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="9" font-weight="700" fill="#38bdf8" text-anchor="middle">API</text>
      </g>
    </g>

    <g class="orbit-path-2">
      <g transform="translate(685, 125)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#070a10" stroke="#c49d63" stroke-width="1.2" />
        <text x="0" y="5" class="font-mono" font-size="11" font-weight="700" fill="#fde68a" text-anchor="middle">PY</text>
      </g>
      <g transform="translate(215, 125)">
        <rect x="-18" y="-18" width="36" height="36" rx="8" fill="#070a10" stroke="#ffffff" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="9.5" font-weight="700" fill="#ffffff" text-anchor="middle">SQL</text>
      </g>
      <g transform="translate(450, 58)">
        <rect x="-16" y="-16" width="32" height="32" rx="8" fill="#070a10" stroke="#38bdf8" stroke-width="1.2" />
        <polygon points="0,-8 7,6 -7,6" fill="#38bdf8" />
      </g>
    </g>

    <g class="orbit-path-3">
      <g transform="translate(775, 125)">
        <rect x="-20" y="-18" width="40" height="36" rx="8" fill="#070a10" stroke="#38bdf8" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="9" font-weight="700" fill="#38bdf8" text-anchor="middle">KALI</text>
      </g>
      <g transform="translate(125, 125)">
        <rect x="-20" y="-18" width="40" height="36" rx="8" fill="#070a10" stroke="#ffffff" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="9" font-weight="700" fill="#ffffff" text-anchor="middle">NMAP</text>
      </g>
      <g transform="translate(450, 42)">
        <rect x="-16" y="-16" width="32" height="32" rx="8" fill="#070a10" stroke="#c49d63" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="9.5" font-weight="700" fill="#fde68a" text-anchor="middle">GIT</text>
      </g>
      <g transform="translate(450, 208)">
        <rect x="-16" y="-16" width="32" height="32" rx="8" fill="#070a10" stroke="#ffffff" stroke-width="1.2" />
        <text x="0" y="4" class="font-mono" font-size="8.5" font-weight="700" fill="#ffffff" text-anchor="middle">STUDIO</text>
      </g>
    </g>

    <g class="atom-center" transform="translate(450, 125)">
      <circle cx="0" cy="0" r="32" fill="#070a10" stroke="#38bdf8" stroke-width="2" />
      <ellipse cx="0" cy="0" rx="26" ry="10" fill="none" stroke="#38bdf8" stroke-width="1.5" transform="rotate(30)" />
      <ellipse cx="0" cy="0" rx="26" ry="10" fill="none" stroke="#38bdf8" stroke-width="1.5" transform="rotate(90)" />
      <ellipse cx="0" cy="0" rx="26" ry="10" fill="none" stroke="#38bdf8" stroke-width="1.5" transform="rotate(150)" />
      <circle cx="0" cy="0" r="8" fill="#c49d63" />
      <text x="0" y="2.5" class="font-mono" font-size="7" font-weight="800" fill="#000000" text-anchor="middle">JS</text>

      <g class="moon-orbit">
        <g transform="translate(42, 0)">
          <circle cx="0" cy="0" r="7" fill="#070a10" stroke="#ffffff" stroke-width="1" />
          <text x="0" y="2.5" class="font-mono" font-size="6" font-weight="700" fill="#ffffff" text-anchor="middle">H5</text>
        </g>
        <g transform="translate(-42, 0)">
          <circle cx="0" cy="0" r="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
          <text x="0" y="2.5" class="font-mono" font-size="6" font-weight="700" fill="#38bdf8" text-anchor="middle">CS</text>
        </g>
      </g>
    </g>
  </g>

  <!-- Chips -->
  <g transform="translate(36, 246)">
    <g transform="translate(0, 0)">
      <text x="0" y="14" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" letter-spacing="1">FRONTEND</text>
      <g transform="translate(0, 24)">
        <rect x="0" y="0" width="76" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="38" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">⚛️ React</text>
        <rect x="84" y="0" width="102" height="26" rx="7" fill="#070a10" stroke="#c49d63" stroke-width="1" />
        <text x="135" y="17" class="font-sans" font-size="11" font-weight="700" fill="#fde68a" text-anchor="middle">⚡ JavaScript</text>
        <rect x="194" y="0" width="104" height="26" rx="7" fill="#070a10" stroke="#ffffff" stroke-width="1" />
        <text x="246" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">📘 TypeScript</text>
        <rect x="306" y="0" width="76" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="344" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🌐 HTML5</text>
        <rect x="390" y="0" width="72" height="26" rx="7" fill="#070a10" stroke="#ffffff" stroke-width="1" />
        <text x="426" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🎨 CSS3</text>
      </g>
    </g>

    <g transform="translate(488, 0)">
      <text x="0" y="14" class="font-mono" font-size="10" font-weight="700" fill="#ffffff" letter-spacing="1">BACKEND &amp; CLOUD</text>
      <g transform="translate(0, 24)">
        <rect x="0" y="0" width="82" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="41" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🟢 Node.js</text>
        <rect x="90" y="0" width="82" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="131" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">⚡ FastAPI</text>
        <rect x="180" y="0" width="80" height="26" rx="7" fill="#070a10" stroke="#c49d63" stroke-width="1" />
        <text x="220" y="17" class="font-sans" font-size="11" font-weight="700" fill="#fde68a" text-anchor="middle">🐍 Python</text>
        <rect x="268" y="0" width="62" height="26" rx="7" fill="#070a10" stroke="#ffffff" stroke-width="1" />
        <text x="299" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🗄️ SQL</text>
      </g>
    </g>

    <g transform="translate(0, 84)">
      <text x="0" y="14" class="font-mono" font-size="10" font-weight="700" fill="#c49d63" letter-spacing="1">AI &amp; MACHINE LEARNING</text>
      <g transform="translate(0, 24)">
        <rect x="0" y="0" width="84" height="26" rx="7" fill="#070a10" stroke="#c49d63" stroke-width="1" />
        <text x="42" y="17" class="font-sans" font-size="11" font-weight="700" fill="#fde68a" text-anchor="middle">🐍 Python</text>
        <rect x="92" y="0" width="144" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="164" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🧠 Machine Learning</text>
        <rect x="244" y="0" width="108" height="26" rx="7" fill="#070a10" stroke="#ffffff" stroke-width="1" />
        <text x="298" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">📊 Data Models</text>
      </g>
    </g>

    <g transform="translate(410, 84)">
      <text x="0" y="14" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" letter-spacing="1">CYBERSECURITY &amp; TOOLS</text>
      <g transform="translate(0, 24)">
        <rect x="0" y="0" width="98" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="49" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🐉 Kali Linux</text>
        <rect x="106" y="0" width="76" height="26" rx="7" fill="#070a10" stroke="#ffffff" stroke-width="1" />
        <text x="144" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">📡 Nmap</text>
        <rect x="190" y="0" width="118" height="26" rx="7" fill="#070a10" stroke="#38bdf8" stroke-width="1" />
        <text x="249" y="17" class="font-sans" font-size="11" font-weight="700" fill="#ffffff" text-anchor="middle">🛡️ Recon Basics</text>
        <rect x="316" y="0" width="58" height="26" rx="7" fill="#070a10" stroke="#c49d63" stroke-width="1" />
        <text x="345" y="17" class="font-sans" font-size="11" font-weight="700" fill="#fde68a" text-anchor="middle">🐙 Git</text>
      </g>
    </g>
  </g>
</svg>
'''
with open('stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)

# ==================== 5. ID-DASHBOARD.SVG (CHARCOAL & SAPPHIRE) ====================
id_dashboard_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 410" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * { box-sizing: border-box; }
      .font-sans { font-family: 'Plus Jakarta Sans', sans-serif; }
      .font-mono { font-family: 'JetBrains Mono', monospace; }
      @keyframes pendulum-swing {
        0% { transform: rotate(0deg); }
        20% { transform: rotate(3.2deg); }
        40% { transform: rotate(-2.8deg); }
        60% { transform: rotate(1.8deg); }
        80% { transform: rotate(-1deg); }
        100% { transform: rotate(0deg); }
      }
      @keyframes holo-sweep {
        0% { transform: translateX(-180px) rotate(25deg); opacity: 0; }
        30% { opacity: 0.5; }
        60% { opacity: 0.5; }
        100% { transform: translateX(360px) rotate(25deg); opacity: 0; }
      }
      @keyframes travel-light {
        0% { stroke-dashoffset: 800; }
        100% { stroke-dashoffset: 0; }
      }
      @keyframes live-radar {
        0% { transform: scale(1); opacity: 0.9; }
        100% { transform: scale(2.6); opacity: 0; }
      }
      .pendulum-group { animation: pendulum-swing 7s ease-in-out infinite; transform-origin: 190px 0px; }
      .holo-beam { animation: holo-sweep 5s ease-in-out infinite; }
      .light-border { stroke-dasharray: 100 700; animation: travel-light 4s linear infinite; }
      .radar-pulse { animation: live-radar 2s ease-out infinite; transform-origin: center; }
    </style>

    <linearGradient id="suit-id-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
      <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="70%" stop-color="#1d4ed8" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#c49d63" stop-opacity="0.6" />
    </linearGradient>

    <linearGradient id="suit-id-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141822" />
      <stop offset="45%" stop-color="#0f131b" />
      <stop offset="100%" stop-color="#0a0d13" />
    </linearGradient>

    <linearGradient id="holo-foil" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="30%" stop-color="#38bdf8" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.4" />
      <stop offset="70%" stop-color="#2563eb" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="gold-chip-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#c49d63" />
      <stop offset="100%" stop-color="#854d0e" />
    </linearGradient>

    <linearGradient id="bar-fill-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#1d4ed8" />
    </linearGradient>

    <pattern id="dash-suit-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#ffffff" fill-opacity="0.04" />
    </pattern>

    <clipPath id="badge-clip">
      <rect x="0" y="0" width="260" height="300" rx="14" />
    </clipPath>
  </defs>

  <rect x="2" y="2" width="896" height="406" rx="20" fill="url(#suit-id-bg)" stroke="url(#suit-id-border)" stroke-width="1.6" />
  <rect x="2" y="2" width="896" height="406" rx="20" fill="url(#dash-suit-dots)" />

  <!-- Lanyard Badge -->
  <g class="pendulum-group">
    <g transform="translate(162, 0)">
      <path d="M 12 0 L 20 48 L 36 48 L 44 0 Z" fill="#070a10" stroke="#25354e" stroke-width="1" />
      <text x="28" y="26" class="font-mono" font-size="7" font-weight="700" fill="#38bdf8" text-anchor="middle" letter-spacing="1">HARSH-2959</text>
      <text x="28" y="38" class="font-mono" font-size="6" font-weight="600" fill="#ffffff" text-anchor="middle">ENGG</text>
      <circle cx="28" cy="52" r="8" fill="none" stroke="#cbd5e1" stroke-width="2.5" />
      <rect x="23" y="56" width="10" height="14" rx="2" fill="#ffffff" stroke="#64748b" stroke-width="0.5" />
      <polygon points="21,70 35,70 32,77 24,77" fill="#94a3b8" />
    </g>

    <g transform="translate(60, 78)">
      <rect x="4" y="4" width="260" height="300" rx="14" fill="#000000" fill-opacity="0.5" />
      <rect x="0" y="0" width="260" height="300" rx="14" fill="#070a10" stroke="#25354e" stroke-width="1.4" />
      <rect x="0" y="0" width="260" height="300" rx="14" fill="none" stroke="#38bdf8" stroke-width="2" class="light-border" />

      <g clip-path="url(#badge-clip)">
        <rect x="-80" y="-40" width="100" height="380" fill="url(#holo-foil)" class="holo-beam" />
      </g>

      <rect x="105" y="10" width="50" height="7" rx="3.5" fill="#020305" stroke="#334155" stroke-width="0.8" />
      <text x="130" y="36" class="font-mono" font-size="8.5" font-weight="700" fill="#38bdf8" text-anchor="middle" letter-spacing="1.5">VIVA INSTITUTE OF TECHNOLOGY</text>
      <text x="130" y="48" class="font-sans" font-size="7.5" font-weight="600" fill="#ffffff" text-anchor="middle">UNIVERSITY OF MUMBAI</text>

      <g transform="translate(20, 60)">
        <rect x="0" y="0" width="70" height="82" rx="8" fill="#131a27" stroke="#38bdf8" stroke-width="1.2" />
        <circle cx="35" cy="32" r="16" fill="#38bdf8" fill-opacity="0.25" stroke="#38bdf8" stroke-width="1.2" />
        <circle cx="35" cy="28" r="8" fill="#ffffff" />
        <path d="M 23 44 Q 35 38 47 44" fill="none" stroke="#ffffff" stroke-width="2" />
        <line x1="28" y1="28" x2="42" y2="28" stroke="#38bdf8" stroke-width="1.2" />
        <rect x="4" y="66" width="62" height="12" rx="3" fill="#070a10" />
        <text x="35" y="75" class="font-mono" font-size="7" font-weight="700" fill="#ffffff" text-anchor="middle">DEV // 2959</text>
      </g>

      <g transform="translate(100, 72)">
        <text x="0" y="0" class="font-mono" font-size="7" font-weight="600" fill="#94a3b8">STUDENT &amp; DEVELOPER</text>
        <text x="0" y="16" class="font-sans" font-size="13" font-weight="800" fill="#ffffff">Harsh Patil</text>
        <text x="0" y="32" class="font-mono" font-size="8" font-weight="700" fill="#38bdf8">ID: HP-2029-BE</text>
        <circle cx="4" cy="46" r="3" fill="#38bdf8" />
        <text x="12" y="49" class="font-sans" font-size="8.5" font-weight="600" fill="#ffffff">Active / Enrolled</text>
      </g>

      <g transform="translate(20, 156)">
        <rect x="0" y="0" width="36" height="26" rx="4" fill="url(#gold-chip-grad)" stroke="#c49d63" stroke-width="0.8" />
        <line x1="18" y1="0" x2="18" y2="26" stroke="#854d0e" stroke-width="0.8" />
        <line x1="0" y1="13" x2="36" y2="13" stroke="#854d0e" stroke-width="0.8" />
        <rect x="11" y="7" width="14" height="12" rx="2" fill="none" stroke="#713f12" stroke-width="0.8" />
      </g>

      <g transform="translate(68, 156)">
        <rect x="0" y="0" width="172" height="26" rx="6" fill="#131a27" stroke="#38bdf8" stroke-width="1" />
        <text x="10" y="17" font-size="12">🛡️</text>
        <text x="28" y="17" class="font-mono" font-size="8" font-weight="700" fill="#ffffff">SECURE VERIFIED IDENTITY</text>
      </g>

      <g transform="translate(20, 196)">
        <text x="0" y="0" class="font-mono" font-size="7.5" font-weight="600" fill="#94a3b8">PROGRAM OF STUDY</text>
        <text x="0" y="14" class="font-sans" font-size="10.5" font-weight="700" fill="#ffffff">B.E. Computer Engineering</text>
        <text x="0" y="27" class="font-mono" font-size="8" fill="#38bdf8">Expected Graduation: 2029</text>
      </g>

      <g transform="translate(20, 242)">
        <line x1="0" y1="0" x2="220" y2="0" stroke="#1c2434" stroke-width="0.8" />
        <g transform="translate(0, 10)">
          <line x1="2" y1="0" x2="2" y2="22" stroke="#ffffff" stroke-width="2" />
          <line x1="7" y1="0" x2="7" y2="22" stroke="#ffffff" stroke-width="1" />
          <line x1="11" y1="0" x2="11" y2="22" stroke="#ffffff" stroke-width="3" />
          <line x1="17" y1="0" x2="17" y2="22" stroke="#ffffff" stroke-width="1.5" />
          <line x1="22" y1="0" x2="22" y2="22" stroke="#ffffff" stroke-width="2" />
          <line x1="28" y1="0" x2="28" y2="22" stroke="#ffffff" stroke-width="1" />
          <line x1="33" y1="0" x2="33" y2="22" stroke="#ffffff" stroke-width="2.5" />
          <line x1="38" y1="0" x2="38" y2="22" stroke="#ffffff" stroke-width="1" />
          <line x1="43" y1="0" x2="43" y2="22" stroke="#ffffff" stroke-width="3" />
          <line x1="50" y1="0" x2="50" y2="22" stroke="#ffffff" stroke-width="1.5" />
          <line x1="56" y1="0" x2="56" y2="22" stroke="#ffffff" stroke-width="2" />
          <line x1="62" y1="0" x2="62" y2="22" stroke="#ffffff" stroke-width="1" />
          <line x1="68" y1="0" x2="68" y2="22" stroke="#ffffff" stroke-width="2.5" />
          <line x1="74" y1="0" x2="74" y2="22" stroke="#ffffff" stroke-width="1.5" />
          <line x1="80" y1="0" x2="80" y2="22" stroke="#ffffff" stroke-width="3" />
        </g>
        <text x="220" y="24" class="font-mono" font-size="8" font-weight="600" fill="#cbd5e1" text-anchor="end">#2959-HP-2029</text>
      </g>
    </g>
  </g>

  <!-- Right Dashboard -->
  <g transform="translate(360, 28)">
    <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" fill="#38bdf8" letter-spacing="1.5">// ACADEMICS &amp; VELOCITY</text>
    <text x="0" y="22" class="font-sans" font-size="19" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Live Milestone Dashboard</text>

    <!-- KPI Tiles -->
    <g transform="translate(0, 42)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="246" height="82" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="82" rx="2" fill="#38bdf8" />
        <text x="16" y="22" class="font-mono" font-size="9" font-weight="700" fill="#38bdf8" letter-spacing="1">CURRENT DEGREE</text>
        <text x="16" y="48" class="font-sans" font-size="22" font-weight="800" fill="#ffffff">B.E. Comp</text>
        <text x="140" y="48" class="font-mono" font-size="11" font-weight="700" fill="#38bdf8">Exp 2029</text>
        <text x="16" y="68" class="font-sans" font-size="10.5" font-weight="500" fill="#cbd5e1">Viva Inst of Tech · Mumbai Univ</text>
      </g>

      <g transform="translate(258, 0)">
        <rect x="0" y="0" width="246" height="82" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="82" rx="2" fill="#c49d63" />
        <text x="16" y="22" class="font-mono" font-size="9" font-weight="700" fill="#c49d63" letter-spacing="1">DIPLOMA MERIT</text>
        <text x="16" y="48" class="font-sans" font-size="24" font-weight="800" fill="#ffffff">82.29%</text>
        <text x="120" y="48" class="font-mono" font-size="10" font-weight="700" fill="#fde68a">DISTINCTION</text>
        <text x="16" y="68" class="font-sans" font-size="10.5" font-weight="500" fill="#cbd5e1">Diploma in Computer Engineering</text>
      </g>
    </g>

    <!-- Velocity Bar Chart -->
    <g transform="translate(0, 140)">
      <rect x="0" y="0" width="504" height="130" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
      <text x="16" y="22" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" letter-spacing="1">DOMAIN FOCUS VELOCITY</text>

      <g transform="translate(16, 36)">
        <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="600" fill="#ffffff">Interactive UI &amp; Web Apps</text>
        <text x="472" y="10" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="end">94%</text>
        <rect x="0" y="14" width="472" height="6" rx="3" fill="#131a27" />
        <rect x="0" y="14" width="443" height="6" rx="3" fill="url(#bar-fill-grad)" />
      </g>

      <g transform="translate(16, 62)">
        <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="600" fill="#ffffff">AI / Machine Learning Exploration</text>
        <text x="472" y="10" class="font-mono" font-size="10" font-weight="700" fill="#38bdf8" text-anchor="end">88%</text>
        <rect x="0" y="14" width="472" height="6" rx="3" fill="#131a27" />
        <rect x="0" y="14" width="415" height="6" rx="3" fill="url(#bar-fill-grad)" />
      </g>

      <g transform="translate(16, 88)">
        <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="600" fill="#ffffff">Cybersecurity &amp; Network Recon</text>
        <text x="472" y="10" class="font-mono" font-size="10" font-weight="700" fill="#c49d63" text-anchor="end">85%</text>
        <rect x="0" y="14" width="472" height="6" rx="3" fill="#131a27" />
        <rect x="0" y="14" width="401" height="6" rx="3" fill="url(#bar-fill-grad)" />
      </g>
    </g>

    <!-- NOW Panel -->
    <g transform="translate(0, 286)">
      <rect x="0" y="0" width="504" height="66" rx="12" fill="#070a10" stroke="#38bdf8" stroke-width="1.2" />
      <g transform="translate(24, 33)">
        <circle cx="0" cy="0" r="10" fill="#38bdf8" fill-opacity="0.3" class="radar-pulse" />
        <circle cx="0" cy="0" r="5" fill="#38bdf8" />
      </g>
      <g transform="translate(46, 22)">
        <text x="0" y="0" class="font-mono" font-size="9" font-weight="700" fill="#38bdf8" letter-spacing="1.5">CURRENT FOCUS // LIVE NOW</text>
        <text x="0" y="20" class="font-mono" font-size="12" font-weight="800" fill="#ffffff" letter-spacing="0.5">
          EXPLORING AI · WEB DEVELOPMENT · CYBERSECURITY
        </text>
      </g>
    </g>
  </g>
</svg>
'''
with open('id-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(id_dashboard_svg)

# ==================== 6. CONNECT.SVG (CHARCOAL & SAPPHIRE) ====================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 270" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * {{ box-sizing: border-box; }}
      a {{ cursor: pointer; }}
      .font-sans {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
      .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
      @keyframes nudge-arrow {{ 0%, 100% {{ transform: translateX(0px); }} 50% {{ transform: translateX(6px); }} }}
      @keyframes sapphire-flicker {{
        0%, 100% {{ filter: drop-shadow(0 0 10px #38bdf8) drop-shadow(0 0 22px rgba(37, 99, 235, 0.7)); }}
        50% {{ filter: drop-shadow(0 0 16px #60a5fa) drop-shadow(0 0 32px rgba(56, 189, 248, 0.9)); }}
      }}
      @keyframes sparkle-pulse {{
        0%, 100% {{ transform: scale(0.9) rotate(0deg); opacity: 0.6; }}
        50% {{ transform: scale(1.2) rotate(18deg); opacity: 1; }}
      }}
      .nudge {{ animation: nudge-arrow 1.6s ease-in-out infinite; }}
      .neon-glow {{ animation: sapphire-flicker 4s ease-in-out infinite; }}
      .sparkle {{ animation: sparkle-pulse 2.5s ease-in-out infinite; transform-origin: center; }}
    </style>

    <linearGradient id="suit-connect-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.8" />
      <stop offset="35%" stop-color="#38bdf8" stop-opacity="0.8" />
      <stop offset="70%" stop-color="#1d4ed8" stop-opacity="0.6" />
      <stop offset="100%" stop-color="#c49d63" stop-opacity="0.6" />
    </linearGradient>

    <linearGradient id="suit-connect-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#141822" />
      <stop offset="45%" stop-color="#0f131b" />
      <stop offset="100%" stop-color="#0a0d13" />
    </linearGradient>

    <linearGradient id="neon-sapphire-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="50%" stop-color="#7dd3fc" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>

    <pattern id="connect-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#ffffff" fill-opacity="0.04" />
    </pattern>
  </defs>

  <rect x="2" y="2" width="896" height="266" rx="20" fill="url(#suit-connect-bg)" stroke="url(#suit-connect-border)" stroke-width="1.6" />
  <rect x="2" y="2" width="896" height="266" rx="20" fill="url(#connect-dots)" />

  <!-- Left: Character & Neon Sign -->
  <g transform="translate(36, 25)">
    <ellipse cx="140" cy="180" rx="90" ry="24" fill="#1d4ed8" fill-opacity="0.2" />
    <g transform="translate(10, 10)">
      <image href="data:image/png;base64,{v_connect}" x="0" y="0" width="195" height="195" />
    </g>

    <g transform="translate(180, 50)" class="neon-glow">
      <rect x="0" y="0" width="180" height="48" rx="14" fill="#070a10" stroke="#38bdf8" stroke-width="1.5" />
      <text x="90" y="31" class="font-sans" font-size="19" font-weight="800" fill="url(#neon-sapphire-grad)" text-anchor="middle" letter-spacing="1">Harsh-2959</text>
    </g>

    <g class="sparkle" transform="translate(170, 40)">
      <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#ffffff" />
    </g>
    <g class="sparkle" transform="translate(368, 42)">
      <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#38bdf8" />
    </g>
    <g class="sparkle" transform="translate(360, 96)">
      <text font-size="12">✨</text>
    </g>

    <g transform="translate(180, 114)">
      <rect x="0" y="0" width="180" height="24" rx="8" fill="#070a10" stroke="#25354e" stroke-width="1" />
      <text x="90" y="16" class="font-mono" font-size="9.5" font-weight="700" fill="#38bdf8" text-anchor="middle">LET'S CONNECT ⚡</text>
    </g>
  </g>

  <!-- Right: Link Cards -->
  <g transform="translate(420, 26)">
    <text x="0" y="10" class="font-mono" font-size="10.5" font-weight="700" fill="#38bdf8" letter-spacing="1.5">// REACH OUT &amp; EXPLORE</text>
    <text x="0" y="28" class="font-sans" font-size="17" font-weight="800" fill="#ffffff" letter-spacing="-0.3">Official Profiles &amp; Networks</text>

    <!-- GitHub -->
    <a href="https://github.com/Harsh-2959" xlink:href="https://github.com/Harsh-2959" target="_blank" rel="noopener noreferrer">
      <g transform="translate(0, 42)">
        <rect x="0" y="0" width="440" height="52" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="52" rx="2" fill="#ffffff" />
        <g transform="translate(18, 14)">
          <circle cx="12" cy="12" r="14" fill="#131a27" />
          <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="#ffffff" transform="scale(0.8) translate(3, 3)" />
        </g>
        <text x="56" y="24" class="font-sans" font-size="13" font-weight="700" fill="#ffffff">GitHub</text>
        <text x="56" y="40" class="font-mono" font-size="10.5" fill="#38bdf8">github.com/Harsh-2959</text>
        <g class="nudge" transform="translate(404, 30)">
          <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </g>
    </a>

    <!-- LinkedIn -->
    <a href="https://linkedin.com/in/harshpatil2959" xlink:href="https://linkedin.com/in/harshpatil2959" target="_blank" rel="noopener noreferrer">
      <g transform="translate(0, 104)">
        <rect x="0" y="0" width="440" height="52" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="52" rx="2" fill="#38bdf8" />
        <g transform="translate(18, 14)">
          <rect x="0" y="0" width="24" height="24" rx="5" fill="#0077b5" />
          <text x="12" y="17" class="font-sans" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">in</text>
        </g>
        <text x="56" y="24" class="font-sans" font-size="13" font-weight="700" fill="#ffffff">LinkedIn</text>
        <text x="56" y="40" class="font-mono" font-size="10.5" fill="#38bdf8">linkedin.com/in/harshpatil2959</text>
        <g class="nudge" transform="translate(404, 30)">
          <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" fill="none" stroke="#38bdf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </g>
    </a>

    <!-- University -->
    <g transform="translate(0, 166)">
      <rect x="0" y="0" width="440" height="52" rx="12" fill="#070a10" stroke="#25354e" stroke-width="1.2" />
      <rect x="0" y="0" width="4" height="52" rx="2" fill="#c49d63" />
      <g transform="translate(18, 14)">
        <rect x="0" y="0" width="24" height="24" rx="5" fill="#1c160e" />
        <text x="12" y="17" font-size="14" text-anchor="middle">🎓</text>
      </g>
      <text x="56" y="24" class="font-sans" font-size="13" font-weight="700" fill="#ffffff">Viva Institute of Technology</text>
      <text x="56" y="40" class="font-mono" font-size="10.5" fill="#fde68a">Open to Collaborations &amp; Projects</text>
      <g transform="translate(320, 16)">
        <rect x="0" y="0" width="96" height="20" rx="10" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="0.8" />
        <circle cx="10" cy="10" r="3" fill="#38bdf8" />
        <text x="18" y="13.5" class="font-mono" font-size="8" font-weight="700" fill="#ffffff">COLLAB</text>
      </g>
    </g>
  </g>
</svg>
'''
with open('connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)

print("ALL 6 SVGs permanently generated in Final Tailored Charcoal & Sapphire!")
