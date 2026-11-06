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
 "id": "dry-sand", "form": "Dry sand", "name": "Dry sand (graded silica sand)", "short": "Dry sand",
 "img": "img/san-pham/cat-hero.jpg",
 "pledge": [("CLEAN", "Clean"), ("CONSISTENT", "Consistent"), ("RELIABLE", "Reliable")],
 "intro": "Kiln-dried, screened and graded sand used as aggregate for dry-mix mortar, tile adhesive, self-levelling compounds, decorative concrete and other industrial applications.",
 "points": [
   "Multiple grain-size ranges to match your product formulation.",
   "Packing on request: jumbo bags or small bags.",
   "Technical data (moisture, grading, impurities) provided per lot and per order.",
 ],
 "grades": [
   ("No. 1", "0.0 – 0.3 mm", "img/san-pham/cat-so-1.jpg"),
   ("No. 2", "0.3 – 0.7 mm", "img/san-pham/cat-so-2.jpg"),
   ("No. 3", "0.7 – 1.7 mm", "img/san-pham/cat-so-3.jpg"),
   ("No. 4", "1.7 – 2.4 mm", "img/san-pham/cat-so-4.jpg"),
   ("No. 5", "2.4 – 3.5 mm", "img/san-pham/cat-so-5.jpg"),
   ("No. 6", "3.5 – 5.0 mm", "img/san-pham/cat-so-6.jpg"),
 ],
 "grades_note": "Sample photos of graded sand. Size ranges are indicative; official values follow the inspection report of each lot.",
 "slots": ["Sample quality report (moisture, grading) – pending", "Photos of real packing / delivery"],
},
{
 "id": "white-cement", "form": "White cement", "name": "White cement", "short": "White cement",
 "img": "img/san-pham/xi-mang-trang-coremat-bao.jpg",
 "img_full": "img/san-pham/xi-mang-trang-coremat.jpg",
 "img_caption": "Illustration of planned CoreMat packaging: 40 kg bag and jumbo bag, grade 42.5 / 52.5",
 "pledge": [("WHITENESS", "Whiteness"), ("CONSISTENCY", "Consistency"), ("STRENGTH", "Strength")],
 "intro": "White cement supply for material production (mortars, tile adhesives, putty, terrazzo tiles, decorative products) and for construction.",
 "points": [
   "Composition, strength class, whiteness and origin are provided for each specific product.",
   "Certificate of analysis (COA) supplied with every lot.",
   "Advice on choosing the right white cement for your application.",
   "Developing a blended white cement line under our own CoreMat brand (planned: 40 kg and jumbo bags, grade 42.5 / 52.5).",
 ],
 "slots": ["Data sheet per product code (strength class, whiteness, bag size)"],
},
{
 "id": "admixtures", "form": "VAE / RDP", "name": "Construction admixtures & chemicals (VAE, RDP…)", "short": "VAE / RDP",
 "img": None,
 "intro": "VAE emulsions, redispersible polymer powders (RDP) and other admixtures for dry-mix mortar, tile adhesive, waterproofing and putty.",
 "points": [
   "Advice on admixture selection by application and technical requirement.",
   "Technical documents (TDS, SDS) supplied for each product.",
 ],
 "slots": ["Product code list and TDS"],
},
{
 "id": "decorative", "form": "Terrazzo chips / colour granules / pigments", "name": "Terrazzo chips, glass granules & pigments", "short": "Decorative materials",
 "img": "img/da-ho-phach.jpg",
 "intro": "Decorative materials for terrazzo, architectural concrete and finishes: stone chips, coloured glass granules, coloured sand and pigments.",
 "points": [
   "Wide range of colours and grain sizes.",
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
 "img": "img/thiet-bi/may-phun-vua-2.jpg",
 "gallery": ["img/thiet-bi/may-phun-vua-1.jpg", "img/thiet-bi/may-phun-vua-4.jpg", "img/thiet-bi/may-phun-vua-5.jpg"],
 "short": "Mechanises feeding, pumping and spraying of plaster mortar, reducing manual labour and speeding up construction.",
 "intro": [
   "A mortar spraying machine mechanises mortar feeding, pumping and spraying onto walls instead of hand plastering. The mortar is applied evenly, the coat is denser and progress improves.",
   "It works best together with a suitable ready-mixed mortar, a trained crew and a proper operating and cleaning routine.",
 ],
 "sections": [
   ("Suitable mortars", ["Cement-based ready-mixed plaster", "Other mortars and putties as recommended by the machine maker"]),
   ("Machine configuration", ["Machine body, hopper and mortar pump", "Mortar hose and spray gun", "Air compressor (depending on configuration)"]),
   ("Power / water / air", ["Power supply as per machine specification", "Clean water for mixing and cleaning", "Compressed air for the spray gun"]),
   ("Operation & cleaning", ["Check and lubricate before each shift", "Pre-wet hopper, pump and hoses before feeding mortar", "Flush with clean water after work to prevent blockages"]),
 ],
 "package": [
   ("Survey & trial", "Clarify site conditions and run a mock-up spray with the mortar to be used."),
   ("Operator training", "Training on operation, safety, cleaning and basic troubleshooting for the crew."),
   ("On-site support", "Support during the first phase of putting the machine into real work."),
   ("Spare parts & support", "Spare-parts plan and technical support channel as agreed."),
 ],
 "spec": [("Model", None), ("Spraying output", None), ("Pumping height / distance", None), ("Power supply", None), ("Dimensions, weight", None)],
 "videos": [("media/video-phun-vua.mp4", "media/video-phun-vua-poster.jpg", "Spraying mortar onto a wall", "Video from the equipment supplier")],
 "slots": ["Confirmed catalogue and data sheet", "Video/photos of jobs in Vietnam"],
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
 ("Raw materials & Materials", ["Dry sand", "White cement", "VAE / RDP", "Terrazzo chips / colour granules / pigments"]),
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
