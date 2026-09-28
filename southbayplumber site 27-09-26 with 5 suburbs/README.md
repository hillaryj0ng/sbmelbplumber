# South Bay Plumber — website

A static, SEO-structured site for southbayplumber.com.au: a homepage, a
services hub with 12 individual service pages, a service-areas hub with 38
individual suburb pages, About and Contact — all cross-linked in a
service ⇄ suburb "silo" pattern (like the footer service-area list on
stansac.com), with Plumber/LocalBusiness, Service, FAQPage and
BreadcrumbList JSON-LD schema on every relevant page.

## Structure

```
index.html              Homepage
services.html            Services hub
services/*.html           12 individual service pages
service-areas.html       Service areas hub (grouped by region)
areas/*.html               38 individual suburb pages
about.html
contact.html
sitemap.xml               all 55 URLs
robots.txt
css/styles.css
js/main.js                mobile nav toggle only
```

## Before you launch — replace these placeholders

Everything below is clearly fake/placeholder data used to make the template
complete. Search-and-replace before going live:

- **Phone number**: `(03) 8338 4090` / `+61383384090` (in `gen_data.py`
  under `BIZ`, or find/replace across the built HTML)
- **Email**: `hello@southbayplumber.com.au`
- **Street address / postcode**: `12 Bay Street, Mentone VIC 3194` — used
  in the NAP block and schema `address`/`geo`. Update `lat`/`lng` too.
- **Sample reviews** on the homepage — replace with real, verifiable
  customer reviews (ideally pulled live from Google).
- **Contact form** on `contact.html` is static markup only — wire it up to
  a real backend or a form service (Formspree, Netlify Forms, etc.) and
  add a spam honeypot/reCAPTCHA.
- **`og:image` / `images/og-cover.jpg`** referenced in schema — add a real
  1200×630 image at that path.
- **Google Business Profile + real map embed** — the suburb pages don't
  currently embed a live map; add one once you have a verified GBP listing.

## Regenerating the site

The whole site is generated from two Python files so content stays
consistent across all 55 pages:

- `gen_data.py` — business details, the 12 services, the 4 regions and all
  38 suburbs (with postcodes, nearest-neighbour suburbs for internal
  linking, and region-specific "local pain point" copy).
- `gen_site.py` — builds every page from that data.

To regenerate after editing data (e.g. adding a 39th suburb, or a new
service):

```
cd site
python3 gen_site.py
```

## SEO notes on how this is structured

- **Silo/hub-and-spoke internal linking**: every service page links to all
  38 suburb pages; every suburb page links to its top services and its
  nearest neighbouring suburbs; both hubs link back to every child page.
  This is the same pattern used on the stansac.com reference site's
  mega-menu + footer service-area list.
- **Unique content per suburb**: each of the 38 pages varies beyond the
  H1 — postcode, a local landmark, and region-specific "why" copy (coastal
  corrosion for Bayside, period-home pipework for the Inner South-East,
  slab plumbing for the South-East growth corridor, holiday-home checks
  for the Mornington Peninsula) rather than a single template with only
  the suburb name swapped.
- **Schema**: `Plumber` (LocalBusiness) on every page, `Service` schema on
  each service page, `FAQPage` schema wherever FAQs appear, and
  `BreadcrumbList` on every page.
- **One canonical H1 per page**, descriptive `<title>` and meta
  description built from the suburb/service name + postcode, a single
  sitemap.xml covering all 55 URLs, and a robots.txt pointing to it.

## Multi-location GMB / NAP setup

Some suburb pages are tied to their own dedicated Google Business Profile
listing rather than the single head-office listing — this matters because
Google checks that a location's website page shows the exact same
name/address/phone (NAP) as its GMB listing.

This is driven by `LOCAL_LISTINGS` in `gen_data.py`. Right now it has two
entries (from the GMB list you shared):

- **Mornington** — Southbay Plumber Mornington, 81 Watt Rd, Mornington VIC
  3931, (03) 8338 4090
- **Dandenong** — Southbay Plumber Dandenong, Level 10/14 Mason St,
  Dandenong VIC 3175, (03) 8338 1909

For those two suburbs, the header phone number, the hero and CTA call
buttons, the "at a glance" card, the footer contact block, and the
`Plumber` JSON-LD (name/telephone/address/geo) on that one page all switch
to the dedicated listing — everywhere else on the site still shows the
head-office NAP. The other 36 suburb pages currently fall back to the
head-office listing until they have their own GMB.

**To add the rest:** send the same three columns (GMB name, address, phone)
for any other suburb and add a matching entry to `LOCAL_LISTINGS`, e.g.:

```python
"glen-waverley": dict(
    gmb_name="Southbay Plumber Glen Waverley",
    street="<street address>",
    locality="Glen Waverley",
    postcode="3150",
    phone_display="(03) XXXX XXXX",
    phone_tel="+613XXXXXXXX",
    lat="<latitude>", lng="<longitude>",
),
```
then rerun `python3 gen_site.py`. Note: the phone numbers you provided were
formatted unusually (e.g. `+61 (383) 384 - 090`) — I've read them as valid
Australian landline numbers (`03 8338 4090` / `03 8338 1909`), but it's
worth double-checking these against your actual GMB dashboard before
publishing, since a wrong number on a live listing is worse than a missing
one.
