#!/usr/bin/env python3
"""Generator za ARC METAL stran.

python3 build.py preview  -> dist-preview/  (relativne povezave .../index.html)
python3 build.py site     -> dist-site/     (čisti URL-ji /o-nas/, za GitHub Pages)
"""
import html, os, shutil, sys

MODE = sys.argv[1] if len(sys.argv) > 1 else "site"
OUT = "dist-preview" if MODE == "preview" else "dist-site"
HERE = os.path.dirname(os.path.abspath(__file__))

PHONE = "+386 70 557 514"
PHONE_HREF = "tel:+38670557514"
EMAIL = "info@arcmetal.si"
ADDR1 = "ARC METAL, Blaž Bratušek s.p."
ADDR2 = "Zgornje Hoče 7, 2311 Hoče, Slovenija"
MAT = "9418792000"
DDV = "SI99750716"

MARK = open(os.path.join(HERE, "logo", "logo-inline.svg"), encoding="utf-8").read()

SERVICES = [
    ("storitve-jeklene-konstrukcije", "Jeklene konstrukcije",
     "Izdelava, varjenje in montaža jeklenih konstrukcij po tehnični dokumentaciji: hale, podporni sistemi, platforme in podesti."),
    ("industrijska-montaza", "Industrijska montaža",
     "Montaža konstrukcij, tehnološke opreme, cevovodov in kovinskih sklopov v proizvodnih obratih ali na terenu."),
    ("storitve-varjenje-cevovodov", "Varjenje cevovodov",
     "TIG varjenje procesnih cevovodov iz ogljikovega in nerjavnega jekla, v delavnici ali na lokaciji."),
    ("remonti-in-popravila", "Remonti in popravila",
     "Načrtovani remonti, sanacije, ojačitve in intervencijska popravila industrijske opreme in konstrukcij."),
    ("prefabrikacija-cevovodov", "Prefabrikacija cevovodov",
     "Izdelava cevnih sklopov po izometrijah v delavnici, pripravljenih za montažo na objektu."),
    ("nedestruktivno-testiranje-ndt", "Neporušitvene preiskave (NDT)",
     "Kontrola kakovosti varjenih spojev in komponent ter dokumentiranje rezultatov skladno z zahtevami projekta."),
]
SVC_NAME = {s[0]: s[1] for s in SERVICES}

STANDARDS = [
    ("ISO 9606-1", "Preskušanje usposobljenosti varilcev – talilno varjenje jekel",
     "Naši varilci so certificirani po SIST EN ISO 9606-1 za postopke, položaje in skupine materialov, ki jih uporabljajo pri delu."),
    ("WPS · WPQR", "EN ISO 15609-1 · EN ISO 15614-1",
     "Za vsak projekt pripravimo navodila za varjenje (WPS). Kadar projekt zahteva kvalificiran postopek, izvedemo kvalifikacijo (WPQR) po EN ISO 15614-1."),
    ("Kontrola in dokumentacija", "Vizualna kontrola · NDT · poročila",
     "Zvare kontroliramo med izdelavo in pred predajo. Vrsto neporušitvenih preiskav in obseg dokumentacije določijo zahteve projekta."),
]

PROJECTS = [
    ("Industrijsko varjenje cevi", "Cevovodi",
     "Precizno varjenje cevi za industrijske sisteme s poudarkom na vzdržljivosti, poravnavi in tehničnih zahtevah."),
    ("Montaža jeklene konstrukcije", "Konstrukcije",
     "Montaža in varjenje jeklenih konstrukcij, izvedeno v skladu s projektnimi specifikacijami."),
    ("Industrijsko vzdrževanje in popravila", "Vzdrževanje",
     "Popravila in ojačitvena dela za obnovitev poškodovanih komponent in nadaljnje obratovanje."),
    ("Podpora pri varjenju na terenu", "Teren",
     "Varilske storitve neposredno na industrijskih lokacijah, s hitrim odzivom in minimalnimi izpadi proizvodnje."),
    ("Montaža kovinskih konstrukcij in komponent", "Montaža",
     "Montaža in vgradnja kovinskih konstrukcij in komponent v skladu s tehničnimi zahtevami in pogoji na gradbišču."),
    ("Popravilo industrijske opreme", "Popravila",
     "Popravilo in obnova industrijske opreme ter komponent za ohranjanje zmogljivosti, varnosti in učinkovitosti."),
]

INDUSTRIES = ["Proizvodnja", "Avtomobilska industrija", "Energetika", "Procesna industrija",
              "Živilska industrija", "Kemična industrija", "Gradbeništvo"]

STD_LINE = ("Standardi", "Varilci po ISO 9606-1 · WPS/WPQR po zahtevah projekta")

SVC_FACTS = {
    "storitve-jeklene-konstrukcije": [
        ("Postopki", "MIG/MAG · MMA", "ISO 4063: 135 · 111"),
        ("Material", "Ogljikovo (konstrukcijsko) jeklo", None),
        ("Obseg", "Hale, podporni sistemi, platforme, podesti", None),
        ("Izvedba", "Delavnica in montaža na lokaciji", None),
        STD_LINE + (None,)],
    "industrijska-montaza": [
        ("Obseg", "Konstrukcije, tehnološka oprema, cevovodi, kovinski sklopi", None),
        ("Panoge", "Proizvodnja, avtomobilska in procesna industrija", None),
        ("Izvedba", "Delavnica in teren", None),
        ("Zahteve", "Po tehnični dokumentaciji, tolerancah in varnostnih zahtevah", None),
        STD_LINE + (None,)],
    "storitve-varjenje-cevovodov": [
        ("Postopek", "TIG", "ISO 4063: 141"),
        ("Material", "Ogljikovo in nerjavno jeklo", None),
        ("Elementi", "Cevi, kolena, T-kosi, prirobnice, reducirke", None),
        ("Izvedba", "Delavnica in teren", None),
        STD_LINE + (None,)],
    "remonti-in-popravila": [
        ("Vrsta del", "Načrtovani remonti in intervencijska popravila", None),
        ("Obseg", "Varilska popravila, sanacije, ojačitve, zamenjava delov", None),
        ("Izvedba", "Na lokaciji, usklajeno z zaustavitvami proizvodnje", None),
        STD_LINE + (None,)],
    "prefabrikacija-cevovodov": [
        ("Podlaga", "Izometrije, risbe in specifikacije materiala", None),
        ("Postopek", "TIG", "ISO 4063: 141"),
        ("Material", "Ogljikovo in nerjavno jeklo", None),
        ("Kontrola", "Dimenzijski pregled in zahtevane preiskave pred odpremo", None),
        STD_LINE + (None,)],
    "nedestruktivno-testiranje-ndt": [
        ("Predmet", "Varjeni spoji, komponente, konstrukcijski elementi", None),
        ("Metoda", "Glede na zahteve projekta in vrsto materiala", None),
        ("Izvedba", "Med izdelavo, pri montaži in med remonti", None),
        ("Rezultat", "Zapisi in poročila o pregledih", None)],
}


def e(s):
    return html.escape(s, quote=True)


class Page:
    def __init__(self, slug):
        self.slug = slug

    def root(self):
        return "../" if self.slug else ""

    def link(self, slug):
        if MODE == "preview":
            return f"{self.root()}{slug + '/' if slug else ''}index.html"
        return f"{self.root()}{slug + '/' if slug else ''}" or "./"


def facts(rows, title=None):
    t = f'<p class="facts-title">{e(title)}</p>' if title else ""
    body = "".join(
        f'<div><dt>{e(k)}</dt><dd>{e(v)}{f"<small>{e(sm)}</small>" if sm else ""}</dd></div>'
        for k, v, sm in rows)
    return f'<div>{t}<dl class="facts">{body}</dl></div>'


def header(p, current):
    def cur(s):
        return ' aria-current="page"' if s == current else ""
    dd = "".join(f'<a href="{p.link(s)}">{e(n)}</a>' for s, n, _ in SERVICES)
    return f'''<a class="skip" href="#main">Preskoči na vsebino</a>
<header class="site-header"><div class="wrap">
  <a class="brand" href="{p.link('')}" aria-label="ARC METAL, domača stran">{MARK}</a>
  <button class="menu-toggle" id="menu-toggle" aria-expanded="false" aria-controls="nav">Meni</button>
  <nav class="nav" id="nav" aria-label="Glavni meni">
    <a href="{p.link('o-nas')}"{cur('o-nas')}>O nas</a>
    <div class="dd"><a href="{p.link('storitve')}"{cur('storitve')}>Storitve</a><div class="dd-menu">{dd}</div></div>
    <a href="{p.link('projekti')}"{cur('projekti')}>Projekti</a>
    <a href="{p.link('kontakt')}"{cur('kontakt')}>Kontakt</a>
    <a class="nav-tel" href="{PHONE_HREF}">{PHONE}</a>
  </nav>
</div></header>'''


def partner_block():
    return '''<div class="partner"><div class="wrap">
  <div style="display:grid;gap:8px"><h2>Mreža partnerjev in podizvajalcev</h2>
  <p class="muted">Če vas zanima dolgoročno sodelovanje ali podizvajalsko partnerstvo, nam pustite e-poštni naslov.</p></div>
  <div><form class="js-partner" novalidate>
    <label for="partner-email" class="skip">E-poštni naslov</label>
    <input id="partner-email" type="email" name="email" placeholder="ime@podjetje.si" autocomplete="email" required>
    <button class="btn btn-line" type="submit">Pošlji</button></form>
  <p class="form-note" aria-live="polite"></p></div>
</div></div>'''


def cta(p, title="Pošljite dokumentacijo ali opis projekta.",
        text="Pripravimo ponudbo glede na obseg, materiale, zahtevane standarde in rok izvedbe."):
    return f'''<section class="cta"><div class="wrap">
  <div style="display:grid;gap:18px"><h2>{e(title)}</h2><p style="max-width:56ch">{e(text)}</p>
  <div class="btn-row" style="margin-top:8px"><a class="btn btn-white" href="{p.link('kontakt')}">Kontaktirajte nas</a></div></div>
  <div class="contact-lines"><span class="label" style="color:#8d9298">Neposredno</span>
  <a href="{PHONE_HREF}">{PHONE}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div></section>'''


def footer(p):
    svcs = "".join(f'<li><a href="{p.link(s)}">{e(n)}</a></li>' for s, n, _ in SERVICES)
    return f'''<footer class="site-footer"><div class="wrap">
  <div class="foot-grid">
    <div class="foot-about"><a class="brand" href="{p.link('')}" aria-label="ARC METAL">{MARK}</a>
      <p>Industrijsko varjenje, montaža, remonti in kontrola zvarov. V delavnici ali na terenu, za naročnike v Sloveniji in tujini.</p>
      <p class="foot-std">Varilci certificirani po ISO 9606-1</p></div>
    <div><h4>Podjetje</h4><ul><li><a href="{p.link('o-nas')}">O nas</a></li><li><a href="{p.link('storitve')}">Storitve</a></li>
      <li><a href="{p.link('projekti')}">Projekti</a></li><li><a href="{p.link('kontakt')}">Kontakt</a></li></ul></div>
    <div><h4>Storitve</h4><ul>{svcs}</ul></div>
    <div><h4>Kontakt</h4><ul><li><a href="{PHONE_HREF}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
      <li>{e(ADDR1)}<br>{e(ADDR2)}</li><li>Matična št.: {MAT}<br>ID za DDV: {DDV}</li></ul></div>
  </div>
  <div class="foot-bottom"><span>© 2026 ARC METAL. Vse pravice pridržane.</span>
    <span class="links"><a href="{p.link('pravilnik-o-zasebnosti-2')}">Pravilnik o zasebnosti</a><a href="{p.link('pogoji-poslovanja')}">Pogoji poslovanja</a></span></div>
</div></footer>'''


def layout(p, title, desc, body, current):
    full = "ARC METAL | Industrijsko varjenje, montaža in remonti" if title is None else f"{title} | ARC METAL"
    return f'''<!DOCTYPE html>
<html lang="sl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400&family=IBM+Plex+Sans:wght@400;450;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p.root()}style.css">
</head>
<body>
{header(p, current)}
<main id="main">
{body}
</main>
{partner_block() if p.slug == "o-nas" else ""}
{footer(p)}
<script src="{p.root()}main.js"></script>
</body>
</html>
'''


def page_head(p, crumbs, h1, lead=None):
    c = [f'<a href="{p.link("")}">Domov</a>']
    for label, slug in crumbs:
        c.append('<span aria-hidden="true">/</span>')
        c.append(f'<a href="{p.link(slug)}">{e(label)}</a>' if slug is not None else f'<span aria-current="page">{e(label)}</span>')
    ld = f'<p class="lead">{e(lead)}</p>' if lead else ""
    return f'''<div class="page-head"><div class="wrap">
  <nav class="crumbs" aria-label="Drobtinice">{"".join(c)}</nav><h1>{e(h1)}</h1>{ld}
</div></div>'''


def sec_head(label, title, text=None, extra=""):
    t = f'<p class="muted" style="max-width:60ch">{e(text)}</p>' if text else ""
    return f'<div class="sec-head"><span class="label">{e(label)}</span><div class="body"><h2>{e(title)}</h2>{t}{extra}</div></div>'


def svc_list(p, exclude=None):
    rows = []
    for i, (s, n, d) in enumerate(SERVICES):
        if s == exclude:
            continue
        rows.append(f'<a class="svc-row" href="{p.link(s)}"><span class="n">{i+1:02d}</span><h3>{e(n)}</h3><p>{e(d)}</p><span class="go">Podrobnosti →</span></a>')
    return f'<div class="svc-list">{"".join(rows)}</div>'


def std_block():
    items = "".join(f'<div class="std"><span class="num">{e(c)}</span><span class="name">{e(n)}</span><p>{e(d)}</p></div>'
                    for c, n, d in STANDARDS)
    return f'<div class="std-grid">{items}</div><p class="std-note">Certifikate varilcev, navodila WPS in poročila o kontroli predložimo skladno z zahtevami projekta. Oznake postopkov so navedene po ISO 4063.</p>'


def steps(items):
    return '<div class="steps">' + "".join(
        f'<div class="step"><span class="n">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>'
        for i, (t, d) in enumerate(items)) + "</div>"


def proj_list(items):
    return '<div class="proj-list">' + "".join(
        f'<article class="proj"><span class="n">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p><span class="cat">{e(c)}</span></article>'
        for i, (t, c, d) in enumerate(items)) + "</div>"


PROCESS = [("Pregled zahtev", "Pregled dokumentacije, materialov, zahtevanih standardov in pogojev izvedbe."),
           ("Priprava", "Izbira varilnega postopka in WPS, priprava materiala in organizacija dela."),
           ("Izvedba", "Varjenje in montaža po tehnični dokumentaciji, v delavnici ali na lokaciji."),
           ("Kontrola in predaja", "Vizualna in po potrebi neporušitvena kontrola, dokumentacija in predaja.")]


def home():
    p = Page("")
    faq = [
        ("Ali so vaši varilci certificirani?", "Da, varilci so certificirani po SIST EN ISO 9606-1. Za vsak projekt pripravimo navodila za varjenje (WPS), kvalifikacijo postopka (WPQR po EN ISO 15614-1) pa izvedemo, kadar jo projekt zahteva."),
        ("Katere materiale varite?", "Ogljikovo jeklo, nerjavno jeklo in aluminij. Postopek izberemo glede na material, debelino stene, položaj zvara in zahteve dokumentacije."),
        ("Ali izvajate neporušitvene preiskave?", "Da. Vrsto kontrole določijo zahteve projekta, rezultate pa dokumentiramo v poročilih."),
        ("Ali delate na lokaciji naročnika in v tujini?", "Da. Dela izvajamo v naši delavnici ali na lokaciji naročnika, v Sloveniji in v tujini."),
        ("Ali izdelujete tudi serije?", "Izdelujemo posamične kose, manjše serije in serijsko proizvodnjo."),
    ]
    faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq)
    tags = "".join(f"<span>{e(x)}</span>" for x in INDUSTRIES)
    body = f'''
<div class="intro"><div class="wrap intro-grid">
  <div class="intro-copy">
    <span class="label">Industrijsko varjenje in montaža · Slovenija</span>
    <h1>Varjenje, montaža in remonti za industrijske naročnike.</h1>
    <p class="lead">Izdelujemo in montiramo jeklene konstrukcije in cevovode, izvajamo remonte ter kontrolo zvarov. Po tehnični dokumentaciji, v delavnici ali na vaši lokaciji.</p>
    <div class="btn-row"><a class="btn btn-dark" href="{p.link('kontakt')}">Kontaktirajte nas</a>
    <a class="btn btn-line" href="{p.link('storitve')}">Pregled storitev</a></div>
  </div>
  {facts([("Varjenje", "TIG · MIG/MAG · MMA", "ISO 4063: 141 · 131/135 · 111"),
          ("Materiali", "Ogljikovo jeklo, nerjavno jeklo, aluminij", None),
          ("Varilci", "ISO 9606-1", "Certificirana usposobljenost varilcev"),
          ("Postopki", "WPS · WPQR", "Po EN ISO 15609-1 / 15614-1, glede na zahteve projekta"),
          ("Kontrola", "Vizualna kontrola in NDT", "Z dokumentiranimi rezultati"),
          ("Izvedba", "Delavnica in teren", "Slovenija in tujina")], "ARC METAL na kratko")}
</div></div>

<section><div class="wrap">
  {sec_head("Storitve", "Celoten obseg varilskih in montažnih del", "Od pregleda dokumentacije in izdelave do montaže, kontrole in predaje. En izvajalec, ena odgovornost.")}
  {svc_list(p)}
</div></section>

<section class="alt"><div class="wrap">
  {sec_head("Standardi in kakovost", "Certificirani varilci, dokumentirani postopki", "Kakovost zvara se ne preverja šele na koncu. Zagotovijo jo usposobljeni varilci, ustrezen varilni postopek in dokumentirana kontrola.")}
  {std_block()}
</div></section>

<section><div class="wrap">
  {sec_head("Potek dela", "Od zahtev do predaje")}
  {steps(PROCESS)}
</div></section>

<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">Panoge</span><h2>Za koga delamo</h2>
  <p class="muted" style="max-width:52ch">Industrijski naročniki in izvajalci, ki potrebujejo zanesljivega partnerja za varjenje, montažo in vzdrževanje.</p></div>
  <div style="display:grid;gap:28px"><div class="tags">{tags}</div>
  <ul class="checks"><li>Posamični kosi, manjše serije in serijska proizvodnja</li><li>Izvedba v delavnici ali na lokaciji naročnika</li><li>Projekti v Sloveniji in tujini</li></ul></div>
</div></section>

<section><div class="wrap">
  {sec_head("Reference", "Izbrani projekti", None, f'<div><a class="textlink" href="{p.link("projekti")}">Vsi projekti</a></div>')}
  {proj_list(PROJECTS[:3])}
</div></section>

<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">Pogosta vprašanja</span><h2>Vprašanja naročnikov</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>

{cta(p)}'''
    return p, layout(p, None, "ARC METAL: industrijsko varjenje TIG, MIG/MAG in MMA, jeklene konstrukcije, cevovodi, montaža, remonti in NDT. Varilci certificirani po ISO 9606-1.", body, "")


def o_nas():
    p = Page("o-nas")
    body = f'''{page_head(p, [("O nas", None)], "O podjetju", "ARC METAL je slovensko podjetje za industrijsko varjenje in montažo. Gradimo na znanju, stalnem usposabljanju in odgovornem odnosu do naročnikov.")}
<section><div class="wrap cols wide-left">
  <div class="prose">
    <p>Verjamemo, da so znanje, izkušnje in nenehen razvoj temelj kakovostno izvedenih projektov. Že od ustanovitve gradimo podjetje na strokovnem pristopu, odgovornosti in dolgoročnem razmišljanju.</p>
    <p>Poseben poudarek namenjamo stalnemu izobraževanju in usposabljanju zaposlenih, da sledimo razvoju tehnologij, novim varilnim postopkom in sodobnim industrijskim standardom. Sodelujemo z akreditiranimi izobraževalnimi in certifikacijskimi ustanovami, prek katerih pridobivamo nova znanja, usposobljenosti in mednarodno priznane certifikate.</p>
    <p>Vlaganje v ljudi pomeni vlaganje v kakovost našega dela.</p>
  </div>
  {facts([("Podjetje", "ARC METAL, Blaž Bratušek s.p.", None), ("Sedež", "Zgornje Hoče 7, 2311 Hoče", None),
          ("Področje", "Industrijsko varjenje, montaža, remonti, NDT", None), ("Certifikati", "Varilci po ISO 9606-1", None),
          ("Trgi", "Slovenija in tujina", None)])}
</div></section>
<section class="alt"><div class="wrap">
  {sec_head("Standardi in kakovost", "Kako zagotavljamo kakovost zvarov")}
  {std_block()}
</div></section>
<section><div class="wrap">
  {sec_head("Načela", "Kako delamo")}
  <div class="steps">
    <div class="step"><span class="n">01</span><h3>Natančnost</h3><p>Delo po tehnični dokumentaciji, s pozornostjo do detajlov, toleranc in zahtev projekta.</p></div>
    <div class="step"><span class="n">02</span><h3>Zanesljivost</h3><p>Dogovorjeni roki in izvedba, ki čim manj moti proizvodnjo naročnika.</p></div>
    <div class="step"><span class="n">03</span><h3>Varnost</h3><p>Vsa dela izvajamo z zavezanostjo varnosti pri delu in industrijskim predpisom.</p></div>
    <div class="step"><span class="n">04</span><h3>Razvoj</h3><p>Stalno usposabljanje, nova oprema in postopki za vedno zahtevnejše projekte.</p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">Vizija</span><h2>Sodobno industrijsko podjetje, prepoznavno po strokovnosti</h2></div>
  <div class="prose"><p>Naša vizija je razvijati podjetje, ki bo prepoznavno po strokovnosti, kakovosti izvedbe in odgovornem odnosu do naročnikov.</p>
  <p>Z razvojem znanja, opreme in storitev želimo graditi dolgoročna partnerstva ter sodelovati pri vedno zahtevnejših industrijskih projektih v Sloveniji in tujini.</p></div>
</div></section>
{cta(p)}'''
    return p, layout(p, "O nas", "ARC METAL, slovensko podjetje za industrijsko varjenje in montažo. Varilci certificirani po ISO 9606-1.", body, "o-nas")


def storitve():
    p = Page("storitve")
    body = f'''{page_head(p, [("Storitve", None)], "Storitve", "Izdelava, varjenje, montaža, remonti in kontrola kakovosti zvarov. V delavnici ali na lokaciji naročnika.")}
<section><div class="wrap">{svc_list(p)}</div></section>
<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">Splošni podatki</span><h2>Velja za vse storitve</h2>
  <p class="muted" style="max-width:52ch">Pri vsakem projektu se prilagodimo dokumentaciji, obsegu in rokom. Postopek varjenja izberemo glede na material, debelino, položaj zvara in zahteve projekta.</p></div>
  {facts([("Postopki", "TIG · MIG/MAG · MMA", "ISO 4063: 141 · 131/135 · 111"), ("Materiali", "Ogljikovo jeklo, nerjavno jeklo, aluminij", None),
          STD_LINE + (None,), ("Obseg", "Posamični kosi, serije, serijska proizvodnja", None), ("Izvedba", "Delavnica in teren, Slovenija in tujina", None)])}
</div></section>
<section><div class="wrap">{sec_head("Potek dela", "Od zahtev do predaje")}{steps(PROCESS)}</div></section>
{cta(p)}'''
    return p, layout(p, "Storitve", "Jeklene konstrukcije, industrijska montaža, varjenje cevovodov, remonti, prefabrikacija cevovodov in NDT. Certificirani varilci po ISO 9606-1.", body, "storitve")


def service_page(slug):
    d = SVC_PAGES[slug]
    p = Page(slug)
    ov = "".join(f"<p>{e(x)}</p>" for x in d["ov"])
    body = f'''{page_head(p, [("Storitve", "storitve"), (SVC_NAME[slug], None)], d["h1"], d["lead"])}
<section><div class="wrap cols wide-left">
  <div style="display:grid;gap:22px;align-content:start"><h2>{e(d["ov_title"])}</h2><div class="prose">{ov}</div>
  <div class="btn-row" style="margin-top:6px"><a class="btn btn-dark" href="{p.link('kontakt')}">Kontaktirajte nas</a></div></div>
  {facts(SVC_FACTS[slug], "Ključni podatki")}
</div></section>
<section class="alt"><div class="wrap">{sec_head(d["list_label"], d["list_title"])}{steps(d["items"])}</div></section>
<section><div class="wrap">{sec_head("Ostale storitve", "Kaj še izvajamo")}{svc_list(p, exclude=slug)}</div></section>
{cta(p)}'''
    return p, layout(p, d["h1"], d["lead"], body, "storitve")


def projekti():
    p = Page("projekti")
    body = f'''{page_head(p, [("Projekti", None)], "Projekti", "Izbor del s področja varjenja cevovodov, jeklenih konstrukcij, montaže in vzdrževanja industrijske opreme.")}
<section><div class="wrap">{proj_list(PROJECTS)}</div></section>
{cta(p, "Imate podoben projekt?", "Pošljite nam opis ali dokumentacijo in pripravili bomo ponudbo.")}'''
    return p, layout(p, "Projekti", "Reference ARC METAL: varjenje cevovodov, montaža jeklenih konstrukcij, vzdrževanje in popravila industrijske opreme.", body, "projekti")


def kontakt():
    p = Page("kontakt")
    body = f'''{page_head(p, [("Kontakt", None)], "Kontakt", "Za ponudbo nas pokličite ali nam pošljite opis del in tehnično dokumentacijo po e-pošti.")}
<section id="kontakt-podatki"><div class="wrap cols">
  <div class="contact-big">
    <div><span class="label">Telefon</span><a href="{PHONE_HREF}">{PHONE}</a></div>
    <div><span class="label">E-pošta</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
  {facts([("Podjetje", ADDR1, None), ("Naslov", "Zgornje Hoče 7", "2311 Hoče, Slovenija"),
          ("Matična št.", MAT, None), ("ID za DDV", DDV, None)], "Podatki podjetja")}
</div></section>'''
    return p, layout(p, "Kontakt", "Kontakt ARC METAL: +386 70 557 514, info@arcmetal.si, Zgornje Hoče 7, 2311 Hoče.", body, "kontakt")


def legal(slug, title, sections):
    p = Page(slug)
    secs = "".join(f"<section><h2>{e(h)}</h2>{c}</section>" for h, c in sections)
    body = f'''{page_head(p, [(title, None)], title)}
<section><div class="wrap"><div class="legal">{secs}</div></div></section>'''
    return p, layout(p, title, f"{title} spletne strani ARC METAL.", body, "")


COMPANY = f"<p>{e(ADDR1)}, {e(ADDR2)}<br>Matična številka: {MAT} · ID za DDV: {DDV}<br>Telefon: {PHONE} · E-pošta: {EMAIL}</p>"
SVC_PAGES = {
    "storitve-jeklene-konstrukcije": dict(
        h1="Jeklene konstrukcije", eyebrow="Storitev 01",
        lead="Profesionalna izdelava, varjenje in montaža jeklenih konstrukcij po tehnični dokumentaciji.",
        ov_title="Od industrijskih hal do podestov in platform",
        ov=["Izvajamo izdelavo, varjenje in montažo jeklenih konstrukcij po tehnični dokumentaciji in zahtevah posameznega projekta.",
            "Dela izvajamo v delavnici ali na lokaciji naročnika: industrijski objekti, hale, podporni sistemi, platforme in podesti."],
        img=("jeklene-konstrukcije.jpg", "Fotografija: jeklena konstrukcija v delavnici"),
        list_label="Potek izvedbe", list_title="Od načrta do končne montaže",
        items=[("Pregled projekta", "Pregled dokumentacije, zahtev, materialov in pogojev izvedbe."),
               ("Priprava izvedbe", "Priprava materialov, izdelovalne dokumentacije in organizacije dela."),
               ("Izdelava in varjenje", "Izvedba po tehnični dokumentaciji in standardih, s poudarkom na natančnosti in kakovosti."),
               ("Montaža in predaja", "Montaža na lokaciji po potrebi, končni pregled in zaključek projekta.")]),
    "industrijska-montaza": dict(
        h1="Industrijska montaža", eyebrow="Storitev 02",
        lead="Montaža konstrukcij, tehnološke opreme in kovinskih sklopov v proizvodnih in industrijskih obratih.",
        ov_title="Montaža za industrijske in proizvodne obrate",
        ov=["Izvajamo montažo jeklenih konstrukcij, tehnološke opreme, kovinskih sklopov in drugih elementov v proizvodnih in industrijskih obratih: pri novih postavitvah, širitvah proizvodnje in prilagoditvah obstoječih sistemov.",
            "Montaža poteka po tehnični dokumentaciji in zahtevah naročnika, ob upoštevanju predpisanih toleranc, varnostnih zahtev in pogojev projekta."],
        img=("industrijska-montaza.jpg", "Fotografija: ventili in cevovodi v industrijskem obratu"),
        list_label="Obseg storitev", list_title="Področja izvedbe",
        items=[("Proizvodni obrati", "Montaža konstrukcij, nosilcev, podestov, zaščit, kovinskih sklopov in druge opreme."),
               ("Avtomobilska industrija", "Montažna in prilagoditvena dela na proizvodnih linijah, konstrukcijah, tehnoloških sklopih in pomožnih sistemih."),
               ("Procesna industrija", "Montaža cevovodov, nosilnih konstrukcij, tehnoloških sklopov in komponent po projektni dokumentaciji."),
               ("Montaža na terenu", "Montažna dela neposredno pri naročniku, vključno s sestavo, pozicioniranjem in prilagoditvijo sklopov.")]),
    "storitve-varjenje-cevovodov": dict(
        h1="Varjenje cevovodov", eyebrow="Storitev 03",
        lead="Industrijsko varjenje cevovodov za proizvodne, procesne in druge tehnične sisteme.",
        ov_title="TIG varjenje ogljikovih in nerjavnih cevovodov",
        ov=["Izvajamo industrijsko varjenje cevovodov za proizvodne, procesne in druge tehnične sisteme, v delavnici ali na terenu.",
            "Postopek varjenja izberemo glede na material, debelino stene, položaj zvara in zahteve tehnične dokumentacije."],
        img=("varjenje-cevovodov.jpg", "Fotografija: varilec pri varjenju cevi"),
        list_label="Obseg storitev", list_title="Področja izvedbe",
        items=[("Procesni cevovodi", "Varjenje cevovodov za procesne sisteme v proizvodnji, energetiki, živilski, kemični in drugih industrijah."),
               ("Nerjavni in ogljikovi cevovodi", "Varjenje cevovodov iz nerjavnega in ogljikovega jekla, prilagojeno zahtevam projekta in mediju."),
               ("Cevni sklopi in priključki", "Varjenje cevnih sklopov, kolen, T-kosov, prirobnic, reducirk in drugih elementov."),
               ("Terensko varjenje", "Varjenje na lokaciji za nove sisteme, razširitve ali prilagoditve obstoječih cevovodov.")]),
    "remonti-in-popravila": dict(
        h1="Industrijski remonti in popravila", eyebrow="Storitev 04",
        lead="Remontna in popravljalna dela na industrijski opremi, kovinskih sklopih in obstoječih sistemih.",
        ov_title="Hitra in zanesljiva ponovna vzpostavitev delovanja",
        ov=["Izvajamo remontna in popravljalna dela na industrijski opremi, kovinskih sklopih in obstoječih sistemih. Poseg prilagodimo dejanskemu stanju opreme, tehničnim zahtevam in pogojem v proizvodnji.",
            "Dela vključujejo sanacijo poškodb in obrabe, varilska popravila, zamenjavo poškodovanih delov in prilagoditve sklopov."],
        img=("remonti.jpg", "Fotografija: rezervoarji v proizvodnem obratu"),
        list_label="Obseg storitev", list_title="Področja izvedbe",
        items=[("Varilska popravila", "Sanacija razpok, poškodb, obrabljenih zvarov in drugih kritičnih mest na opremi in sklopih."),
               ("Remontna dela", "Načrtovani posegi med remonti in zaustavitvami proizvodnje, z usklajenim časovnim načrtom."),
               ("Sanacije in ojačitve", "Popravila poškodovanih ali obrabljenih elementov ter ojačitve in prilagoditve glede na stanje."),
               ("Intervencijska popravila", "Odprava poškodb in okvar, ki vplivajo na proizvodno opremo ali povzročajo nenačrtovane zastoje.")]),
    "prefabrikacija-cevovodov": dict(
        h1="Prefabrikacija cevovodov", eyebrow="Storitev 05",
        lead="Izdelava cevovodnih sklopov po tehnični dokumentaciji, pripravljenih za montažo na objektu.",
        ov_title="Izdelava cevovodnih sklopov po tehnični dokumentaciji",
        ov=["Izdelujemo industrijske cevovode in cevne sklope po risbah, izometrijah in zahtevah projekta. Cevi pripravimo, razrežemo, sestavimo in zvarimo v sklope, pripravljene za montažo na objektu.",
            "Izdelava v nadzorovanem delavniškem okolju pomeni boljšo kakovost, krajši čas montaže na lokaciji in učinkovitejši potek projekta."],
        img=("prefabrikacija.jpg", "Fotografija: varjenje cevi v delavnici"),
        list_label="Naš postopek", list_title="Potek prefabrikacije",
        items=[("Pregled dokumentacije", "Pregled izometrij, načrtov, specifikacij materiala in zahtev projekta."),
               ("Priprava materiala", "Razrez, priprava robov, označevanje in pozicioniranje cevnih elementov ter fitingov."),
               ("Sestava in varjenje", "Sestavljanje cevnih sklopov in varjenje v skladu s tehnično dokumentacijo."),
               ("Kontrola in priprava za montažo", "Dimenzijski pregled, zahtevani pregledi ter priprava za transport in montažo.")]),
    "nedestruktivno-testiranje-ndt": dict(
        h1="Neporušitvene preiskave (NDT)", eyebrow="Storitev 06",
        lead="Preverjanje kakovosti varjenih spojev in kovinskih komponent brez vpliva na njihovo uporabnost.",
        ov_title="Kontrola kakovosti zvarov skladno z zahtevami projekta",
        ov=["Izvajamo neporušitvene preiskave za preverjanje kakovosti varjenih spojev in drugih kovinskih komponent, brez vpliva na njihovo uporabnost.",
            "Preglede izvajamo glede na zahteve projekta, tehnično dokumentacijo in vrsto materiala."],
        img=("ndt.jpg", "Fotografija: pregled zvara"),
        list_label="Obseg storitev", list_title="Področja izvedbe",
        items=[("Kontrola varjenih spojev", "Preverjanje kakovosti zvarov in odkrivanje površinskih ali drugih napak glede na uporabljeno metodo."),
               ("Kontrola kovinskih komponent", "Pregledi posameznih komponent, sklopov in konstrukcijskih elementov glede na zahteve projekta."),
               ("Kontrole pri remontih", "Pregledi kritičnih mest med remonti, vzdrževalnimi deli in zaustavitvami proizvodnje."),
               ("Dokumentiranje rezultatov", "Priprava zapisov in poročil o pregledih skladno z zahtevami projekta.")]),
}

def zasebnost():
    return legal("pravilnik-o-zasebnosti-2", "Pravilnik o zasebnosti", [
        ("Podatki o podjetju", COMPANY),
        ("Informacije, ki jih zbiramo", "<p>Zbiramo podatke, ki nam jih posredujete sami prek obrazcev ali v komunikaciji z nami (npr. ime, podjetje, e-poštni naslov, telefon, vsebina sporočila), ter tehnične podatke, kot sta IP naslov in podatki o napravi.</p>"),
        ("Kako uporabljamo vaše podatke", "<ul><li>odgovarjanje na poizvedbe in priprava ponudb,</li><li>izvajanje dogovorjenih storitev,</li><li>izboljšave in varnost spletne strani,</li><li>izpolnjevanje zakonskih obveznosti.</li></ul>"),
        ("Pravna podlaga za obdelavo", "<p>Podatke obdelujemo na podlagi vaše privolitve, pogodbe, zakonskih obveznosti ali zakonitih poslovnih interesov, v skladu s Splošno uredbo o varstvu podatkov (GDPR).</p>"),
        ("Hranjenje podatkov", "<p>Osebne podatke hranimo le, dokler je to potrebno za namen, za katerega so bili zbrani, ali kolikor to zahtevajo predpisi.</p>"),
        ("Varnost podatkov", "<p>Uporabljamo ustrezne tehnične in organizacijske ukrepe za zaščito pred zlorabo in nepooblaščenim dostopom. Popolne varnosti prenosa podatkov prek interneta ni mogoče zagotoviti.</p>"),
        ("Piškotki", "<p>Spletna stran lahko uporablja piškotke, potrebne za delovanje in analitiko. Piškotke lahko kadarkoli onemogočite v nastavitvah brskalnika.</p>"),
        ("Storitve tretjih oseb", "<p>Podatke lahko v potrebnem obsegu obdelujejo zunanji ponudniki, ki nam zagotavljajo gostovanje spletne strani, varnost, analitiko in obdelavo kontaktnih obrazcev.</p>"),
        ("Vaše pravice", "<p>Zahtevate lahko dostop do svojih podatkov, njihov popravek ali izbris, omejitev obdelave in prenosljivost podatkov, ter kadarkoli prekličete privolitev. Pritožbo lahko vložite pri Informacijskem pooblaščencu RS.</p>"),
        ("Zunanje povezave", "<p>Ne odgovarjamo za vsebino ali prakse zasebnosti spletnih strani tretjih oseb, na katere vodijo povezave.</p>"),
        ("Spremembe pravilnika", "<p>Pravilnik lahko kadarkoli posodobimo. Spremembe objavimo na tej strani.</p>"),
        ("Kontakt", f"<p>Za vprašanja o zasebnosti nam pišite na {EMAIL} ali pokličite {PHONE}.</p>"),
    ])


def pogoji():
    return legal("pogoji-poslovanja", "Pogoji poslovanja", [
        ("1. Uvod", "<p>Ti pogoji urejajo uporabo spletne strani in storitev podjetja ARC METAL. Z uporabo strani se z njimi strinjate.</p>"),
        ("2. Podatki o podjetju", COMPANY),
        ("3. Namen spletne strani", "<p>Spletna stran informira o industrijskem varjenju, vzdrževanju, popravilih, montaži in sorodnih storitvah. Informacije na strani niso zavezujoča ponudba.</p>"),
        ("4. Ponudba in storitve", "<p>Ponudbe pripravimo glede na posamezen projekt. Dogovor postane veljaven šele po pisni potrditvi obeh strani.</p>"),
        ("5. Intelektualna lastnina", "<p>Vsebina strani pripada podjetju ARC METAL ali imetnikom licenc. Brez pisnega dovoljenja je ni dovoljeno kopirati ali uporabljati.</p>"),
        ("6. Ravnanje uporabnikov", "<p>Prepovedana je uporaba strani za nezakonite namene, nepooblaščen dostop, širjenje zlonamerne vsebine ali motenje njenega delovanja.</p>"),
        ("7. Omejitev odgovornosti", "<p>Ne jamčimo za popolnost in točnost informacij na strani ter v zakonsko dovoljenem obsegu ne odgovarjamo za škodo, nastalo zaradi njene uporabe.</p>"),
        ("8. Povezave do tretjih oseb", "<p>Zunanjih spletnih strani, na katere vodijo povezave, ne nadzorujemo in zanje ne odgovarjamo.</p>"),
        ("9. Zasebnost", "<p>Obdelavo osebnih podatkov ureja Pravilnik o zasebnosti.</p>"),
        ("10. Dostopnost spletne strani", "<p>Delovanje strani lahko kadarkoli spremenimo, omejimo ali ustavimo. Neprekinjenega dostopa ne zagotavljamo.</p>"),
        ("11. Uveljavljivo pravo", "<p>Za pogoje velja pravo Republike Slovenije. Za spore je pristojno stvarno pristojno sodišče v Sloveniji.</p>"),
        ("12. Spremembe pogojev", "<p>Pogoje lahko kadarkoli spremenimo. Spremembe veljajo z objavo na tej strani.</p>"),
        ("13. Kontakt", f"<p>Za vprašanja v zvezi s pogoji nam pišite na {EMAIL} ali pokličite {PHONE}.</p>"),
    ])




def main():
    out = os.path.join(HERE, OUT)
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(out)
    pages = [home(), o_nas(), storitve(), projekti(), kontakt(), zasebnost(), pogoji()]
    pages += [service_page(s) for s, *_ in SERVICES]
    for p, content in pages:
        d = os.path.join(out, p.slug) if p.slug else out
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(content)
    for name in ("style.css", "main.js"):
        shutil.copy(os.path.join(HERE, "src", name), os.path.join(out, name))
    print(f"{len(pages)} strani -> {out}")


if __name__ == "__main__":
    main()
