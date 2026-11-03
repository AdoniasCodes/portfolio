"""One source of truth for the website portfolio: the web page and the PDF both read this."""

NAME = "Adonias Nigussie"
EMAIL = "adoniasnigussie@gmail.com"
PHONE_TEXT = "+2519 44 72 16 82"
PHONE_TEL = "+251944721682"
WHATSAPP = "https://wa.me/251944721682"
GITHUB = "https://github.com/AdoniasCodes"
LINKEDIN = "https://www.linkedin.com/in/adoniasn"
SITE_URL = "https://adoniascodes.github.io/portfolio/"

# Client work. video=True means media/<slug>.mp4 exists; otherwise media/<slug>-top.png or shots/<slug>.png.
CLIENTS = [
    dict(slug="inteltech", name="Inteltech", url="inteltech.et", sector="Software and ERP, Ethiopia",
         role="Full rebuild, solo: design system, front end, 3D hero, SEO, blog",
         stack=["Astro", "Three.js", "Anime.js", "Web3Forms"],
         note="A software company selling ERP to manufacturers and traders. I rebuilt their approved design "
              "from scratch as a static site: 15 pages, an interactive 3D logo in the hero, a circuit-style "
              "wave field behind the dark sections, and a blog built around the questions ERP buyers search for.",
         metrics=[("15", "pages"), ("99-100", "Lighthouse scores"), ("8", "blog posts")]),
    dict(slug="nucleus", name="Nucleus International Schools", url="nucleusinternationalschoolsystem.com",
         sector="Education, Ethiopia", role="Full build, solo: design, front end, back end, SEO",
         stack=["Next.js", "Payload CMS", "React", "Tailwind"],
         note="A 46-page school site taken from blank page to launch on my own. It reached the top 3 on "
              "Google for 8 target keywords within two months, and was built for AI answer engines from day one.",
         metrics=[("46", "pages"), ("8", "keywords in Google's top 3"), ("2 months", "to rank")]),
    dict(slug="ethiolifecare", name="EthioLifecare", url="ethiolifecare.com", sector="Healthcare supply, Ethiopia",
         role="Full build and redesign, plus an ongoing SEO retainer",
         stack=["WordPress", "Custom CSS", "Technical SEO"],
         note="Ethiopia's supplier of medicines and medical equipment to hospitals, pharmacies and NGOs. "
              "I built the site, gave it a full redesign this year, and still run its search work every month.",
         metrics=[("Redesigned", "2026"), ("Monthly", "SEO retainer")]),
    dict(slug="agc", name="Advanced General Contractor", url="advancedgeneralcontractor.com",
         sector="Construction, Ethiopia", role="Full build, solo: custom front end, custom admin, SEO",
         stack=["Hand-coded front end", "Custom CMS", "In-template SEO"],
         note="A Grade One contractor wanted easy editing without a heavy CMS. I hand-wrote the site and built "
              "a custom admin behind it, so the team edits every page the way they would in WordPress.",
         metrics=[("100%", "custom code"), ("Own", "admin panel")]),
    dict(slug="mekaneselam", name="Mekane Selam Senbet School", url="mekaneselamss.com",
         sector="Community school, Ethiopia", role="Full build, solo: ERP back end, hand-coded front end",
         stack=["Custom ERP", "Hand-coded front end", "English and Amharic"],
         note="A full ERP for members, attendance and reports, under a bilingual front end that switches "
              "between English and Amharic on the page without a reload.",
         metrics=[("2", "languages, live switch"), ("Full", "ERP back end")]),
    dict(slug="cribcrm", name="Crib CRM", url="cribcrm.com", sector="SaaS",
         role="Product front end solo, back end with the product team",
         stack=["React", "Node", "Email automation", "Funnel builder"],
         note="A CRM for network-marketing teams. I own the product front end and shipped two features end "
              "to end: the email automation engine and the funnel builder.",
         metrics=[("2", "features shipped end to end"), ("Live", "SaaS product")]),
    dict(slug="intelmotion", name="IntelMotion Lifts", url="intelmotionlifts.com", sector="Industrial, Ethiopia",
         role="Branding, social media and full website build", stack=["WordPress", "SEO", "Content"],
         note="Ethiopia's lift and escalator provider, with 300+ projects delivered. Full website build plus "
              "the brand and social media around it.",
         metrics=[("300+", "projects showcased"), ("Brand", "and social")]),
    dict(slug="adoniascodes", name="Adonias Codes", url="adoniascodes.github.io", sector="My own site",
         role="Hand-built, deployed on every push", stack=["Astro", "Three.js", "GSAP", "GitHub Actions"],
         note="My own site, with a 3D growth terrain in the hero. Green on all three Core Web Vitals, and it "
              "ships JSON-LD, a sitemap, robots.txt and llms.txt.",
         metrics=[("3 of 3", "Core Web Vitals green"), ("CI/CD", "on every push")]),
]

# Smaller index of more client work (static screenshot from the old deck's shots/).
MORE = [
    dict(slug="eccuk", name="Electric Car Chargers UK", url="electriccarchargersuk.co.uk",
         line="Content and SEO for UK commercial EV charging: 14 keywords in Google's top 3, sales up about 70%."),
    dict(slug="acrylate", name="Acrylate", url="acrylate.it",
         line="An Italian online store for personalised gifts, built end to end on my own."),
    dict(slug="ayat", name="Ayat Real Estate", url="ayatrealestate.com",
         line="Development and SEO for one of Ethiopia's largest property developers: organic traffic up about 30%."),
    dict(slug="bluesky", name="Blue Sky Real Estate", url="bluesky.et",
         line="Content strategy and SEO behind the property listing pages."),
    dict(slug="gashuna", name="Gashuna Coffee", url="gashuna.com",
         line="Brand, social media and a full website for an Ethiopian speciality coffee brand."),
]

# Passion projects: shown from the inside, no public links.
PASSION = [
    dict(slug="hermella", tab="Hermella's studio site", kind="Architecture portfolio with a 3D hero",
         title="A portfolio for an architect",
         body="A personal site for an architect. As you scroll, a 3D house turns, splits into its four layers, "
              "then lifts the upper floors away to show the ground plan. Her photo stands inside the model as "
              "the human for scale. After that: a project gallery that tilts in 3D, her quote revealed word by "
              "word, and a downloadable lookbook.",
         how=["React and Vite, with the 3D built in Three.js (React Three Fiber)",
              "The house is generated in code, not a downloaded model",
              "The 3D part loads only when needed, so the page stays fast",
              "Gallery scrolls on desktop and swipes on phones"],
         phone=False),
    dict(slug="amore", tab="Amore Movies", kind="Private app for two, installs on a phone",
         title="A movie night app for a couple",
         body="Two people who can never decide what to watch each swipe on movies. When both like the same one, "
              "the app shows \"It's a match\" on both phones at once and adds it to tonight's shortlist. It also "
              "tracks what they are watching, shows shared taste stats, and has an AI helper that turns a plain "
              "request (\"something funny, under two hours\") into picks with a reason for each.",
         how=["Next.js app that installs to the home screen like a native app",
              "Supabase for login and a shared database; both phones update in about 1.4 seconds",
              "Push notifications sent from the database itself, so they arrive even on bad networks",
              "Each person chooses which alerts they get"],
         shots=["amore-1.png", "amore-2.png", "amore-3.png", "amore-4.png", "amore-5.png"], phone=True),
    dict(slug="jobportal", tab="Job portal", kind="Personal tool: data pipeline with AI",
         title="A job portal that reads the job market for me",
         body="Every morning and evening it pulls new remote jobs from public job feeds and Telegram channels, "
              "keeps only jobs open to someone in Ethiopia, and scores each one against my CVs. It flags stale "
              "and fake-looking posts, shows which skills the best jobs ask for that my CV lacks, and drafts a "
              "tailored cover letter and CV for a job in the background.",
         how=["Python (FastAPI) with HTMX pages and a SQLite database",
              "Runs on a schedule twice a day",
              "AI drafting runs in a background queue, so the page never freezes",
              "Tailored CVs come out as clean PDFs"],
         shots=["jobportal-1.png", "jobportal-2.png", "jobportal-3.png"], phone=False),
]

TOTAL_SITES = "30+"
