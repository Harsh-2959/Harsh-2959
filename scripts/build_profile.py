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

print("1. Extracting character frames...")
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

# Read and namespace signature.svg components for embedding in hero.svg
with open('signature.svg', 'r', encoding='utf-8') as f:
    sig_raw = f.read()

sig_defs = sig_raw[sig_raw.find('<defs>')+6:sig_raw.find('</defs>')]
sig_defs = sig_defs.replace('id="ink"', 'id="sig-ink"')
sig_defs = sig_defs.replace('id="write"', 'id="sig-write"')
sig_defs = sig_defs.replace('id="g"', 'id="sig-g"')
sig_defs = sig_defs.replace('url(#write)', 'url(#sig-write)')
sig_defs = sig_defs.replace('url(#ink)', 'url(#sig-ink)')
sig_defs = sig_defs.replace('url(#g)', 'url(#sig-g)')
sig_defs = sig_defs.replace('@keyframes k', '@keyframes sig-k')
sig_defs = sig_defs.replace('animation:k', 'animation:sig-k')
sig_defs = sig_defs.replace('.p', '.sig-p')
sig_defs = sig_defs.replace('class="p', 'class="sig-p')
sig_defs = sig_defs.replace('@keyframes scene', '@keyframes sig-scene')
sig_defs = sig_defs.replace('animation:scene', 'animation:sig-scene')
sig_defs = sig_defs.replace('.scene', '.sig-scene')

print("2. Generating Deep Atlas Navy Suite...")

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
      @keyframes float-bubble {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-4px); }}
      }}
      .pulse-pill {{ animation: pulse-dot 2s ease-in-out infinite; }}
      .rec-dot {{ animation: rec-blink 1.2s ease-in-out infinite; }}
      .speech-bubble {{ animation: float-bubble 3s ease-in-out infinite; }}
    </style>

    <clipPath id="rec-scrubber-clip">
      <rect x="0" y="14" width="288" height="2" rx="1" />
    </clipPath>

    {sig_defs}

    <linearGradient id="panel-navy-grad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#162A7E" />
      <stop offset="100%" stop-color="#122268" />
    </linearGradient>

    <pattern id="navy-suit-weave" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#E8E0D2" fill-opacity="0.04" />
    </pattern>
  </defs>

  <!-- Solid Deep Atlas Navy Rounded Card (GitHub Light & Dark Theme Safe) -->
  <rect x="2" y="2" width="896" height="371" rx="20" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
  <rect x="2" y="2" width="896" height="371" rx="20" fill="url(#navy-suit-weave)" />

  <!-- Top Tags -->
  <g transform="translate(36, 30)">
    <polygon points="0,-7 2,-2 7,0 2,2 0,7 -2,2 -7,0 -2,-2" fill="#B89A5A" />
    <text x="14" y="4" class="font-mono" font-size="11" font-weight="700" fill="#E8E0D2" letter-spacing="1.5">HARSH</text>
    <text x="68" y="4" class="font-mono" font-size="11" fill="rgba(232,224,210,0.4)">/</text>
    <text x="80" y="4" class="font-mono" font-size="11" fill="rgba(232,224,210,0.7)">WELCOME TO MY SPACE</text>
  </g>

  <!-- Open to Collabs Pill -->
  <g transform="translate(36, 52)">
    <rect x="0" y="0" width="168" height="26" rx="13" fill="#162A7E" stroke="rgba(232,224,210,0.2)" stroke-width="1" />
    <circle cx="16" cy="13" r="4" fill="#B89A5A" class="pulse-pill" />
    <text x="27" y="17" class="font-mono" font-size="10" font-weight="700" fill="#E8E0D2" letter-spacing="1">OPEN TO COLLABS</text>
  </g>

  <!-- Animated Calligraphy Signature in freed space (Harsh Patil + Underline sweep) -->
  <g transform="translate(36, 76) scale(0.40)">
    <g class="sig-scene">
      <g mask="url(#sig-write)">
        <rect width="880" height="329" fill="url(#sig-g)" mask="url(#sig-ink)"/>
      </g>
    </g>
  </g>

  <!-- Key Metrics Row -->
  <g transform="translate(36, 224)">
    <g transform="translate(0, 0)">
      <text x="0" y="18" class="font-sans" font-size="20" font-weight="800" fill="#E8E0D2">10+</text>
      <text x="0" y="32" class="font-mono" font-size="10" font-weight="600" fill="rgba(232,224,210,0.7)">Projects</text>
    </g>
    <g transform="translate(90, 0)">
      <text x="0" y="18" class="font-sans" font-size="20" font-weight="800" fill="#B89A5A">3+</text>
      <text x="0" y="32" class="font-mono" font-size="10" font-weight="600" fill="rgba(232,224,210,0.7)">Tech Stacks</text>
    </g>
    <g transform="translate(195, 0)">
      <text x="0" y="18" class="font-sans" font-size="20" font-weight="800" fill="#E8E0D2">100%</text>
      <text x="0" y="32" class="font-mono" font-size="10" font-weight="600" fill="rgba(232,224,210,0.7)">Passion</text>
    </g>
  </g>

  <!-- Bottom Info Chips -->
  <g transform="translate(36, 285)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="168" height="28" rx="8" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <path d="M 16 7 L 11 15 L 14.5 15 L 12.5 21 L 19 12 L 15.5 12 Z" fill="#B89A5A" />
      <text x="26" y="18" class="font-sans" font-size="11.5" font-weight="700" fill="#E8E0D2">Harsh Nilesh Patil</text>
    </g>
    <g transform="translate(176, 0)">
      <rect x="0" y="0" width="144" height="28" rx="8" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <path d="M 15 7.5 C 13.1 7.5 11.5 9.1 11.5 11 C 11.5 14 15 18.5 15 18.5 C 15 18.5 18.5 14 18.5 11 C 18.5 9.1 16.9 7.5 15 7.5 Z M 15 12.2 A 1.2 1.2 0 1 1 15 9.8 A 1.2 1.2 0 1 1 15 12.2 Z" fill="#B89A5A" />
      <text x="26" y="18" class="font-sans" font-size="11.5" font-weight="600" fill="rgba(232,224,210,0.7)">Maharashtra, IN</text>
    </g>
    <g transform="translate(328, 0)">
      <rect x="0" y="0" width="148" height="28" rx="8" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <path d="M 15 8 L 8.5 11.2 L 15 14.4 L 21.5 11.2 Z M 11.2 13 L 11.2 15.8 C 11.2 17.5 15 18.5 15 18.5 C 15 18.5 18.8 17.5 18.8 15.8 L 18.8 13 L 15 14.8 Z" fill="#B89A5A" />
      <text x="26" y="18" class="font-sans" font-size="11.5" font-weight="600" fill="rgba(232,224,210,0.7)">Viva Tech ('29)</text>
    </g>
  </g>

  <!-- Right: Violet Viewfinder Frame -->
  <g transform="translate(540, 24)">
    <rect x="0" y="0" width="324" height="324" rx="16" fill="url(#panel-navy-grad)" stroke="rgba(232,224,210,0.14)" stroke-width="1.4" />
    <path d="M 14 30 L 14 14 L 30 14" fill="none" stroke="#B89A5A" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 294 14 L 310 14 L 310 30" fill="none" stroke="#B89A5A" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 14 294 L 14 310 L 30 310" fill="none" stroke="#B89A5A" stroke-width="2.5" stroke-linecap="round" />
    <path d="M 294 310 L 310 310 L 310 294" fill="none" stroke="#B89A5A" stroke-width="2.5" stroke-linecap="round" />

    <g transform="translate(18, 20)">
      <circle cx="4" cy="4" r="3.5" fill="#B89A5A" class="rec-dot" />
      <text x="14" y="7" class="font-mono" font-size="9.5" font-weight="700" fill="#E8E0D2" letter-spacing="1">REC</text>
      <text x="284" y="7" class="font-mono" font-size="9" fill="rgba(232,224,210,0.7)" text-anchor="end">4K 60FPS</text>
      <rect x="0" y="14" width="288" height="2" rx="1" fill="#0E1D61" />
      <g clip-path="url(#rec-scrubber-clip)">
        <rect x="0" y="14" width="0" height="2" fill="#B89A5A">
          <animate attributeName="width" dur="3.2s" repeatCount="indefinite" values="0;250;288;0" keyTimes="0;0.8;0.95;1" />
        </rect>
      </g>
    </g>

    <g transform="translate(162, 162)">
      <line x1="-12" y1="0" x2="-4" y2="0" stroke="rgba(232,224,210,0.2)" stroke-width="1" />
      <line x1="4" y1="0" x2="12" y2="0" stroke="rgba(232,224,210,0.2)" stroke-width="1" />
      <line x1="0" y1="-12" x2="0" y2="-4" stroke="rgba(232,224,210,0.2)" stroke-width="1" />
      <line x1="0" y1="4" x2="0" y2="12" stroke="rgba(232,224,210,0.2)" stroke-width="1" />
    </g>

    <!-- Violet Waving Animation -->
    <g transform="translate(32, 42)">
      <image href="data:image/png;base64,{vw0}" x="0" y="0" width="260" height="260">
        <animate attributeName="opacity" dur="1.2s" repeatCount="indefinite" values="1;1;0;0;0;0;0;0" keyTimes="0;0.24;0.25;0.49;0.50;0.74;0.75;1" />
      </image>
      <image href="data:image/png;base64,{vw1}" x="0" y="0" width="260" height="260">
        <animate attributeName="opacity" dur="1.2s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0" keyTimes="0;0.24;0.25;0.49;0.50;0.74;0.75;1" />
      </image>
      <image href="data:image/png;base64,{vw2}" x="0" y="0" width="260" height="260">
        <animate attributeName="opacity" dur="1.2s" repeatCount="indefinite" values="0;0;0;0;1;1;0;0" keyTimes="0;0.49;0.50;0.74;0.75;0.99;1;1" />
      </image>
      <image href="data:image/png;base64,{vw3}" x="0" y="0" width="260" height="260" opacity="0">
        <animate attributeName="opacity" dur="1.2s" repeatCount="indefinite" values="0;0;0;0;0;0;1;1" keyTimes="0;0.74;0.75;0.99;1;1;1;1" />
      </image>
    </g>

    <!-- Floating Speech Bubble -->
    <g class="speech-bubble" transform="translate(200, 52)">
      <rect x="0" y="0" width="86" height="24" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.2)" stroke-width="1.2" />
      <polygon points="12,24 16,30 20,24" fill="#0E1D61" />
      <text x="43" y="16" class="font-mono" font-size="10" font-weight="700" fill="#E8E0D2" text-anchor="middle">HI THERE!</text>
    </g>

    <!-- Bottom Role Badges cycling -->
    <g transform="translate(18, 280)">
      <g>
        <rect x="0" y="0" width="144" height="24" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <circle cx="14" cy="12" r="3" fill="#B89A5A" />
        <text x="25" y="16" class="font-mono" font-size="9" font-weight="700" fill="#E8E0D2">FULL-STACK DEV</text>
        <animate attributeName="opacity" dur="6s" repeatCount="indefinite" values="1;1;0;0;0;0" keyTimes="0;0.30;0.33;0.97;0.98;1" />
      </g>
      <g>
        <rect x="0" y="0" width="154" height="24" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <circle cx="14" cy="12" r="3" fill="#B89A5A" />
        <text x="25" y="16" class="font-mono" font-size="9" font-weight="700" fill="#E8E0D2">SECURITY RECON</text>
        <animate attributeName="opacity" dur="6s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.32;0.34;0.64;0.66;1" />
      </g>
      <g>
        <rect x="0" y="0" width="162" height="24" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <circle cx="14" cy="12" r="3" fill="#B89A5A" />
        <text x="25" y="16" class="font-mono" font-size="9" font-weight="700" fill="#E8E0D2">AI &amp; ML EXPLORER</text>
        <animate attributeName="opacity" dur="6s" repeatCount="indefinite" values="0;0;1;1;0;0" keyTimes="0;0.65;0.67;0.97;0.98;1" />
      </g>
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
    <linearGradient id="ring-ivory" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E8E0D2" />
      <stop offset="100%" stop-color="rgba(232,224,210,0.6)" />
    </linearGradient>
    <linearGradient id="ring-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#B89A5A" />
    </linearGradient>
    <linearGradient id="ring-ivory-muted" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(232,224,210,0.8)" />
      <stop offset="100%" stop-color="rgba(232,224,210,0.4)" />
    </linearGradient>
    <pattern id="about-navy-weave" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#E8E0D2" fill-opacity="0.04" />
    </pattern>
  </defs>

  <!-- Solid Deep Atlas Navy Rounded Card Base (Light & Dark Theme Safe) -->
  <rect x="0" y="0" width="900" height="410" rx="20" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />

  <!-- Left Card: Developer Browser -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="432" height="390" rx="16" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
    <rect x="0" y="0" width="432" height="390" rx="16" fill="url(#about-navy-weave)" />
    <text x="24" y="32" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1.5">// DEVELOPMENT</text>
    <text x="24" y="56" class="font-sans" font-size="20" font-weight="800" fill="#E8E0D2" letter-spacing="-0.3">Interfaces &amp; Systems</text>

    <!-- Browser: Deep Navy Panel -->
    <g transform="translate(24, 72)">
      <rect x="0" y="0" width="384" height="154" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <rect x="0" y="0" width="384" height="28" rx="12" fill="#162A7E" />
      <rect x="0" y="24" width="384" height="4" fill="#162A7E" />
      <circle cx="14" cy="14" r="4" fill="#B89A5A" />
      <circle cx="26" cy="14" r="4" fill="rgba(232,224,210,0.4)" />
      <circle cx="38" cy="14" r="4" fill="#E8E0D2" />
      <rect x="52" y="5" width="260" height="18" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
      <text x="64" y="18" class="font-mono" font-size="9" fill="rgba(232,224,210,0.7)">localhost:3000/harsh/capabilities</text>
      <rect x="238" y="9" width="1.5" height="10" fill="#B89A5A" class="cursor-blink" />

      <!-- Terminal Code -->
      <g transform="translate(18, 46)">
        <text x="0" y="14" class="font-mono" font-size="11" fill="#E8E0D2">
          const engineer = {{
        </text>
        <text x="14" y="34" class="font-mono" font-size="11" fill="rgba(232,224,210,0.7)">
          role: <tspan fill="#B89A5A">'Full-Stack &amp; Security'</tspan>,
        </text>
        <text x="14" y="54" class="font-mono" font-size="11" fill="rgba(232,224,210,0.7)">
          status: <tspan fill="#E8E0D2">'Building &amp; Exploring'</tspan>
        </text>
        <text x="0" y="74" class="font-mono" font-size="11" fill="#E8E0D2">
          }};
        </text>
      </g>
    </g>

    <!-- Violet Typing Character -->
    <g transform="translate(122, 210)">
      <image href="data:image/png;base64,{vt0}" x="0" y="0" width="190" height="190">
        <animate attributeName="opacity" dur="0.8s" repeatCount="indefinite" values="1;1;0;0;0;0;0;0" keyTimes="0;0.24;0.25;0.49;0.50;0.74;0.75;1" />
      </image>
      <image href="data:image/png;base64,{vt1}" x="0" y="0" width="190" height="190">
        <animate attributeName="opacity" dur="0.8s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0" keyTimes="0;0.24;0.25;0.49;0.50;0.74;0.75;1" />
      </image>
      <image href="data:image/png;base64,{vt2}" x="0" y="0" width="190" height="190">
        <animate attributeName="opacity" dur="0.8s" repeatCount="indefinite" values="0;0;0;0;1;1;0;0" keyTimes="0;0.49;0.50;0.74;0.75;0.99;1;1" />
      </image>
      <image href="data:image/png;base64,{vt3}" x="0" y="0" width="190" height="190" opacity="0">
        <animate attributeName="opacity" dur="0.8s" repeatCount="indefinite" values="0;0;0;0;0;0;1;1" keyTimes="0;0.74;0.75;0.99;1;1;1;1" />
      </image>
    </g>

    <g transform="translate(24, 345)">
      <rect x="0" y="0" width="144" height="24" rx="8" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
      <circle cx="12" cy="12" r="3" fill="#B89A5A" />
      <text x="20" y="16" class="font-mono" font-size="9.5" font-weight="700" fill="#E8E0D2">FULL-STACK CRAFT</text>
    </g>
  </g>

  <!-- Right Card: Beyond the Screen -->
  <g transform="translate(458, 10)">
    <rect x="0" y="0" width="432" height="390" rx="16" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
    <rect x="0" y="0" width="432" height="390" rx="16" fill="url(#about-navy-weave)" />
    <text x="24" y="32" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1.5">// INTERESTS &amp; FOCUS</text>
    <text x="24" y="56" class="font-sans" font-size="20" font-weight="800" fill="#E8E0D2" letter-spacing="-0.3">Beyond the Screen</text>

    <!-- Cycling Carousel Cards -->
    <g transform="translate(24, 76)">
      <g>
        <rect x="0" y="0" width="384" height="84" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <g transform="translate(18, 22)">
          <path d="M 0 0 C -2 0 -3 2 -2 5 L -1 9 C -0.5 10 1 10 2 9 L 4 7 L 10 7 L 12 9 C 13 10 14.5 10 15 9 L 16 5 C 17 2 16 0 14 0 Z M 2 3 L 4 3 M 3 2 L 3 4 M 11 3 A 0.8 0.8 0 1 1 11 2 A 0.8 0.8 0 1 1 11 3 M 13 5 A 0.8 0.8 0 1 1 13 4 A 0.8 0.8 0 1 1 13 5" stroke="#B89A5A" fill="none" stroke-width="1.2" transform="scale(0.85) translate(0, -3)"/>
          <text x="20" y="8" class="font-sans" font-size="14" font-weight="700" fill="#E8E0D2">Cinematic Gaming</text>
        </g>
        <text x="18" y="54" class="font-sans" font-size="11.5" fill="rgba(232,224,210,0.7)">Immersion, Narrative Design &amp; Lore Architecture</text>
        <circle cx="360" cy="42" r="14" fill="#162A7E" />
        <path d="M 353 45 L 351 38 L 356 41 L 360 36 L 364 41 L 369 38 L 367 45 Z" fill="#B89A5A" />
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="1;1;0;0;0;0;0;0" keyTimes="0;0.22;0.25;0.97;0.98;1;1;1" />
      </g>
      <g>
        <rect x="0" y="0" width="384" height="84" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <g transform="translate(18, 22)">
          <path d="M 6 -5 L 12 -2 L 12 3 C 12 7.5 6 11 6 11 C 6 11 0 7.5 0 3 L 0 -2 Z" fill="#162A7E" stroke="#B89A5A" stroke-width="1.2" transform="translate(0, 1)"/>
          <path d="M 4 3 L 5.5 4.5 L 8.5 1.5" fill="none" stroke="#E8E0D2" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="20" y="8" class="font-sans" font-size="14" font-weight="700" fill="#E8E0D2">Security Recon</text>
        </g>
        <text x="18" y="54" class="font-sans" font-size="11.5" fill="rgba(232,224,210,0.7)">Kali Linux, Port Analysis &amp; Ethical Exploration</text>
        <circle cx="360" cy="42" r="14" fill="#162A7E" />
        <circle cx="360" cy="42" r="7" fill="none" stroke="#B89A5A" stroke-width="1.1"/>
        <line x1="360" y1="42" x2="365" y2="37" stroke="#E8E0D2" stroke-width="1.3" stroke-linecap="round"/>
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0" keyTimes="0;0.23;0.25;0.47;0.50;0.98;1;1" />
      </g>
      <g>
        <rect x="0" y="0" width="384" height="84" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <g transform="translate(18, 22)">
          <path d="M 2 5 L 2 1 C 2 -3 10 -3 10 1 L 10 5" fill="none" stroke="#B89A5A" stroke-width="1.3" stroke-linecap="round"/>
          <rect x="0" y="3" width="3" height="5" rx="1.5" fill="#E8E0D2"/>
          <rect x="9" y="3" width="3" height="5" rx="1.5" fill="#E8E0D2"/>
          <text x="20" y="8" class="font-sans" font-size="14" font-weight="700" fill="#E8E0D2">Lo-Fi Audio &amp; Design</text>
        </g>
        <text x="18" y="54" class="font-sans" font-size="11.5" fill="rgba(232,224,210,0.7)">Soundscapes, Minimal Aesthetics &amp; Calm Flow</text>
        <circle cx="360" cy="42" r="14" fill="#162A7E" />
        <path d="M 357 44 L 357 37 L 364 35 L 364 42 M 357 41 A 2 1.5 0 1 1 355 42.5 A 2 1.5 0 0 1 357 41 M 364 39 A 2 1.5 0 1 1 362 40.5 A 2 1.5 0 0 1 364 39" fill="none" stroke="#B89A5A" stroke-width="1.2"/>
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0" keyTimes="0;0.48;0.50;0.72;0.75;0.98;1;1" />
      </g>
      <g>
        <rect x="0" y="0" width="384" height="84" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <g transform="translate(18, 22)">
          <rect x="1" y="-3" width="10" height="10" rx="2" fill="#162A7E" stroke="#B89A5A" stroke-width="1.2"/>
          <circle cx="6" cy="2" r="1.5" fill="#E8E0D2"/>
          <line x1="3" y1="-5" x2="3" y2="-3" stroke="#B89A5A" stroke-width="1"/>
          <line x1="6" y1="-5" x2="6" y2="-3" stroke="#B89A5A" stroke-width="1"/>
          <line x1="9" y1="-5" x2="9" y2="-3" stroke="#B89A5A" stroke-width="1"/>
          <line x1="3" y1="7" x2="3" y2="9" stroke="#B89A5A" stroke-width="1"/>
          <line x1="6" y1="7" x2="6" y2="9" stroke="#B89A5A" stroke-width="1"/>
          <line x1="9" y1="7" x2="9" y2="9" stroke="#B89A5A" stroke-width="1"/>
          <text x="20" y="8" class="font-sans" font-size="14" font-weight="700" fill="#E8E0D2">Hardware Prototyping</text>
        </g>
        <text x="18" y="54" class="font-sans" font-size="11.5" fill="rgba(232,224,210,0.7)">Arduino, Assistive Gloves &amp; Sensor Fusion</text>
        <circle cx="360" cy="42" r="14" fill="#162A7E" />
        <circle cx="360" cy="42" r="6" fill="none" stroke="#B89A5A" stroke-width="1.5" stroke-dasharray="3,2"/>
        <circle cx="360" cy="42" r="2.5" fill="#B89A5A"/>
        <animate attributeName="opacity" dur="12s" repeatCount="indefinite" values="0;0;1;1;0;0;0;0" keyTimes="0;0.73;0.75;0.97;0.98;1;1;1" />
      </g>
    </g>

    <!-- Daily Focus Rings Section -->
    <g transform="translate(24, 182)">
      <rect x="0" y="0" width="384" height="188" rx="12" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />

      <!-- Concentric Rings on Left -->
      <g transform="translate(74, 94)">
        <circle cx="0" cy="0" r="42" fill="none" stroke="#162A7E" stroke-width="7" />
        <circle cx="0" cy="0" r="42" fill="none" stroke="url(#ring-ivory)" stroke-width="7"
                stroke-linecap="round" stroke-dasharray="264" class="ring-anim-1"
                transform="rotate(-90)" />

        <circle cx="0" cy="0" r="30" fill="none" stroke="#162A7E" stroke-width="7" />
        <circle cx="0" cy="0" r="30" fill="none" stroke="url(#ring-gold)" stroke-width="7"
                stroke-linecap="round" stroke-dasharray="188" class="ring-anim-2"
                transform="rotate(-90)" />

        <circle cx="0" cy="0" r="18" fill="none" stroke="#162A7E" stroke-width="7" />
        <circle cx="0" cy="0" r="18" fill="none" stroke="url(#ring-ivory-muted)" stroke-width="7"
                stroke-linecap="round" stroke-dasharray="113" class="ring-anim-3"
                transform="rotate(-90)" />
      </g>

      <!-- Rings Legend -->
      <g transform="translate(142, 22)">
        <text x="0" y="10" class="font-mono" font-size="10" font-weight="700" fill="#B89A5A" letter-spacing="1">DAILY FOCUS RINGS</text>

        <g transform="translate(0, 24)">
          <circle cx="5" cy="0" r="4" fill="#E8E0D2" />
          <text x="16" y="4" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Code &amp; Architecture</text>
          <text x="170" y="4" class="font-mono" font-size="10" font-weight="700" fill="#E8E0D2">92%</text>
        </g>

        <g transform="translate(0, 48)">
          <circle cx="5" cy="0" r="4" fill="#B89A5A" />
          <text x="16" y="4" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Research &amp; Security</text>
          <text x="170" y="4" class="font-mono" font-size="10" font-weight="700" fill="#B89A5A">86%</text>
        </g>

        <g transform="translate(0, 72)">
          <circle cx="5" cy="0" r="4" fill="rgba(232,224,210,0.6)" />
          <text x="16" y="4" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Modern Web Craft</text>
          <text x="170" y="4" class="font-mono" font-size="10" font-weight="700" fill="#E8E0D2">95%</text>
        </g>

        <g transform="translate(0, 102)">
          <rect x="0" y="0" width="194" height="22" rx="6" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
          <text x="8" y="15" class="font-mono" font-size="9" fill="rgba(232,224,210,0.7)">GOAL: RELENTLESS MASTERY</text>
        </g>
      </g>
    </g>
  </g>
</svg>
'''
with open('about-life.svg', 'w', encoding='utf-8') as f:
    f.write(about_life_svg)

# ==================== 3. ROYAL-SCENE.SVG ====================
# PER UPDATES.MD SECTION 2 & 7: "Exception: the gaming avatars section ('Beyond the Code') keeps its own colors. Do not change it."
# Leaving existing royal-scene.svg untouched!

# ==================== 4. STACK.SVG ====================
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
        0%, 100% { transform: scale(1); filter: drop-shadow(0 0 16px rgba(184, 154, 90, 0.6)); }
        50% { transform: scale(1.08); filter: drop-shadow(0 0 26px rgba(232, 224, 210, 0.8)); }
      }
      .orbit-path-1 { animation: orbit-spin 24s linear infinite; transform-origin: 450px 125px; }
      .orbit-path-2 { animation: orbit-spin-rev 32s linear infinite; transform-origin: 450px 125px; }
      .orbit-path-3 { animation: orbit-spin 40s linear infinite; transform-origin: 450px 125px; }
      .moon-orbit { animation: orbit-spin 6s linear infinite; transform-origin: 0px 0px; }
      .atom-center { animation: core-pulse 4s ease-in-out infinite; transform-origin: 450px 125px; }
    </style>

    <radialGradient id="stack-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#E8E0D2" />
      <stop offset="50%" stop-color="#B89A5A" />
      <stop offset="100%" stop-color="#0E1D61" stop-opacity="0" />
    </radialGradient>

    <pattern id="stack-navy-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#E8E0D2" fill-opacity="0.04" />
    </pattern>
  </defs>

  <!-- Solid Deep Atlas Navy Rounded Card (Light & Dark Theme Safe) -->
  <rect x="2" y="2" width="896" height="456" rx="20" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
  <rect x="2" y="2" width="896" height="456" rx="20" fill="url(#stack-navy-dots)" />

  <g transform="translate(36, 32)">
    <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1.5">// TECH ORBIT &amp; CAPABILITIES</text>
    <text x="0" y="22" class="font-sans" font-size="19" font-weight="800" fill="#E8E0D2" letter-spacing="-0.3">Interactive Planetary Tech Stack</text>
  </g>

  <g transform="translate(710, 32)">
    <rect x="0" y="-14" width="154" height="24" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
    <circle cx="14" cy="-2" r="3.5" fill="#B89A5A" />
    <text x="26" y="2" class="font-mono" font-size="9.5" font-weight="600" fill="#E8E0D2">ATOMIC ORBITS</text>
  </g>

  <!-- Orbits -->
  <g transform="translate(0, 5)">
    <circle cx="450" cy="125" r="54" fill="none" stroke="rgba(232,224,210,0.16)" stroke-width="1.2" stroke-dasharray="4,4" />
    <circle cx="450" cy="125" r="92" fill="none" stroke="rgba(232,224,210,0.16)" stroke-width="1.2" stroke-dasharray="4,4" />
    <circle cx="450" cy="125" r="130" fill="none" stroke="rgba(232,224,210,0.16)" stroke-width="1.2" stroke-dasharray="4,4" />

    <!-- Central Core Sun -->
    <g class="atom-center">
      <circle cx="450" cy="125" r="26" fill="url(#stack-core-glow)" />
      <circle cx="450" cy="125" r="18" fill="#E8E0D2" />
      <text x="450" y="129" class="font-mono" font-size="10" font-weight="800" fill="#0E1D61" text-anchor="middle">CORE</text>
    </g>

    <!-- Orbit 1: React -->
    <g class="orbit-path-1">
      <g transform="translate(450, 71)">
        <circle cx="0" cy="0" r="16" fill="#0E1D61" stroke="#61DAFB" stroke-width="1.5" />
        <g transform="scale(0.85)">
          <ellipse cx="0" cy="0" rx="10.5" ry="4" fill="none" stroke="#61DAFB" stroke-width="1.2" />
          <ellipse cx="0" cy="0" rx="10.5" ry="4" fill="none" stroke="#61DAFB" stroke-width="1.2" transform="rotate(60)" />
          <ellipse cx="0" cy="0" rx="10.5" ry="4" fill="none" stroke="#61DAFB" stroke-width="1.2" transform="rotate(120)" />
          <circle cx="0" cy="0" r="2.2" fill="#61DAFB" />
        </g>
        <text x="0" y="27" class="font-mono" font-size="8.5" font-weight="700" fill="#E8E0D2" text-anchor="middle">React</text>
        <g class="moon-orbit">
          <circle cx="21" cy="0" r="3.5" fill="#B89A5A" />
        </g>
      </g>
    </g>

    <!-- Orbit 2: Python & Android -->
    <g class="orbit-path-2">
      <g transform="translate(542, 125)">
        <circle cx="0" cy="0" r="16" fill="#0E1D61" stroke="#B89A5A" stroke-width="1.5" />
        <g transform="scale(0.65)">
          <path d="M -1 -10 C -5.5 -10 -9 -7.5 -9 -4 L -9 -1 L -1 -1 L -1 0 L -9 0 C -12 0 -14 2.5 -14 6.5 C -14 10.5 -12 13 -9 13 L -7 13 L -7 11 C -7 8 -4.5 6 -1.5 6 L 3 6 C 6.5 6 9 3.5 9 0 L 9 -4 C 9 -7.5 6.5 -10 3 -10 Z M -5 -7 A 1.2 1.2 0 1 1 -5 -4.6 A 1.2 1.2 0 1 1 -5 -7 Z" fill="#3776AB" />
          <path d="M 1 10 C 5.5 10 9 7.5 9 4 L 9 1 L 1 1 L 1 0 L 9 0 C 12 0 14 -2.5 14 -6.5 C 14 -10.5 12 -13 9 -13 L 7 -13 L 7 -11 C 7 -8 4.5 -6 1.5 -6 L -3 -6 C -6.5 -6 -9 -3.5 -9 0 L -9 4 C -9 7.5 -6.5 10 -3 10 Z M 5 7 A 1.2 1.2 0 1 1 5 4.6 A 1.2 1.2 0 1 1 5 7 Z" fill="#FFD438" />
        </g>
        <text x="0" y="27" class="font-mono" font-size="8.5" font-weight="700" fill="#B89A5A" text-anchor="middle">Python</text>
        <g class="moon-orbit">
          <circle cx="21" cy="0" r="3.5" fill="#E8E0D2" />
        </g>
      </g>
      <g transform="translate(358, 125)">
        <circle cx="0" cy="0" r="16" fill="#0E1D61" stroke="#3DDC84" stroke-width="1.5" />
        <g transform="translate(0, 1) scale(0.85)">
          <path d="M -8 1 A 8 8 0 0 1 8 1 Z" fill="#3DDC84" />
          <line x1="-5" y1="-3.5" x2="-7.5" y2="-7" stroke="#3DDC84" stroke-width="1.3" stroke-linecap="round" />
          <line x1="5" y1="-3.5" x2="7.5" y2="-7" stroke="#3DDC84" stroke-width="1.3" stroke-linecap="round" />
          <circle cx="-3" cy="-1.5" r="1" fill="#0E1D61" />
          <circle cx="3" cy="-1.5" r="1" fill="#0E1D61" />
        </g>
        <text x="0" y="27" class="font-mono" font-size="8.5" font-weight="700" fill="#E8E0D2" text-anchor="middle">Android</text>
      </g>
    </g>

    <!-- Orbit 3: Security Recon (Kali) -->
    <g class="orbit-path-3">
      <g transform="translate(450, 255)">
        <circle cx="0" cy="0" r="16" fill="#0E1D61" stroke="#B89A5A" stroke-width="1.5" />
        <g transform="translate(0, -1)">
          <path d="M 0 -7 L 7 -3.5 L 7 2 C 7 6 0 9.5 0 9.5 C 0 9.5 -7 6 -7 2 L -7 -3.5 Z" fill="#162A7E" stroke="#B89A5A" stroke-width="1.2" />
          <path d="M -2.5 -0.5 L -0.5 1.5 L -2.5 3.5" fill="none" stroke="#E8E0D2" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
          <line x1="1" y1="3.5" x2="3.5" y2="3.5" stroke="#B89A5A" stroke-width="1.2" stroke-linecap="round" />
        </g>
        <text x="0" y="28" class="font-mono" font-size="8.5" font-weight="700" fill="#B89A5A" text-anchor="middle">Kali Linux</text>
      </g>
    </g>
  </g>

  <!-- Bottom Grouped Chip Cards -->
  <g transform="translate(36, 255)">
    <!-- Frontend -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="200" height="185" rx="14" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <text x="16" y="26" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1">FRONTEND</text>
      <g transform="translate(16, 42)">
        <rect x="0" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(14, 13)">
          <ellipse cx="0" cy="0" rx="6.5" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="0.9" />
          <ellipse cx="0" cy="0" rx="6.5" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="0.9" transform="rotate(60)" />
          <ellipse cx="0" cy="0" rx="6.5" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="0.9" transform="rotate(120)" />
          <circle cx="0" cy="0" r="1.5" fill="#61DAFB" />
        </g>
        <text x="26" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">React</text>

        <rect x="84" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(98, 13)">
          <circle cx="0" cy="0" r="5.5" fill="#000000" stroke="rgba(232,224,210,0.4)" stroke-width="0.8" />
          <path d="M -2.5 3 L -2.5 -3 L -1.2 -3 L 2 2 L 2 -3 L 2.8 -3 L 2.8 3 L 1.6 3 L -1.7 -2 L -1.7 3 Z" fill="#ffffff" />
        </g>
        <text x="110" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Next.js</text>
      </g>
      <g transform="translate(16, 76)">
        <rect x="0" y="0" width="88" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(13, 13)">
          <rect x="-5.5" y="-5.5" width="11" height="11" rx="1.5" fill="#F7DF1E" />
          <text x="0" y="3.2" font-family="'JetBrains Mono', monospace" font-size="7" font-weight="800" fill="#000000" text-anchor="middle">JS</text>
        </g>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">JavaScript</text>

        <rect x="92" y="0" width="72" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(104, 13)">
          <path d="M -5 -1 C -3.5 -3.5 -1.2 -3.5 -0.4 -1 C 0.4 1.2 1.8 1.2 3 0 C 1.8 2.5 -0.4 2.5 -1.2 0.4 C -2 -1.8 -3.2 -1.8 -5 -1 Z M -0.2 1 C 0.8 -1 2.4 -1 3.2 0.8 C 4 2 4.8 2 5.6 1.2 C 4.8 3.2 3.2 3.2 2.4 1.6 C 1.6 0 0.8 0 -0.2 1 Z" fill="#38BDF8" transform="scale(0.85) translate(0, 0)" />
        </g>
        <text x="115" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Tailwind</text>
      </g>
      <g transform="translate(16, 110)">
        <rect x="0" y="0" width="164" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(16, 13)">
          <path d="M -5 -4.5 L 5 -4.5 L 4 3.5 L 0 5 L -4 3.5 Z" fill="#E34F26" />
          <path d="M 0 -3.2 L 3.2 -3.2 L 2.6 2.4 L 0 3.5 Z" fill="#F06529" />
          <path d="M -2.5 -1.5 L 2.5 -1.5 L 2.2 1.5 L 0 2.2 L -2.2 1.5 L -2.3 0.5 L -1.2 0.5 L -1.1 1 L 0 1.3 L 1.2 1 L 1.3 -0.5 L -2.5 -0.5 Z" fill="#ffffff" />
        </g>
        <text x="28" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">HTML5 · Modern CSS</text>
      </g>
    </g>

    <!-- Backend & AI -->
    <g transform="translate(210, 0)">
      <rect x="0" y="0" width="200" height="185" rx="14" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <text x="16" y="26" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1">BACKEND &amp; AI</text>
      <g transform="translate(16, 42)">
        <rect x="0" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(13, 13)">
          <polygon points="0,-5.5 5,-2.8 5,2.8 0,5.5 -5,2.8 -5,-2.8" fill="#539E43" />
        </g>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Node.js</text>

        <rect x="84" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(97, 13)">
          <circle cx="0" cy="0" r="5.5" fill="#059669" />
          <path d="M 0.5 -4 L -2 0 L 0 0 L -0.5 4 L 2 0 L 0 0 Z" fill="#ffffff" />
        </g>
        <text x="108" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">FastAPI</text>
      </g>
      <g transform="translate(16, 76)">
        <rect x="0" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(14, 13) scale(0.38)">
          <path d="M -1 -10 C -5.5 -10 -9 -7.5 -9 -4 L -9 -1 L -1 -1 L -1 0 L -9 0 C -12 0 -14 2.5 -14 6.5 C -14 10.5 -12 13 -9 13 L -7 13 L -7 11 C -7 8 -4.5 6 -1.5 6 L 3 6 C 6.5 6 9 3.5 9 0 L 9 -4 C 9 -7.5 6.5 -10 3 -10 Z M -5 -7 A 1.2 1.2 0 1 1 -5 -4.6 A 1.2 1.2 0 1 1 -5 -7 Z" fill="#3776AB" />
          <path d="M 1 10 C 5.5 10 9 7.5 9 4 L 9 1 L 1 1 L 1 0 L 9 0 C 12 0 14 -2.5 14 -6.5 C 14 -10.5 12 -13 9 -13 L 7 -13 L 7 -11 C 7 -8 4.5 -6 1.5 -6 L -3 -6 C -6.5 -6 -9 -3.5 -9 0 L -9 4 C -9 7.5 -6.5 10 -3 10 Z M 5 7 A 1.2 1.2 0 1 1 5 4.6 A 1.2 1.2 0 1 1 5 7 Z" fill="#FFD438" />
        </g>
        <text x="25" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Python</text>

        <rect x="84" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(98, 13)">
          <ellipse cx="0" cy="-3.5" rx="5" ry="1.8" fill="none" stroke="#B89A5A" stroke-width="0.9" />
          <path d="M -5 -3.5 L -5 0 A 5 1.8 0 0 0 5 0 L 5 -3.5" fill="none" stroke="#B89A5A" stroke-width="0.9" />
          <path d="M -5 0 L -5 3.5 A 5 1.8 0 0 0 5 3.5 L 5 0" fill="none" stroke="#B89A5A" stroke-width="0.9" />
        </g>
        <text x="110" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">SQL</text>
      </g>
      <g transform="translate(16, 110)">
        <rect x="0" y="0" width="164" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(16, 13)">
          <circle cx="-4" cy="-3" r="1.3" fill="#B89A5A" />
          <circle cx="-4" cy="3" r="1.3" fill="#B89A5A" />
          <circle cx="0" cy="0" r="1.6" fill="#E8E0D2" />
          <circle cx="4" cy="-3" r="1.3" fill="#B89A5A" />
          <circle cx="4" cy="3" r="1.3" fill="#B89A5A" />
          <line x1="-4" y1="-3" x2="0" y2="0" stroke="rgba(232,224,210,0.5)" stroke-width="0.8" />
          <line x1="-4" y1="3" x2="0" y2="0" stroke="rgba(232,224,210,0.5)" stroke-width="0.8" />
          <line x1="0" y1="0" x2="4" y2="-3" stroke="rgba(232,224,210,0.5)" stroke-width="0.8" />
          <line x1="0" y1="0" x2="4" y2="3" stroke="rgba(232,224,210,0.5)" stroke-width="0.8" />
        </g>
        <text x="28" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Machine Learning</text>
      </g>
    </g>

    <!-- Systems & Recon -->
    <g transform="translate(420, 0)">
      <rect x="0" y="0" width="200" height="185" rx="14" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <text x="16" y="26" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1">SYSTEMS &amp; RECON</text>
      <g transform="translate(16, 42)">
        <rect x="0" y="0" width="88" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(13, 13)">
          <path d="M -4 2.5 L -1 0 L -4 -2.5 M 0.5 2.5 L 4 2.5" fill="none" stroke="#38BDF8" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Kali Linux</text>

        <rect x="92" y="0" width="72" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(104, 13)">
          <circle cx="0" cy="0" r="5" fill="none" stroke="#B89A5A" stroke-width="0.9" />
          <circle cx="0" cy="0" r="2.5" fill="none" stroke="#B89A5A" stroke-width="0.7" stroke-dasharray="1.5,1.5" />
          <line x1="0" y1="0" x2="3.5" y2="-3.5" stroke="#E8E0D2" stroke-width="1" stroke-linecap="round" />
        </g>
        <text x="116" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Nmap</text>
      </g>
      <g transform="translate(16, 76)">
        <rect x="0" y="0" width="164" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(16, 13)">
          <path d="M 0 -5.5 L 5 -2.8 L 5 1 C 5 4 0 7 0 7 C 0 7 -5 4 -5 1 L -5 -2.8 Z" fill="none" stroke="#B89A5A" stroke-width="1" />
          <path d="M -2 0 L -0.5 1.5 L 2 -1" fill="none" stroke="#E8E0D2" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" />
        </g>
        <text x="28" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Recon Fundamentals</text>
      </g>
      <g transform="translate(16, 110)">
        <rect x="0" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(13, 14) scale(0.65)">
          <path d="M -7 1 A 7 7 0 0 1 7 1 Z" fill="#3DDC84" />
          <line x1="-4" y1="-2.5" x2="-6.5" y2="-5.5" stroke="#3DDC84" stroke-width="1.2" stroke-linecap="round" />
          <line x1="4" y1="-2.5" x2="6.5" y2="-5.5" stroke="#3DDC84" stroke-width="1.2" stroke-linecap="round" />
          <circle cx="-2.5" cy="-0.5" r="0.9" fill="#0E1D61" />
          <circle cx="2.5" cy="-0.5" r="0.9" fill="#0E1D61" />
        </g>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Android</text>

        <rect x="84" y="0" width="80" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(96, 13)">
          <circle cx="-2.8" cy="0" r="2.8" fill="none" stroke="#00979D" stroke-width="1" />
          <circle cx="2.8" cy="0" r="2.8" fill="none" stroke="#00979D" stroke-width="1" />
          <line x1="-3.8" y1="0" x2="-1.8" y2="0" stroke="#00979D" stroke-width="0.8" />
          <line x1="-2.8" y1="-1" x2="-2.8" y2="1" stroke="#00979D" stroke-width="0.8" />
          <line x1="1.8" y1="0" x2="3.8" y2="0" stroke="#00979D" stroke-width="0.8" />
        </g>
        <text x="108" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Arduino</text>
      </g>
    </g>

    <!-- Developer Tools -->
    <g transform="translate(630, 0)">
      <rect x="0" y="0" width="200" height="185" rx="14" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <text x="16" y="26" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1">DEVELOPER TOOLS</text>
      <g transform="translate(16, 42)">
        <rect x="0" y="0" width="76" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(13, 13) scale(0.7)">
          <rect x="-4.5" y="-4.5" width="9" height="9" rx="1.5" transform="rotate(45)" fill="#F05032" />
          <circle cx="-1.5" cy="0" r="1.1" fill="#ffffff" />
          <circle cx="2" cy="-2" r="1.1" fill="#ffffff" />
          <circle cx="2" cy="2" r="1.1" fill="#ffffff" />
          <path d="M -1.5 0 L 0.5 0 C 1 0 2 -0.8 2 -2 M 0.5 0 C 1 0 2 0.8 2 2" fill="none" stroke="#ffffff" stroke-width="0.9" />
        </g>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Git</text>

        <rect x="80" y="0" width="84" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(92, 13) scale(0.48) translate(-12, -12)">
          <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="#E8E0D2" />
        </g>
        <text x="106" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">GitHub</text>
      </g>
      <g transform="translate(16, 76)">
        <rect x="0" y="0" width="82" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(13, 13) scale(0.6)">
          <path d="M 5 -7 L -2 -1.5 L -5 -4 L -7 -3 L -4 0 L -7 3 L -5 4 L -2 1.5 L 5 7 L 7 6 L 7 -6 Z" fill="#007ACC" />
        </g>
        <text x="24" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">VS Code</text>

        <rect x="88" y="0" width="76" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(98, 13) scale(0.6) translate(-1, 0)">
          <rect x="-5" y="-3" width="1.8" height="1.8" fill="#2496ED" />
          <rect x="-2.8" y="-3" width="1.8" height="1.8" fill="#2496ED" />
          <rect x="-0.6" y="-3" width="1.8" height="1.8" fill="#2496ED" />
          <rect x="-2.8" y="-5.2" width="1.8" height="1.8" fill="#2496ED" />
          <rect x="-0.6" y="-5.2" width="1.8" height="1.8" fill="#2496ED" />
          <path d="M -7 -0.5 C -7 3 -3 4 3.5 4 C 6 4 7 2 7 0.5 C 6.5 0.5 5.8 1 5 1 C 4 1 3.5 -0.5 1.5 -0.5 Z" fill="#2496ED" />
        </g>
        <text x="110" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Docker</text>
      </g>
      <g transform="translate(16, 110)">
        <rect x="0" y="0" width="164" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(16, 13)">
          <rect x="-6" y="-4.5" width="12" height="9" rx="1.5" fill="#0E1D61" stroke="#B89A5A" stroke-width="0.8" />
          <path d="M -3.5 -1.8 L -1.8 0 L -3.5 1.8 M -0.8 1.8 L 1.8 1.8" fill="none" stroke="#E8E0D2" stroke-width="0.8" stroke-linecap="round" stroke-linejoin="round" />
        </g>
        <text x="28" y="17" class="font-sans" font-size="11" font-weight="700" fill="#E8E0D2">Linux CLI · Postman</text>
      </g>
    </g>
  </g>
</svg>
'''
with open('stack.svg', 'w', encoding='utf-8') as f:
    f.write(stack_svg)

# ==================== 5. ID-DASHBOARD.SVG ====================
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
        30% { opacity: 0.35; }
        60% { opacity: 0.35; }
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

    <linearGradient id="holo-foil" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E8E0D2" stop-opacity="0" />
      <stop offset="30%" stop-color="#B89A5A" stop-opacity="0.25" />
      <stop offset="50%" stop-color="#E8E0D2" stop-opacity="0.35" />
      <stop offset="70%" stop-color="#B89A5A" stop-opacity="0.25" />
      <stop offset="100%" stop-color="#E8E0D2" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="gold-chip-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5DEB3" />
      <stop offset="50%" stop-color="#B89A5A" />
      <stop offset="100%" stop-color="#7A602B" />
    </linearGradient>

    <linearGradient id="bar-ivory-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E8E0D2" />
      <stop offset="100%" stop-color="rgba(232,224,210,0.6)" />
    </linearGradient>

    <linearGradient id="bar-gold-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D4AF37" />
      <stop offset="100%" stop-color="#B89A5A" />
    </linearGradient>

    <pattern id="dash-navy-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#E8E0D2" fill-opacity="0.04" />
    </pattern>

    <clipPath id="badge-clip">
      <rect x="0" y="0" width="260" height="300" rx="14" />
    </clipPath>
  </defs>

  <!-- Solid Deep Atlas Navy Rounded Card (Light & Dark Theme Safe) -->
  <rect x="2" y="2" width="896" height="406" rx="20" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
  <rect x="2" y="2" width="896" height="406" rx="20" fill="url(#dash-navy-dots)" />

  <!-- Lanyard Badge -->
  <g class="pendulum-group">
    <g transform="translate(162, 0)">
      <path d="M 12 0 L 20 48 L 36 48 L 44 0 Z" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
      <text x="28" y="26" class="font-mono" font-size="7" font-weight="700" fill="#B89A5A" text-anchor="middle" letter-spacing="1">HARSH-2959</text>
      <text x="28" y="38" class="font-mono" font-size="6" font-weight="600" fill="#E8E0D2" text-anchor="middle">ENGG</text>
      <circle cx="28" cy="52" r="8" fill="none" stroke="#B89A5A" stroke-width="2" />
      <rect x="23" y="56" width="10" height="14" rx="2" fill="#162A7E" stroke="rgba(232,224,210,0.2)" stroke-width="0.8" />
      <polygon points="21,70 35,70 32,77 24,77" fill="#B89A5A" />
    </g>

    <g transform="translate(60, 78)">
      <rect x="4" y="4" width="260" height="300" rx="14" fill="#000000" fill-opacity="0.35" />
      <rect x="0" y="0" width="260" height="300" rx="14" fill="#162A7E" stroke="rgba(232,224,210,0.2)" stroke-width="1.4" />
      <rect x="0" y="0" width="260" height="300" rx="14" fill="none" stroke="#B89A5A" stroke-width="1.5" class="light-border" />

      <g clip-path="url(#badge-clip)">
        <rect x="-80" y="-40" width="100" height="380" fill="url(#holo-foil)" class="holo-beam" />
      </g>

      <rect x="105" y="10" width="50" height="7" rx="3.5" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
      <text x="130" y="36" class="font-mono" font-size="8.5" font-weight="700" fill="#B89A5A" text-anchor="middle" letter-spacing="1.5">VIVA INSTITUTE OF TECHNOLOGY</text>
      <text x="130" y="48" class="font-sans" font-size="7.5" font-weight="600" fill="rgba(232,224,210,0.7)" text-anchor="middle">UNIVERSITY OF MUMBAI</text>

      <g transform="translate(20, 60)">
        <rect x="0" y="0" width="70" height="82" rx="8" fill="#0E1D61" stroke="rgba(232,224,210,0.2)" stroke-width="1.2" />
        <circle cx="35" cy="32" r="16" fill="#162A7E" stroke="#B89A5A" stroke-width="1" />
        <circle cx="35" cy="28" r="8" fill="#E8E0D2" />
        <path d="M 23 44 Q 35 38 47 44" fill="none" stroke="#E8E0D2" stroke-width="2" />
        <rect x="4" y="66" width="62" height="12" rx="3" fill="#162A7E" />
        <text x="35" y="75" class="font-mono" font-size="7" font-weight="700" fill="#E8E0D2" text-anchor="middle">DEV // 2959</text>
      </g>

      <g transform="translate(100, 72)">
        <text x="0" y="0" class="font-mono" font-size="7" font-weight="600" fill="rgba(232,224,210,0.7)">STUDENT &amp; DEVELOPER</text>
        <text x="0" y="16" class="font-sans" font-size="13" font-weight="800" fill="#E8E0D2">Harsh Patil</text>
        <text x="0" y="32" class="font-mono" font-size="8" font-weight="700" fill="#B89A5A">ID: HP-2029-BE</text>
        <circle cx="4" cy="46" r="3" fill="#B89A5A" />
        <text x="12" y="49" class="font-sans" font-size="8.5" font-weight="600" fill="rgba(232,224,210,0.85)">Active / Enrolled</text>
      </g>

      <g transform="translate(20, 156)">
        <rect x="0" y="0" width="36" height="26" rx="4" fill="url(#gold-chip-grad)" stroke="#B89A5A" stroke-width="0.8" />
        <line x1="18" y1="0" x2="18" y2="26" stroke="#7A602B" stroke-width="0.8" />
        <line x1="0" y1="13" x2="36" y2="13" stroke="#7A602B" stroke-width="0.8" />
        <rect x="11" y="7" width="14" height="12" rx="2" fill="none" stroke="#7A602B" stroke-width="0.8" />
      </g>

      <g transform="translate(68, 156)">
        <rect x="0" y="0" width="172" height="26" rx="6" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
        <g transform="translate(14, 13)">
          <path d="M 0 -6 L 5.5 -3 L 5.5 1 C 5.5 4.5 0 7.5 0 7.5 C 0 7.5 -5.5 4.5 -5.5 1 L -5.5 -3 Z" fill="#162A7E" stroke="#B89A5A" stroke-width="1.1" />
          <path d="M -2 0 L -0.5 1.5 L 2.5 -1.5" fill="none" stroke="#E8E0D2" stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round" />
        </g>
        <text x="28" y="17" class="font-mono" font-size="8" font-weight="700" fill="#E8E0D2">SECURE VERIFIED IDENTITY</text>
      </g>

      <g transform="translate(20, 196)">
        <text x="0" y="0" class="font-mono" font-size="7.5" font-weight="600" fill="rgba(232,224,210,0.7)">PROGRAM OF STUDY</text>
        <text x="0" y="14" class="font-sans" font-size="10.5" font-weight="700" fill="#E8E0D2">B.E. Computer Engineering</text>
        <text x="0" y="27" class="font-mono" font-size="8" fill="#B89A5A">Expected Graduation: 2029</text>
      </g>

      <g transform="translate(20, 242)">
        <line x1="0" y1="0" x2="220" y2="0" stroke="rgba(232,224,210,0.14)" stroke-width="0.8" />
        <g transform="translate(0, 10)">
          <line x1="2" y1="0" x2="2" y2="22" stroke="#E8E0D2" stroke-width="2" />
          <line x1="7" y1="0" x2="7" y2="22" stroke="#E8E0D2" stroke-width="1" />
          <line x1="11" y1="0" x2="11" y2="22" stroke="#B89A5A" stroke-width="3" />
          <line x1="17" y1="0" x2="17" y2="22" stroke="#E8E0D2" stroke-width="1.5" />
          <line x1="22" y1="0" x2="22" y2="22" stroke="#E8E0D2" stroke-width="2" />
          <line x1="28" y1="0" x2="28" y2="22" stroke="#B89A5A" stroke-width="1" />
          <line x1="33" y1="0" x2="33" y2="22" stroke="#E8E0D2" stroke-width="2.5" />
          <line x1="38" y1="0" x2="38" y2="22" stroke="#E8E0D2" stroke-width="1" />
          <line x1="43" y1="0" x2="43" y2="22" stroke="#B89A5A" stroke-width="3" />
          <line x1="50" y1="0" x2="50" y2="22" stroke="#E8E0D2" stroke-width="1.5" />
          <line x1="56" y1="0" x2="56" y2="22" stroke="#E8E0D2" stroke-width="2" />
          <line x1="62" y1="0" x2="62" y2="22" stroke="#B89A5A" stroke-width="1" />
          <line x1="68" y1="0" x2="68" y2="22" stroke="#E8E0D2" stroke-width="2.5" />
          <line x1="74" y1="0" x2="74" y2="22" stroke="#E8E0D2" stroke-width="1.5" />
          <line x1="80" y1="0" x2="80" y2="22" stroke="#B89A5A" stroke-width="3" />
        </g>
        <text x="220" y="24" class="font-mono" font-size="8" font-weight="600" fill="rgba(232,224,210,0.7)" text-anchor="end">#2959-HP-2029</text>
      </g>
    </g>
  </g>

  <!-- Right Dashboard -->
  <g transform="translate(360, 28)">
    <text x="0" y="0" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A" letter-spacing="1.5">// ACADEMICS &amp; VELOCITY</text>
    <text x="0" y="22" class="font-sans" font-size="19" font-weight="800" fill="#E8E0D2" letter-spacing="-0.3">Live Milestone Dashboard</text>

    <!-- KPI Tiles -->
    <g transform="translate(0, 42)">
      <g transform="translate(0, 0)">
        <rect x="0" y="0" width="246" height="82" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="82" rx="2" fill="#E8E0D2" />
        <text x="16" y="22" class="font-mono" font-size="9" font-weight="700" fill="#B89A5A" letter-spacing="1">CURRENT DEGREE</text>
        <text x="16" y="48" class="font-sans" font-size="22" font-weight="800" fill="#E8E0D2">B.E. Comp</text>
        <text x="140" y="48" class="font-mono" font-size="11" font-weight="700" fill="#B89A5A">Exp 2029</text>
        <text x="16" y="68" class="font-sans" font-size="10.5" font-weight="500" fill="rgba(232,224,210,0.7)">Viva Inst of Tech · Mumbai Univ</text>
      </g>

      <g transform="translate(258, 0)">
        <rect x="0" y="0" width="246" height="82" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="82" rx="2" fill="#B89A5A" />
        <text x="16" y="22" class="font-mono" font-size="9" font-weight="700" fill="#B89A5A" letter-spacing="1">DIPLOMA MERIT</text>
        <text x="16" y="48" class="font-sans" font-size="24" font-weight="800" fill="#E8E0D2">82.29%</text>
        <text x="120" y="48" class="font-mono" font-size="10" font-weight="700" fill="#B89A5A">DISTINCTION</text>
        <text x="16" y="68" class="font-sans" font-size="10.5" font-weight="500" fill="rgba(232,224,210,0.7)">Diploma in Computer Engineering</text>
      </g>
    </g>

    <!-- Velocity Bar Chart -->
    <g transform="translate(0, 140)">
      <rect x="0" y="0" width="504" height="130" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <text x="16" y="22" class="font-mono" font-size="10" font-weight="700" fill="#B89A5A" letter-spacing="1">DOMAIN FOCUS VELOCITY</text>

      <g transform="translate(16, 36)">
        <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="600" fill="#E8E0D2">Interactive UI &amp; Web Apps</text>
        <text x="472" y="10" class="font-mono" font-size="10" font-weight="700" fill="#E8E0D2" text-anchor="end">94%</text>
        <rect x="0" y="14" width="472" height="6" rx="3" fill="#0E1D61" />
        <rect x="0" y="14" width="443" height="6" rx="3" fill="url(#bar-ivory-grad)" />
      </g>

      <g transform="translate(16, 62)">
        <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="600" fill="#E8E0D2">AI / Machine Learning Exploration</text>
        <text x="472" y="10" class="font-mono" font-size="10" font-weight="700" fill="#E8E0D2" text-anchor="end">88%</text>
        <rect x="0" y="14" width="472" height="6" rx="3" fill="#0E1D61" />
        <rect x="0" y="14" width="415" height="6" rx="3" fill="url(#bar-ivory-grad)" />
      </g>

      <g transform="translate(16, 88)">
        <text x="0" y="10" class="font-sans" font-size="10.5" font-weight="600" fill="#E8E0D2">Cybersecurity &amp; Network Recon</text>
        <text x="472" y="10" class="font-mono" font-size="10" font-weight="700" fill="#B89A5A" text-anchor="end">85%</text>
        <rect x="0" y="14" width="472" height="6" rx="3" fill="#0E1D61" />
        <rect x="0" y="14" width="401" height="6" rx="3" fill="url(#bar-gold-grad)" />
      </g>
    </g>

    <!-- Radar / Now Scan Box -->
    <g transform="translate(0, 286)">
      <rect x="0" y="0" width="504" height="66" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <g transform="translate(24, 33)">
        <circle cx="0" cy="0" r="10" fill="#B89A5A" fill-opacity="0.3" class="radar-pulse" />
        <circle cx="0" cy="0" r="5" fill="#B89A5A" />
      </g>
      <g transform="translate(46, 22)">
        <text x="0" y="0" class="font-mono" font-size="9" font-weight="700" fill="#B89A5A" letter-spacing="1.5">CURRENT FOCUS // LIVE NOW</text>
        <text x="0" y="20" class="font-mono" font-size="12" font-weight="800" fill="#E8E0D2" letter-spacing="0.5">
          EXPLORING AI · WEB DEVELOPMENT · CYBERSECURITY
        </text>
      </g>
    </g>
  </g>
</svg>
'''
with open('id-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(id_dashboard_svg)

# ==================== 6. CONNECT.SVG ====================
connect_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 270" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=JetBrains+Mono:wght@400;500;600;700&amp;display=swap');
      * {{ box-sizing: border-box; }}
      a {{ cursor: pointer; }}
      .font-sans {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
      .font-mono {{ font-family: 'JetBrains Mono', monospace; }}
      @keyframes nudge-arrow {{ 0%, 100% {{ transform: translateX(0px); }} 50% {{ transform: translateX(6px); }} }}
      @keyframes gold-flicker {{
        0%, 100% {{ filter: drop-shadow(0 0 8px rgba(184, 154, 90, 0.5)) drop-shadow(0 0 20px rgba(184, 154, 90, 0.3)); }}
        50% {{ filter: drop-shadow(0 0 14px rgba(232, 224, 210, 0.8)) drop-shadow(0 0 28px rgba(184, 154, 90, 0.6)); }}
      }}
      @keyframes sparkle-pulse {{
        0%, 100% {{ transform: scale(0.9) rotate(0deg); opacity: 0.6; }}
        50% {{ transform: scale(1.2) rotate(18deg); opacity: 1; }}
      }}
      .nudge {{ animation: nudge-arrow 1.6s ease-in-out infinite; }}
      .neon-glow {{ animation: gold-flicker 4s ease-in-out infinite; }}
      .sparkle {{ animation: sparkle-pulse 2.5s ease-in-out infinite; transform-origin: center; }}
    </style>

    <pattern id="connect-navy-dots" width="24" height="24" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.9" fill="#E8E0D2" fill-opacity="0.04" />
    </pattern>
  </defs>

  <!-- Solid Deep Atlas Navy Rounded Card (Light & Dark Theme Safe) -->
  <rect x="2" y="2" width="896" height="266" rx="20" fill="#0E1D61" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
  <rect x="2" y="2" width="896" height="266" rx="20" fill="url(#connect-navy-dots)" />

  <!-- Left: Character & Neon Sign -->
  <g transform="translate(36, 25)">
    <ellipse cx="140" cy="180" rx="90" ry="24" fill="#162A7E" fill-opacity="0.4" />
    <g transform="translate(10, 10)">
      <image href="data:image/png;base64,{v_connect}" x="0" y="0" width="195" height="195" />
    </g>

    <g transform="translate(180, 50)" class="neon-glow">
      <rect x="0" y="0" width="180" height="48" rx="14" fill="#162A7E" stroke="#B89A5A" stroke-width="1.5" />
      <text x="90" y="31" class="font-sans" font-size="19" font-weight="800" fill="#E8E0D2" text-anchor="middle" letter-spacing="1">Harsh-2959</text>
    </g>

    <g class="sparkle" transform="translate(170, 40)">
      <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#E8E0D2" />
    </g>
    <g class="sparkle" transform="translate(368, 42)">
      <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#B89A5A" />
    </g>
    <g class="sparkle" transform="translate(360, 96)">
      <polygon points="0,-6 2,-2 6,0 2,2 0,6 -2,2 -6,0 -2,-2" fill="#B89A5A" />
    </g>

    <g transform="translate(180, 114)">
      <rect x="0" y="0" width="180" height="24" rx="8" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1" />
      <text x="90" y="16" class="font-mono" font-size="9.5" font-weight="700" fill="#B89A5A" text-anchor="middle" letter-spacing="1">LET'S CONNECT</text>
    </g>
  </g>

  <!-- Right: Link Cards -->
  <g transform="translate(420, 26)">
    <text x="0" y="10" class="font-mono" font-size="10.5" font-weight="700" fill="#B89A5A" letter-spacing="1.5">// REACH OUT &amp; EXPLORE</text>
    <text x="0" y="28" class="font-sans" font-size="17" font-weight="800" fill="#E8E0D2" letter-spacing="-0.3">Official Profiles &amp; Networks</text>

    <!-- GitHub -->
    <a href="https://github.com/Harsh-2959" xlink:href="https://github.com/Harsh-2959" target="_blank" rel="noopener noreferrer">
      <g transform="translate(0, 42)">
        <rect x="0" y="0" width="440" height="52" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
        <rect x="0" y="0" width="4" height="52" rx="2" fill="#E8E0D2" />
        <g transform="translate(18, 14)">
          <circle cx="12" cy="12" r="14" fill="#0E1D61" />
          <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" fill="#E8E0D2" transform="scale(0.8) translate(3, 3)" />
        </g>
        <text x="56" y="24" class="font-sans" font-size="13" font-weight="700" fill="#E8E0D2">GitHub</text>
        <text x="56" y="40" class="font-mono" font-size="10.5" fill="rgba(232,224,210,0.7)">github.com/Harsh-2959</text>
        <g class="nudge" transform="translate(404, 30)">
          <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" fill="none" stroke="#E8E0D2" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </g>
    </a>

    <!-- LinkedIn -->
    <a href="https://linkedin.com/in/harshpatil2959" xlink:href="https://linkedin.com/in/harshpatil2959" target="_blank" rel="noopener noreferrer">
      <g transform="translate(0, 104)">
        <rect x="0" y="0" width="440" height="52" rx="12" fill="#162A7E" stroke="#B89A5A" stroke-width="1.4" />
        <rect x="0" y="0" width="4" height="52" rx="2" fill="#B89A5A" />
        <g transform="translate(18, 14)">
          <rect x="0" y="0" width="24" height="24" rx="5" fill="#0077b5" />
          <text x="12" y="17" class="font-sans" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">in</text>
        </g>
        <text x="56" y="24" class="font-sans" font-size="13" font-weight="700" fill="#E8E0D2">LinkedIn</text>
        <text x="56" y="40" class="font-mono" font-size="10.5" fill="#B89A5A">linkedin.com/in/harshpatil2959</text>
        <g class="nudge" transform="translate(404, 30)">
          <path d="M 0 0 L 10 0 M 6 -4 L 10 0 L 6 4" fill="none" stroke="#B89A5A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />
        </g>
      </g>
    </a>

    <!-- University -->
    <g transform="translate(0, 166)">
      <rect x="0" y="0" width="440" height="52" rx="12" fill="#162A7E" stroke="rgba(232,224,210,0.14)" stroke-width="1.2" />
      <rect x="0" y="0" width="4" height="52" rx="2" fill="#B89A5A" />
      <g transform="translate(18, 14)">
        <rect x="0" y="0" width="24" height="24" rx="5" fill="#0E1D61" />
        <g transform="translate(12, 12)">
          <path d="M 0 -4 L -7 -0.5 L 0 3 L 7 -0.5 Z M -4.5 1.5 L -4.5 4.5 C -4.5 6 0 7.5 0 7.5 C 0 7.5 4.5 6 4.5 4.5 L 4.5 1.5 L 0 3.5 Z" fill="#B89A5A" />
        </g>
      </g>
      <text x="56" y="24" class="font-sans" font-size="13" font-weight="700" fill="#E8E0D2">Viva Institute of Technology</text>
      <text x="56" y="40" class="font-mono" font-size="10.5" fill="rgba(232,224,210,0.7)">Open to Collaborations &amp; Projects</text>
      <g transform="translate(320, 16)">
        <rect x="0" y="0" width="96" height="20" rx="10" fill="#0E1D61" stroke="#B89A5A" stroke-width="0.8" />
        <circle cx="10" cy="10" r="3" fill="#B89A5A" />
        <text x="18" y="13.5" class="font-mono" font-size="8" font-weight="700" fill="#E8E0D2">COLLAB</text>
      </g>
    </g>
  </g>
</svg>
'''
with open('connect.svg', 'w', encoding='utf-8') as f:
    f.write(connect_svg)

print("ALL SVGs generated in Deep Atlas Navy (#0E1D61), Ivory (#E8E0D2), and Gold (#B89A5A)!")
