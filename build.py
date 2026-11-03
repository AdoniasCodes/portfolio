#!/usr/bin/env python3
"""Builds the website portfolio landing page (site/index.html) from data.py.

Run:  python3 build.py        -> site/index.html (+ copies media and shots into site/)
Then: bash topdf.sh           -> site/Adonias_Nigussie_Website_Portfolio.pdf (from pdf.html)
"""
import html, json, pathlib, shutil
import data as D

ROOT = pathlib.Path(__file__).parent
SITE = ROOT / "site"
MEDIA = ROOT / "media"
OLD_SHOTS = ROOT.parent / "portfolio-deck" / "shots"
PDF_NAME = "Adonias_Nigussie_Website_Portfolio.pdf"
e = html.escape


def copy_assets():
    (SITE / "media").mkdir(parents=True, exist_ok=True)
    (SITE / "shots").mkdir(parents=True, exist_ok=True)
    from PIL import Image
    for f in MEDIA.glob("*"):
        stem = f.stem
        if f.suffix.lower() == ".webm":
            continue  # mp4 plays everywhere; skipping webm halves the repo
        if stem.endswith("-top") and (MEDIA / f"{stem[:-4]}.jpg").exists():
            continue  # backup still, the jpg poster is used instead
        if f.suffix.lower() == ".png":  # screenshots ship as jpg to keep the site light
            im = Image.open(f).convert("RGB")
            im.save(SITE / "media" / f"{stem}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
        elif f.suffix.lower() in {".mp4", ".webm", ".jpg", ".webp"}:
            shutil.copy2(f, SITE / "media" / f.name)
    for m in D.MORE:
        src = OLD_SHOTS / f"{m['slug']}.png"
        if src.exists():
            shutil.copy2(src, SITE / "shots" / src.name)


def has(name):
    return (MEDIA / name).exists()


def poster(slug):
    for n in (f"{slug}.jpg", f"{slug}-top.png", f"{slug}-1.png"):
        if has(n):
            return f"media/{n[:-4]}.jpg"
    return f"shots/{slug}.png"


def web(name):
    """Published name of a media screenshot (PNGs are converted to JPG on copy)."""
    return name[:-4] + ".jpg" if name.endswith(".png") else name


def screen(slug, url, label):
    """Browser-like frame with a looping recording (or still image if no video)."""
    p = poster(slug)
    if has(f"{slug}.mp4"):
        srcs = ""
        if False and has(f"{slug}.webm"):
            srcs += f'<source src="media/{slug}.webm" type="video/webm">'
        srcs += f'<source src="media/{slug}.mp4" type="video/mp4">'
        body = (f'<video muted loop playsinline preload="none" poster="{p}" '
                f'aria-label="Screen recording of {e(label)}">{srcs}</video>')
    else:
        body = f'<img src="{p}" alt="Home page of {e(label)}" loading="lazy" width="1440" height="900">'
    bar = f'<div class="bar"><span class="addr">{e(url)}</span></div>' if url else '<div class="bar"></div>'
    return f'<figure class="screen">{bar}<div class="view">{body}</div></figure>'


def client_rows():
    out = []
    for i, c in enumerate(D.CLIENTS):
        stack = "".join(f"<li>{e(s)}</li>" for s in c["stack"])
        mets = "".join(f'<div><b>{e(v)}</b><span>{e(k)}</span></div>' for v, k in c["metrics"])
        flip = " flip" if i % 2 else ""
        out.append(f"""
    <article class="proj{flip}" id="{c['slug']}">
      {screen(c['slug'], c['url'], c['name'])}
      <div class="proj-text">
        <p class="sector">{e(c['sector'])}</p>
        <h3>{e(c['name'])}</h3>
        <p class="role">{e(c['role'])}</p>
        <p class="note">{e(c['note'])}</p>
        <div class="mets">{mets}</div>
        <ul class="stack" aria-label="Built with">{stack}</ul>
        <a class="visit" href="https://{e(c['url'])}" target="_blank" rel="noopener">Visit {e(c['url'])}</a>
      </div>
    </article>""")
    return "".join(out)


def more_grid():
    out = []
    for m in D.MORE:
        out.append(f"""
      <a class="mini" href="https://{e(m['url'])}" target="_blank" rel="noopener">
        <img src="shots/{m['slug']}.png" alt="Home page of {e(m['name'])}" loading="lazy" width="1440" height="900">
        <span class="mini-name">{e(m['name'])}</span>
        <span class="mini-line">{e(m['line'])}</span>
      </a>""")
    return "".join(out)


def shots_for(slug):
    return sorted(p.name for p in MEDIA.glob(f"{slug}-[0-9].png"))


def passion():
    tabs, panels = [], []
    for i, p in enumerate(D.PASSION):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button role="tab" id="tab-{p["slug"]}" aria-controls="pan-{p["slug"]}" '
                    f'aria-selected="{sel}" tabindex="{0 if i == 0 else -1}">{e(p["tab"])}</button>')
        how = "".join(f"<li>{e(h)}</li>" for h in p["how"])
        imgs = [web(n) for n in (p.get("shots") or shots_for(p["slug"]))]
        if has(f"{p['slug']}.mp4") and not p["phone"]:
            lead = screen(p["slug"], "", p["title"])
        elif imgs and not p["phone"]:
            lead = (f'<figure class="screen"><div class="bar"></div><div class="view">'
                    f'<img src="media/{imgs[0]}" alt="{e(p["title"])}, inside the app" loading="lazy"></div></figure>')
        else:
            lead = ""
        if p["phone"]:
            vid = ""
            if has(f"{p['slug']}.mp4"):
                vid = (f'<figure class="phone"><video muted loop playsinline preload="none" '
                       f'poster="media/{imgs[0] if imgs else ""}" aria-label="Recording of Amore Movies in use">'
                       f'<source src="media/{p["slug"]}.mp4" type="video/mp4"></video></figure>')
            phones = "".join(f'<figure class="phone"><img src="media/{n}" alt="Amore Movies screen {k+1}" loading="lazy"></figure>'
                             for k, n in enumerate(imgs[:5]))
            gallery = f'<div class="phones">{vid}{phones}</div>'
        else:
            rest = imgs[1:] if (lead and not has(f"{p['slug']}.mp4")) else imgs
            gallery = "".join(f'<img src="media/{n}" alt="{e(p["title"])}, view {k+1}" loading="lazy">'
                              for k, n in enumerate(rest[:3]))
            gallery = f'<div class="thumbs">{gallery}</div>' if gallery else ""
        hidden = "" if i == 0 else " hidden"
        panels.append(f"""
      <div role="tabpanel" id="pan-{p['slug']}" aria-labelledby="tab-{p['slug']}" class="panel"{hidden}>
        <div class="panel-head">
          <p class="kind">{e(p['kind'])}</p>
          <h3>{e(p['title'])}</h3>
          <p class="note">{e(p['body'])}</p>
          <ul class="how">{how}</ul>
          <p class="private">Private project, so there is no public link. I can walk you through it live on a call.</p>
        </div>
        {lead}
        {gallery}
      </div>""")
    return "".join(tabs), "".join(panels)


def hero_textures():
    items = []
    for c in D.CLIENTS:
        items.append(dict(src=poster(c["slug"]), url=c["url"], href=f"#{c['slug']}"))
    for m in D.MORE:
        items.append(dict(src=f"shots/{m['slug']}.png", url=m["url"], href="#work"))
    if has("hermella.jpg"):
        items.insert(2, dict(src="media/hermella.jpg", url="studio portfolio", href="#passion"))
    return json.dumps(items)


def page():
    tabs, panels = passion()
    n_shown = len(D.CLIENTS) + len(D.MORE) + len(D.PASSION)
    ld = {
        "@context": "https://schema.org", "@type": "ProfilePage",
        "mainEntity": {"@type": "Person", "name": D.NAME, "jobTitle": "Web developer",
                       "email": f"mailto:{D.EMAIL}", "telephone": D.PHONE_TEL,
                       "address": {"@type": "PostalAddress", "addressLocality": "Addis Ababa", "addressCountry": "ET"},
                       "url": D.SITE_URL, "sameAs": [D.GITHUB, D.LINKEDIN, "https://adoniascodes.github.io/"]},
    }
    tpl = (ROOT / "template.html").read_text()
    return (tpl.replace("{{CLIENTS}}", client_rows())
               .replace("{{MORE}}", more_grid())
               .replace("{{TABS}}", tabs).replace("{{PANELS}}", panels)
               .replace("{{HERO_JSON}}", hero_textures())
               .replace("{{LD}}", json.dumps(ld))
               .replace("{{N_SHOWN}}", str(n_shown)).replace("{{TOTAL}}", D.TOTAL_SITES)
               .replace("{{EMAIL}}", D.EMAIL).replace("{{PHONE_TEXT}}", D.PHONE_TEXT)
               .replace("{{PHONE_TEL}}", D.PHONE_TEL).replace("{{WHATSAPP}}", D.WHATSAPP)
               .replace("{{GITHUB}}", D.GITHUB).replace("{{LINKEDIN}}", D.LINKEDIN)
               .replace("{{SITE_URL}}", D.SITE_URL).replace("{{PDF}}", PDF_NAME))


if __name__ == "__main__":
    SITE.mkdir(exist_ok=True)
    copy_assets()
    (SITE / "index.html").write_text(page())
    (SITE / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {D.SITE_URL}sitemap.xml\n")
    (SITE / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f"<url><loc>{D.SITE_URL}</loc></url></urlset>\n")
    (SITE / ".nojekyll").write_text("")
    print("built", SITE / "index.html")
