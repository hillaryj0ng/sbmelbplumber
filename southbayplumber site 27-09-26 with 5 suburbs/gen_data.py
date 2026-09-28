# -*- coding: utf-8 -*-
"""Data for South Bay Plumber site generation."""

BIZ = {
    "name": "South Bay Plumber",
    "domain": "southbayplumber.com.au",
    "url": "https://www.southbayplumber.com.au",
    "phone_display": "(03) 8338 4090",
    "phone_tel": "+61383384090",
    "email": "hello@southbayplumber.com.au",
    "address_locality": "Mornington",
    "address_region": "VIC",
    "postal_code": "3931",
    "address_street": "81 Watt Rd",
    "lat": "-38.2201",
    "lng": "145.0356",
    "founded": "2011",
    "tagline": "Melbourne's Southern Suburbs, Sorted.",
}

# ---------------------------------------------------------------- SERVICES
# slug, name, short, icon key, long intro, bullet list, faq list
SERVICES = [
    dict(
        slug="blocked-drains",
        name="Blocked Drain Plumber",
        short="Fast diagnosis and clearing for blocked sinks, toilets, floor drains and stormwater lines.",
        icon="drop",
        intro="A blocked drain rarely stays a small problem for long. Our drain technicians carry "
              "electric eels, high-pressure jetters and fibre-optic cameras on every van, so most "
              "blockages in Melbourne's southern suburbs are found and cleared in a single visit.",
        bullets=[
            "Kitchen, bathroom and laundry drain clearing",
            "Blocked and overflowing toilets",
            "Stormwater and downpipe blockages",
            "Tree-root intrusion clearing and pipe relining referrals",
            "CCTV drain camera inspection with a copy of the footage",
            "High-pressure water jetting for grease and scale build-up",
        ],
        faqs=[
            ("How do I know if my drain is blocked or my sewer is blocked?",
             "If only one fixture is slow (a single sink or shower) it's usually a local blockage. "
             "If several fixtures back up at once, or you can hear gurgling from other drains when "
             "you flush, it's more likely a main line issue — worth mentioning when you call so we "
             "bring the right gear the first time."),
            ("Do you use drain cameras before you quote?",
             "For anything beyond a simple sink trap, yes. A camera inspection tells us exactly "
             "where the blockage or damage is before we start work, which keeps the job to the "
             "area that actually needs it rather than guessing."),
            ("Can tree roots really block a pipe?",
             "Very common in the leafier southern suburbs and older streets with established street "
             "trees — roots find their way in through tiny joint gaps and expand from there. We can "
             "clear the immediate blockage and talk you through longer-term options like relining."),
        ],
    ),
    dict(
        slug="hot-water-systems",
        name="Hot Water Systems",
        short="Repairs, servicing and replacement for gas, electric, solar and heat pump hot water units.",
        icon="flame",
        intro="No hot water is a same-day job in our book. We repair and replace gas, electric, "
              "solar and heat pump systems from all major brands, and can usually give you an "
              "accurate replacement quote over the phone if your current unit is past repair.",
        bullets=[
            "Same-day hot water repairs and replacements",
            "Gas, electric, solar and heat pump systems",
            "Continuous flow and storage tank units",
            "Government rebate guidance on eligible heat pump upgrades",
            "Leaking, noisy or under-performing unit diagnostics",
            "Scheduled servicing to extend system life",
        ],
        faqs=[
            ("Is it worth repairing my hot water system or replacing it?",
             "It depends on the age and the fault. As a rough guide, a storage tank past 10 years "
             "old with a tank leak (rather than a part fault) is usually better replaced. We'll give "
             "you both options with pricing so it's your call, not ours."),
            ("Can you replace a hot water system the same day?",
             "In most of our southern suburbs coverage, yes, provided the replacement is a like-for-"
             "like swap and the unit is in stock. Call early in the day to give us the best chance "
             "of a same-day fit."),
            ("Do heat pump hot water systems suit coastal areas?",
             "Yes — we fit corrosion-resistant models for bayside and peninsula properties exposed "
             "to salt air, and can advise on positioning to reduce long-term wear."),
        ],
    ),
    dict(
        slug="leak-detection-and-repair",
        name="Leak Detection & Repair",
        short="Non-invasive leak detection for hidden pipe, slab and wall leaks before they cause damage.",
        icon="wrench",
        intro="A rising water bill, a damp patch on a wall, or the hiss of water behind a slab — "
              "hidden leaks are one of the most common calls we get across the southern suburbs. "
              "We use acoustic and thermal leak detection to pinpoint the source before any digging "
              "or wall-opening starts.",
        bullets=[
            "Acoustic and thermal leak detection",
            "Slab leak location and repair",
            "Wall and ceiling leak tracing",
            "Water meter and pressure testing to confirm a leak exists",
            "Insurance-ready leak detection reports",
            "Pipe relining as an alternative to full excavation",
        ],
        faqs=[
            ("How do you find a leak without breaking tiles or concrete?",
             "Acoustic detection listens for the specific sound water makes escaping a pressurised "
             "pipe, and thermal imaging picks up temperature differences from hot water pipes. "
             "Together they narrow a leak to a small, precise area before any opening-up work."),
            ("Will my insurer accept your leak detection report?",
             "We provide a written report with photos and findings that's suitable to submit with "
             "an insurance claim, though acceptance always depends on your specific policy."),
        ],
    ),
    dict(
        slug="gas-fitting",
        name="Gas Fitting",
        short="Licensed gas fitting for appliance installs, gas leak checks, and cooktop and heater connections.",
        icon="flame",
        intro="Gas work has to be done right the first time. Our licensed gas fitters handle "
              "everything from a new cooktop connection to a full gas leak investigation, with a "
              "compliance certificate issued for every job.",
        bullets=[
            "Gas cooktop, oven and BBQ point installation",
            "Gas heater and log fire connections",
            "Gas leak detection and repair",
            "Gas hot water system connections",
            "New gas line installation for renovations and extensions",
            "Compliance certificates issued on completion",
        ],
        faqs=[
            ("I can smell gas — what should I do?",
             "Turn off the gas at the meter if it's safe to do so, don't use switches or naked "
             "flames, ventilate the area, and call us straight away. If it's strong or you're "
             "unsure, leave the property and call 000 or your gas distributor's emergency line first."),
            ("Do you supply a compliance certificate?",
             "Yes, every gas fitting job is certified and lodged as required, which you'll need for "
             "insurance and if you ever sell the property."),
        ],
    ),
    dict(
        slug="emergency-plumbing",
        name="24/7 Emergency Plumbing",
        short="Burst pipes, flooding, no hot water and blocked toilets — a real person answers, day or night.",
        icon="alert",
        intro="Plumbing emergencies don't wait for business hours, and neither do we. Our on-call "
              "team covers bayside, the inner south-east and the Mornington Peninsula around the "
              "clock for burst pipes, flooding, gas leaks and total blockages.",
        bullets=[
            "Burst and bursting pipe repairs",
            "Flooding and water damage callouts",
            "No hot water emergencies",
            "Total blockages and sewage backups",
            "Emergency gas leak response",
            "Upfront emergency call-out pricing before we start",
        ],
        faqs=[
            ("What counts as a plumbing emergency?",
             "Anything causing active water damage, a total loss of water or hot water, sewage "
             "backing up into the house, or a suspected gas leak. If you're not sure, call — we'd "
             "rather talk it through than have you guess."),
            ("What should I do while I wait for the plumber?",
             "For a burst pipe, shut off the water at the mains if you know where the tap is. For a "
             "suspected gas leak, turn off the gas at the meter if safe, don't use switches or "
             "flames, and ventilate the area."),
        ],
    ),
    dict(
        slug="toilet-repairs-and-installation",
        name="Toilet Repairs & Installation",
        short="Running, blocked or leaking toilets fixed, plus new toilet suite supply and installation.",
        icon="drop",
        intro="From a constantly running cistern to a full toilet suite replacement as part of a "
              "bathroom renovation, we handle the full range of toilet plumbing across the southern "
              "suburbs.",
        bullets=[
            "Running or leaking cistern repairs",
            "Blocked toilet clearing",
            "Wall-hung and floor-mounted toilet installation",
            "Water-efficient toilet suite upgrades",
            "Cracked pan and cistern replacement",
        ],
        faqs=[
            ("Why does my toilet keep running?",
             "Usually a worn inlet valve or a flapper/seal that isn't sealing properly in the "
             "cistern — both are quick, inexpensive fixes in most cases."),
        ],
    ),
    dict(
        slug="burst-pipe-repair",
        name="Burst Pipe Repair",
        short="Rapid response burst pipe repairs to stop water damage fast across all pipe materials.",
        icon="wrench",
        intro="A burst pipe can put litres of water into your home every minute. We prioritise burst "
              "pipe calls, aiming to have a plumber on the way as quickly as possible to stop the "
              "damage and repair the pipe properly — not just patch it.",
        bullets=[
            "Copper, PVC and poly pipe repairs",
            "Underground and slab pipe bursts",
            "External tap and garden line repairs",
            "Water damage minimisation on arrival",
            "Permanent repair, not a temporary patch",
        ],
        faqs=[
            ("Should I turn off my water mains during a burst pipe?",
             "Yes, if it's safe and accessible — this limits the damage while you wait for us. Most "
             "Melbourne homes have a mains tap near the front boundary or water meter."),
        ],
    ),
    dict(
        slug="bathroom-plumbing-renovations",
        name="Bathroom Plumbing & Renovations",
        short="Plumbing rough-in and fit-off for bathroom renovations, from period homes to new builds.",
        icon="drop",
        intro="Bathroom renovations across the southern suburbs range from restoring the plumbing in "
              "a Camberwell or Malvern period home to fitting out a brand-new ensuite in a Cranbourne "
              "or Berwick estate. We handle the full rough-in and fit-off, working alongside your "
              "builder or tiler.",
        bullets=[
            "Rough-in plumbing for new bathroom layouts",
            "Fit-off for tapware, showers, vanities and toilets",
            "Waterproofing-stage drainage and floor waste positioning",
            "Period home pipework upgrades",
            "Ensuite and second-bathroom additions",
        ],
        faqs=[
            ("Can you work directly with my builder or tiler?",
             "Yes — we regularly coordinate rough-in and fit-off timing directly with renovation "
             "trades and can attend site meetings if needed."),
        ],
    ),
    dict(
        slug="drain-camera-inspection",
        name="Drain Camera Inspection",
        short="CCTV drain inspections for pre-purchase checks, recurring blockages and insurance reports.",
        icon="wrench",
        intro="Whether you're buying a property, dealing with a recurring blockage, or need evidence "
              "for an insurance claim, our fibre-optic drain cameras show exactly what's happening "
              "inside your pipes without digging.",
        bullets=[
            "Pre-purchase drain and sewer inspections",
            "Recurring blockage diagnosis",
            "Root intrusion and pipe collapse detection",
            "Digital footage and written report provided",
            "Locating pipe depth and position before excavation",
        ],
        faqs=[
            ("Is a drain camera inspection worth it before buying a property?",
             "Very often, yes, particularly for older homes in the inner south-east where original "
             "clay pipework is common — a collapsed or root-affected pipe is an expensive surprise "
             "to inherit."),
        ],
    ),
    dict(
        slug="backflow-prevention",
        name="Backflow Prevention",
        short="Backflow device testing, installation and annual compliance certification.",
        icon="alert",
        intro="Backflow prevention devices stop contaminated water flowing back into the drinking "
              "water supply, and most councils require annual testing. We install, test and certify "
              "devices for residential and commercial properties across the southern suburbs.",
        bullets=[
            "Backflow prevention device installation",
            "Annual compliance testing and certification",
            "Reduced pressure zone (RPZ) device servicing",
            "Council lodgement of test results",
        ],
        faqs=[
            ("Who needs a backflow prevention device?",
             "It depends on your property's water connections and council requirements — common on "
             "properties with irrigation systems, pools, or certain commercial fixtures. We can "
             "check what applies to your address."),
        ],
    ),
    dict(
        slug="roof-plumbing-and-stormwater",
        name="Roof Plumbing & Stormwater",
        short="Gutter, downpipe and stormwater drainage repairs to keep water moving away from your home.",
        icon="drop",
        intro="Blocked gutters and undersized stormwater drainage are a common cause of water damage "
              "in Melbourne's wetter months. We repair and upgrade guttering, downpipes and "
              "stormwater connections across the southern suburbs.",
        bullets=[
            "Gutter and downpipe repairs",
            "Stormwater drain clearing and relining",
            "Rainwater tank plumbing connections",
            "Overflow and ponding diagnosis",
            "Leaf guard and gutter guard installation referrals",
        ],
        faqs=[
            ("Why is water pooling near my house after rain?",
             "Usually a blocked, undersized or damaged stormwater line, or a downpipe disconnected "
             "underground. A camera inspection will usually find the cause quickly."),
        ],
    ),
    dict(
        slug="commercial-plumbing",
        name="Commercial Plumbing",
        short="Maintenance, fit-outs and compliance plumbing for shops, offices and strata properties.",
        icon="wrench",
        intro="From a strip of shops in Dandenong to a strata block in Glen Waverley, we support "
              "commercial and strata clients across the southern suburbs with scheduled maintenance, "
              "fit-out plumbing and urgent repairs that minimise disruption to your business or "
              "tenants.",
        bullets=[
            "Scheduled preventative maintenance programs",
            "Shop and office fit-out plumbing",
            "Strata common-area plumbing repairs",
            "Backflow and trade waste compliance",
            "After-hours callouts to limit trading disruption",
        ],
        faqs=[
            ("Do you offer maintenance contracts for strata or commercial sites?",
             "Yes, we set up scheduled inspection and maintenance programs tailored to the "
             "property, with priority response built in."),
        ],
    ),
]

# ---------------------------------------------------------------- REGIONS
REGIONS = {
    "bayside": dict(
        label="Bayside",
        pain="Salt air off the bay is hard on old galvanised pipework and tapware, and many homes "
             "here still have their original plumbing beneath recent renovations.",
        focus="corrosion-aware repairs and hot water systems built to handle coastal conditions",
    ),
    "inner-south-east": dict(
        label="Inner South-East",
        pain="Period homes with original earthenware drains and ageing internal pipework are common, "
             "often hidden behind a more recent renovation.",
        focus="careful diagnostics before any wall or floor is opened, and drainage upgrades that "
              "respect heritage detailing",
    ),
    "south-east": dict(
        label="South-East Growth Corridor",
        pain="Newer estates bring slab-on-ground plumbing, larger blocks with long stormwater runs, "
             "and fast-growing streets where trade availability matters.",
        focus="responsive scheduling and full rough-in through to fit-off for new and near-new homes",
    ),
    "mornington-peninsula": dict(
        label="Mornington Peninsula & Frankston",
        pain="A mix of permanent residences and holiday homes means properties are sometimes left "
             "unattended for weeks, so a small leak can become a big one before anyone notices.",
        focus="holiday-home check-in plumbing inspections alongside standard repairs and installs",
    ),
}

# slug, name, postcode, region key, landmark reference, lat, lng
SUBURBS = [
    # --- named by client ---
    ("mornington", "Mornington", "3931", "mornington-peninsula", "Main Street and Mills Beach"),
    ("glen-waverley", "Glen Waverley", "3150", "south-east", "The Glen and Kingsway"),
    ("port-melbourne", "Port Melbourne", "3207", "bayside", "Bay Street and Station Pier"),
    ("camberwell", "Camberwell", "3124", "inner-south-east", "Camberwell Junction"),
    ("malvern", "Malvern", "3144", "inner-south-east", "Glenferrie Road and Malvern Central"),
    ("sandringham", "Sandringham", "3191", "bayside", "Sandringham foreshore and yacht club"),
    ("dandenong", "Dandenong", "3175", "south-east", "Dandenong Plaza and the Market"),
    ("caulfield", "Caulfield", "3162", "inner-south-east", "Caulfield Racecourse"),
    # --- additional 30 most populated southern suburbs ---
    ("frankston", "Frankston", "3199", "mornington-peninsula", "Frankston waterfront and pier"),
    ("brighton", "Brighton", "3186", "bayside", "Brighton Beach bathing boxes"),
    ("hampton", "Hampton", "3188", "bayside", "Hampton Street shopping strip"),
    ("cheltenham", "Cheltenham", "3192", "bayside", "Southland shopping precinct"),
    ("mentone", "Mentone", "3194", "bayside", "Mentone foreshore and station"),
    ("mordialloc", "Mordialloc", "3195", "bayside", "Mordialloc Creek and pier"),
    ("chelsea", "Chelsea", "3196", "bayside", "Chelsea foreshore"),
    ("mount-eliza", "Mount Eliza", "3930", "mornington-peninsula", "Mount Eliza Village"),
    ("mount-martha", "Mount Martha", "3934", "mornington-peninsula", "Mount Martha beach and village"),
    ("rosebud", "Rosebud", "3939", "mornington-peninsula", "Rosebud foreshore"),
    ("hastings", "Hastings", "3915", "mornington-peninsula", "Hastings foreshore and marina"),
    ("somerville", "Somerville", "3912", "mornington-peninsula", "Eramosa Road shopping strip"),
    ("cranbourne", "Cranbourne", "3977", "south-east", "Cranbourne Park Shopping Centre"),
    ("berwick", "Berwick", "3806", "south-east", "Berwick Village and High Street"),
    ("narre-warren", "Narre Warren", "3805", "south-east", "Fountain Gate Shopping Centre"),
    ("pakenham", "Pakenham", "3810", "south-east", "Pakenham Main Street"),
    ("springvale", "Springvale", "3171", "south-east", "Springvale Road shopping precinct"),
    ("noble-park", "Noble Park", "3174", "south-east", "Noble Park Market"),
    ("keysborough", "Keysborough", "3173", "south-east", "Parkmore Shopping Centre"),
    ("hampton-park", "Hampton Park", "3976", "south-east", "Hallam Road shops"),
    ("clayton", "Clayton", "3168", "south-east", "Monash University precinct"),
    ("oakleigh", "Oakleigh", "3166", "inner-south-east", "Eaton Mall and Oakleigh Market"),
    ("mount-waverley", "Mount Waverley", "3149", "south-east", "Pinewood shopping village"),
    ("wheelers-hill", "Wheelers Hill", "3150", "south-east", "Brandon Park Shopping Centre"),
    ("rowville", "Rowville", "3178", "south-east", "Stud Park Shopping Centre"),
    ("bentleigh", "Bentleigh", "3204", "bayside", "Centre Road shopping strip"),
    ("bentleigh-east", "Bentleigh East", "3165", "bayside", "Bentleigh East Village"),
    ("moorabbin", "Moorabbin", "3189", "bayside", "Moorabbin Airport precinct"),
    ("highett", "Highett", "3190", "bayside", "Highett Village"),
    ("carrum-downs", "Carrum Downs", "3201", "mornington-peninsula", "Eastlink and Ballarto Road corridor"),
]

# ---------------------------------------------------------------- LOCAL LISTINGS
# Suburb-specific Google Business Profile data. Each entry here means that
# Suburbs with dedicated local NAP details. Other suburb pages use the
# Mornington phone number and omit the address from their footer.
LOCAL_LISTINGS = {
    "mornington": dict(
        gmb_name="Southbay Plumber Mornington",
        street="81 Watt Rd",
        locality="Mornington",
        postcode="3931",
        phone_display="(03) 8338 4090",
        phone_tel="+61383384090",
        lat="-38.2201",
        lng="145.0356",
    ),
    "dandenong": dict(
        gmb_name="Southbay Plumber Dandenong",
        street="Level 10/14 Mason St",
        locality="Dandenong",
        postcode="3175",
        phone_display="(03) 8338 1909",
        phone_tel="+61383381909",
    ),
    "glen-waverley": dict(
        gmb_name="Southbay Plumber Glen Waverley",
        street="66 Kingsway",
        locality="Glen Waverley",
        postcode="3150",
        phone_display="(03) 8338 4093",
        phone_tel="+61383384093",
    ),
    "frankston": dict(
        gmb_name="Southbay Plumber Frankston",
        street="435 Nepean Hwy",
        locality="Frankston",
        postcode="3199",
        phone_display="(03) 8338 4756",
        phone_tel="+61383384756",
    ),
    "cranbourne": dict(
        gmb_name="Southbay Plumber Cranbourne",
        street="198 Sladen St",
        locality="Cranbourne",
        postcode="3977",
        phone_display="(03) 8338 4729",
        phone_tel="+61383384729",
    ),
}


NEARBY_MAP = {
    # explicit override list of 4 nearest suburbs per slug for internal linking
    "mornington": ["mount-eliza", "mount-martha", "frankston", "somerville"],
    "glen-waverley": ["mount-waverley", "wheelers-hill", "clayton", "rowville"],
    "port-melbourne": ["brighton", "sandringham", "hampton", "moorabbin"],
    "camberwell": ["malvern", "caulfield", "oakleigh", "bentleigh"],
    "malvern": ["camberwell", "caulfield", "bentleigh", "oakleigh"],
    "sandringham": ["hampton", "brighton", "cheltenham", "moorabbin"],
    "dandenong": ["springvale", "noble-park", "keysborough", "hampton-park"],
    "caulfield": ["malvern", "camberwell", "bentleigh", "bentleigh-east"],
    "frankston": ["carrum-downs", "mount-eliza", "somerville", "mornington"],
    "brighton": ["hampton", "port-melbourne", "sandringham", "bentleigh"],
    "hampton": ["brighton", "sandringham", "highett", "bentleigh"],
    "cheltenham": ["mentone", "highett", "moorabbin", "sandringham"],
    "mentone": ["mordialloc", "cheltenham", "highett", "chelsea"],
    "mordialloc": ["mentone", "chelsea", "carrum-downs", "cheltenham"],
    "chelsea": ["mordialloc", "carrum-downs", "mentone", "frankston"],
    "mount-eliza": ["mornington", "mount-martha", "frankston", "somerville"],
    "mount-martha": ["mount-eliza", "mornington", "rosebud", "somerville"],
    "rosebud": ["mount-martha", "hastings", "mornington", "somerville"],
    "hastings": ["somerville", "mount-martha", "rosebud", "frankston"],
    "somerville": ["hastings", "mount-eliza", "frankston", "carrum-downs"],
    "cranbourne": ["berwick", "narre-warren", "hampton-park", "pakenham"],
    "berwick": ["narre-warren", "cranbourne", "pakenham", "hampton-park"],
    "narre-warren": ["berwick", "hampton-park", "cranbourne", "rowville"],
    "pakenham": ["cranbourne", "berwick", "narre-warren", "hastings"],
    "springvale": ["noble-park", "dandenong", "keysborough", "clayton"],
    "noble-park": ["springvale", "dandenong", "keysborough", "hampton-park"],
    "keysborough": ["springvale", "dandenong", "noble-park", "carrum-downs"],
    "hampton-park": ["narre-warren", "dandenong", "cranbourne", "noble-park"],
    "clayton": ["oakleigh", "springvale", "mount-waverley", "wheelers-hill"],
    "oakleigh": ["clayton", "caulfield", "bentleigh-east", "malvern"],
    "mount-waverley": ["glen-waverley", "wheelers-hill", "clayton", "oakleigh"],
    "wheelers-hill": ["glen-waverley", "mount-waverley", "rowville", "clayton"],
    "rowville": ["wheelers-hill", "glen-waverley", "narre-warren", "clayton"],
    "bentleigh": ["bentleigh-east", "brighton", "moorabbin", "caulfield"],
    "bentleigh-east": ["bentleigh", "moorabbin", "oakleigh", "caulfield"],
    "moorabbin": ["highett", "cheltenham", "bentleigh", "sandringham"],
    "highett": ["moorabbin", "cheltenham", "sandringham", "hampton"],
    "carrum-downs": ["frankston", "chelsea", "mordialloc", "somerville"],
}

ICONS = {
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3c3.5 4 6 7.6 6 10.5A6 6 0 0 1 6 13.5C6 10.6 8.5 7 12 3Z" stroke-linejoin="round"/></svg>',
    "flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 21c4 0 6.5-2.6 6.5-6 0-2.7-1.8-4.4-2.7-6.3-.5 1.4-1.4 2.2-2.1 1.6.6-2.6-.6-5.1-2.6-6.8.4 2.4-.6 4.3-2.3 6C7 11 5.5 12.8 5.5 15c0 3.4 2.5 6 6.5 6Z" stroke-linejoin="round"/></svg>',
    "wrench": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M14.7 6.3a4 4 0 0 0-5.4 5l-6 6 2.4 2.4 6-6a4 4 0 0 0 5-5.4l-2.6 2.6-2-2 2.6-2.6Z" stroke-linejoin="round"/></svg>',
    "alert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 2 20h20L12 3Z" stroke-linejoin="round"/><path d="M12 10v4" stroke-linecap="round"/><circle cx="12" cy="17" r=".9" fill="currentColor" stroke="none"/></svg>',
}
