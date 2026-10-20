# WORX | Kitchen & Dressing — website

Static one-page site (HTML/CSS/JS, no build step). Open `index.html` in a browser, or host the folder on any static host (GitHub Pages, Netlify, Vercel).

- `index.html` — content
- `styles.css` — styling
- `script.js` — mobile menu, gallery lightbox, scroll effects, WhatsApp quote form (`WHATSAPP_NUMBER` at the top)
- `assets/img/` — logo and photos

Project photos and video live in `assets/img/work/` (each photo has a full-size `name.jpg` and a `name-sm.jpg` thumbnail).

## Arabic version

`ar.html` is the Arabic (right-to-left) page. It is generated from `index.html` — don't edit it by hand. After changing the English page, update the matching English/Arabic pair in `tools/build_ar.py` and run:

    python3 tools/build_ar.py

The script stops with an error if any English text it expects is missing, so nothing is left untranslated by accident.
