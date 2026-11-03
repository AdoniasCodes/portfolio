#!/usr/bin/env python3
"""Builds pdf.html (16:9 slides, 1600x900) from data.py, same look as the web page. topdf.sh prints it."""
import base64, html, pathlib
import data as D
from build import MEDIA, OLD_SHOTS, poster

ROOT = pathlib.Path(__file__).parent
e = html.escape


def uri(rel):
    p = ROOT / rel if not rel.startswith("shots/") else OLD_SHOTS / rel.split("/", 1)[1]
    if rel.startswith("media/"):
        p = MEDIA / rel.split("/", 1)[1]
    from PIL import Image
    import io
    im = Image.open(p).convert("RGB")
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=82, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def frame(src, url=""):
    addr = f'<span class="addr">{e(url)}</span>' if url else ""
    return f'<div class="screen"><div class="bar">{addr}</div><div class="view"><img src="{uri(src)}"></div></div>'


def client_slide(i, c):
    mets = "".join(f'<div><b>{e(v)}</b><span>{e(k)}</span></div>' for v, k in c["metrics"])
    stack = "".join(f"<li>{e(s)}</li>" for s in c["stack"])
    flip = " flip" if i % 2 else ""
    return f"""<section class="slide proj{flip}">
  {frame(poster(c['slug']), c['url'])}
  <div class="txt">
    <p class="sector">{e(c['sector'])}</p><h2>{e(c['name'])}</h2>
    <p class="role">{e(c['role'])}</p><p class="note">{e(c['note'])}</p>
    <div class="mets">{mets}</div><ul class="stack">{stack}</ul>
    <p class="url">{e(c['url'])}</p>
  </div>
</section>"""


def passion_slide(p):
    imgs = p.get("shots") or sorted(x.name for x in MEDIA.glob(f"{p['slug']}-[0-9].png"))
    how = "".join(f"<li>{e(h)}</li>" for h in p["how"])
    if p["phone"]:
        vis = '<div class="phones">' + "".join(f'<div class="phone"><img src="{uri("media/" + n)}"></div>' for n in imgs[:3]) + "</div>"
    else:
        lead = f"media/{p['slug']}.jpg" if (MEDIA / f"{p['slug']}.jpg").exists() else (f"media/{imgs[0]}" if imgs else None)
        vis = frame(lead) if lead else ""
    return f"""<section class="slide passion">
  <div class="sheet">
    <div class="txt"><p class="kind">{e(p['kind'])}</p><h2>{e(p['title'])}</h2>
      <p class="note">{e(p['body'])}</p><ul class="how">{how}</ul>
      <p class="private">Private project, no public link. Live walkthrough on request.</p></div>
    {vis}
  </div>
</section>"""


CSS = """
@page { size: 1600px 900px; margin: 0; }
*{ margin:0; padding:0; box-sizing:border-box; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
:root{ --paper:#F8F5F4; --paper-2:#EFE8E5; --ink:#1C1411; --muted:#625855; --line:#D7CFCC; --signal:#EC5022;
       --signal-ink:#B22900; --manila:#FCBA43; --manila-2:#E19B34; }
body{ font-family:'Hanken Grotesk',sans-serif; color:var(--ink); background:var(--paper); }
.slide{ width:1600px; height:900px; overflow:hidden; position:relative; page-break-after:always; background:var(--paper); padding:80px 96px; }
.slide:last-child{ page-break-after:auto; }
h1,h2,b{ font-family:'Bricolage Grotesque',sans-serif; }
.screen{ background:#fff; border-radius:14px; overflow:hidden; border:1px solid #E3DCDA;
         box-shadow:0 40px 80px -40px rgba(28,20,17,.5), 0 4px 14px -6px rgba(28,20,17,.18); }
.bar{ height:38px; background:var(--paper-2); border-bottom:1px solid #E3DCDA; display:flex; align-items:center; justify-content:center; }
.addr{ font-size:14px; color:var(--muted); background:#fff; border:1px solid #E3DCDA; border-radius:7px; padding:3px 16px; }
.view{ aspect-ratio:16/10; overflow:hidden; } .view img{ width:100%; height:100%; object-fit:cover; object-position:top; }

.cover{ display:flex; flex-direction:column; justify-content:space-between; }
.cover h1{ font-size:150px; line-height:.88; letter-spacing:-.04em; font-weight:800; max-width:1000px; }
.cover h1 span{ display:block; font-weight:400; color:var(--muted); }
.cover .lede{ font-size:24px; max-width:760px; line-height:1.5; margin-top:36px; color:#453A37; }
.cover .foot{ display:flex; justify-content:space-between; border-top:1px solid var(--line); padding-top:26px; font-size:18px; }
.cover .foot b{ font-size:30px; display:block; }
.cover .stackshots{ position:absolute; right:-120px; top:110px; width:760px; transform:rotate(-6deg); }
.cover .stackshots .screen{ position:absolute; width:620px; }

.proj{ display:grid; grid-template-columns:860px 1fr; gap:64px; align-items:center; }
.proj.flip{ grid-template-columns:1fr 860px; } .proj.flip .screen{ order:2; }
.sector{ font-size:17px; color:var(--muted); font-weight:500; }
.slide h2{ font-size:56px; line-height:1; letter-spacing:-.03em; font-weight:800; margin:10px 0 18px; }
.role{ font-weight:600; font-size:19px; } .note{ font-size:19px; line-height:1.6; margin-top:16px; color:#453A37; }
.mets{ display:flex; gap:40px; margin-top:28px; } .mets b{ display:block; font-size:38px; line-height:1; }
.mets span{ font-size:15px; color:var(--muted); }
.stack{ list-style:none; display:flex; flex-wrap:wrap; gap:8px; margin-top:26px; }
.stack li{ font-size:14px; font-weight:500; padding:6px 12px; border:1px solid var(--line); border-radius:999px; background:var(--paper-2); }
.url{ margin-top:22px; font-weight:600; font-size:17px; color:var(--signal-ink); }

.more h2{ font-size:64px; margin-bottom:40px; }
.minis{ display:grid; grid-template-columns:repeat(5, 1fr); gap:26px; }
.minis img{ width:100%; aspect-ratio:16/10; object-fit:cover; object-position:top; border-radius:10px; border:1px solid #E3DCDA; }
.minis b{ display:block; font-family:'Hanken Grotesk'; font-size:18px; margin-top:14px; }
.minis span{ display:block; font-size:15px; color:var(--muted); line-height:1.5; margin-top:4px; }

.divider{ background:var(--manila); display:flex; flex-direction:column; justify-content:flex-end; }
.divider h2{ font-size:130px; letter-spacing:-.04em; }
.divider p{ font-size:24px; max-width:760px; line-height:1.5; }
.passion{ background:var(--manila); padding:56px; }
.sheet{ background:#fff; border-radius:14px; height:100%; padding:56px; display:grid; grid-template-columns:560px 1fr; gap:56px; align-items:center; }
.kind{ display:inline-block; font-size:15px; font-weight:600; color:var(--signal-ink); background:#FFE3D9; padding:6px 14px; border-radius:999px; }
.passion h2{ font-size:46px; } .passion .note{ font-size:17.5px; }
.how{ margin:18px 0 0 20px; font-size:16.5px; line-height:1.55; color:#453A37; } .how li{ margin-top:4px; }
.private{ margin-top:20px; font-size:15px; color:var(--muted); border-left:3px solid var(--manila-2); padding-left:12px; }
.phones{ display:flex; gap:22px; justify-content:center; }
.phone{ width:230px; aspect-ratio:390/844; border:8px solid var(--ink); border-radius:34px; overflow:hidden; background:var(--ink); }
.phone img{ width:100%; height:100%; object-fit:cover; object-position:top; }

.end{ background:var(--ink); color:var(--paper); display:flex; flex-direction:column; justify-content:space-between; }
.end h2{ font-size:110px; line-height:.92; letter-spacing:-.04em; max-width:1100px; }
.end p{ font-size:24px; color:#BFB5B2; max-width:900px; line-height:1.5; margin-top:28px; }
.end ul{ list-style:none; display:grid; grid-template-columns:1fr 1fr; gap:0 64px; font-size:22px; }
.end li{ padding:16px 0; border-top:1px solid #3F3633; display:flex; justify-content:space-between; }
.end li span{ color:#BFB5B2; }
"""


def build():
    covers = [c for c in D.CLIENTS[:3]]
    stack = "".join(f'<div class="screen" style="top:{k*150}px;left:{k*70}px">'
                    f'<div class="bar"></div><div class="view"><img src="{uri(poster(c["slug"]))}"></div></div>'
                    for k, c in enumerate(covers))
    slides = [f"""<section class="slide cover">
  <div class="stackshots">{stack}</div>
  <div><h1>Websites that move. <span>And get found.</span></h1>
  <p class="lede">I design and build sites with 3D, motion and real SEO behind them, for schools, contractors, software companies and shops in Ethiopia, the UK and Italy. {D.TOTAL_SITES} websites built.</p></div>
  <div class="foot"><div><b>{D.NAME}</b>Web developer, Addis Ababa</div>
  <div style="text-align:right">{D.EMAIL}<br>{D.PHONE_TEXT}<br>{D.SITE_URL.replace('https://','')}</div></div>
</section>"""]
    slides += [client_slide(i, c) for i, c in enumerate(D.CLIENTS)]
    minis = "".join(f'<div><img src="{uri("shots/" + m["slug"] + ".png")}"><b>{e(m["name"])}</b><span>{e(m["line"])}</span></div>'
                    for m in D.MORE)
    slides.append(f'<section class="slide more"><h2>More client sites</h2><div class="minis">{minis}</div></section>')
    slides.append("""<section class="slide divider"><h2>Passion projects</h2>
  <p>Things I built because I wanted them to exist. No client brief, so this is where I try the hardest ideas first.</p></section>""")
    slides += [passion_slide(p) for p in D.PASSION]
    n = len(D.CLIENTS) + len(D.MORE) + len(D.PASSION)
    slides.append(f"""<section class="slide end">
  <div><h2>You've seen {n} of {D.TOTAL_SITES}.</h2>
  <p>The rest are presented on request: landing pages, online stores, school systems, internal tools and company sites. Tell me what you are building and I will show you the ones closest to it.</p></div>
  <ul><li><span>Email</span>{D.EMAIL}</li><li><span>Phone and WhatsApp</span>{D.PHONE_TEXT}</li>
  <li><span>Portfolio</span>{D.SITE_URL.replace('https://','')}</li><li><span>GitHub</span>github.com/AdoniasCodes</li></ul>
</section>""")
    fonts = '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Hanken+Grotesk:wght@400;500;600&display=swap" rel="stylesheet">'
    (ROOT / "pdf.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8">{fonts}<style>{CSS}</style></head><body>{"".join(slides)}</body></html>')
    print("built pdf.html,", len(slides), "slides")


if __name__ == "__main__":
    build()
