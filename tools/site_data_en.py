# -*- coding: utf-8 -*-
"""ENGLISH CONTENT for www.corematerial.vn/en/ — mirrors tools/site_data.py.
Edit text here, then run: python3 tools/build_site.py && python3 tools/build_site_en.py
"""
from site_data import COMPANY as _VN_COMPANY

COMPANY = dict(_VN_COMPANY)
COMPANY.update({
    "legal": "CORE MATERIAL SCIENCE AND TECHNOLOGY JOINT STOCK COMPANY",
    "address": "114bis Tran Quoc Toan St., Xuan Hoa Ward, Ho Chi Minh City, Vietnam",
})
LEGAL_VN = _VN_COMPANY["legal"]

VALUES = [
    ("INTEGRITY", "Integrity", "Transparent about origin, quality and scope of supply. We only commit to what is backed by documents and clear agreements."),
    ("INNOVATION", "Innovation", "Actively sourcing better-suited materials, equipment and technology solutions for production and construction in Vietnam."),
    ("PARTNERSHIP", "Partnership", "Long-term work with customers and suppliers: from choosing a solution and trials to after-sales support."),
]

MATERIALS = [
{
 "id": "dry-sand", "form": "Dry sand", "name": "Dry sand (dried & graded silica sand)", "short": "Dry sand",
 "img": "img/san-pham/cat-hero.jpg",
 "pledge": [("CLEAN", "Clean"), ("CONSISTENT", "Consistent"), ("RELIABLE", "Reliable")],
 "intro": "Kiln-dried, screened and graded sand used as aggregate for dry-mix mortar, tile adhesive, self-levelling compounds, GRC, decorative concrete and other industrial applications. Core Material supplies from two sources: Mekong river sand dried and screened at the plant, and white quarry sand from Bao Loc for light-coloured products.",
 "points": [
   "Multiple grain-size ranges to match your product formulation.",
   "Packing on request: jumbo bags or small bags.",
   "Technical data (moisture, grading, impurities) provided per lot and per order.",
 ],
 "sources": [
   ("Mekong river sand – dried & screened at the plant", "River sand is dried in a rotary drum dryer, screened into size grades and filled into jumbo bags on site.", ["No. 1: 0 – 0.3 mm", "No. 2: 0.3 – 0.7 mm", "No. 3: 0.7 – 1.2 mm", "No. 4: 1.2 – 2.4 mm"]),
   ("Bao Loc white sand (quarry sand)", "Light-coloured quarry sand for products that need a white tone: white tile adhesive, decorative mortar and putty, terrazzo.", []),
 ],
 "grades_title": "Bao Loc white sand – graded samples",
 "grades": [
   ("No. 1", "0.0 – 0.3 mm", "img/san-pham/cat-so-1.jpg"),
   ("No. 2", "0.3 – 0.7 mm", "img/san-pham/cat-so-2.jpg"),
   ("No. 3", "0.7 – 1.7 mm", "img/san-pham/cat-so-3.jpg"),
   ("No. 4", "1.7 – 2.4 mm", "img/san-pham/cat-so-4.jpg"),
   ("No. 5", "2.4 – 3.5 mm", "img/san-pham/cat-so-5.jpg"),
   ("No. 6", "3.5 – 5.0 mm", "img/san-pham/cat-so-6.jpg"),
 ],
 "grades_note": "Sample photos of graded sand. Size ranges are indicative; official values follow the inspection report of each lot.",
 "gallery_title": "Mekong river sand drying & screening plant",
 "gallery": [
   ("img/san-pham/cat-mekong-xuong-say.jpg", "Rotary dryer & control room"), ("img/san-pham/cat-mekong-mau-so-1.jpg", "Sand sample No. 1"),
   ("img/san-pham/cat-mekong-mau-so-2.jpg", "Sand sample No. 2"), ("img/san-pham/cat-mekong-dong-bao-jumbo.jpg", "Jumbo bag filling at the plant"),
   ("img/san-pham/cat-mekong-bao-jumbo.jpg", "Finished jumbo bag"), ("img/san-pham/cat-kho-bao-jumbo-minh-hoa.jpg", "Finished-goods store – 1-tonne jumbo bags (illustration)"), ("img/san-pham/cat-kho-thanh-pham-minh-hoa.jpg", "Jumbo bag storage (illustration)"), ("img/san-pham/cat-bao-jumbo-minh-hoa.jpg", "Illustration of planned Core Material jumbo bag"),
 ],
 "videos": [("media/video-cat-mekong-xuong.mp4", "media/video-cat-mekong-xuong-poster.jpg", "Sand drying & screening plant", "Mekong river sand"),
            ("media/video-cat-mekong-mau.mp4", "media/video-cat-mekong-mau-poster.jpg", "Checking finished sand", "Mekong river sand")],
 "slots": ["Sample quality report (moisture, grading) – pending"],
},
{
 "id": "white-cement", "form": "White cement", "name": "White cement", "short": "White cement",
 "img": "img/san-pham/xi-mang-trang-coremat-bao.jpg",
 "img_full": "img/san-pham/xi-mang-trang-coremat.jpg",
 "img_caption": "Illustration of planned CoreMat packaging: 40 kg bag and jumbo bag",
 "pledge": [("WHITENESS", "Whiteness"), ("CONSISTENCY", "Consistency"), ("STRENGTH", "Strength")],
 "intro": "White cement supply for material production (mortars, tile adhesives, putty, terrazzo tiles, terrazzo grinding stones, decorative products) and for construction.",
 "points": [
   "Blended white cement line under our own CoreMat brand (in development), 40 kg and jumbo bags: PCW 32.5 – for grinding stones; PCW 42.5 – for terrazzo and putty; PCW 52.5 – for premium putty.",
   "Composition, strength class, whiteness and origin are provided for each specific product; certificate of analysis (COA) with every lot.",
   "Advice on choosing the right white cement for your application.",
   "Research direction for specialty white cements: UHPC, micro-cement, self-levelling compounds, terrazzo-specific cement.",
 ],
 "slots": ["Data sheet per product code (strength class, whiteness, bag size)"],
},
{
 "id": "admixtures", "form": "VAE / RDP", "name": "Admixtures, minerals & construction chemicals", "short": "Admixtures & minerals",
 "img": None,
 "intro": "VAE emulsions, redispersible polymer powders (RDP), minerals and other admixtures for dry-mix mortar, tile adhesive, waterproofing, putty and paint.",
 "points": [
   "Polymer admixtures: VAE, RDP – better adhesion and anti-sag for tile adhesives and mortars.",
   "Minerals: ultra-white CaCO₃ powder, talc, BaSO₄, gypsum, titanium dioxide (TiO₂).",
   "Planned extensions: waterproofing admixtures, surface hardeners, specialty adhesives.",
   "Selection advice by application; technical documents (TDS, SDS) for each product.",
 ],
 "slots": ["Product code list and TDS"],
},
{
 "id": "concrete-fibres", "form": "Concrete reinforcing fibres", "name": "Concrete reinforcing fibres (steel, PP)", "short": "Concrete fibres",
 "img": None,
 "intro": "Fibres dispersed in concrete and mortar limit shrinkage cracking and improve toughness and impact resistance – for industrial floors, shotcrete, precast elements and mortars.",
 "points": [
   "Hooked-end steel fibres 3D / 4D: industrial floors, tunnel and slope shotcrete, precast elements.",
   "Polypropylene (PP) fibres: shrinkage-crack control for mortar, concrete, floors and screeds.",
   "Dosage advice by application; technical data sheet (TDS) for each product code.",
 ],
 "slots": ["Photos of steel / PP fibre products and data sheets"],
},
{
 "id": "decorative", "form": "Terrazzo chips / colour granules / pigments", "name": "Terrazzo chips, coloured sand, glass granules & pigments", "short": "Decorative materials",
 "img": "img/da-ho-phach.jpg",
 "intro": "Decorative materials for terrazzo, decorative floors and walls, architectural concrete and finishes: stone chips, coloured sand, coloured glass granules and pigments.",
 "points": [
   "Wide range of colours and grain sizes.",
   "Natural coloured sand, epoxy-coated coloured sand and colour flakes for decorative floors and walls.",
   "Toll grinding of coloured stone / sand into ultra-fine powder for paints and coloured mortars, on order.",
   "Samples available for architects and contractors.",
 ],
 "gallery": [
   ("img/hat-xanh-tay.jpg", "Blue glass granules"), ("img/da-ho-phach.jpg", "Amber granules"),
   ("img/thuy-tinh-luc.jpg", "Green glass"), ("img/da-ngoc.jpg", "Turquoise granules"),
   ("img/bot-mau.jpg", "Coloured sand & pigments"), ("img/cat-den.jpg", "Black sand"),
   ("img/da-xanh-duong.jpg", "Blue glass"), ("img/hat-luc.jpg", "Green granules"),
 ],
},
]

TECH_INTRO = "Core Material is building an equipment and technology trading business, connecting suitable suppliers with production and construction needs in Vietnam."

EQUIPMENT = [
{
 "id": "grc-spraying", "form": "GRC/GFRC spraying equipment",
 "name": "GRC / GFRC spraying equipment", "k": "Precast production",
 "img": "img/thiet-bi/may-phun-grc.jpg",
 "gallery": ["img/thiet-bi/may-phun-grc-2.jpg", "img/thiet-bi/may-phun-grc-3.jpg"],
 "short": "Spray systems for glass-fibre reinforced concrete: façade panels, cornices and architectural elements.",
 "intro": [
   "GRC/GFRC (glass-fibre reinforced concrete) is used to make thin, light yet durable elements: façade cladding, cornices, louvres, planters and decorative architectural pieces.",
   "GRC spraying equipment delivers the mortar and glass fibre onto the mould, giving more uniform output and higher productivity than manual work.",
 ],
 "diff": "Unlike wall-plastering machines (used on site), GRC spraying equipment serves precast production in the workshop, together with moulds and its own curing process.",
 "sections": [
   ("Applications", ["Façade panels, cornices, columns, decorative louvres", "Architectural elements and decorative GFRC products", "Precast element workshops"]),
   ("Standard set", ["Screw-type GRC sprayer with horizontal jib and control cabinet", "200 L high-speed mixer (2.2 kW, 960 rpm) – included in the set", "Mortar pump stator / rotor", "Spray gun with built-in fibre chopper, spare nozzle and gun core", "16 m air hose, 10 m mortar hose", "Fibre cutting blades, GRC rollers and accessories"]),
   ("Fibre chopping & mix ratio", ["Uses alkali-resistant roving of 2,400 tex or 4,800 tex", "Fibre / mortar ratio adjustable from 3 to 5%", "Cut length set by the number and spacing of blades on the roller; short lengths down to 6 – 8 mm possible"]),
   ("Optional equipment & consumables", ["AR glass fibre: 19 kg rolls, 2,400 tex, ZrO₂ content 16.75% – independent test report to EN 15422", "Air compressor (not included): recommended 15 kW screw compressor, 1.1 m³/min, max. 1.58 MPa", "Spare-parts kit: stator/rotor, topcoat spray gun, coaxial spray gun"]),
   ("Wear parts (manufacturer data)", ["Pump stator / rotor: service life about 5,000 m² of spraying, then replace", "Spray-gun motor: replacement recommended about every 6 months in daily continuous use"]),
   ("Warranty & support", ["12-month manufacturer warranty for defects not caused by the user", "English operating manual, wiring diagram and instruction videos included", "Remote video training for first operation and commissioning", "Installation, training and support by Core Material as agreed"]),
 ],
 "spec": [
   ("Model", "Type 80 screw GRC sprayer"),
   ("Spray motor / mixing motor", "4.0 kW / 2.2 kW"),
   ("Screw speed", "20 – 200 rpm"),
   ("Mortar conveying capacity", "1,600 kg/h"),
   ("Hopper capacity", "80 L"),
   ("Working air pressure", "0.6 – 0.8 MPa"),
   ("Horizontal jib radius", "4.5 m"),
   ("Spraying output (manufacturer data)", "up to 500 m²/h – net spraying time by an experienced operator; excludes mortar feeding, cleaning and stops"),
   ("Power supply", "3-phase 380 V / 50 Hz (sprayer and mixer)"),
   ("Compressed air required", "recommended 1.1 m³/min (15 kW screw compressor)"),
   ("Dimensions (L × W × H)", "1,400 × 1,000 × 2,200 mm"),
   ("Weight", "700 kg (sprayer + mixer)"),
   ("Packing", "Wooden cases, 2 packages"),
 ],
 "videos": [("media/video-phun-grc.mp4", "media/video-phun-grc-poster.jpg", "GRC spraying equipment", "Video from the equipment supplier"),
            ("media/video-san-xuat-grc.mp4", "media/video-san-xuat-grc-poster.jpg", "Mixing & feeding", "Video from the equipment supplier")],
 "slots": ["Photos of the actual machine on arrival in Vietnam"],
},
{
 "id": "wall-plastering-machine", "form": "Wall plastering machine",
 "name": "Wall plastering (mortar spraying) machine", "k": "On-site construction",
 "img": "img/thiet-bi/may-bom-phun-vua-tw20f.jpg",
 "gallery": ["img/thiet-bi/ung-dung-phun-vua-to.jpg", "img/thiet-bi/ung-dung-phun-vua-tran-tuong.jpg", "img/thiet-bi/ung-dung-gia-co-mai-doc.jpg"],
 "short": "Two mortar-spraying machine lines for on-site work: squeeze-type mortar pumps (3 models, long-distance and high-rise pumping) and a mobile screw-type plastering machine.",
 "intro": [
   "Shortage of skilled plasterers, rising labour costs and uneven hand-applied quality (hollows, cracks, varying coat thickness) are the bottlenecks of traditional plastering. A mortar pump mechanises the whole chain: mixing – pumping through the line – spraying directly onto the surface.",
   "The machines Core Material offers use the squeeze-pump principle: rollers compress a squeeze hose to push the mortar, so the mortar only travels inside the hose – fewer wearing parts in contact with mortar and quick cleaning.",
   "It works best together with a suitable ready-mixed mortar, a trained crew and a proper operating and cleaning routine.",
 ],
 "sections": [
   ("Applications", ["Spray plastering of walls and ceilings – interior and exterior", "Grouting the core of lightweight partition walls", "Spraying mortar onto stay-in-place formwork (expanded metal mesh)", "Slope, riverbank and embankment protection"]),
   ("Standard set (per manufacturer's quotation)", ["Squeeze pump with 2 squeeze hoses", "Mortar mixer and anti-settling hopper agitator", "About 60 m of steel delivery pipe (TW-60: about 30 m) with 45°/90° elbows and stainless clamps", "2 × 10 m flexible hoses with camlock couplings", "Spray gun", "Exact items and quantities confirmed per order"]),
   ("4-step workflow", ["Site preparation: position the machine and centralise power, water and materials", "Metered feeding: batch mortar and water by ratio for a consistent mix", "Pumping & spraying: mortar runs through steel lines and hoses and is sprayed with a dedicated gun", "Fast cleanout: dedicated sponge balls are circulated through the line – routine cleaning in about 10 minutes (per manufacturer)"]),
   ("Reference productivity (per manufacturer)", ["Traditional hand plastering: about 20 m² per man-day", "Mixer + hand plastering: about 90 m² per man-day", "Squeeze-pump spraying: about 200 m² per man-day", "Actual output depends on mix design, aggregate, admixtures, coat thickness and line layout"]),
   ("Power / water", ["Pump and hopper agitator: 3-phase 220 V / 50 Hz (standard configuration); mixer: single-phase 220 V / 50 Hz", "Sites on a 3-phase 380 V grid: power arrangement confirmed when ordering", "Clean water for mixing and cleaning"]),
   ("Operation & cleaning", ["Check the machine and squeeze hose before each shift", "Pre-wet hopper, squeeze hose and line before feeding mortar", "Clean the line right after work to prevent blockages"]),
 ],
 "models_title": "Models & specifications",
 "models_lead": "Three squeeze-pump model lines, selected by project scale and the pumping height/distance required.",
 "model_cols": ["Flow rate", "Max. vertical / horizontal", "Squeeze hose (inner dia.)", "Delivery pipe"],
 "models": [
   ("TW-60", "img/thiet-bi/may-bom-phun-vua-tw60.jpg", "Houses, small projects, demonstration and trials", ["0.7 – 2 m³/h", "12 m / 40 m", "33 mm", "D38"]),
   ("TW-20F", "img/thiet-bi/may-bom-phun-vua-tw20f.jpg", "Large-area projects, factory buildings", ["1.4 – 2.5 m³/h", "60 m / 200 m", "38 mm", "D38"]),
   ("TW-75 / TW-105", "img/thiet-bi/may-bom-phun-vua-tw75.jpg", "High pumping volumes – highest flow in the range", ["2 – 6 m³/h", "45 m / 160 m", "43 / 50 mm", "D43"]),
 ],
 "models_note": "Flow rates and distances are manufacturer-stated; maximum vertical and horizontal distances are not achieved at the same time. Actual results depend on mortar mix, aggregate characteristics, admixture ratio and line layout – confirm with your mortar and site conditions before selecting a machine.",
 "apps_title": "Applications",
 "apps": [
   ("img/thiet-bi/ung-dung-phun-vua-tran-tuong.jpg", "Spray plastering of walls"),
   ("img/thiet-bi/ung-dung-bom-vua-vach-nhe.jpg", "Lightweight partition wall grouting"),
   ("img/thiet-bi/ung-dung-coffa-de-lai.jpg", "Stay-in-place formwork"),
   ("img/thiet-bi/ung-dung-gia-co-mai-doc.jpg", "Slope and riverbank protection"),
 ],
 "package": [
   ("Survey & trial", "Clarify site conditions and run a mock-up spray with the mortar to be used."),
   ("Operator training", "Training on operation, safety, cleaning and basic troubleshooting for the crew."),
   ("On-site support", "Support during the first phase of putting the machine into real work."),
   ("Spare parts & support", "Spare-parts plan (squeeze hoses, spray guns…) and technical support channel as agreed."),
 ],
 "spec": [
   ("Principle", "Squeeze (peristaltic) pump or screw pump (rotor / stator)"),
   ("Models", "Squeeze pumps: TW-60 · TW-20F · TW-75 / TW-105; mobile screw-type plastering machine"),
   ("Flow rate", "0.7 – 6 m³/h depending on model"),
   ("Max. pumping distance", "up to 60 m vertical, 200 m horizontal depending on model"),
   ("Power supply", "3-phase 220 V / 50 Hz (standard); 380 V grid arrangement confirmed when ordering"),
   ("Origin", "Taiwan"),
 ],
 "line2": {
   "title": "Screw-type plastering machine",
   "lead": "A second line from a different manufacturer: a compact, mobile screw-type plastering machine for wall plastering on small and medium projects.",
   "gallery": [("img/thiet-bi/may-phun-vua-5.jpg", "Machine overview"), ("img/thiet-bi/may-phun-vua-4.jpg", "Hopper with screen"), ("img/thiet-bi/may-phun-vua-2.jpg", "Rear view"), ("img/thiet-bi/may-phun-vua-1.jpg", "Control panel")],
   "points": ["Screw pump (rotor / stator) for continuous, steady mortar delivery", "Hopper with screen and vibrator motor to break up lumps", "Electrical control panel; on-board air compressor (depending on configuration)", "Wheeled frame, easy to move around the site", "Specifications and configuration supplied with the catalogue – please contact us"],
 },
 "videos": [("media/video-phun-vua.mp4", "media/video-phun-vua-poster.jpg", "Screw-type plastering machine", "Video from the equipment supplier")],
 "slots": ["Video/photos of jobs in Vietnam", "Dimensions and weight per model (pending detailed catalogue)"],
},
{
 "id": "palletizing-robot", "form": "Bag handling & palletizing robot",
 "name": "Bag handling & palletizing robot", "k": "Factory automation",
 "img": None,
 "short": "Automated bag handling and palletizing in the factory: less reliance on manual labour, steadier production rhythm.",
 "intro": [
   "In dry-mortar, cement and stone-powder plants, bag handling and palletizing require a lot of heavy labour. Palletizing robots and automatic feeding systems reduce that effort and stabilise output.",
   "Each project needs a survey of layout, bag type and production rate to select the right configuration.",
 ],
 "sections": [
   ("Survey information", ["Product handled: bag type, bag weight, bag material", "Payload and target output (bags/hour)", "Suitable gripper type", "Conveyors and pallet positions", "Layout and area safety"]),
 ],
 "spec": [("Product handled", None), ("Payload", None), ("Output", None), ("Gripper", None), ("Conveyors & layout", None)],
 "videos": [],
 "slots": ["Licensed photos / video of real robots", "Specifications and scope of supply"],
},
]

PROCESS = [
 ("Understand the need", "Collect requirements and operating conditions: product, site, layout, output."),
 ("Select configuration", "Work with suppliers to choose a suitable equipment configuration."),
 ("Implementation plan", "Agree on supply, installation and commissioning."),
 ("Training & after-sales", "Agree on training, spare parts and after-sales support."),
]
SCOPE_NOTE = "Scope of supply and support is defined per equipment and per specific agreement."

FORM_GROUPS = [
 ("Raw materials & Materials", ["Dry sand", "White cement", "VAE / RDP", "Concrete reinforcing fibres", "Terrazzo chips / colour granules / pigments"]),
 ("Equipment & Automation", [e["form"] for e in EQUIPMENT]),
 ("Other", ["Investment partnership", "Other"]),
]

# VN path -> EN path (language switch + hreflang)
PATHS = {
 "/": "/en/", "/gioi-thieu/": "/en/about/", "/vat-lieu/": "/en/materials/", "/may-moc/": "/en/equipment/",
 "/may-moc/phun-grc/": "/en/equipment/grc-spraying/", "/may-moc/phun-vua-to-tuong/": "/en/equipment/wall-plastering-machine/",
 "/may-moc/robot-xep-pallet/": "/en/equipment/palletizing-robot/", "/ung-dung/": "/en/applications/",
 "/lien-he/": "/en/contact/", "/hop-tac-dau-tu/": "/en/investment/",
}
