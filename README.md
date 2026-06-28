<!--
  ╔══════════════════════════════════════════════════════════════╗
  ║                  S K I L L S Y N C                          ║
  ║           School for What's Ahead — Web Clone               ║
  ╚══════════════════════════════════════════════════════════════╝
-->

<div align="center">
  <img src="Logo.svg" alt="SkillSync Logo" width="160"/>
  <br/><br/>

  <h1>SkillSync · School for What's Ahead</h1>
  <p><em>A teacher-led K–8 model built on mastery in reading, writing, and math.</em></p>

  <p>
    <img src="https://img.shields.io/badge/Built%20With-Webflow-4353FF?style=flat-square&logo=webflow&logoColor=white"/>
    <img src="https://img.shields.io/badge/Language-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
    <img src="https://img.shields.io/badge/Scripts-Python%203-3776AB?style=flat-square&logo=python&logoColor=white"/>
    <img src="https://img.shields.io/badge/Fonts-Open%20Sans-EA4335?style=flat-square&logo=google-fonts&logoColor=white"/>
    <img src="https://img.shields.io/badge/Hosting-GitHub%20Pages-222222?style=flat-square&logo=github-pages&logoColor=white"/>
    <img src="https://img.shields.io/badge/Status-Live-2ECC71?style=flat-square"/>
  </p>

  <br/>

  > **SkillSync** is a high-fidelity static website clone of a modern K-8 educational platform,
  > exported from Webflow and optimized with Python post-processing scripts for local and
  > GitHub Pages hosting.

</div>

---

## 📋 Table of Contents

- [✨ Overview](#-overview)
- [🗂️ Folder Structure](#-folder-structure)
- [🧩 Pages & Features](#-pages--features)
- [🛠️ Tech Stack](#-tech-stack)
- [⚙️ Python Scripts](#-python-scripts)
- [🚀 Quick Start](#-quick-start)
- [🌐 GitHub Pages Deployment](#-github-pages-deployment)
- [🤝 Contributing](#-contributing)

---

## ✨ Overview

SkillSync is built around a simple, powerful philosophy: **safe classrooms, expert teachers, and proven methods** produce the best outcomes for K–8 students. This repository contains the fully functional static export of the site, complete with:

- 🎓 **Mastery-focused curriculum** pages (reading, writing, math)
- 🏫 **Multi-campus school finder** across Miami-Dade, Broward, Phoenix, and more
- 📝 **Admissions & lead capture** forms powered by Webflow
- 📰 **Newsroom** and company timeline
- 🔒 **Legal** and **Terms** pages

---

## 🗂️ Folder Structure

```
SkillSync/
│
├── 📄 index.htm                     # 🏠 Homepage — Hero, Features, CTA
├── 📄 admissions.html               # 📋 Admissions & lead capture forms
├── 📄 approach.html                 # 🧠 Pedagogy & teaching philosophy
├── 📄 careers.html                  # 💼 Open roles & culture page
├── 📄 company.html                  # 🏢 Company timeline & mission
├── 📄 contact.html                  # 📞 Contact & general enquiries
├── 📄 fellowship.html               # 🎓 Teacher fellowship programme
├── 📄 legal.html                    # ⚖️  Legal policies overview
├── 📄 newsroom.html                 # 📰 Press releases & media coverage
├── 📄 real-estate.html              # 🏘️  Real estate & campus info
├── 📄 schools.html                  # 🗺️  School finder & locations
├── 📄 signin.html                   # 🔐 Parent / staff sign-in
├── 📄 tuition.html                  # 💰 Tuition pricing & scholarships
│
├── 🐍 rename_assets.py              # Renames asset files for local paths
├── 🐍 update_svg.py                 # Fixes SVG references post-export
├── 🐍 remove_integrity.py           # Strips SRI hashes for local hosting
│
├── 🖼️  Logo.svg                     # Brand logo (SVG)
├── 🖼️  favicon.ico                  # Browser tab icon
├── 📝 webcopy-origin.txt            # Original Webflow copy reference
│
├── 📁 assets/                       # Primary static assets
│   └── Logo.svg
│
├── 📁 assets_global/                # Shared global assets
│   ├── 🅰️  ABCGintoNord-*.woff2    # Custom brand typography
│   ├── 🌍  *-map.webp              # Campus location maps
│   ├── 🖼️  *.webp / *.png / *.svg  # UI illustrations & icons
│   ├── 📁 css/
│   │   └── *.shared.css            # Global Webflow stylesheet
│   └── 📁 js/
│       └── webflow.*.js            # Webflow runtime & chunk scripts
│
├── 📁 assets_media/                 # High-res campus & classroom photography
│   ├── campus-*.avif               # Campus images (multiple resolutions)
│   ├── 102825-NEWKID-*.avif        # Professional classroom photography
│   └── company-timeline-*.avif     # Company history images
│
├── 📁 assets_site/                  # Page-specific assets
│   ├── 📁 css/
│   │   └── skillsync-*.min.css     # Minified page CSS
│   ├── Favicon.png
│   └── webclip.png
│
├── 📁 ajax/                         # CDN-mirrored JavaScript libraries
│   └── libs/
│       ├── jquery/3.6.3/           # jQuery (locally served)
│       └── webfont/1.6.26/         # Google WebFont Loader
│
├── 📁 api/                          # Embedded media API
│   └── player.js                   # Video player integration
│
├── 📁 fonts/                        # Self-hosted web fonts
├── 📁 img/                          # Miscellaneous images
├── 📁 js/                           # Additional JavaScript modules
├── 📁 grades/                       # Grade-level sub-pages
├── 📁 schools/                      # Individual school detail pages
├── 📁 states/                       # State-specific landing pages
├── 📁 legal/                        # Legal document sub-pages
├── 📁 news/                         # Newsroom article pages
├── 📁 p/                            # Short-form / campaign landing pages
├── 📁 static/                       # Next.js / static output artefacts
├── 📁 _next/                        # Next.js build output (if applicable)
├── 📁 npm/                          # Locally vendored npm packages
└── 📁 concierge-js/                 # Concierge form-handling scripts
```

---

## 🧩 Pages & Features

| Page | Route | Description |
|------|-------|-------------|
| **Homepage** | `index.htm` | Hero section, feature highlights, campus map, testimonials |
| **Admissions** | `admissions.html` | Lead capture forms with Webflow form integration |
| **Our Approach** | `approach.html` | Pedagogy, curriculum model, mastery framework |
| **Tuition** | `tuition.html` | Pricing tiers, scholarship options, FAQ |
| **Schools** | `schools.html` | Interactive campus finder, city/state filter |
| **Newsroom** | `newsroom.html` | Press releases, media mentions, blog |
| **Careers** | `careers.html` | Open roles, culture page, teacher fellowship |
| **Company** | `company.html` | Mission, history timeline, leadership team |
| **Fellowship** | `fellowship.html` | Teacher training & development programme |
| **Contact** | `contact.html` | Contact form, office locations |
| **Sign In** | `signin.html` | Parent/staff authentication page |
| **Legal** | `legal.html` | Privacy policy, terms of service |

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **HTML5** | Semantic page structure (Webflow export) |
| **CSS3** | Responsive, utility-first styles via Webflow |
| **JavaScript ES6+** | Animations, form handling, lazy-loading |
| **jQuery 3.6.3** | DOM manipulation (locally vendored) |
| **Webflow.js** | Webflow interactions & CMS runtime |
| **Python 3** | Post-export asset optimisation scripts |
| **AVIF / WebP** | Next-gen image formats for performance |
| **WOFF2** | Self-hosted custom typography |
| **Open Sans** | Body typography via Google Fonts |

---

## ⚙️ Python Scripts

Three utility scripts handle the gap between a Webflow export and a locally hostable static site:

### `rename_assets.py`
Renames all hashed asset filenames to human-readable equivalents and updates all HTML references accordingly. Run this immediately after exporting from Webflow.

```bash
python rename_assets.py
```

### `update_svg.py`
Patches inline `<use>` references and SVG `href` paths that break when served outside the Webflow CDN.

```bash
python update_svg.py
```

### `remove_integrity.py`
Strips `integrity=""` and `crossorigin=""` attributes from `<link>` and `<script>` tags — required when assets are self-hosted rather than served from their original CDN origin.

```bash
python remove_integrity.py
```

> **Recommended order:** `rename_assets.py` → `update_svg.py` → `remove_integrity.py`

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Mausam5055/skillsync.git
cd skillsync
```

### 2. (Optional) Re-run post-processing scripts
Only needed if you've pulled a fresh Webflow export:
```bash
python rename_assets.py
python update_svg.py
python remove_integrity.py
```

### 3. Serve locally

**Using Python:**
```bash
python -m http.server 8000
# Visit → http://localhost:8000
```

**Using Node (npx):**
```bash
npx serve .
# Visit → http://localhost:3000
```

**Using VS Code:**
Install the [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension → right-click `index.htm` → **Open with Live Server**

---

## 🌐 GitHub Pages Deployment

This repo is configured for zero-config GitHub Pages hosting:

1. **Push** your code to `main` branch
2. Go to **Settings → Pages**
3. Set **Source** → `Deploy from a branch` → `main` → `/ (root)`
4. Click **Save** — your site goes live at:

```
https://Mausam5055.github.io/skillsync/
```

> No build step required. All assets are pre-compiled and statically served.

---

## 🤝 Contributing

Contributions, improvements, and bug reports are welcome!

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a **Pull Request**

---

<div align="center">
  <br/>
  <sub>Built with ❤️ by <a href="https://github.com/Mausam5055">Mausam5055</a> · Empowering the next generation of learners</sub>
  <br/><br/>
  <img src="https://img.shields.io/badge/K--8%20Education-Mastery%20First-4353FF?style=for-the-badge"/>
</div>
