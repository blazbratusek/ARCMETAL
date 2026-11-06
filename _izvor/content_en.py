"""Angleška vsebina strani ARC METAL. load(g) vrne podatke in funkcije strani, ki zamenjajo slovenske."""


def load(g):
    Page, facts, layout, page_head, sec_head = g["Page"], g["facts"], g["layout"], g["page_head"], g["sec_head"]
    svc_list, std_block, steps, proj_list, cta, legal, e = g["svc_list"], g["std_block"], g["steps"], g["proj_list"], g["cta"], g["legal"], g["e"]
    PHONE, PHONE_HREF, EMAIL, ADDR1, MAT, DDV = g["PHONE"], g["PHONE_HREF"], g["EMAIL"], g["ADDR1"], g["MAT"], g["DDV"]

    SERVICES = [
        ("storitve-jeklene-konstrukcije", "Steel structures",
         "Fabrication, welding and installation of steel structures to technical drawings: halls, support systems, platforms and walkways."),
        ("industrijska-montaza", "Industrial installation",
         "Installation of structures, process equipment, piping and metal assemblies in production plants or on site."),
        ("storitve-varjenje-cevovodov", "Pipe welding",
         "TIG welding of process piping in carbon and stainless steel, in our workshop or on site."),
        ("remonti-in-popravila", "Maintenance and repairs",
         "Planned shutdowns, repairs, reinforcements and emergency repairs of industrial equipment and structures."),
        ("prefabrikacija-cevovodov", "Pipe prefabrication",
         "Workshop fabrication of pipe spools to isometric drawings, ready for installation on site."),
        ("nedestruktivno-testiranje-ndt", "Non-destructive testing (NDT)",
         "Quality inspection of welded joints and components, with results documented as required by the project."),
    ]
    SVC_NAME = {s[0]: s[1] for s in SERVICES}

    STANDARDS = [
        ("ISO 9606-1", "Qualification testing of welders – fusion welding of steels",
         "Our welders are certified to EN ISO 9606-1 for the processes, positions and material groups they use in their work."),
        ("WPS · WPQR", "EN ISO 15609-1 · EN ISO 15614-1",
         "We prepare welding procedure specifications (WPS) for every project. Where a qualified procedure is required, we carry out procedure qualification (WPQR) to EN ISO 15614-1."),
        ("Inspection and documentation", "Visual inspection · NDT · reports",
         "Welds are inspected during fabrication and before handover. The type of non-destructive testing and the scope of documentation follow the project requirements."),
    ]

    PROJECTS = [
        ("Industrial pipe welding", "Piping",
         "Precision pipe welding for industrial systems, with a focus on durability, alignment and technical requirements."),
        ("Steel structure installation", "Structures",
         "Installation and welding of steel structures in accordance with project specifications."),
        ("Industrial maintenance and repairs", "Maintenance",
         "Repairs and reinforcement work to restore damaged components and keep equipment in operation."),
        ("On-site welding support", "On site",
         "Welding services directly at industrial sites, with fast response and minimal production downtime."),
        ("Installation of metal structures and components", "Installation",
         "Installation of metal structures and components in line with technical requirements and site conditions."),
        ("Industrial equipment repair", "Repairs",
         "Repair and refurbishment of industrial equipment and components to maintain performance, safety and efficiency."),
    ]

    INDUSTRIES = ["Manufacturing", "Automotive", "Energy", "Process industry", "Food industry", "Chemical industry", "Construction"]

    STD_LINE = ("Standards", "Welders to ISO 9606-1 · WPS/WPQR as required by the project")

    SVC_FACTS = {
        "storitve-jeklene-konstrukcije": [
            ("Processes", "MIG/MAG · MMA", "ISO 4063: 135 · 111"),
            ("Material", "Carbon (structural) steel", None),
            ("Scope", "Halls, support systems, platforms, walkways", None),
            ("Execution", "Workshop fabrication and on-site installation", None),
            STD_LINE + (None,)],
        "industrijska-montaza": [
            ("Scope", "Structures, process equipment, piping, metal assemblies", None),
            ("Industries", "Manufacturing, automotive and process industry", None),
            ("Execution", "Workshop and on site", None),
            ("Requirements", "To technical documentation, tolerances and safety requirements", None),
            STD_LINE + (None,)],
        "storitve-varjenje-cevovodov": [
            ("Process", "TIG", "ISO 4063: 141"),
            ("Material", "Carbon and stainless steel", None),
            ("Components", "Pipes, elbows, tees, flanges, reducers", None),
            ("Execution", "Workshop and on site", None),
            STD_LINE + (None,)],
        "remonti-in-popravila": [
            ("Type of work", "Planned shutdowns and emergency repairs", None),
            ("Scope", "Weld repairs, refurbishment, reinforcement, part replacement", None),
            ("Execution", "On site, coordinated with production shutdowns", None),
            STD_LINE + (None,)],
        "prefabrikacija-cevovodov": [
            ("Basis", "Isometrics, drawings and material specifications", None),
            ("Process", "TIG", "ISO 4063: 141"),
            ("Material", "Carbon and stainless steel", None),
            ("Inspection", "Dimensional check and required testing before dispatch", None),
            STD_LINE + (None,)],
        "nedestruktivno-testiranje-ndt": [
            ("Object", "Welded joints, components, structural elements", None),
            ("Method", "According to project requirements and material", None),
            ("Execution", "During fabrication, installation and shutdowns", None),
            ("Result", "Inspection records and reports", None)],
    }

    SVC_PAGES = {
        "storitve-jeklene-konstrukcije": dict(
            h1="Steel structures",
            lead="Fabrication, welding and installation of steel structures to technical documentation.",
            ov_title="From industrial halls to platforms and walkways",
            ov=["We fabricate, weld and install steel structures according to technical documentation and the requirements of each project.",
                "Work is carried out in our workshop or at the client's site: industrial buildings, halls, support systems, platforms and walkways."],
            list_label="Project flow", list_title="From drawing to final installation",
            items=[("Project review", "Review of documentation, requirements, materials and site conditions."),
                   ("Preparation", "Preparation of materials, shop drawings and work organisation."),
                   ("Fabrication and welding", "Execution to technical documentation and standards, with a focus on accuracy and quality."),
                   ("Installation and handover", "On-site installation where required, final inspection and project close-out.")]),
        "industrijska-montaza": dict(
            h1="Industrial installation",
            lead="Installation of structures, process equipment and metal assemblies in production and industrial plants.",
            ov_title="Installation for industrial and production plants",
            ov=["We install steel structures, process equipment, metal assemblies and other components in production and industrial plants: for new lines, production expansions and modifications of existing systems.",
                "Installation follows the technical documentation and client requirements, with the specified tolerances, safety requirements and project conditions."],
            list_label="Scope of services", list_title="Areas of work",
            items=[("Production plants", "Installation of structures, supports, platforms, guards, metal assemblies and other equipment."),
                   ("Automotive industry", "Installation and modification work on production lines, structures, process assemblies and auxiliary systems."),
                   ("Process industry", "Installation of piping, support structures, process assemblies and components to project documentation."),
                   ("On-site installation", "Installation work directly at the client's site, including assembly, positioning and adjustment.")]),
        "storitve-varjenje-cevovodov": dict(
            h1="Pipe welding",
            lead="Industrial pipe welding for production, process and other technical systems.",
            ov_title="TIG welding of carbon and stainless steel piping",
            ov=["We weld industrial piping for production, process and other technical systems, in our workshop or on site.",
                "The welding process is selected according to the material, wall thickness, weld position and the requirements of the technical documentation."],
            list_label="Scope of services", list_title="Areas of work",
            items=[("Process piping", "Pipe welding for process systems in manufacturing, energy, food, chemical and other industries."),
                   ("Stainless and carbon steel piping", "Welding of stainless and carbon steel piping, matched to project requirements and the medium."),
                   ("Pipe spools and fittings", "Welding of pipe spools, elbows, tees, flanges, reducers and other components."),
                   ("Field welding", "On-site welding for new systems, extensions or modifications of existing piping.")]),
        "remonti-in-popravila": dict(
            h1="Industrial maintenance and repairs",
            lead="Shutdown and repair work on industrial equipment, metal assemblies and existing systems.",
            ov_title="Fast and reliable return to operation",
            ov=["We carry out shutdown and repair work on industrial equipment, metal assemblies and existing systems. Each intervention is adapted to the actual condition of the equipment, the technical requirements and production conditions.",
                "Work includes repair of damage and wear, weld repairs, replacement of damaged parts and modification of assemblies."],
            list_label="Scope of services", list_title="Areas of work",
            items=[("Weld repairs", "Repair of cracks, damage, worn welds and other critical areas on equipment and assemblies."),
                   ("Shutdown work", "Planned interventions during shutdowns and production stops, on a coordinated schedule."),
                   ("Refurbishment and reinforcement", "Repair of damaged or worn elements, with reinforcement and modification as required."),
                   ("Emergency repairs", "Repair of damage and failures that affect production equipment or cause unplanned downtime.")]),
        "prefabrikacija-cevovodov": dict(
            h1="Pipe prefabrication",
            lead="Fabrication of pipe spools to technical documentation, ready for installation on site.",
            ov_title="Pipe spool fabrication to technical documentation",
            ov=["We fabricate industrial piping and pipe spools to drawings, isometrics and project requirements. Pipes are prepared, cut, fitted and welded into spools ready for installation on site.",
                "Fabrication in a controlled workshop environment means better quality, shorter installation time on site and a more efficient project."],
            list_label="Our process", list_title="Prefabrication workflow",
            items=[("Documentation review", "Review of isometrics, drawings, material specifications and project requirements."),
                   ("Material preparation", "Cutting, edge preparation, marking and positioning of pipe components and fittings."),
                   ("Fit-up and welding", "Fit-up of pipe spools and welding in accordance with the technical documentation."),
                   ("Inspection and dispatch", "Dimensional check, required inspections and preparation for transport and installation.")]),
        "nedestruktivno-testiranje-ndt": dict(
            h1="Non-destructive testing (NDT)",
            lead="Quality inspection of welded joints and metal components without affecting their usability.",
            ov_title="Weld quality inspection to project requirements",
            ov=["We carry out non-destructive testing to verify the quality of welded joints and other metal components, without affecting their usability.",
                "Inspections are performed according to project requirements, technical documentation and material type."],
            list_label="Scope of services", list_title="Areas of work",
            items=[("Weld inspection", "Verification of weld quality and detection of surface or other defects, depending on the method used."),
                   ("Component inspection", "Inspection of individual components, assemblies and structural elements to project requirements."),
                   ("Shutdown inspections", "Inspection of critical areas during shutdowns, maintenance work and production stops."),
                   ("Reporting", "Inspection records and reports in accordance with project requirements.")]),
    }

    PROCESS = [("Requirements review", "Review of documentation, materials, required standards and execution conditions."),
               ("Preparation", "Selection of the welding process and WPS, material preparation and work organisation."),
               ("Execution", "Welding and installation to technical documentation, in the workshop or on site."),
               ("Inspection and handover", "Visual and, where required, non-destructive testing, documentation and handover.")]

    COMPANY = f"<p>{e(ADDR1)}, Zgornje Hoče 7, 2311 Hoče, Slovenia<br>Reg. No.: {MAT} · VAT ID: {DDV}<br>Phone: {PHONE} · E-mail: {EMAIL}</p>"

    def home():
        p = Page("")
        faq = [
            ("Are your welders certified?", "Yes, our welders are certified to EN ISO 9606-1. We prepare a welding procedure specification (WPS) for every project and carry out procedure qualification (WPQR to EN ISO 15614-1) when the project requires it."),
            ("Which materials do you weld?", "Carbon steel, stainless steel and aluminium. The process is selected according to the material, wall thickness, weld position and documentation requirements."),
            ("Do you offer non-destructive testing?", "Yes. The type of inspection is defined by the project requirements, and results are documented in reports."),
            ("Do you work on site and abroad?", "Yes. We work in our own workshop or at the client's site, in Slovenia and abroad."),
            ("Do you also produce series?", "We produce single pieces, small batches and series production."),
        ]
        faq_html = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in faq)
        tags = "".join(f"<span>{e(x)}</span>" for x in INDUSTRIES)
        body = f'''
<div class="intro"><div class="wrap intro-grid">
  <div class="intro-copy">
    <span class="label">Industrial welding and installation · Slovenia</span>
    <h1>Welding, installation and maintenance for industrial clients.</h1>
    <p class="lead">We fabricate and install steel structures and piping, carry out maintenance shutdowns and weld inspection. To technical documentation, in our workshop or at your site.</p>
    <div class="btn-row"><a class="btn btn-dark" href="{p.link('kontakt')}">Contact us</a>
    <a class="btn btn-line" href="{p.link('storitve')}">Our services</a></div>
  </div>
  {facts([("Welding", "TIG · MIG/MAG · MMA", "ISO 4063: 141 · 131/135 · 111"),
          ("Materials", "Carbon steel, stainless steel, aluminium", None),
          ("Welders", "ISO 9606-1", "Certified welder qualification"),
          ("Procedures", "WPS · WPQR", "To EN ISO 15609-1 / 15614-1, as required by the project"),
          ("Inspection", "Visual inspection and NDT", "With documented results"),
          ("Execution", "Workshop and on site", "Slovenia and abroad")], "ARC METAL at a glance")}
</div></div>

<section><div class="wrap">
  {sec_head("Services", "The full scope of welding and installation work", "From documentation review and fabrication to installation, inspection and handover. One contractor, one point of responsibility.")}
  {svc_list(p)}
</div></section>

<section class="alt"><div class="wrap">
  {sec_head("Standards and quality", "Certified welders, documented procedures", "Weld quality is not only checked at the end. It is ensured by qualified welders, the right welding procedure and documented inspection.")}
  {std_block()}
</div></section>

<section><div class="wrap">
  {sec_head("How we work", "From requirements to handover")}
  {steps(PROCESS)}
</div></section>

<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">Industries</span><h2>Who we work for</h2>
  <p class="muted" style="max-width:52ch">Industrial clients and contractors who need a reliable partner for welding, installation and maintenance.</p></div>
  <div style="display:grid;gap:28px"><div class="tags">{tags}</div>
  <ul class="checks"><li>Single pieces, small batches and series production</li><li>Work in our workshop or at the client's site</li><li>Projects in Slovenia and abroad</li></ul></div>
</div></section>

<section><div class="wrap">
  {sec_head("References", "Selected projects", None, f'<div><a class="textlink" href="{p.link("projekti")}">All projects</a></div>')}
  {proj_list(PROJECTS[:3])}
</div></section>

<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">FAQ</span><h2>Questions from clients</h2></div>
  <div class="faq">{faq_html}</div>
</div></section>

{cta(p)}'''
        return p, layout(p, None, "ARC METAL: industrial TIG, MIG/MAG and MMA welding, steel structures, piping, installation, maintenance and NDT. Welders certified to ISO 9606-1.", body, "")

    def o_nas():
        p = Page("o-nas")
        body = f'''{page_head(p, [("About", None)], "About the company", "ARC METAL is a Slovenian company for industrial welding and installation. We build on expertise, continuous training and a responsible attitude towards our clients.")}
<section><div class="wrap cols wide-left">
  <div class="prose">
    <p>We believe that knowledge, experience and continuous development are the foundation of well-executed projects. Since the company was founded, we have built it on a professional approach, responsibility and long-term thinking.</p>
    <p>We place particular emphasis on continuous education and training of our staff, so that we keep up with new technologies, welding processes and modern industrial standards. We work with accredited training and certification bodies, through which we gain new knowledge, qualifications and internationally recognised certificates.</p>
    <p>Investing in people means investing in the quality of our work.</p>
  </div>
  {facts([("Company", "ARC METAL, Blaž Bratušek s.p.", None), ("Location", "Zgornje Hoče 7, 2311 Hoče, Slovenia", None),
          ("Field", "Industrial welding, installation, maintenance, NDT", None), ("Certification", "Welders to ISO 9606-1", None),
          ("Markets", "Slovenia and abroad", None)])}
</div></section>
<section class="alt"><div class="wrap">
  {sec_head("Standards and quality", "How we ensure weld quality")}
  {std_block()}
</div></section>
<section><div class="wrap">
  {sec_head("Principles", "How we work")}
  <div class="steps">
    <div class="step"><span class="n">01</span><h3>Precision</h3><p>Work to technical documentation, with attention to detail, tolerances and project requirements.</p></div>
    <div class="step"><span class="n">02</span><h3>Reliability</h3><p>Agreed deadlines and execution that disrupts the client's production as little as possible.</p></div>
    <div class="step"><span class="n">03</span><h3>Safety</h3><p>All work is carried out with a commitment to occupational safety and industrial regulations.</p></div>
    <div class="step"><span class="n">04</span><h3>Development</h3><p>Continuous training, new equipment and processes for increasingly demanding projects.</p></div>
  </div>
</div></section>
<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">Vision</span><h2>A modern industrial company, recognised for its expertise</h2></div>
  <div class="prose"><p>Our vision is to develop a company recognised for its expertise, quality of execution and responsible attitude towards clients.</p>
  <p>By developing our knowledge, equipment and services, we aim to build long-term partnerships and take part in increasingly demanding industrial projects in Slovenia and abroad.</p></div>
</div></section>
{cta(p)}'''
        return p, layout(p, "About", "ARC METAL, a Slovenian company for industrial welding and installation. Welders certified to ISO 9606-1.", body, "o-nas")

    def storitve():
        p = Page("storitve")
        body = f'''{page_head(p, [("Services", None)], "Services", "Fabrication, welding, installation, maintenance and weld quality inspection. In our workshop or at the client's site.")}
<section><div class="wrap">{svc_list(p)}</div></section>
<section class="alt"><div class="wrap cols">
  <div style="display:grid;gap:18px;align-content:start"><span class="label">General information</span><h2>Applies to all services</h2>
  <p class="muted" style="max-width:52ch">For every project we adapt to the documentation, scope and schedule. The welding process is selected according to the material, thickness, weld position and project requirements.</p></div>
  {facts([("Processes", "TIG · MIG/MAG · MMA", "ISO 4063: 141 · 131/135 · 111"), ("Materials", "Carbon steel, stainless steel, aluminium", None),
          STD_LINE + (None,), ("Scope", "Single pieces, batches, series production", None), ("Execution", "Workshop and on site, Slovenia and abroad", None)])}
</div></section>
<section><div class="wrap">{sec_head("How we work", "From requirements to handover")}{steps(PROCESS)}</div></section>
{cta(p)}'''
        return p, layout(p, "Services", "Steel structures, industrial installation, pipe welding, maintenance, pipe prefabrication and NDT. Welders certified to ISO 9606-1.", body, "storitve")

    def projekti():
        p = Page("projekti")
        body = f'''{page_head(p, [("Projects", None)], "Projects", "A selection of work in pipe welding, steel structures, installation and maintenance of industrial equipment.")}
<section><div class="wrap">{proj_list(PROJECTS)}</div></section>
{cta(p, "Have a similar project?", "Send us a description or drawings and we will prepare a quotation.")}'''
        return p, layout(p, "Projects", "ARC METAL references: pipe welding, steel structure installation, maintenance and repair of industrial equipment.", body, "projekti")

    def kontakt():
        p = Page("kontakt")
        body = f'''{page_head(p, [("Contact", None)], "Contact", "For a quotation, call us or send a description of the work and technical documentation by e-mail.")}
<section id="contact-details"><div class="wrap cols">
  <div class="contact-big">
    <div><span class="label">Phone</span><a href="{PHONE_HREF}">{PHONE}</a></div>
    <div><span class="label">E-mail</span><a href="mailto:{EMAIL}">{EMAIL}</a></div>
  </div>
  {facts([("Company", ADDR1, None), ("Address", "Zgornje Hoče 7", "2311 Hoče, Slovenia"),
          ("Reg. No.", MAT, None), ("VAT ID", DDV, None)], "Company details")}
</div></section>'''
        return p, layout(p, "Contact", "Contact ARC METAL: +386 70 557 514, info@arcmetal.si, Zgornje Hoče 7, 2311 Hoče, Slovenia.", body, "kontakt")

    def zasebnost():
        return legal("pravilnik-o-zasebnosti-2", "Privacy policy", [
            ("Company details", COMPANY),
            ("Information we collect", "<p>We collect data that you provide yourself through forms or in communication with us (e.g. name, company, e-mail address, phone number, message content), and technical data such as IP address and device information.</p>"),
            ("How we use your data", "<ul><li>responding to enquiries and preparing quotations,</li><li>performing agreed services,</li><li>improving and securing the website,</li><li>meeting legal obligations.</li></ul>"),
            ("Legal basis for processing", "<p>We process data on the basis of your consent, a contract, legal obligations or legitimate business interests, in accordance with the General Data Protection Regulation (GDPR).</p>"),
            ("Data retention", "<p>Personal data is kept only as long as necessary for the purpose for which it was collected, or as required by law.</p>"),
            ("Data security", "<p>We use appropriate technical and organisational measures to protect data against misuse and unauthorised access. Complete security of data transmission over the internet cannot be guaranteed.</p>"),
            ("Cookies", "<p>The website may use cookies required for operation and analytics. You can disable cookies at any time in your browser settings.</p>"),
            ("Third-party services", "<p>Data may be processed, to the extent necessary, by external providers that supply website hosting, security, analytics and contact form processing.</p>"),
            ("Your rights", "<p>You may request access to your data, its correction or deletion, restriction of processing and data portability, and you may withdraw your consent at any time. You may lodge a complaint with the Information Commissioner of the Republic of Slovenia.</p>"),
            ("External links", "<p>We are not responsible for the content or privacy practices of third-party websites linked from this site.</p>"),
            ("Changes to this policy", "<p>We may update this policy at any time. Changes are published on this page.</p>"),
            ("Contact", f"<p>For privacy questions, write to {EMAIL} or call {PHONE}.</p>"),
        ])

    def pogoji():
        return legal("pogoji-poslovanja", "Terms of business", [
            ("1. Introduction", "<p>These terms govern the use of the website and services of ARC METAL. By using the website you agree to them.</p>"),
            ("2. Company details", COMPANY),
            ("3. Purpose of the website", "<p>The website provides information about industrial welding, maintenance, repairs, installation and related services. Information on the website does not constitute a binding offer.</p>"),
            ("4. Quotations and services", "<p>Quotations are prepared for each individual project. An agreement becomes valid only after written confirmation by both parties.</p>"),
            ("5. Intellectual property", "<p>The content of the website belongs to ARC METAL or its licensors and may not be copied or used without written permission.</p>"),
            ("6. User conduct", "<p>Using the website for unlawful purposes, unauthorised access, distributing malicious content or disrupting its operation is prohibited.</p>"),
            ("7. Limitation of liability", "<p>We do not guarantee the completeness and accuracy of information on the website and, to the extent permitted by law, are not liable for damage arising from its use.</p>"),
            ("8. Third-party links", "<p>We do not control external websites linked from this site and are not responsible for them.</p>"),
            ("9. Privacy", "<p>The processing of personal data is governed by the Privacy policy.</p>"),
            ("10. Website availability", "<p>We may change, restrict or discontinue the website at any time. Uninterrupted access is not guaranteed.</p>"),
            ("11. Governing law", "<p>These terms are governed by the law of the Republic of Slovenia. Disputes fall under the jurisdiction of the competent court in Slovenia.</p>"),
            ("12. Changes to these terms", "<p>We may change these terms at any time. Changes take effect when published on this page.</p>"),
            ("13. Contact", f"<p>For questions about these terms, write to {EMAIL} or call {PHONE}.</p>"),
        ])

    return dict(SERVICES=SERVICES, SVC_NAME=SVC_NAME, STANDARDS=STANDARDS, PROJECTS=PROJECTS, INDUSTRIES=INDUSTRIES,
                STD_LINE=STD_LINE, SVC_FACTS=SVC_FACTS, SVC_PAGES=SVC_PAGES, PROCESS=PROCESS, COMPANY=COMPANY,
                home=home, o_nas=o_nas, storitve=storitve, projekti=projekti, kontakt=kontakt, zasebnost=zasebnost, pogoji=pogoji)
