"""Build original, self-contained SVG artwork. Python standard library only."""
from pathlib import Path
from html import escape

ASSETS = Path(__file__).resolve().parents[1] / "assets"
PALETTES = {
    "dark": dict(bg="#101521", panel="#181f30", ink="#f2eee6", muted="#abb3c4", line="#354057", teal="#71e8c7", violet="#bcadff", orange="#ffbe83"),
    "light": dict(bg="#f6f2e9", panel="#fffdf8", ink="#202c3d", muted="#5b6576", line="#d6d5cf", teal="#087c69", violet="#6e4cb4", orange="#9c4b23"),
}


def svg(width, height, title, description, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<style>
text{{font-family:'Segoe UI',Arial,sans-serif}} .mono{{font-family:Consolas,'Courier New',monospace}}
.scan{{animation:scan 5s linear infinite}} .spark{{animation:twinkle 4s ease-in-out infinite}} .float{{animation:float 6s ease-in-out infinite}}
@keyframes scan{{from{{stroke-dashoffset:520}}to{{stroke-dashoffset:0}}}}
@keyframes twinkle{{0%,100%{{opacity:.3}}50%{{opacity:1}}}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}
@media(prefers-reduced-motion:reduce){{.scan,.spark,.float{{animation:none}}}}
</style>
{body}
</svg>'''


def text(x, y, value, size, color, weight="400", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" {extra}>{escape(value)}</text>'


def hero(p):
    b = f'''<defs>
<linearGradient id="sky" x2="0" y2="1"><stop stop-color="#20213e"/><stop offset="1" stop-color="#624364"/></linearGradient>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="{p['muted']}" opacity=".12"/></pattern>
<clipPath id="scene"><rect x="712" y="104" width="434" height="344" rx="12"/></clipPath>
</defs>
<rect width="1200" height="540" rx="20" fill="{p['bg']}"/>
<rect width="1200" height="540" rx="20" fill="url(#dots)"/>
<path d="M44 58H1156M44 484H1156" stroke="{p['line']}"/>
<circle cx="51" cy="33" r="4" fill="{p['teal']}"/>
'''
    b += text(66, 38, "BME-SAURAV / PERSONAL LAB", 15, p['muted'], "600", 'class="mono" letter-spacing="1.5"')
    b += text(1154, 38, "ENGINEERING × CURIOSITY × PLAY", 13, p['muted'], extra='text-anchor="end" class="mono"')
    b += text(49, 155, "Hello, world. I'm", 23, p['muted'])
    b += text(43, 266, "Saurav.", 116, p['ink'], "750", 'letter-spacing="-6"')
    b += text(51, 334, "Serious systems.", 42, p['ink'], "600", 'letter-spacing="-1"')
    b += text(51, 387, "Playful possibilities.", 42, p['teal'], "600", 'letter-spacing="-1"')
    b += text(52, 440, "Biomedical engineer · Indie hacker · Game dev enthusiast", 18, p['muted'])
    b += text(51, 516, "BASED IN THE LAND OF ENCHANTMENT", 14, p['muted'], extra='class="mono" letter-spacing="1"')
    b += text(1152, 516, "A LITTLE SCIENCE. A LITTLE SIDE QUEST.", 14, p['muted'], extra='text-anchor="end" class="mono"')
    b += f'''<rect x="700" y="78" width="458" height="382" rx="18" fill="{p['panel']}" stroke="{p['line']}"/>
<circle cx="720" cy="92" r="3" fill="#db8c87"/><circle cx="732" cy="92" r="3" fill="#dfbd85"/><circle cx="744" cy="92" r="3" fill="#71bca7"/>
<g clip-path="url(#scene)">
<rect x="712" y="104" width="434" height="344" fill="url(#sky)"/>
<circle cx="1059" cy="161" r="29" fill="#f9d2a3"/><circle cx="1048" cy="151" r="29" fill="#282440"/>
<g fill="#e7d9e9"><path class="spark" d="M765 145h4v4h-4zM890 130h3v3h-3zM996 206h4v4h-4zM1117 128h3v3h-3z"/>
<path class="spark" style="animation-delay:-2s" d="M825 199h3v3h-3zM964 156h3v3h-3zM1094 227h3v3h-3z"/></g>
<path d="M712 329V274H744V250H776V274H808V310H840V295H872V265H904V243H936V265H968V301H1000V319H1032V286H1064V260H1096V286H1128V311H1146V448H712Z" fill="#79506d"/>
<path d="M712 373V333H750V303H789V320H812V352H850V375H914V340H951V318H990V338H1015V375H1062V351H1100V330H1146V448H712Z" fill="#b56f77"/>
<path d="M712 405H748V389H803V400H863V417H935V400H1000V389H1050V405H1110V393H1146V448H712Z" fill="#e0a08d"/>
<path d="M712 431H810V423H876V434H987V420H1068V430H1146V448H712Z" fill="#f0c2a2"/>
<g fill="#3c4c52" shape-rendering="crispEdges"><path d="M1080 359h10v-28h9v34h-9v35h-10v-25h-17v-27h9v17h8z"/><path d="M773 383h8v-24h7v29h-7v22h-8v-17h-10v-20h6v10z"/></g>
<g shape-rendering="crispEdges"><path d="M943 378h13v13h-13z" fill="#f4d8b4"/><path d="M940 375h19v6h-19z" fill="#43304d"/><path d="M940 391h19v18h-19z" fill="#78e0cf"/><path d="M940 409h7v10h-7zM952 409h7v10h-7z" fill="#43304d"/><path d="M936 394h4v12h-4zM959 394h4v12h-4z" fill="#f4d8b4"/></g>
<path d="M966 419H983M993 419h9M1012 419h5" stroke="#9c6467" stroke-width="2"/>
</g>'''
    b += text(1137, 96, "WORLD_01", 10, p['muted'], extra='class="mono" text-anchor="end"')
    b += f'''<g class="float"><rect x="822" y="221" width="242" height="100" rx="10" fill="#121e2c" stroke="#6ebfae" stroke-opacity=".7"/>
<path d="M838 254H1048M838 276H1048M838 298H1048M868 247V307M902 247V307M936 247V307M970 247V307M1004 247V307" stroke="#6ebfae" stroke-opacity=".11"/>
<path d="M838 279H866L877 268L889 289L902 252L916 301L929 279H955L966 268L978 289L991 252L1005 301L1018 279H1048" fill="none" stroke="#71e8c7" stroke-width="2.5"/>
<path class="scan" d="M838 279H866L877 268L889 289L902 252L916 301L929 279H955L966 268L978 289L991 252L1005 301L1018 279H1048" fill="none" stroke="#f4ffe7" stroke-width="3" stroke-dasharray="30 490"/>
{text(838, 239, 'SIGNAL / MEETS / SANDBOX', 10, '#97cdbf', extra='class="mono"')}</g>'''
    return svg(1200, 540, "Saurav's personal lab", "Serious systems. Playful possibilities. A biomedical signal floats above an original pixel desert landscape, with a moon, mesas, cacti, and a tiny explorer.", b)


def card(p, kind):
    config = {
        'systems': ('01', 'Systems', 'Think in connections.', 'Biomedical engineering', p['teal']),
        'ideas': ('02', 'Side quests', 'Follow the what-if.', 'Independent experiments', p['orange']),
        'worlds': ('03', 'Worlds', 'Leave room to play.', 'Game development', p['violet']),
    }
    number, title, subtitle, label, accent = config[kind]
    b = f'<rect x="1" y="1" width="358" height="274" rx="16" fill="{p["panel"]}" stroke="{p["line"]}"/>'
    b += text(26, 40, number + ' / EXPLORE', 13, p['muted'], extra='class="mono" letter-spacing="2"')
    b += text(26, 181, title, 34, p['ink'], '700', 'letter-spacing="-1"')
    b += text(26, 218, subtitle, 21, accent, '600')
    b += text(26, 251, label, 16, p['muted'])
    if kind == 'systems':
        b += f'''<g stroke="{accent}" fill="{p['panel']}" stroke-width="2"><path d="M38 98H104L141 78H206L243 109H314M104 98L144 124H240" fill="none"/>
<circle cx="38" cy="98" r="8"/><circle cx="104" cy="98" r="11"/><circle cx="206" cy="78" r="8"/><circle cx="243" cy="109" r="11"/><circle cx="314" cy="109" r="8"/><circle cx="144" cy="124" r="6"/>
<circle class="spark" cx="243" cy="109" r="4" fill="{accent}"/></g>'''
    elif kind == 'ideas':
        b += f'''<g fill="none" stroke="{accent}" stroke-width="2.5" stroke-linecap="round"><path d="M154 112C127 85 151 61 177 61C203 61 227 85 200 112L195 127H159Z"/>
<path d="M159 134H195M164 141H190M177 115V92M166 86L177 97L188 86M177 43V34M131 57L124 50M223 57L230 50M119 91H109M235 91H245"/>
<path class="spark" d="M268 68V84M260 76H276M82 115V125M77 120H87"/></g>'''
    else:
        b += f'''<g fill="none" stroke="{accent}" stroke-width="2.5" stroke-linejoin="round"><path d="M114 81L177 53L240 81L177 111Z"/><path d="M114 81V113L177 143L240 113V81M177 111V143"/>
<path d="M143 68L208 96M145 96L208 67" opacity=".5"/><path d="M255 65H271M263 57V73M87 112H99M93 106V118"/>
<path class="spark" d="M177 32V42M172 37H182"/></g>'''
    return svg(360, 276, title, f'{subtitle} {label}.', b)


def footer(p):
    b = f'<rect width="1200" height="92" rx="12" fill="{p["bg"]}"/>'
    b += f'<path d="M30 46H143L155 33L168 59L182 22L197 69L210 46H300" stroke="{p["teal"]}" stroke-width="2" fill="none"/>'
    b += text(1155, 54, 'STAY CURIOUS. KEEP BUILDING. LEAVE ROOM TO PLAY.', 19, p['ink'], '600', 'class="mono" text-anchor="end" letter-spacing="1"')
    return svg(1200, 92, 'A note to build by', 'Stay curious. Keep building. Leave room to play.', b)


if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    for theme, palette in PALETTES.items():
        (ASSETS / f'hero-{theme}.svg').write_text(hero(palette), encoding='utf-8')
        for name in ('systems', 'ideas', 'worlds'):
            (ASSETS / f'{name}-{theme}.svg').write_text(card(palette, name), encoding='utf-8')
        (ASSETS / f'footer-{theme}.svg').write_text(footer(palette), encoding='utf-8')
    print('Generated 10 SVG assets.')
