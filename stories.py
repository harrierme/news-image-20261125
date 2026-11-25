# Story data for the 25 November 2026 front page.
# Researched 25 Nov 2026 from Reuters, CNBC, ESA, CMSA, BusinessLine and
# other outlets. Every item happened, or was first reported, on 25 Nov 2026.
# Fields: n, region, field, label, source, headline, summary, pin (lon, lat)
# or None, art (illustration kind).

LEADS = [
    {
        "n": 1, "region": "ASIA-PACIFIC", "field": "SPACE",
        "label": "CONFIRMED", "source": "CMSA",
        "headline": "Shenzhou-24 lifts off with Pakistan's first astronaut",
        "summary": "China launches Shenzhou-24 at 00:18 UTC from Jiuquan. A Pakistani "
                   "astronaut flies to Tiangong — the first non-Chinese visitor — and one "
                   "crew member stays a year.",
        "pin": (98.5, 39.8), "art": "rocket",
    },
    {
        "n": 2, "region": "EUROPE", "field": "SPACE",
        "label": "CONFIRMED", "source": "ESA",
        "headline": "Hera shows Dimorphos up close",
        "summary": "ESA unveils the first close-up images of asteroid Dimorphos, three "
                   "weeks after Hera arrived at the DART impact site. Livestream 18:45 UTC.",
        "pin": (13.4, 52.5), "art": "asteroid",
    },
    {
        "n": 3, "region": "EUROPE", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "Sanofi",
        "headline": "Sanofi buys Insmed for $41bn",
        "summary": "French drugmaker Sanofi agrees to buy US biotech Insmed in cash — the "
                   "pharma sector's biggest deal since 2023.",
        "pin": (2.35, 48.85), "art": "pharma",
    },
    {
        "n": 4, "region": "NORTH AMERICA", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "Dell / CNBC",
        "headline": "Dell rides AI servers to a $54.94bn quarter",
        "summary": "Dell beats forecasts with $9.45 EPS, raises its FY2027 revenue outlook "
                   "to $202bn and authorises a $25bn buyback.",
        "pin": (-97.7, 30.5), "art": "server",
    },
]

MEDIUM = [
    {
        "n": 5, "region": "NORTH AMERICA", "field": "POLITICS",
        "label": "REPORTED", "source": "Reuters",
        "headline": "US weighs tariffs on 16 partners",
        "summary": "Washington prepares new duties on India, China and 14 others after a "
                   "probe into excess factory capacity.",
        "pin": (-77.0, 38.9), "art": "ship",
    },
    {
        "n": 6, "region": "MIDDLE EAST", "field": "POLITICS",
        "label": "REPORTED", "source": "Reuters",
        "headline": "US envoy doubts Israel aid ends this year",
        "summary": "The US envoy is 'not certain' military aid to Israel will end this "
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
        "summary": "NATO plans early-warning aircraft in Poland after missiles landed "
                   "there during an attack on Ukraine.",
        "pin": (21.0, 52.2), "art": "radar",
    },
    {
        "n": 9, "region": "MIDDLE EAST", "field": "CONFLICT",
        "label": "CLAIM", "source": "IRGC",
        "headline": "Mines hit three tankers in Hormuz",
        "summary": "Iran's Revolutionary Guard Navy says three oil tankers were hit by "
                   "naval mines in the Strait of Hormuz.",
        "pin": (56.5, 26.6), "art": "mine",
    },
    {
        "n": 10, "region": "MIDDLE EAST", "field": "CYBER",
        "label": "REPORTED", "source": "WSJ",
        "headline": "Iran suspected in tanker cyber raids",
        "summary": "Hackers suspected to be Iranian targeted as many as 50 oil and "
                   "shipping tankers, breaching navigation systems.",
        "pin": (51.4, 35.7), "art": "cyber",
    },
    {
        "n": 11, "region": "MIDDLE EAST", "field": "ENERGY",
        "label": "REPORTED", "source": "Oilprice",
        "headline": "Iraq rejects OPEC+ oil verdict",
        "summary": "Baghdad refuses a capacity assessment below 5m barrels a day and "
                   "pushes for about 6m ahead of Sunday's meeting.",
        "pin": (44.4, 33.3), "art": "oil",
    },
    {
        "n": 12, "region": "MIDDLE EAST", "field": "ENERGY",
        "label": "REPORTED", "source": "Reuters",
        "headline": "Baghdad orders Kurdish oilfields taken over",
        "summary": "Iraq's PM orders the federal government to run Kurdish-controlled "
                   "oilfields; Kurdish authorities reject the move.",
        "pin": (44.0, 36.2), "art": "oil",
    },
    {
        "n": 13, "region": "NORTH AMERICA", "field": "BUSINESS",
        "label": "CONFIRMED", "source": "FTC",
        "headline": "Shein pays $100m over FTC claims",
        "summary": "The fast-fashion retailer settles US claims it deceived shoppers, hid "
                   "bad reviews and failed on service.",
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
BRIEFS = [
    (17, "Russia keeps up massive missile attacks on Ukraine", "REPORTED", "The Germany Eye", "EUROPE"),
    (18, "IAEA names blacklisted Russian as deputy chief; Kyiv demands withdrawal", "REPORTED", "sangaku-journal", "EUROPE"),
    (19, "Zelensky meets Hungary's PM on Ukrainian soil", "REPORTED", "sangaku-journal", "EUROPE"),
    (20, "US and Qatar hold strategic cooperation talks", "REPORTED", "JagranJosh", "MIDDLE EAST"),
    (21, "UN flags deepening humanitarian strain in Gaza", "REPORTED", "JagranJosh", "MIDDLE EAST"),
    (22, "EU unveils fresh sanctions on Russia", "REPORTED", "JagranJosh", "EUROPE"),
    (23, "Microsoft declares Code Red after 24-hour Teams outage", "REPORTED", "SuMarket / CNBC", "NORTH AMERICA"),
    (24, "Anthropic shares slide below $83 IPO price", "REPORTED", "Newsmriti", "NORTH AMERICA"),
    (25, "India markets reopen after Guru Nanak holiday", "OFFICIAL", "BSE", "ASIA-PACIFIC"),
    (26, "BJP and Akali Dal reunite for Punjab 2027 polls", "CONFIRMED", "JagranJosh", "ASIA-PACIFIC"),
    (27, "Jupiter Wagons ties up with Korea's Woojin on metro trains", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (28, "Brigade buys Secunderabad land for ₹180-crore homes", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (29, "Lupin wins US FDA nod for kidney-disease drug", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (30, "PhysicsWallah plans a digital university in Punjab", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (31, "Uranus at opposition, in the sky all night", "OFFICIAL", "Star Walk", "SPACE"),
    (32, "'Impossible' star system found 28 light-years away", "REPORTED", "SciTechDaily", "SPACE"),
    (33, "World marks day against violence on women", "OFFICIAL", "UN", "GLOBAL"),
    (34, "Romania seals strategic pact; Armenia signs declaration", "REPORTED", "sangaku-journal", "EUROPE"),
    (35, "North Korea to shut Swiss embassy after camp sanctions", "REPORTED", "sangaku-journal", "ASIA-PACIFIC"),
    (36, "Australia weighs laws on AI likenesses", "REPORTED", "sangaku-journal", "ASIA-PACIFIC"),
    (37, "Wars push WFP costs to $727m", "REPORTED", "sangaku-journal", "GLOBAL"),
    (38, "French government admits failures after riots", "REPORTED", "The Germany Eye", "EUROPE"),
    (39, "Car bomb hits governor's office in Meta, Colombia", "REPORTED", "sangaku-journal", "LATIN AMERICA"),
    (40, "Gold ₹1,28,000; Brent $90.70; rupee ₹92.91", "OFFICIAL", "BusinessLine", "ASIA-PACIFIC"),
    (41, "Tech Mahindra fixes Nov 30 date for 1:1 bonus shares", "REPORTED", "BusinessLine", "ASIA-PACIFIC"),
    (42, "63 Moons arm begins ₹1,950-crore payout", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (43, "HDB Financial allots ₹992-crore debentures", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (44, "SJVN's Lower Arun hydro project reaches foundation stage", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (45, "Sathlokhar wins two contracts worth ₹291 crore", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (46, "ABB India parent buys industrial cooling business", "REPORTED", "OneTrader", "ASIA-PACIFIC"),
    (47, "Hexaware named Challenger in Gartner SIAM ranking", "REPORTED", "DSIJ", "ASIA-PACIFIC"),
    (48, "Talbros board to meet Nov 27 on fundraising", "FORECAST", "DSIJ", "ASIA-PACIFIC"),
]

NUMBERS = [
    ("$41bn", "Sanofi deal"),
    ("$54.94bn", "Dell quarter"),
    ("€1tn", "German tax forecast"),
    ("$202bn", "Dell outlook"),
    ("$380m", "Netflix lot"),
    ("$100m", "Shein fine"),
    ("6m b/d", "Iraq's oil ask"),
    ("28 ly", "'impossible' star"),
    ("00:18 UTC", "Shenzhou launch"),
    ("53", "soldiers killed, Yemen"),
]

TIMELINE = [
    ("00:18 UTC", "Shenzhou-24 launches from Jiuquan"),
    ("00:11 UTC", "Germany publishes €1tn tax forecast"),
    ("01:14 UTC", "US weighs tariffs on 16 partners, reported"),
    ("10:00 UTC", "Hera media conference opens in Berlin"),
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
