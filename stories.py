# Story data for the 25 November 2026 front page.
# Researched 25 Nov 2026 from Reuters, CNBC, ESA, CMSA, BusinessLine and
# other outlets. Every item happened, or was first reported, on 25 Nov 2026.
# Fields: n, region, field, label, source, headline, summary, pin (lon, lat)
# or None, art (illustration kind).
#
# v2 (26 Nov 2026): 40 stories (was 48) — briefs 41-48 dropped; all lead and
# medium summaries rewritten short so the render never truncates with "…".

LEADS = [
    {
        "n": 1, "region": "ASIA-PACIFIC", "field": "SPACE",
        "label": "CONFIRMED", "source": "CMSA",
        "headline": "Shenzhou-24 lifts off with Pakistan's first astronaut",
        "summary": "Shenzhou-24 lifts off at 00:18 UTC carrying Pakistan's "
                   "first astronaut.",
        "pin": (98.5, 39.8), "art": "rocket",
    },
    {
        "n": 2, "region": "EUROPE", "field": "SPACE",
        "label": "CONFIRMED", "source": "ESA",
        "headline": "Hera shows Dimorphos up close",
        "summary": "ESA shows the first close-up images of asteroid "
                   "Dimorphos. Livestream 18:45 UTC.",
        "pin": (13.4, 52.5), "art": "asteroid",
    },
    {
        "n": 3, "region": "EUROPE", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "Sanofi",
        "headline": "Sanofi buys Insmed for $41bn",
        "summary": "Sanofi to buy US biotech Insmed in cash — pharma's "
                   "biggest deal since 2023.",
        "pin": (2.35, 48.85), "art": "pharma",
    },
    {
        "n": 4, "region": "NORTH AMERICA", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "Dell / CNBC",
        "headline": "Dell rides AI servers to a $54.94bn quarter",
        "summary": "Dell beats forecasts and lifts its FY2027 outlook to "
                   "$202bn. A $25bn buyback too.",
        "pin": (-97.7, 30.5), "art": "server",
    },
]

MEDIUM = [
    {
        "n": 5, "region": "NORTH AMERICA", "field": "POLITICS",
        "label": "REPORTED", "source": "Reuters",
        "headline": "US weighs tariffs on 16 partners",
        "summary": "Washington plans new duties on India, China and 14 "
                   "others after a factory-capacity probe.",
        "pin": (-77.0, 38.9), "art": "ship",
    },
    {
        "n": 6, "region": "MIDDLE EAST", "field": "POLITICS",
        "label": "REPORTED", "source": "Reuters",
        "headline": "US envoy doubts Israel aid ends this year",
        "summary": "The US envoy is 'not certain' aid to Israel ends this "
                   "year, as Trump promised.",
        "pin": (35.2, 31.8), "art": "aid",
    },
    {
        "n": 7, "region": "EUROPE", "field": "ECONOMY",
        "label": "OFFICIAL", "source": "German govt",
        "headline": "Germany sees €1tn in tax by 2027",
        "summary": "Berlin forecasts record tax revenue of one trillion euros in 2027.",
        "pin": (13.4, 52.5), "art": "bank",
    },
    {
        "n": 8, "region": "EUROPE", "field": "SECURITY",
        "label": "REPORTED", "source": "Reuters",
        "headline": "NATO jets to watch Poland's skies",
        "summary": "NATO plans early-warning jets for Poland after missiles "
                   "landed there during a Ukraine attack.",
        "pin": (21.0, 52.2), "art": "radar",
    },
    {
        "n": 9, "region": "MIDDLE EAST", "field": "CONFLICT",
        "label": "CLAIM", "source": "IRGC",
        "headline": "Mines hit three tankers in Hormuz",
        "summary": "Iran's Guard Navy says three oil tankers were hit by "
                   "naval mines in the Strait of Hormuz.",
        "pin": (56.5, 26.6), "art": "mine",
    },
    {
        "n": 10, "region": "MIDDLE EAST", "field": "CYBER",
        "label": "REPORTED", "source": "WSJ",
        "headline": "Iran suspected in tanker cyber raids",
        "summary": "Hackers suspected to be Iranian hit up to 50 oil and "
                   "shipping tankers, breaching navigation.",
        "pin": (51.4, 35.7), "art": "cyber",
    },
    {
        "n": 11, "region": "MIDDLE EAST", "field": "ENERGY",
        "label": "REPORTED", "source": "Oilprice",
        "headline": "Iraq rejects OPEC+ oil verdict",
        "summary": "Baghdad rejects a capacity verdict below 5m barrels a "
                   "day and pushes for about 6m.",
        "pin": (44.4, 33.3), "art": "oil",
    },
    {
        "n": 12, "region": "MIDDLE EAST", "field": "ENERGY",
        "label": "REPORTED", "source": "Reuters",
        "headline": "Baghdad orders Kurdish oilfields taken over",
        "summary": "Iraq's PM orders Baghdad to run Kurdish oilfields; "
                   "Kurdish authorities reject the move.",
        "pin": (44.0, 36.2), "art": "oil",
    },
    {
        "n": 13, "region": "NORTH AMERICA", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "FTC",
        "headline": "Shein pays $100m over FTC claims",
        "summary": "The retailer settles US claims it deceived shoppers, "
                   "hid bad reviews and failed on service.",
        "pin": (-77.0, 38.9), "art": "gavel",
    },
    {
        "n": 14, "region": "NORTH AMERICA", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "Netflix",
        "headline": "Netflix buys a Hollywood lot for $380m",
        "summary": "Netflix acquires the 55-acre Radford Studio Center in Los Angeles "
                   "from Goldman Sachs.",
        "pin": (-118.4, 34.1), "art": "film",
    },
    {
        "n": 15, "region": "EUROPE", "field": "POLITICS",
        "label": "OFFICIAL", "source": "Riksdag",
        "headline": "Sweden votes on keeping Kristersson",
        "summary": "Parliament votes on whether Moderate leader Ulf Kristersson stays "
                   "prime minister.",
        "pin": (18.1, 59.3), "art": "ballot",
    },
    {
        "n": 16, "region": "MIDDLE EAST", "field": "CONFLICT",
        "label": "REPORTED", "source": "The Germany Eye",
        "headline": "Houthi rocket kills 53 soldiers",
        "summary": "A Houthi rocket attack kills 53 soldiers in Yemen as forces push "
                   "toward Aden.",
        "pin": (45.0, 12.8), "art": "blast",
    },
]

# One line each: (number, text, label, source, region)
# v2: every text rewritten to fit one line (target <= 30 chars) so the
# render never truncates. Briefs 41-48 dropped (all ASIA-PACIFIC).
BRIEFS = [
    (17, "Russian missiles hit Ukraine", "REPORTED", "The Germany Eye", "EUROPE"),
    (18, "Blacklisted Russian joins IAEA", "REPORTED", "sangaku-journal", "EUROPE"),
    (19, "Zelensky meets Hungary's PM", "REPORTED", "sangaku-journal", "EUROPE"),
    (20, "US, Qatar hold strategic talks", "REPORTED", "JagranJosh", "MIDDLE EAST"),
    (21, "UN flags deepening Gaza strain", "REPORTED", "JagranJosh", "MIDDLE EAST"),
    (22, "EU unveils new Russia sanctions", "REPORTED", "JagranJosh", "EUROPE"),
    (23, "Teams outage sparks Code Red", "REPORTED", "SuMarket / CNBC", "NORTH AMERICA"),
    (24, "Anthropic below $83 IPO price", "REPORTED", "Newsmriti", "NORTH AMERICA"),
    (25, "India markets reopen after holiday", "OFFICIAL", "BSE", "ASIA-PACIFIC"),
    (26, "BJP, Akali Dal reunite for 2027", "CONFIRMED", "JagranJosh", "ASIA-PACIFIC"),
    (27, "Jupiter Wagons links with Woojin", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (28, "Brigade buys Secunderabad land", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (29, "Lupin wins US FDA drug nod", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (30, "PhysicsWallah plans e-university", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (31, "Uranus at opposition all night", "OFFICIAL", "Star Walk", "SPACE"),
    (32, "Strange star found 28 ly away", "REPORTED", "SciTechDaily", "SPACE"),
    (33, "Day against violence on women", "OFFICIAL", "UN", "GLOBAL"),
    (34, "Romania, Armenia sign pacts", "REPORTED", "sangaku-journal", "EUROPE"),
    (35, "N. Korea shuts Swiss embassy", "REPORTED", "sangaku-journal", "ASIA-PACIFIC"),
    (36, "Australia eyes AI likeness law", "REPORTED", "sangaku-journal", "ASIA-PACIFIC"),
    (37, "Wars push WFP costs to $727m", "REPORTED", "sangaku-journal", "GLOBAL"),
    (38, "France admits riot failures", "REPORTED", "The Germany Eye", "EUROPE"),
    (39, "Car bomb hits Colombia office", "REPORTED", "sangaku-journal", "LATIN AMERICA"),
    (40, "Gold ₹1.28L; Brent $90.70", "OFFICIAL", "BusinessLine", "ASIA-PACIFIC"),
]

# v2: six big-number cells, one row (was ten small items in two rows).
NUMBERS = [
    ("$41bn", "Sanofi deal"),
    ("$54.94bn", "Dell quarter"),
    ("€1tn", "German tax forecast"),
    ("$202bn", "Dell outlook"),
    ("6m b/d", "Iraq's oil ask"),
    ("53", "soldiers killed, Yemen"),
]

# v2: seven slots, chronological (was five).
TIMELINE = [
    ("00:11 UTC", "Germany publishes €1tn tax forecast"),
    ("00:18 UTC", "Shenzhou-24 launches from Jiuquan"),
    ("01:14 UTC", "US weighs tariffs on 16 partners, reported"),
    ("03:45 UTC", "India markets reopen after holiday"),
    ("10:00 UTC", "Hera media conference opens in Berlin"),
    ("14:30 UTC", "US markets open; Anthropic below $83 IPO"),
    ("18:45 UTC", "ESA streams Dimorphos images"),
]

# News deliberately left out because it is NOT from 25 November.
DATE_CHECK = [
    ("Huawei guilty of trade-secret theft", "verdict Mon 24 Nov"),
    ("Spotify down, 14,000 reports", "Tue 24 Nov"),
    ("Trump pardons turkeys Freedom & Feathers", "Tue 24 Nov"),
    ("Giuliani receives Medal of Freedom", "Tue 24 Nov"),
    ("Sarkozy corruption case sent to trial", "Tue 24 Nov"),
    ("Fort Hood gunman seeks stay of execution", "Tue 24 Nov"),
    ("WHO: lift US fuel blockade on Cuba", "Tue 24 Nov"),
    ("O'Hare radar outage delays flights", "Tue 24 Nov"),
    ("Houthis 'won't seize Aden', army says", "Tue 24 Nov"),
    ("Abrego Garcia to leave US voluntarily", "Tue 24 Nov"),
    ("Thomas Markle indicted in US", "Tue 24 Nov"),
    ("Putin: retaliation 'inevitable'", "Mon 24 Nov"),
]

DATE_CHECK_NOT_YET = [
    ("OPEC+ meeting on 2027 targets", "due Sun 29 Nov"),
    ("Cygnus NG-25 launch to the ISS", "due Sun 29 Nov"),
    ("Talbros fundraising board decision", "due Fri 27 Nov"),
]

TOTAL_STORIES = len(LEADS) + len(MEDIUM) + len(BRIEFS)
