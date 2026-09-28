# -*- coding: utf-8 -*-
import os, json, html
from gen_data import BIZ, SERVICES, REGIONS, SUBURBS, NEARBY_MAP, ICONS, LOCAL_LISTINGS

ROOT = os.path.dirname(os.path.abspath(__file__))

SUBURB_BY_SLUG = {s[0]: s for s in SUBURBS}
SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

REGION_ORDER = ["bayside", "inner-south-east", "south-east", "mornington-peninsula"]

def region_suburbs(region_key):
    return [s for s in SUBURBS if s[3] == region_key]

# ---------------------------------------------------------------- helpers

def esc(s):
    return html.escape(s, quote=True)

def nav_link(href, label, current):
    is_current = href.split("/")[-1] == current
    cls = ' aria-current="page"' if is_current else ''
    return f'<a href="{href}"{cls}>{label}</a>'

def base_path(depth):
    """depth=0 for root, 1 for /services/ or /areas/ pages."""
    return "" if depth == 0 else "../"

def header_html(current, depth=0, page_title_area=None, nap=None):
    bp = base_path(depth)
    phone_tel = nap["phone_tel"] if nap else BIZ["phone_tel"]
    phone_disp = nap["phone_display"] if nap else BIZ["phone_display"]
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<div class="top-strip">
  <div class="wrap">
    <div>Servicing Bayside, Inner South-East, South-East &amp; the Mornington Peninsula &mdash; <strong>licensed &amp; insured</strong></div>
    <div><a href="tel:{phone_tel}">Call now: <strong>{phone_disp}</strong></a> &nbsp;|&nbsp; <strong>Open 24/7 for emergencies</strong></div>
  </div>
</div>
<header class="site-header">
  <div class="wrap header-row">
    <a class="logo" href="{bp}index.html">
      <img class="brand-logo" src="{bp}images/southbay-plumber-logo.png" alt="South Bay Plumber">
    </a>
    <nav class="primary-nav" aria-label="Primary">
      {nav_link(bp+"index.html","Home",current)}
      {nav_link(bp+"services.html","Services",current)}
      {nav_link(bp+"service-areas.html","Service Areas",current)}
      {nav_link(bp+"about.html","About",current)}
      {nav_link(bp+"contact.html","Contact",current)}
    </nav>
    <div class="header-cta">
      <div class="phone-cta">
        <span class="label">Call now &mdash; 24/7</span>
        <a href="tel:{phone_tel}">{phone_disp}</a>
      </div>
      <a class="btn btn-teal btn-sm" href="{bp}contact.html">Get a quote</a>
      <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18M3 12h18M3 18h18" stroke-linecap="round"/></svg>
      </button>
    </div>
  </div>
</header>
'''

def footer_html(depth=0, nap=None, include_address=True):
    bp = base_path(depth)
    phone_tel = nap["phone_tel"] if nap else BIZ["phone_tel"]
    phone_disp = nap["phone_display"] if nap else BIZ["phone_display"]
    contact_name = nap["gmb_name"] if nap else BIZ["name"]
    contact_email = BIZ["email"]
    if nap:
        contact_addr = f'{nap["street"]}, {nap["locality"]} VIC {nap["postcode"]}'
    elif include_address:
        contact_addr = f'{BIZ["address_street"]}, {BIZ["address_locality"]} {BIZ["address_region"]} {BIZ["postal_code"]}'
    else:
        contact_addr = None

    service_links = "\n".join(
        f'<li><a href="{bp}services/{s["slug"]}.html">{esc(s["name"])}</a></li>' for s in SERVICES[:8]
    )
    company_links = f'''<li><a href="{bp}about.html">About Us</a></li>
    <li><a href="{bp}service-areas.html">Service Areas</a></li>
    <li><a href="{bp}services.html">All Services</a></li>
    <li><a href="{bp}contact.html">Contact &amp; Quotes</a></li>'''

    area_chips = "\n".join(
        f'<a class="chip" href="{bp}areas/{slug}.html">{esc(name)}</a>'
        for slug, name, pc, region, land in SUBURBS
    )

    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="logo" href="{bp}index.html" style="color:#fff;">
          <svg class="mark" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="17" cy="17" r="16" fill="#F1EAD9"/>
            <path d="M17 8c4.5 5.1 7.6 9.6 7.6 13.2a7.6 7.6 0 0 1-15.2 0C9.4 17.6 12.5 13.1 17 8Z" fill="#1C7A72"/>
          </svg>
          <span>South Bay Plumber</span>
        </a>
        <p>Licensed plumbers servicing Bayside, the Inner South-East, the South-East growth corridor
        and the Mornington Peninsula. Founded {esc(BIZ["founded"])}.</p>
      </div>
      <div>
        <h4>Popular Services</h4>
        <ul>{service_links}</ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>{company_links}</ul>
      </div>
      <div>
        <h4>Get in Touch{" &mdash; " + esc(contact_name) if nap else ""}</h4>
        <ul>
          <li><a href="tel:{phone_tel}">{phone_disp}</a></li>
          <li><a href="mailto:{contact_email}">{contact_email}</a></li>
          {f'<li>{esc(contact_addr)}</li>' if contact_addr else ''}
          <li>Open 24/7 for emergency calls</li>
        </ul>
      </div>
    </div>
    <div class="footer-areas">
      <h4>All Service Areas</h4>
      <div class="chip-row">
        {area_chips}
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; {esc(BIZ["founded"])}&ndash;2026 {esc(BIZ["name"])}. All rights reserved.</div>
      <div><a href="{bp}contact.html">Privacy Policy</a> &middot; <a href="{bp}contact.html">Terms of Service</a></div>
    </div>
  </div>
</footer>
<script src="{bp}js/main.js"></script>
'''

def page_shell(*, title, description, canonical_path, depth, current, body, schema_blocks, og_type="website", nap=None, footer_address=True):
    bp = base_path(depth)
    schema_json = "\n".join(
        f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in schema_blocks
    )
    return f'''<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{BIZ["url"]}/{canonical_path}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{BIZ["url"]}/{canonical_path}">
<meta property="og:site_name" content="{esc(BIZ["name"])}">
<meta property="og:locale" content="en_AU">
<meta name="twitter:card" content="summary">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{bp}css/styles.css">
{schema_json}
</head>
<body>
{header_html(current, depth, nap=nap)}
<main id="main">
{body}
</main>
{footer_html(depth, nap=nap, include_address=footer_address)}
</body>
</html>'''

def local_business_schema(extra_area=None, nap=None):
    areas = extra_area if extra_area else [name for slug, name, pc, region, land in SUBURBS]
    if nap:
        biz_name = nap["gmb_name"]
        telephone = nap["phone_tel"]
        address = {
            "@type": "PostalAddress",
            "streetAddress": nap["street"],
            "addressLocality": nap["locality"],
            "addressRegion": "VIC",
            "postalCode": nap["postcode"],
            "addressCountry": "AU",
        }
    else:
        biz_name = BIZ["name"]
        telephone = BIZ["phone_tel"]
        address = {
            "@type": "PostalAddress",
            "streetAddress": BIZ["address_street"],
            "addressLocality": BIZ["address_locality"],
            "addressRegion": BIZ["address_region"],
            "postalCode": BIZ["postal_code"],
            "addressCountry": "AU",
        }
    return {
        "@context": "https://schema.org",
        "@type": "Plumber",
        "name": biz_name,
        "image": f'{BIZ["url"]}/images/southbay-plumber-logo.png',
        "url": BIZ["url"],
        "telephone": telephone,
        "email": BIZ["email"],
        "priceRange": "$$",
        "address": address,
        **({
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": nap["lat"],
                "longitude": nap["lng"],
            }
        } if nap and "lat" in nap and "lng" in nap else ({
            "geo": {"@type": "GeoCoordinates", "latitude": BIZ["lat"], "longitude": BIZ["lng"]}
        } if not nap else {})),
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens": "00:00", "closes": "23:59",
        }],
        "areaServed": [{"@type": "City", "name": a} for a in areas],
        "sameAs": [],
    }

def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i+1, "name": name, "item": f'{BIZ["url"]}/{path}'}
            for i, (name, path) in enumerate(items)
        ],
    }

def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }

def breadcrumb_html(items):
    parts = []
    for i, (name, path) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{esc(name)}</span>')
        else:
            parts.append(f'<a href="{path}">{esc(name)}</a><span>/</span>')
    return f'<div class="wrap breadcrumb">{" ".join(parts)}</div>'

def icon(key):
    return ICONS.get(key, ICONS["drop"])

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ---------------------------------------------------------------- HOME PAGE

def build_home():
    services_cards = "\n".join(f'''
      <div class="card">
        <svg class="icon">{icon(s["icon"])}</svg>
        <h3>{esc(s["name"])}</h3>
        <p>{esc(s["short"])}</p>
        <a class="more" href="services/{s["slug"]}.html">View service &rsaquo;</a>
      </div>''' for s in SERVICES)

    region_blocks = ""
    for rkey in REGION_ORDER:
        subs = region_suburbs(rkey)
        chips = "\n".join(f'<a class="chip" href="areas/{slug}.html">{esc(name)}</a>' for slug, name, pc, rg, land in subs)
        region_blocks += f'''
        <div class="region-block">
          <h3>{esc(REGIONS[rkey]["label"])}</h3>
          <div class="chip-row">{chips}</div>
        </div>'''

    body = f'''
<section class="hero">
  <div class="wrap">
    <div>
      <div class="eyebrow">Licensed &amp; insured &middot; 24/7 emergency callouts</div>
      <h1>Southern Melbourne's local plumber, on call day and night.</h1>
      <p class="lede">From a blocked drain in Brighton to a new hot water system in Cranbourne,
      South Bay Plumber covers Bayside, the Inner South-East, the South-East growth corridor and
      the Mornington Peninsula &mdash; with a real local answering the phone.</p>
      <div class="cta-row">
        <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
        <a class="btn btn-ghost-light" href="contact.html">Get a free quote</a>
      </div>
      <div class="badges">
        <div><strong>24/7</strong>Emergency response</div>
        <div><strong>38</strong>Suburbs covered</div>
        <div><strong>{esc(BIZ["founded"])}</strong>Serving locally since</div>
      </div>
    </div>
  </div>
</section>

<div class="trust-bar">
  <div class="wrap">
    <div class="item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 4 6v6c0 5 3.4 8.7 8 9 4.6-.3 8-4 8-9V6l-8-3Z" stroke-linejoin="round"/></svg>Licensed &amp; fully insured</div>
    <div class="item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2" stroke-linecap="round"/></svg>24/7 emergency response</div>
    <div class="item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 12h16M4 12l5-5M4 12l5 5" stroke-linecap="round" stroke-linejoin="round"/></svg>Upfront, no-surprise pricing</div>
    <div class="item"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m4 12 5 5L20 6" stroke-linecap="round" stroke-linejoin="round"/></svg>Workmanship guarantee</div>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">What we do</div>
      <h2>Plumbing services across the southern suburbs</h2>
      <p>From urgent repairs to full renovation plumbing, our team handles residential and
      commercial jobs across Bayside, the Inner South-East, the South-East and the Mornington
      Peninsula.</p>
    </div>
    <div class="grid-services">
      {services_cards}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Where we work</div>
      <h2>Serving 38 suburbs across four southern Melbourne regions</h2>
      <p>Local knowledge matters &mdash; from salt-air corrosion on the coast to original pipework in
      period inner south-east homes to slab plumbing in newer estates. Find your suburb below.</p>
    </div>
    {region_blocks}
    <a class="btn btn-outline" href="service-areas.html">View all service areas</a>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">How it works</div>
      <h2>Simple, straightforward, no surprises</h2>
    </div>
    <div class="steps">
      <div class="step"><span class="num">1</span><h3>Call or request a quote</h3><p>Tell us what's going on &mdash; we'll ask a few questions to send the right plumber with the right gear.</p></div>
      <div class="step"><span class="num">2</span><h3>We confirm a time</h3><p>Same-day and emergency slots available across all 38 suburbs we cover.</p></div>
      <div class="step"><span class="num">3</span><h3>Upfront pricing</h3><p>You'll know the cost before any work starts &mdash; no surprises on the invoice.</p></div>
      <div class="step"><span class="num">4</span><h3>Job done properly</h3><p>Backed by our workmanship guarantee and a tidy, respectful crew.</p></div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Local reviews</div>
      <h2>What southern suburbs homeowners say</h2>
    </div>
    <div class="testi-grid">
      <div class="testi"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Called about a blocked drain on a Sunday afternoon and someone was at our Mentone place within the hour. Fixed and explained everything clearly."</p><footer>Kirat &mdash; Mentone</footer></div>
      <div class="testi"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Replaced our old hot water system in Berwick the same day it died. Gave us a proper quote first, no pressure to upgrade more than we needed."</p><footer>Annie &mdash; Berwick</footer></div>
      <div class="testi"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>"Used them for the plumbing on our Camberwell bathroom reno. Turned up when they said they would, tidy work, easy to deal with."</p><footer>Ramona &mdash; Camberwell</footer></div>
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <div>
      <h2>Need a plumber today?</h2>
      <p>Our team covers all 38 southern Melbourne suburbs, 24 hours a day.</p>
    </div>
    <div class="cta-row" style="margin:0;">
      <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="contact.html">Request a quote</a>
    </div>
  </div>
</section>
'''
    schema = [
        local_business_schema(),
        breadcrumb_schema([("Home", "")]),
    ]
    html_out = page_shell(
        title="South Bay Plumber | Licensed Plumber Servicing Southern Melbourne",
        description="Licensed 24/7 plumber servicing Bayside, Inner South-East, South-East and the "
                     "Mornington Peninsula. Blocked drains, hot water, gas fitting, leak detection & "
                     "emergency plumbing across 38 southern Melbourne suburbs.",
        canonical_path="",
        depth=0, current="index.html", body=body, schema_blocks=schema,
    )
    write("index.html", html_out)

# ---------------------------------------------------------------- SERVICES INDEX

def build_services_index():
    cards = "\n".join(f'''
      <div class="card">
        <svg class="icon">{icon(s["icon"])}</svg>
        <h3>{esc(s["name"])}</h3>
        <p>{esc(s["short"])}</p>
        <a class="more" href="services/{s["slug"]}.html">View service &rsaquo;</a>
      </div>''' for s in SERVICES)

    body = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="tag">All Services</span>
    <h1>Plumbing services across southern Melbourne</h1>
    <p>Licensed, insured and available 24/7 for emergencies across Bayside, the Inner South-East,
    the South-East growth corridor and the Mornington Peninsula.</p>
  </div>
</section>
{breadcrumb_html([("Home","index.html"),("Services","services.html")])}
<section>
  <div class="wrap">
    <div class="grid-services">
      {cards}
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <div><h2>Not sure which service you need?</h2><p>Call us and describe the problem &mdash; we'll point you in the right direction, no obligation.</p></div>
    <div class="cta-row" style="margin:0;">
      <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="contact.html">Request a quote</a>
    </div>
  </div>
</section>
'''
    schema = [breadcrumb_schema([("Home",""),("Services","services.html")])]
    html_out = page_shell(
        title="Plumbing Services | South Bay Plumber",
        description="Browse all plumbing services from South Bay Plumber: blocked drains, hot water "
                     "systems, gas fitting, leak detection, emergency plumbing and more across "
                     "southern Melbourne.",
        canonical_path="services.html", depth=0, current="services.html", body=body, schema_blocks=schema,
    )
    write("services.html", html_out)

# ---------------------------------------------------------------- SERVICE PAGES

def build_service_pages():
    for s in SERVICES:
        bullets = "\n".join(f"<li style='margin-bottom:10px;padding-left:26px;position:relative;color:var(--ink-soft);'><span style='position:absolute;left:0;color:var(--teal-600);font-weight:700;'>&#10003;</span>{esc(b)}</li>" for b in s["bullets"])
        faqs = "\n".join(f'''
        <details class="faq-item">
          <summary>{esc(q)}<span class="plus">+</span></summary>
          <p>{esc(a)}</p>
        </details>''' for q, a in s["faqs"])

        related = [o for o in SERVICES if o["slug"] != s["slug"]][:3]
        related_html = "\n".join(f'''
          <div class="card">
            <svg class="icon">{icon(o["icon"])}</svg>
            <h3>{esc(o["name"])}</h3>
            <p>{esc(o["short"])}</p>
            <a class="more" href="{o["slug"]}.html">View service &rsaquo;</a>
          </div>''' for o in related)

        area_chips = "\n".join(f'<a class="chip" href="../areas/{slug}.html">{esc(name)}</a>' for slug, name, pc, region, land in SUBURBS)

        body = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="tag">Service</span>
    <h1>{esc(s["name"])}</h1>
    <p>{esc(s["short"])}</p>
    <div class="cta-row" style="margin-top:22px;">
      <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-ghost-light" href="../contact.html">Get a free quote</a>
    </div>
  </div>
</section>
{breadcrumb_html([("Home","../index.html"),("Services","../services.html"),(s["name"], f'services/{s["slug"]}.html')])}

<section>
  <div class="wrap split">
    <div>
      <h2>{esc(s["name"])} across southern Melbourne</h2>
      <p>{esc(s["intro"])}</p>
      <ul>{bullets}</ul>
    </div>
    <div class="split-media">
      <div class="card" style="background:var(--sand-100);border:none;">
        <h3>Why locals choose South Bay Plumber</h3>
        <ul>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Licensed &amp; fully insured team</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Upfront pricing before work starts</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Local to Bayside, Inner South-East, South-East &amp; the Peninsula</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">24/7 availability for genuine emergencies</li>
          <li style="color:var(--ink-soft);">Workmanship guarantee on every job</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">FAQs</div>
      <h2>Common questions about {esc(s["name"].lower())}</h2>
    </div>
    {faqs}
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Coverage</div>
      <h2>{esc(s["name"])} in your suburb</h2>
      <p>We provide {esc(s["name"].lower())} across all of the suburbs below &mdash; select yours for local contact details and response times.</p>
    </div>
    <div class="chip-row">
      {area_chips}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Related services</div>
      <h2>You might also need</h2>
    </div>
    <div class="grid-services">
      {related_html}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <div><h2>Book {esc(s["name"].lower())} today</h2><p>Call now or request a free, no-obligation quote online.</p></div>
    <div class="cta-row" style="margin:0;">
      <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="../contact.html">Request a quote</a>
    </div>
  </div>
</section>
'''
        schema = [
            {
                "@context": "https://schema.org",
                "@type": "Service",
                "serviceType": s["name"],
                "name": f'{s["name"]} | {BIZ["name"]}',
                "description": s["short"],
                "provider": {"@type": "Plumber", "name": BIZ["name"], "telephone": BIZ["phone_tel"], "url": BIZ["url"]},
                "areaServed": [{"@type": "City", "name": name} for slug, name, pc, region, land in SUBURBS],
            },
            faq_schema(s["faqs"]),
            breadcrumb_schema([("Home",""),("Services","services.html"),(s["name"], f'services/{s["slug"]}.html')]),
        ]
        html_out = page_shell(
            title=f'{s["name"]} Southern Melbourne | {BIZ["name"]}',
            description=f'{s["short"]} Licensed & insured, 24/7 availability across Bayside, Inner South-East, South-East & the Mornington Peninsula.',
            canonical_path=f'services/{s["slug"]}.html', depth=1, current="services.html", body=body, schema_blocks=schema,
        )
        write(f'services/{s["slug"]}.html', html_out)

# ---------------------------------------------------------------- SERVICE AREAS INDEX

def build_areas_index():
    region_blocks = ""
    for rkey in REGION_ORDER:
        subs = region_suburbs(rkey)
        chips = "\n".join(
            f'<a class="chip" href="areas/{slug}.html">{esc(name)} <span style="color:var(--ink-soft);font-weight:400;">{pc}</span>{" &middot; local office" if slug in LOCAL_LISTINGS else ""}</a>'
            for slug, name, pc, rg, land in subs
        )
        region_blocks += f'''
        <div class="region-block">
          <h3>{esc(REGIONS[rkey]["label"])} <span style="font-weight:400;color:var(--ink-soft);">({len(subs)} suburbs)</span></h3>
          <p style="max-width:70ch;">{esc(REGIONS[rkey]["pain"])}</p>
          <div class="chip-row">{chips}</div>
        </div>'''

    body = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="tag">Service Areas</span>
    <h1>38 suburbs across southern Melbourne</h1>
    <p>We cover Bayside, the Inner South-East, the South-East growth corridor and the Mornington
    Peninsula. Select your suburb for local response times and contact details.</p>
  </div>
</section>
{breadcrumb_html([("Home","index.html"),("Service Areas","service-areas.html")])}
<section>
  <div class="wrap">
    {region_blocks}
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <div><h2>Don't see your suburb?</h2><p>Call us anyway &mdash; we often cover surrounding streets too.</p></div>
    <div class="cta-row" style="margin:0;">
      <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="contact.html">Request a quote</a>
    </div>
  </div>
</section>
'''
    schema = [breadcrumb_schema([("Home",""),("Service Areas","service-areas.html")])]
    html_out = page_shell(
        title="Service Areas | South Bay Plumber Southern Melbourne",
        description="South Bay Plumber services 38 suburbs across Bayside, Inner South-East, "
                     "South-East and the Mornington Peninsula. Find your local plumber.",
        canonical_path="service-areas.html", depth=0, current="service-areas.html", body=body, schema_blocks=schema,
    )
    write("service-areas.html", html_out)

# ---------------------------------------------------------------- SUBURB PAGES

def build_suburb_pages():
    for slug, name, pc, region_key, landmark in SUBURBS:
        region = REGIONS[region_key]
        nap = LOCAL_LISTINGS.get(slug)  # dedicated GMB listing, if one exists yet
        phone_tel = nap["phone_tel"] if nap else BIZ["phone_tel"]
        phone_disp = nap["phone_display"] if nap else BIZ["phone_display"]

        nearby_slugs = NEARBY_MAP.get(slug, [])
        nearby_html = "\n".join(
            f'<a class="chip" href="{n}.html">{esc(SUBURB_BY_SLUG[n][1])}</a>' for n in nearby_slugs if n in SUBURB_BY_SLUG
        )

        service_cards = "\n".join(f'''
          <div class="card">
            <svg class="icon">{icon(s["icon"])}</svg>
            <h3>{esc(s["name"])} in {esc(name)}</h3>
            <p>{esc(s["short"])}</p>
            <a class="more" href="../services/{s["slug"]}.html">View service &rsaquo;</a>
          </div>''' for s in SERVICES[:6])

        faqs = [
            (f"How quickly can a plumber reach {name}?",
             f"We aim to have a plumber on the way to {name} within the hour for genuine emergencies "
             f"such as burst pipes or total blockages, and can typically offer same-day appointments "
             f"for standard repairs."),
            (f"Do you charge extra for {name} because it's further from the depot?",
             f"No &mdash; {name} sits within our standard {region['label']} coverage area, so there's no "
             f"call-out surcharge for being further out."),
            (f"What plumbing issues are common in {name}?",
             f"{region['pain']} We focus on {region['focus']} for {name} properties specifically."),
        ]

        faq_html = "\n".join(f'''
        <details class="faq-item">
          <summary>{esc(q)}<span class="plus">+</span></summary>
          <p>{a}</p>
        </details>''' for q, a in faqs)

        # "at a glance" card: swap in real local-office NAP when this suburb has
        # its own dedicated GMB listing, otherwise show the general coverage info
        if nap:
            glance_card = f'''
      <div class="card" style="background:var(--sand-100);border:none;">
        <h3>{esc(nap["gmb_name"])}</h3>
        <ul>
          <li style="margin-bottom:10px;color:var(--ink-soft);">{esc(nap["street"])}, {esc(nap["locality"])} VIC {esc(nap["postcode"])}</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Phone: <a href="tel:{phone_tel}">{phone_disp}</a></li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Region: {esc(region["label"])}</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">24/7 emergency callouts available</li>
          <li style="color:var(--ink-soft);">Same-day appointments, subject to availability</li>
        </ul>
      </div>'''
        else:
            glance_card = f'''
      <div class="card" style="background:var(--sand-100);border:none;">
        <h3>{esc(name)} at a glance</h3>
        <ul>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Postcode: {esc(pc)}</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Region: {esc(region["label"])}</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Landmark: {esc(landmark)}</li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">24/7 emergency callouts available</li>
          <li style="color:var(--ink-soft);">Same-day appointments, subject to availability</li>
        </ul>
      </div>'''

        body = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="tag">{esc(region["label"])} &middot; {esc(pc)}</span>
    <h1>Plumber in {esc(name)}</h1>
    <p>Licensed, local plumbing for {esc(name)} and the surrounding streets near {esc(landmark)}.
    Same-day appointments and 24/7 emergency response.</p>
    <div class="cta-row" style="margin-top:22px;">
      <a class="btn btn-signal" href="tel:{phone_tel}">Call {phone_disp}</a>
      <a class="btn btn-ghost-light" href="../contact.html">Get a free quote</a>
    </div>
  </div>
</section>
{breadcrumb_html([("Home","../index.html"),("Service Areas","../service-areas.html"),(name, f'areas/{slug}.html')])}

<section>
  <div class="wrap split">
    <div>
      <h2>Your local {esc(name)} plumber</h2>
      <p>South Bay Plumber has been servicing {esc(name)} and the wider {esc(region["label"])} area
      since {esc(BIZ["founded"])}. {region["pain"]} Our team knows the area well, from the streets
      around {esc(landmark)} to the newer pockets nearby, and focuses on {region["focus"]}.</p>
      <p>Whether it's a blocked drain, no hot water, a gas fitting job or a full bathroom renovation,
      we send a licensed plumber who already knows what {esc(name)} properties tend to need.</p>
    </div>
    <div class="split-media">
      {glance_card}
    </div>
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Services in {esc(name)}</div>
      <h2>Popular plumbing services in {esc(name)}</h2>
    </div>
    <div class="grid-services">
      {service_cards}
    </div>
    <a class="btn btn-outline" href="../services.html" style="margin-top:8px;">View all services</a>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">FAQs</div>
      <h2>{esc(name)} plumbing questions</h2>
    </div>
    {faq_html}
  </div>
</section>

<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Nearby</div>
      <h2>We also service these nearby suburbs</h2>
    </div>
    <div class="nearby-list">
      {nearby_html}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="wrap">
    <div><h2>Need a {esc(name)} plumber?</h2><p>Call now or request a free quote &mdash; we cover {esc(name)} 24 hours a day.</p></div>
    <div class="cta-row" style="margin:0;">
      <a class="btn btn-signal" href="tel:{phone_tel}">Call {phone_disp}</a>
      <a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="../contact.html">Request a quote</a>
    </div>
  </div>
</section>
'''
        schema = [
            local_business_schema(extra_area=[name], nap=nap),
            faq_schema([(q, a.replace("&mdash;", "-")) for q, a in faqs]),
            breadcrumb_schema([("Home",""),("Service Areas","service-areas.html"),(name, f'areas/{slug}.html')]),
        ]
        display_biz_name = nap["gmb_name"] if nap else BIZ["name"]
        html_out = page_shell(
            title=f'Plumber in {name} VIC {pc} | {display_biz_name}',
            description=f'Licensed local plumber servicing {name} {pc} and surrounding {region["label"]} '
                         f'suburbs. Blocked drains, hot water, gas fitting & 24/7 emergency repairs.',
            canonical_path=f'areas/{slug}.html', depth=1, current="service-areas.html", body=body, schema_blocks=schema,
            nap=nap,
            footer_address=bool(nap),
        )
        write(f'areas/{slug}.html', html_out)

# ---------------------------------------------------------------- ABOUT PAGE

def build_about():
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="tag">About Us</span>
    <h1>Local plumbers, southern Melbourne born and based</h1>
    <p>South Bay Plumber has been servicing Bayside, the Inner South-East, the South-East and the
    Mornington Peninsula since {esc(BIZ["founded"])}.</p>
  </div>
</section>
{breadcrumb_html([("Home","index.html"),("About","about.html")])}
<section>
  <div class="wrap split">
    <div>
      <h2>Why we started South Bay Plumber</h2>
      <p>Too many southern suburbs homeowners were being sent plumbers from the other side of the
      city who didn't know the difference between original bluestone-era pipework in Malvern and
      the slab plumbing going into new Cranbourne estates. We built a team that lives and works
      across the same 38 suburbs we service, so the plumber who answers your call already
      understands the property types and common issues in your street.</p>
      <p>Every job is backed by a workmanship guarantee, upfront pricing before any work starts,
      and a licensed, insured team &mdash; whether it's a five-minute tap washer or a full renovation
      re-pipe.</p>
    </div>
    <div class="split-media">
      <div class="card" style="background:var(--sand-100);border:none;">
        <h3>Credentials</h3>
        <ul>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Fully insured &amp; workmanship guaranteed</li>
          <li style="color:var(--ink-soft);">Servicing southern Melbourne since {esc(BIZ["founded"])}</li>
        </ul>
      </div>
    </div>
  </div>
</section>
<section class="alt">
  <div class="wrap">
    <div class="section-head">
      <div class="kicker">Our approach</div>
      <h2>What you can expect</h2>
    </div>
    <div class="steps">
      <div class="step"><span class="num">1</span><h3>Real people answer</h3><p>No overseas call centre &mdash; a local team member takes your call.</p></div>
      <div class="step"><span class="num">2</span><h3>Upfront pricing</h3><p>You approve the price before any work begins.</p></div>
      <div class="step"><span class="num">3</span><h3>Local knowledge</h3><p>We know the property types and common issues across every suburb we cover.</p></div>
      <div class="step"><span class="num">4</span><h3>Guaranteed work</h3><p>Every job is backed by our workmanship guarantee.</p></div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="wrap">
    <div><h2>Get in touch</h2><p>Call now or send us your details for a free quote.</p></div>
    <div class="cta-row" style="margin:0;">
      <a class="btn btn-signal" href="tel:{BIZ["phone_tel"]}">Call {BIZ["phone_display"]}</a>
      <a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="contact.html">Request a quote</a>
    </div>
  </div>
</section>
'''
    schema = [breadcrumb_schema([("Home",""),("About","about.html")])]
    html_out = page_shell(
        title="About Us | South Bay Plumber",
        description="South Bay Plumber is a licensed, insured plumbing team servicing 38 suburbs "
                     "across southern Melbourne since " + BIZ["founded"] + ".",
        canonical_path="about.html", depth=0, current="about.html", body=body, schema_blocks=schema,
    )
    write("about.html", html_out)

# ---------------------------------------------------------------- CONTACT PAGE

def build_contact():
    body = f'''
<section class="page-hero">
  <div class="wrap">
    <span class="tag">Contact</span>
    <h1>Get a free quote or call now</h1>
    <p>Available 24/7 for emergencies across Bayside, the Inner South-East, the South-East and the
    Mornington Peninsula.</p>
  </div>
</section>
{breadcrumb_html([("Home","index.html"),("Contact","contact.html")])}
<section>
  <div class="wrap split">
    <div>
      <h2>Request a quote</h2>
      <p>Fill in a few details and we'll get back to you &mdash; or call {BIZ["phone_display"]} for
      anything urgent.</p>
      <form>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">
          <div><label style="font-size:.85rem;font-weight:600;display:block;margin-bottom:6px;">First name</label><input type="text" required style="width:100%;padding:11px;border:1px solid var(--line);border-radius:var(--radius);font-family:var(--sans);"></div>
          <div><label style="font-size:.85rem;font-weight:600;display:block;margin-bottom:6px;">Last name</label><input type="text" required style="width:100%;padding:11px;border:1px solid var(--line);border-radius:var(--radius);font-family:var(--sans);"></div>
        </div>
        <div style="margin-bottom:16px;"><label style="font-size:.85rem;font-weight:600;display:block;margin-bottom:6px;">Phone</label><input type="tel" required style="width:100%;padding:11px;border:1px solid var(--line);border-radius:var(--radius);font-family:var(--sans);"></div>
        <div style="margin-bottom:16px;"><label style="font-size:.85rem;font-weight:600;display:block;margin-bottom:6px;">Suburb</label><input type="text" required style="width:100%;padding:11px;border:1px solid var(--line);border-radius:var(--radius);font-family:var(--sans);"></div>
        <div style="margin-bottom:16px;"><label style="font-size:.85rem;font-weight:600;display:block;margin-bottom:6px;">What do you need help with?</label><textarea rows="4" style="width:100%;padding:11px;border:1px solid var(--line);border-radius:var(--radius);font-family:var(--sans);"></textarea></div>
        <button type="submit" class="btn btn-signal">Request a quote</button>
        <p style="font-size:.78rem;margin-top:10px;">Form is a static placeholder &mdash; connect it to your booking system or a form service (e.g. Formspree) before launch.</p>
      </form>
    </div>
    <div class="split-media">
      <div class="card" style="background:var(--sand-100);border:none;">
        <h3>Contact details</h3>
        <ul>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Phone: <a href="tel:{BIZ["phone_tel"]}">{BIZ["phone_display"]}</a></li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">Email: <a href="mailto:{BIZ["email"]}">{BIZ["email"]}</a></li>
          <li style="margin-bottom:10px;color:var(--ink-soft);">{esc(BIZ["address_street"])}, {esc(BIZ["address_locality"])} {esc(BIZ["address_region"])} {esc(BIZ["postal_code"])}</li>
          <li style="color:var(--ink-soft);">Open 24/7 for emergency callouts</li>
        </ul>
      </div>
    </div>
  </div>
</section>
'''
    schema = [breadcrumb_schema([("Home",""),("Contact","contact.html")])]
    html_out = page_shell(
        title="Contact Us | South Bay Plumber",
        description="Get a free plumbing quote or call South Bay Plumber now for 24/7 emergency "
                     "service across southern Melbourne.",
        canonical_path="contact.html", depth=0, current="contact.html", body=body, schema_blocks=schema,
    )
    write("contact.html", html_out)

# ---------------------------------------------------------------- SITEMAP / ROBOTS

def build_sitemap_and_robots():
    urls = ["", "services.html", "service-areas.html", "about.html", "contact.html"]
    urls += [f"services/{s['slug']}.html" for s in SERVICES]
    urls += [f"areas/{slug}.html" for slug, *_ in SUBURBS]
    items = "\n".join(f"  <url><loc>{BIZ['url']}/{u}</loc></url>" for u in urls)
    sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{items}
</urlset>'''
    write("sitemap.xml", sitemap)

    robots = f'''User-agent: *
Allow: /

Sitemap: {BIZ["url"]}/sitemap.xml
'''
    write("robots.txt", robots)

# ---------------------------------------------------------------- MAIN

if __name__ == "__main__":
    build_home()
    build_services_index()
    build_service_pages()
    build_areas_index()
    build_suburb_pages()
    build_about()
    build_contact()
    build_sitemap_and_robots()
    print("Build complete.")
