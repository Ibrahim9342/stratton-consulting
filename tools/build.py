"""Generates the static HTML pages. Run: python3 tools/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

BRAND = "Scalehaven"
LEGAL = "Scalehaven Operations LLC"
STREET = "30 N. Gould St., #69980"
CITY = "Sheridan, WY 82801"
COUNTRY = "United States"
EMAIL = "info@scalehaven-consulting.com"
PHONE = "+1 (917) 814-3761"
PHONE_TEL = "+19178143761"
DOMAIN = "scalehaven-consulting.com"
OWNER = "Ibrahim Khaleel Mirza"
OWNER_TITLE = "Founder &amp; Managing Partner"
EFFECTIVE = "October 17, 2026"
URL = f"https://www.{DOMAIN}"

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>'
CHECK = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 8.5l3.2 3L13 4.5"/></svg>'


def mark(dark=False):
    bg = 'fill="#102031" stroke="#26405c"' if dark else 'fill="#0b1622"'
    return (
        '<svg class="brand-mark" viewBox="0 0 36 36" aria-hidden="true">'
        f'<rect x="0.5" y="0.5" width="35" height="35" rx="4" {bg}/>'
        '<path d="M9.5 27V16.5a8.5 8.5 0 0 1 17 0V27" fill="none" stroke="#cfab6e" stroke-width="2.2"/>'
        '<rect x="13.5" y="20" width="3.2" height="7" fill="#ffffff"/>'
        '<rect x="19.3" y="15.5" width="3.2" height="11.5" fill="#ffffff"/>'
        "</svg>"
    )


def brand(dark=False):
    return (
        f'<a class="brand" href="/" aria-label="{BRAND} Consulting – Home">{mark(dark)}'
        f'<span class="brand-name">{BRAND}<small>Consulting</small></span></a>'
    )


NAV = [("services", "Services"), ("approach", "Approach"), ("about", "About")]


def header(active):
    current = ' aria-current="page"'
    items = "\n".join(
        f'        <li><a href="/{slug}"{current if slug == active else ""}>{label}</a></li>'
        for slug, label in NAV
    )
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    {brand()}
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu"><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul class="nav-list">
{items}
        <li><a href="/#faq">FAQ</a></li>
      </ul>
      <a class="btn btn-primary btn-sm" href="/contact">Book a consultation</a>
    </nav>
  </div>
</header>"""


FOOTER = f"""<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-about">
        {brand(dark=True)}
        <p>Independent strategy and management consulting for growing and mid-sized companies.</p>
        <p>{BRAND} Consulting is a trade name of {LEGAL}, a Wyoming limited liability company.</p>
      </div>
      <div>
        <h2>Services</h2>
        <ul>
          <li><a href="/services#strategy">Growth Strategy</a></li>
          <li><a href="/services#operations">Operating Model</a></li>
          <li><a href="/services#digital">Digital &amp; AI</a></li>
          <li><a href="/services#transformation">Transformation</a></li>
          <li><a href="/services#transactions">Transactions</a></li>
          <li><a href="/services#expansion">Market Expansion</a></li>
        </ul>
      </div>
      <div>
        <h2>Firm</h2>
        <ul>
          <li><a href="/about">About</a></li>
          <li><a href="/approach">Approach</a></li>
          <li><a href="/#sectors">Sectors</a></li>
          <li><a href="/#faq">FAQ</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h2>Contact</h2>
        <address>
          {LEGAL}<br>
          {STREET}<br>
          {CITY}<br>
          <a href="mailto:{EMAIL}">{EMAIL}</a><br>
          <a href="tel:{PHONE_TEL}">{PHONE}</a>
        </address>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span data-year>2026</span> {LEGAL}. All rights reserved.</p>
      <ul class="footer-legal">
        <li><a href="/privacy">Privacy Policy</a></li>
        <li><a href="/terms">Terms of Use</a></li>
        <li><a href="/legal-notice">Legal Notice</a></li>
      </ul>
    </div>
  </div>
</footer>"""


def page(slug, title, description, body, active=None, noindex=False, extra_head=""):
    path = "/" if slug == "index" else f"/{slug}"
    full_title = title if slug == "index" else f"{title} | {BRAND} Consulting"
    meta = (
        '  <meta name="robots" content="noindex">'
        if noindex
        else f"""  <link rel="canonical" href="{URL}{path}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{BRAND} Consulting">
  <meta property="og:title" content="{full_title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{URL}{path}">
  <meta property="og:image" content="{URL}/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">"""
    )
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full_title}</title>
  <meta name="description" content="{description}">
{meta}
  <meta name="theme-color" content="#0b1622">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/newsreader.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/styles.css">{extra_head}
  <script src="/assets/js/main.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

{header(active)}

<main id="main">
{body}
</main>

{FOOTER}
</body>
</html>
"""


def page_hero(crumb, eyebrow, title, lead):
    return f"""  <section class="page-hero">
    <div class="wrap">
      <div class="page-hero-inner">
        <ol class="crumbs" aria-label="Breadcrumb"><li><a href="/">Home</a></li><li aria-current="page">{crumb}</li></ol>
        <p class="eyebrow">{eyebrow}</p>
        <h1 class="h1">{title}</h1>
        <p class="lead">{lead}</p>
      </div>
    </div>
  </section>"""


def cta(title="Ready to talk about your next big decision?",
        text="Book a free, no-obligation consultation. We will listen, ask the right questions and tell you honestly whether&nbsp;&mdash; and how&nbsp;&mdash; we can help."):
    return f"""  <section class="cta" aria-labelledby="cta-title">
    <div class="wrap cta-inner reveal">
      <div>
        <h2 class="h2" id="cta-title">{title}</h2>
        <p>{text}</p>
      </div>
      <div class="cta-actions">
        <a class="btn btn-brass" href="/contact">Schedule a consultation {ARROW}</a>
        <a class="btn btn-ghost-light" href="mailto:{EMAIL}">Email us</a>
      </div>
    </div>
  </section>"""


SERVICES = [
    {
        "id": "strategy", "nav": "Growth Strategy", "title": "Corporate &amp; Growth Strategy",
        "short": "Define where to play and how to win, grounded in market evidence and a realistic view of your capabilities.",
        "intro": "Growth rarely fails for lack of ideas. It fails because priorities are unclear and resources are spread too thin. We help leadership teams make explicit choices about markets, customers and offerings&nbsp;&mdash; and back them with evidence.",
        "questions": ["Which markets and segments offer the most attractive growth?", "Where are we winning today, and why?", "What should we stop doing to fund what matters?"],
        "deliver": ["Market, customer and competitor analysis", "Assessment of growth options and portfolio priorities", "Multi-year strategic plan with financial targets", "Board and investor-ready strategy narrative"],
        "outcomes": ["A clear, shared set of strategic priorities", "Resource allocation aligned to growth", "Leadership alignment on targets and trade-offs"],
    },
    {
        "id": "operations", "nav": "Operating Model", "title": "Operating Model &amp; Performance",
        "short": "Align structure, processes and metrics so your organization can actually deliver the strategy.",
        "intro": "As companies grow, the structures that once worked start to slow them down. We redesign how decisions are made, how work flows and how performance is managed&nbsp;&mdash; so the organization can scale without losing speed.",
        "questions": ["Is our organization structured for the next stage of growth?", "Where are we losing margin, and why?", "Do our KPIs actually drive the right behavior?"],
        "deliver": ["Organization and governance design", "Cost and margin improvement programs", "Process redesign for core workflows", "KPI framework and management cadence"],
        "outcomes": ["Clear accountabilities and faster decisions", "Sustainable cost and margin improvement", "Transparent, comparable performance data"],
    },
    {
        "id": "digital", "nav": "Digital &amp; AI", "title": "Digital &amp; AI Strategy",
        "short": "Translate technology and AI opportunities into a prioritized roadmap with clear business cases.",
        "intro": "Most companies do not lack digital initiatives&nbsp;&mdash; they lack focus. We assess where technology and AI create real value in your business, separate signal from hype, and build a vendor-neutral roadmap you can execute.",
        "questions": ["Where can AI and automation create measurable value for us?", "Which digital initiatives should we prioritize or stop?", "Do we have the data, skills and partners we need?"],
        "deliver": ["Digital maturity and capability assessment", "AI and automation use-case portfolio with business cases", "Vendor-neutral technology roadmap", "Governance for data, AI and technology investments"],
        "outcomes": ["A focused portfolio of high-value initiatives", "Clear business cases and ownership", "Lower risk in technology spending"],
    },
    {
        "id": "transformation", "nav": "Transformation", "title": "Transformation Management",
        "short": "Run complex change programs with the governance, pace and discipline they need to land.",
        "intro": "Strategies fail in execution. We set up and run transformation programs with clear governance, realistic plans and relentless follow-through&nbsp;&mdash; while bringing your people along.",
        "questions": ["How do we turn the strategy into a program that delivers?", "Why are our current initiatives stalling?", "How do we keep the organization engaged through change?"],
        "deliver": ["Program design, governance and PMO", "Detailed implementation plans and milestones", "Change management and communication", "Benefit tracking against the business case"],
        "outcomes": ["Initiatives delivered on time and on budget", "Transparency on progress and risks", "An organization that owns the change"],
    },
    {
        "id": "transactions", "nav": "Transactions", "title": "Transactions &amp; Integration",
        "short": "Support for buy-side and sell-side decisions, from commercial due diligence to post-merger integration.",
        "intro": "Deals create value only when the investment thesis holds and the integration is executed well. We support investors, owners and management teams from the first screening to the first hundred days and beyond.",
        "questions": ["Is the market and business plan behind this deal credible?", "Where will the value come from, and how fast?", "How do we integrate without disrupting the business?"],
        "deliver": ["Commercial due diligence", "Value creation and synergy plans", "100-day and integration planning", "Exit readiness and equity story support"],
        "outcomes": ["Better-informed investment decisions", "Faster, more reliable value capture", "Smoother integrations with less disruption"],
    },
    {
        "id": "expansion", "nav": "Market Expansion", "title": "Market Entry &amp; Expansion",
        "short": "Plan and de-risk entry into new markets, customer segments or channels&nbsp;&mdash; in the U.S. and abroad.",
        "intro": "Entering a new market is one of the highest-stakes decisions a company makes. We help you choose the right markets, design the go-to-market model and plan the launch so you can expand with confidence.",
        "questions": ["Which markets should we enter first, and how?", "What will it take to win against local competitors?", "Should we build, partner or acquire?"],
        "deliver": ["Market sizing, attractiveness and prioritization", "Go-to-market and channel strategy", "Partner, location and entry-mode assessment", "Launch plan and business case"],
        "outcomes": ["A clear, prioritized expansion roadmap", "Reduced risk and faster time to revenue", "Confidence for leadership and investors"],
    },
]

SECTORS = [
    ('<rect x="3" y="4" width="18" height="12" rx="1"/><path d="M8 20h8M12 16v4"/>', "Technology &amp; Software", "SaaS, IT services and tech-enabled businesses scaling into new segments."),
    ('<path d="M3 9l9-5 9 5M5 9v9M10 9v9M14 9v9M19 9v9M3 20h18"/>', "Financial Services", "Banks, insurers, fintechs and asset managers navigating regulatory and digital change."),
    ('<path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>', "Healthcare &amp; Life Sciences", "Providers, practices and suppliers improving access, quality and margins."),
    ('<path d="M3 21V10l6 4v-4l6 4V6l6 3v12z"/>', "Industrial &amp; Manufacturing", "Manufacturers and distributors modernizing operations and supply chains."),
    ('<path d="M5 8h14l-1 13H6zM9 8V6a3 3 0 0 1 6 0v2"/>', "Consumer &amp; Retail", "Brands and retailers rethinking channels, pricing and customer experience."),
    ('<rect x="3" y="7" width="18" height="13" rx="1"/><path d="M9 7V4h6v3M3 12h18"/>', "Private Equity &amp; Owners", "Investors and family owners who need diligence, value creation and exit readiness."),
]

STEPS = [
    ("Diagnose", "We interview leadership, analyze the data and pressure-test assumptions to build a fact base everyone trusts.", "Weeks 1&ndash;3"),
    ("Design", "Together we develop options, quantify trade-offs and agree on a clear direction with an actionable roadmap.", "Weeks 3&ndash;6"),
    ("Deliver", "We work alongside your team to implement&nbsp;&mdash; setting up governance, removing blockers and keeping momentum.", "Months 2&ndash;6+"),
    ("Scale", "We measure results against the business case and transfer tools and know-how so improvements last and grow.", "Ongoing"),
]

FAQ = [
    ("What kind of companies do you work with?", "We focus on growing and mid-sized companies&nbsp;&mdash; typically privately held, family-owned or investor-backed businesses, as well as business units of larger corporations. If your situation is different, we are still happy to talk."),
    ("How does an engagement start?", "With a free, no-obligation consultation of 30&ndash;45 minutes. If there is a fit, we send a written proposal with scope, deliverables, timeline and fees, usually within a few business days."),
    ("How are your fees structured?", "Most projects are quoted as a fixed fee for a clearly defined scope, so there are no surprises. Advisory work is billed as a monthly retainer. We will recommend the model that best fits your situation."),
    ("Do you work remotely or on site?", "Both. We combine efficient remote collaboration with on-site workshops and leadership sessions wherever being in the room makes a difference."),
    ("How do you handle confidential information?", "Confidentiality is standard in every engagement. We are happy to sign a mutual NDA before any sensitive information is shared, and we use client information only for the purposes of the engagement."),
]


def steps_html():
    items = "\n".join(
        f"""        <li class="step reveal">
          <div class="step-top"><span class="step-num">0{i}</span><span class="step-line"></span></div>
          <h3>{t}</h3>
          <p>{d}</p>
          <p class="step-meta">{m}</p>
        </li>"""
        for i, (t, d, m) in enumerate(STEPS, 1)
    )
    return f'      <ol class="steps">\n{items}\n      </ol>'


def sectors_html():
    return "\n".join(
        f"""        <div class="sector reveal">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" aria-hidden="true">{icon}</svg>
          <div><h3>{t}</h3><p>{d}</p></div>
        </div>"""
        for icon, t, d in SECTORS
    )


def faq_html():
    return "\n".join(
        f"""        <details>
          <summary>{q}</summary>
          <p>{a}</p>
        </details>"""
        for q, a in FAQ
    )


CHART = """<svg class="chart" viewBox="0 0 460 270" role="img" aria-label="Illustration: a growth curve rising through four phases — diagnose, design, deliver, scale — above a flat status-quo line">
            <defs>
              <linearGradient id="chart-fill" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0" stop-color="#cfab6e" stop-opacity="0.32"/>
                <stop offset="1" stop-color="#cfab6e" stop-opacity="0"/>
              </linearGradient>
            </defs>
            <g class="grid">
              <line x1="0" y1="40" x2="460" y2="40"/><line x1="0" y1="100" x2="460" y2="100"/><line x1="0" y1="160" x2="460" y2="160"/><line x1="0" y1="226" x2="460" y2="226"/>
              <line x1="70" y1="206" x2="70" y2="226"/><line x1="175" y1="178" x2="175" y2="226"/><line x1="285" y1="126" x2="285" y2="226"/><line x1="400" y1="60" x2="400" y2="226"/>
            </g>
            <path class="baseline" d="M10 208 C120 206 260 204 450 198"/>
            <path class="area" d="M10 210 C40 208 55 200 70 198 S140 182 175 170 S250 136 285 118 S365 66 400 52 S435 36 450 32 L450 226 L10 226 Z"/>
            <path class="line" d="M10 210 C40 208 55 200 70 198 S140 182 175 170 S250 136 285 118 S365 66 400 52 S435 36 450 32"/>
            <g>
              <circle class="dot" cx="70" cy="198" r="5"/><circle class="dot" cx="175" cy="170" r="5"/><circle class="dot" cx="285" cy="118" r="5"/><circle class="dot" cx="400" cy="52" r="5"/>
            </g>
            <text x="70" y="252" text-anchor="middle">Diagnose</text>
            <text x="175" y="252" text-anchor="middle">Design</text>
            <text x="285" y="252" text-anchor="middle">Deliver</text>
            <text x="400" y="252" text-anchor="middle" class="label-strong">Scale</text>
          </svg>"""


def build_home():
    cards = "\n".join(
        f"""        <a class="card reveal" href="/services#{s['id']}">
          <span class="card-num">0{i}</span>
          <h3>{s['title']}</h3>
          <p>{s['short']}</p>
          <span class="card-more">Learn more {ARROW}</span>
        </a>"""
        for i, s in enumerate(SERVICES, 1)
    )
    compare_rows = [
        ("Team", "Partner sells, junior staff deliver", "Senior consultants scope and deliver the work"),
        ("Pricing", "Open-ended time-and-materials billing", "Fixed fee for a clearly defined scope"),
        ("Output", "Lengthy slide decks", "Decisions, roadmaps and owners&nbsp;&mdash; built to execute"),
        ("Independence", "Often tied to software or vendor partnerships", "Vendor-neutral; no referral fees or resale"),
        ("After we leave", "Dependency on outside advisors", "Tools and know-how transferred to your team"),
    ]
    rows = "\n".join(
        f"            <tr><th scope=\"row\">{a}</th><td>{b}</td><td>{c}</td></tr>" for a, b, c in compare_rows
    )
    ld = f"""
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "{BRAND} Consulting",
    "legalName": "{LEGAL}",
    "url": "{URL}/",
    "logo": "{URL}/assets/apple-touch-icon.png",
    "image": "{URL}/assets/og-image.png",
    "email": "{EMAIL}",
    "telephone": "{PHONE_TEL}",
    "founder": {{ "@type": "Person", "name": "{OWNER}" }},
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "{STREET}",
      "addressLocality": "Sheridan",
      "addressRegion": "WY",
      "postalCode": "82801",
      "addressCountry": "US"
    }},
    "areaServed": "US",
    "description": "Independent strategy and management consulting for growing and mid-sized companies."
  }}
  </script>"""
    body = f"""
  <section class="hero" aria-labelledby="hero-title">
    <div class="wrap hero-inner">
      <div>
        <p class="eyebrow">Strategy &amp; Management Consulting</p>
        <h1 class="display" id="hero-title">Strategy that <em>scales</em> with your ambition.</h1>
        <p class="lead">{BRAND} Consulting helps executives and owners of growing and mid-sized companies make the decisions that shape their next decade&nbsp;&mdash; and turn them into measurable results.</p>
        <div class="hero-actions">
          <a class="btn btn-brass" href="/contact">Schedule a consultation {ARROW}</a>
          <a class="btn btn-ghost-light" href="/services">Explore our services</a>
        </div>
        <p class="hero-note"><svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M8 1.5l5.5 2v4c0 3.5-2.4 5.9-5.5 7-3.1-1.1-5.5-3.5-5.5-7v-4z"/><path d="M5.5 8l1.8 1.8L10.8 6.3"/></svg>Senior-led, confidential engagements. Mutual NDA on request.</p>
      </div>
      <figure class="chart-card">
        <div class="chart-head"><p>From strategy to scale</p><span>How we work</span></div>
          {CHART}
        <figcaption class="chart-legend"><span><i></i>With a clear strategy and disciplined execution</span><span><i class="dashed"></i>Status quo</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="commit" aria-label="Our commitments">
    <div class="wrap commit-grid">
      <div class="commit-item"><strong>100%</strong><span>senior-led engagements, from first call to final result</span></div>
      <div class="commit-item"><strong>2&ndash;4 weeks</strong><span>to a board-ready strategic assessment</span></div>
      <div class="commit-item"><strong>Fixed fee</strong><span>proposals with scope and deliverables agreed up front</span></div>
      <div class="commit-item"><strong>1 business day</strong><span>to respond to every inquiry</span></div>
    </div>
  </section>

  <section class="section" id="services" aria-labelledby="services-title">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="eyebrow">Services</p>
          <h2 class="h2" id="services-title">Advice for the decisions that <em>matter most</em></h2>
        </div>
        <p class="lead">We focus on a small number of disciplines and go deep. Every engagement is tailored to your situation, grounded in evidence and designed to be executed.</p>
      </div>
      <div class="cards">
{cards}
      </div>
    </div>
  </section>

  <section class="section section-paper" aria-labelledby="model-title">
    <div class="wrap compare-wrap">
      <div class="reveal">
        <p class="eyebrow">The {BRAND} model</p>
        <h2 class="h2" id="model-title">Top-tier rigor, <em>without</em> the overhead</h2>
        <p>We built {BRAND} for leadership teams who want the structure and analytical depth of a leading consultancy&nbsp;&mdash; delivered personally, priced transparently and focused on execution.</p>
      </div>
      <div class="reveal">
        <table class="compare">
          <thead><tr><th scope="col"><span class="visually-hidden">Aspect</span></th><th scope="col">Traditional model</th><th scope="col">{BRAND}</th></tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section section-ink" id="approach" aria-labelledby="approach-title">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="eyebrow">Our approach</p>
          <h2 class="h2" id="approach-title">A structured path from <em>insight</em> to impact</h2>
        </div>
        <p class="lead">Every engagement follows the same disciplined sequence, scaled to the size of the question. You always know where we are, what comes next and what it will deliver.</p>
      </div>
{steps_html()}
      <div class="section-foot reveal"><a class="btn btn-ghost-light" href="/approach">See how we work {ARROW}</a></div>
    </div>
  </section>

  <section class="section" id="sectors" aria-labelledby="sectors-title">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="eyebrow">Sectors</p>
          <h2 class="h2" id="sectors-title">Context in the industries that drive the <em>mid-market</em></h2>
        </div>
        <p class="lead">Our methods travel across industries, but good advice depends on understanding how your market really works. These are the sectors we focus on.</p>
      </div>
      <div class="sectors">
{sectors_html()}
      </div>
    </div>
  </section>

  <section class="section section-paper" aria-labelledby="founder-title">
    <div class="wrap founder">
      <div class="founder-card reveal" aria-hidden="true">
        <div class="founder-monogram">IKM</div>
        <p>{OWNER}</p>
        <span class="founder-role">{OWNER_TITLE}</span>
      </div>
      <div class="reveal">
        <p class="eyebrow" id="founder-title">A note from our founder</p>
        <blockquote>I founded {BRAND} to give growing companies access to the kind of rigorous, independent advice usually reserved for the largest corporations&nbsp;&mdash; delivered personally, and measured by results.</blockquote>
        <p class="founder-sign"><span><strong>{OWNER}</strong>{OWNER_TITLE}</span></p>
      </div>
    </div>
  </section>

  <section class="section" id="faq" aria-labelledby="faq-title">
    <div class="wrap">
      <div class="section-head-center reveal">
        <p class="eyebrow">FAQ</p>
        <h2 class="h2" id="faq-title">Frequently asked <em>questions</em></h2>
      </div>
      <div class="faq reveal">
{faq_html()}
      </div>
    </div>
  </section>

{cta()}
"""
    return page(
        "index", f"{BRAND} Consulting | Strategy &amp; Management Consulting",
        f"{BRAND} Consulting is an independent strategy and management consulting firm helping growing and mid-sized companies with growth strategy, operating models, digital and AI strategy, transformation and transactions.",
        body, extra_head=ld,
    )


def build_services():
    nav = "\n".join(f'        <li><a href="#{s["id"]}">{s["nav"]}</a></li>' for s in SERVICES)

    def lis(items):
        return "\n".join(f"              <li>{x}</li>" for x in items)

    blocks = "\n".join(
        f"""    <article class="svc" id="{s['id']}">
      <div class="svc-intro reveal">
        <span class="card-num">0{i}</span>
        <h2 class="h2">{s['title']}</h2>
        <p>{s['intro']}</p>
        <a class="btn btn-primary" href="/contact">Discuss your situation {ARROW}</a>
      </div>
      <div class="svc-detail reveal">
        <div class="svc-box is-questions">
          <h3>Questions we answer</h3>
          <ul>
{lis(s['questions'])}
          </ul>
        </div>
        <div class="svc-box">
          <h3>What we deliver</h3>
          <ul>
{lis(s['deliver'])}
          </ul>
        </div>
        <div class="svc-box is-ink">
          <h3>Outcomes we work toward</h3>
          <ul>
{lis(s['outcomes'])}
          </ul>
        </div>
      </div>
    </article>"""
        for i, s in enumerate(SERVICES, 1)
    )
    body = f"""{page_hero("Services", "Services", "Six disciplines. One goal: <em>measurable</em> results.", "From strategy to execution, we help leadership teams answer their most important questions&nbsp;&mdash; and follow through until the results show up in the numbers.")}

  <nav class="svc-nav" aria-label="Services">
    <div class="wrap">
      <ul>
{nav}
      </ul>
    </div>
  </nav>

  <div class="wrap">
{blocks}
  </div>

{cta("Not sure where to start?", "Most engagements begin with a short conversation about the decision in front of you. We will help you frame the question and suggest the right scope.")}
"""
    return page("services", "Services", f"Strategy, operating model, digital and AI, transformation, transactions and market expansion services from {BRAND} Consulting.", body, active="services")


def build_approach():
    phases = [
        ("Diagnose", "Weeks 1&ndash;3", "We build a shared, fact-based understanding of where you stand and what really drives performance.",
         ["Leadership and stakeholder interviews", "Analysis of financial, market and operational data", "Hypotheses tested against evidence", "Fact base and key issues summary"]),
        ("Design", "Weeks 3&ndash;6", "We develop and evaluate options with your team, quantify the trade-offs and agree on a clear direction.",
         ["Strategic options with quantified impact", "Recommended direction and rationale", "Roadmap with initiatives, owners and milestones", "Business case and success metrics"]),
        ("Deliver", "Months 2&ndash;6+", "We work alongside your team to turn the plan into results&nbsp;&mdash; with governance, pace and accountability.",
         ["Program governance and PMO", "Hands-on support for priority initiatives", "Regular progress and risk reporting", "Course corrections based on results"]),
        ("Scale", "Ongoing", "We make sure improvements stick and keep growing after our involvement ends.",
         ["Results measured against the business case", "Playbooks, tools and templates handed over", "Coaching for internal owners", "Optional advisory check-ins"]),
    ]
    ph = "\n".join(
        f"""        <li class="phase reveal">
          <span class="phase-num">0{i}</span>
          <div>
            <h3>{t}</h3>
            <p class="phase-time">{time}</p>
            <p>{d}</p>
          </div>
          <div>
            <p class="phase-label">Typical deliverables</p>
            <ul>
{chr(10).join(f'              <li>{CHECK}{x}</li>' for x in items)}
            </ul>
          </div>
        </li>"""
        for i, (t, time, d, items) in enumerate(phases, 1)
    )
    timeline = [
        ("Day 1", "Introductory call", "A 30&ndash;45 minute conversation about your situation, goals and constraints."),
        ("Week 1", "Written proposal", "Scope, deliverables, team, timeline and a fixed fee&nbsp;&mdash; in writing, with no obligation."),
        ("Week 2", "Kick-off", "We align on objectives, success metrics, stakeholders and the data we need."),
        ("Week 4", "First insights", "A structured fact base and initial findings, discussed openly with your leadership team."),
    ]
    tl = "\n".join(
        f"""        <li class="reveal"><strong>{a}</strong><h3>{b}</h3><p>{c}</p></li>""" for a, b, c in timeline
    )
    eng = [
        ("Focused", "Strategic Assessment", "Typically 2&ndash;4 weeks", "A rapid, fact-based answer to one specific question&nbsp;&mdash; ideal before a major decision or investment.",
         ["Leadership interviews and data analysis", "Options with quantified trade-offs", "Board-ready recommendation"], "Discuss an assessment", False),
        ("Comprehensive", "Strategy &amp; Transformation", "Typically 3&ndash;9 months", "End-to-end support from strategy design through implementation, with a dedicated senior team.",
         ["Strategy and implementation roadmap", "Program governance and PMO", "Hands-on implementation support", "Results tracking against the business case"], "Plan a program", True),
        ("Ongoing", "Executive Advisory", "Monthly retainer", "An independent, trusted sounding board for CEOs, owners and leadership teams.",
         ["Regular strategy sessions", "On-call advice for critical decisions", "Board and investor preparation"], "Ask about advisory", False),
    ]
    eng_html = "\n".join(
        f"""        <article class="engagement{' is-featured' if feat else ''} reveal">
          <span class="engagement-tag">{tag}</span>
          <h3>{t}</h3>
          <p class="engagement-duration">{dur}</p>
          <p>{d}</p>
          <ul>
{chr(10).join(f'            <li>{CHECK}{x}</li>' for x in items)}
          </ul>
          <a class="btn {'btn-brass' if feat else 'btn-ghost'}" href="/contact">{btn}</a>
        </article>"""
        for tag, t, dur, d, items, btn, feat in eng
    )
    body = f"""{page_hero("Approach", "How we work", "A disciplined path from <em>insight</em> to impact.", "Every engagement follows the same four phases, scaled to the size of your question. You always know where we are, what comes next and what it will deliver.")}

  <section class="section" aria-labelledby="phases-title">
    <div class="wrap">
      <h2 class="visually-hidden" id="phases-title">The four phases</h2>
      <ol class="phases">
{ph}
      </ol>
    </div>
  </section>

  <section class="section section-ink" aria-labelledby="first-title">
    <div class="wrap">
      <div class="section-head reveal">
        <div>
          <p class="eyebrow">Getting started</p>
          <h2 class="h2" id="first-title">Your first <em>30 days</em> with us</h2>
        </div>
        <p class="lead">No lengthy sales process. Within a month of our first conversation, you have a clear plan and first insights on the table.</p>
      </div>
      <ol class="timeline">
{tl}
      </ol>
    </div>
  </section>

  <section class="section section-paper" aria-labelledby="engagements-title">
    <div class="wrap">
      <div class="section-head-center reveal">
        <p class="eyebrow">Ways to work with us</p>
        <h2 class="h2" id="engagements-title">Engagement models that fit the <em>decision</em> in front of you</h2>
        <p class="lead">Every engagement starts with a written proposal: clear scope, deliverables, timeline and fees&nbsp;&mdash; agreed before work begins.</p>
      </div>
      <div class="engagements">
{eng_html}
      </div>
    </div>
  </section>

{cta()}
"""
    return page("approach", "Our Approach", f"How {BRAND} Consulting works: a four-phase approach from diagnosis to scale, transparent engagement models and fixed-fee proposals.", body, active="approach")


def build_about():
    values = [
        ("Candor over comfort", "We tell you what the evidence says, even when it is not what anyone hoped to hear. Honest advice is the most valuable thing we offer."),
        ("Pragmatism over theory", "Recommendations are only useful if your organization can execute them. We design for the company you are, not an idealized one."),
        ("Confidential by default", "Your data, plans and people are handled with discretion. Mutual NDAs are standard on request, and we never share client information."),
        ("Measurable outcomes", "We define success up front, agree on how to measure it, and report against it throughout the engagement."),
    ]
    vals = "\n".join(
        f"""        <div class="value reveal"><span>0{i}</span><h3>{t}</h3><p>{d}</p></div>"""
        for i, (t, d) in enumerate(values, 1)
    )
    body = f"""{page_hero("About", "About the firm", "Independent advice, built around <em>your</em> business.", f"{BRAND} is an independent strategy and management consulting firm for leadership teams of growing and mid-sized companies.")}

  <section class="section" aria-labelledby="story-title">
    <div class="wrap story">
      <div class="reveal">
        <p class="eyebrow">Our story</p>
        <h2 class="h2" id="story-title">Built for companies on the way <em>up</em></h2>
      </div>
      <div class="story-body reveal">
        <p>Growing companies face the same strategic questions as large corporations&nbsp;&mdash; but rarely get the same quality of advice.</p>
        <p>Large consultancies are built for large clients: big teams, long timelines and fees to match. Smaller advisors are often too narrow, or too close to a particular software vendor or solution. Leadership teams in between are left to make high-stakes decisions without an independent, rigorous partner.</p>
        <p>{BRAND} was founded to close that gap. Our name reflects what we stand for: helping companies <strong>scale</strong>&nbsp;&mdash; and being a <strong>safe haven</strong> for honest, independent advice along the way.</p>
        <p>We are deliberately selective about the work we take on. Every engagement is led by senior consultants who stay involved from the first conversation to the final result, so each client receives our full attention.</p>
      </div>
    </div>
  </section>

  <section class="section section-paper" aria-labelledby="values-title">
    <div class="wrap">
      <div class="section-head-center reveal">
        <p class="eyebrow">What we believe</p>
        <h2 class="h2" id="values-title">The principles behind <em>every</em> engagement</h2>
      </div>
      <div class="values">
{vals}
      </div>
    </div>
  </section>

  <section class="section" aria-labelledby="founder-title">
    <div class="wrap founder">
      <div class="founder-card reveal" aria-hidden="true">
        <div class="founder-monogram">IKM</div>
        <p>{OWNER}</p>
        <span class="founder-role">{OWNER_TITLE}</span>
      </div>
      <div class="reveal">
        <p class="eyebrow" id="founder-title">Leadership</p>
        <blockquote>I founded {BRAND} to give growing companies access to the kind of rigorous, independent advice usually reserved for the largest corporations&nbsp;&mdash; delivered personally, and measured by results.</blockquote>
        <p class="founder-sign"><span><strong>{OWNER}</strong>{OWNER_TITLE}</span></p>
      </div>
    </div>
  </section>

  <section class="section-tight section-ink" aria-label="Company information">
    <div class="wrap">
      <dl class="facts reveal">
        <div class="fact"><dt>Legal entity</dt><dd>{LEGAL}</dd></div>
        <div class="fact"><dt>Organized in</dt><dd>State of Wyoming, United States</dd></div>
        <div class="fact"><dt>Mailing address</dt><dd>{STREET}<br>{CITY}</dd></div>
      </dl>
    </div>
  </section>

{cta()}
"""
    return page("about", "About", f"About {BRAND} Consulting: an independent, senior-led strategy and management consulting firm for growing and mid-sized companies.", body, active="about")


def build_contact():
    options = "\n".join(f"                <option>{s['title']}</option>" for s in SERVICES)
    body = f"""{page_hero("Contact", "Contact", "Let&rsquo;s discuss your <em>goals</em>.", "Tell us briefly about your situation. We respond to every inquiry within one business day.")}

  <section class="section" aria-label="Contact details and form">
    <div class="wrap contact">
      <div class="contact-info reveal">
        <p class="eyebrow">Get in touch</p>
        <h2 class="h2">Start with a conversation</h2>
        <p>The first consultation is free and comes with no obligation. Every inquiry is handled confidentially.</p>
        <ul class="contact-list">
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/></svg>
            <div><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z"/></svg>
            <div><strong>Phone</strong><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
          </li>
          <li>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>
            <div><strong>Mailing address</strong><span>{LEGAL}<br>{STREET}<br>{CITY}</span></div>
          </li>
        </ul>
        <ol class="next-steps">
          <li><div><strong>We reply within one business day</strong><span>to arrange a time that suits you.</span></div></li>
          <li><div><strong>Free 30&ndash;45 minute consultation</strong><span>to understand your situation and goals.</span></div></li>
          <li><div><strong>Written proposal</strong><span>with scope, timeline and a fixed fee&nbsp;&mdash; no obligation.</span></div></li>
        </ol>
      </div>
      <div class="reveal">
        <form class="form" id="contact-form" data-recipient="{EMAIL}">
          <h2>Request a consultation</h2>
          <p>Fields marked <span class="req">*</span> are required.</p>
          <div class="form-grid">
            <div class="field"><label for="f-first">First name <span>*</span></label><input id="f-first" name="firstName" autocomplete="given-name" required></div>
            <div class="field"><label for="f-last">Last name <span>*</span></label><input id="f-last" name="lastName" autocomplete="family-name" required></div>
            <div class="field"><label for="f-email">Work email <span>*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
            <div class="field"><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
            <div class="field"><label for="f-company">Company</label><input id="f-company" name="company" autocomplete="organization"></div>
            <div class="field"><label for="f-role">Role</label><input id="f-role" name="role" autocomplete="organization-title"></div>
            <div class="field field-full">
              <label for="f-interest">Area of interest</label>
              <select id="f-interest" name="interest">
                <option value="">Select a topic</option>
{options}
                <option>Other / not sure yet</option>
              </select>
            </div>
            <div class="field field-full"><label for="f-message">How can we help? <span>*</span></label><textarea id="f-message" name="message" required></textarea></div>
            <label class="consent"><input type="checkbox" name="consent" required><span>I agree that the information I provide will be used to respond to my inquiry, as described in the <a href="/privacy">Privacy Policy</a>. <span class="req">*</span></span></label>
            <div class="form-actions">
              <button class="btn btn-primary" type="submit">Send inquiry {ARROW}</button>
              <p class="form-status" id="form-status" aria-live="polite">Your inquiry opens in your email app, ready to send.</p>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
"""
    return page("contact", "Contact", f"Contact {BRAND} Consulting to schedule a free, no-obligation consultation.", body, active="contact")


ADDRESS = f"""<address>
          {LEGAL}<br>
          (trading as {BRAND} Consulting)<br>
          {STREET}<br>
          {CITY}<br>
          {COUNTRY}<br>
          Email: <a href="mailto:{EMAIL}">{EMAIL}</a><br>
          Phone: <a href="tel:{PHONE_TEL}">{PHONE}</a>
        </address>"""


def legal_page(slug, title, description, intro, sections):
    toc = "\n".join(f'          <li><a href="#{sid}">{label}</a></li>' for sid, label, _ in sections)
    secs = "\n".join(
        f'      <section id="{sid}">\n        <h2>{label}</h2>\n{content}\n      </section>'
        for sid, label, content in sections
    )
    body = f"""{page_hero(title, "Legal", title, intro)}
  <div class="wrap legal">
    <nav class="legal-toc" aria-label="On this page">
      <strong>On this page</strong>
      <ol>
{toc}
      </ol>
    </nav>
    <div class="legal-body">
{secs}
    </div>
  </div>"""
    return page(slug, title, description, body)


PRIVACY = [
    ("who-we-are", "1. Who we are", f"""        <p>This Privacy Policy explains how personal information is collected and used when you visit this website or contact us. The party responsible for processing your personal information (the &ldquo;controller&rdquo;) is:</p>
        <div class="legal-card">
        {ADDRESS}
        </div>
        <p>In this policy, &ldquo;we&rdquo;, &ldquo;us&rdquo; and &ldquo;our&rdquo; refer to {LEGAL}, trading as {BRAND} Consulting.</p>"""),
    ("collect", "2. Information we collect", """        <h3>a) When you visit this website</h3>
        <p>When you access the website, our hosting provider automatically processes technical information that your browser sends, such as your IP address, the date and time of access, the page requested, the referring URL, and your browser type and operating system (&ldquo;server log data&rdquo;). This is technically necessary to deliver the website and to protect it against misuse and attacks.</p>
        <h3>b) When you contact us</h3>
        <p>If you contact us by email, phone or via the contact form, we process the information you provide, such as your name, email address, phone number, company, role and the content of your message. The contact form does not transmit data to our servers; it prepares a message in your own email program, which you then send to us yourself.</p>
        <h3>c) What we do not use</h3>
        <p>This website does not use cookies, analytics or tracking tools, advertising pixels, social media plug-ins or externally loaded fonts. All fonts are hosted on our own website.</p>"""),
    ("use", "3. How we use your information", """        <p>We use personal information only to:</p>
        <ul>
          <li>respond to your inquiry and, where requested, prepare a proposal;</li>
          <li>perform and administer engagements with our clients;</li>
          <li>operate, maintain and secure this website; and</li>
          <li>comply with legal, tax and accounting obligations.</li>
        </ul>
        <p>We do not sell your personal information, and we do not share it for cross-context behavioral advertising. We do not use your information for automated decision-making or profiling.</p>"""),
    ("legal-bases", "4. Legal bases (EEA, UK and Switzerland)", """        <p>If the EU or UK General Data Protection Regulation (GDPR) or the Swiss Federal Act on Data Protection applies, we rely on the following legal bases:</p>
        <ul>
          <li><strong>Art. 6(1)(b) GDPR</strong> &ndash; steps prior to entering into a contract, or performance of a contract, when your inquiry relates to a potential or existing engagement;</li>
          <li><strong>Art. 6(1)(f) GDPR</strong> &ndash; our legitimate interests in answering general inquiries and in operating a secure, stable website;</li>
          <li><strong>Art. 6(1)(c) GDPR</strong> &ndash; compliance with legal obligations, such as statutory retention requirements;</li>
          <li><strong>Art. 6(1)(a) GDPR</strong> &ndash; your consent, where we ask for it. You may withdraw consent at any time with effect for the future.</li>
        </ul>"""),
    ("sharing", "5. Service providers and disclosures", """        <p>We share personal information only where necessary and with service providers who process it on our behalf and under our instructions:</p>
        <ul>
          <li><strong>Website hosting:</strong> Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, USA, which hosts this website and processes server log data.</li>
          <li><strong>Email and IT services:</strong> providers that host our email and office systems.</li>
          <li><strong>Professional advisors and authorities:</strong> lawyers, accountants and auditors, or public authorities where we are legally required to disclose information.</li>
        </ul>
        <p>We are based in the United States, and our service providers may process information in the United States or other countries. Where transfers from the EEA, UK or Switzerland are subject to data protection law, they take place on the basis of an adequacy decision (including the EU-U.S. Data Privacy Framework, where the recipient is certified) or the European Commission&rsquo;s Standard Contractual Clauses.</p>"""),
    ("retention", "6. How long we keep information", """        <p>We keep personal information only as long as necessary for the purposes described above. Inquiry correspondence is generally deleted no later than two years after our last contact, unless it leads to an engagement or statutory retention periods (for example, for commercial or tax records) require longer storage. Server log data is retained by our hosting provider for a limited period for security purposes.</p>"""),
    ("rights", "7. Your privacy rights", f"""        <h3>U.S. state residents</h3>
        <p>Depending on your state of residence (for example California, Colorado, Connecticut, Virginia and other states with comprehensive privacy laws), you may have the right to know what personal information we collect and how we use it, to access, correct or delete your personal information, and to opt out of the sale or sharing of personal information or targeted advertising. As described above, we do not sell or share personal information or engage in targeted advertising. We will not discriminate against you for exercising any of these rights.</p>
        <h3>Visitors from the EEA, UK and Switzerland</h3>
        <p>You have the right to access your personal data, to have it rectified or erased, to restrict its processing, to data portability and to object to processing based on legitimate interests. You also have the right to lodge a complaint with a data protection supervisory authority, in particular in the country where you live or work.</p>
        <h3>How to exercise your rights</h3>
        <p>To make a request, email us at <a href="mailto:{EMAIL}">{EMAIL}</a>. We may need to verify your identity before responding. You may use an authorized agent where permitted by law. If we deny your request, you may appeal by replying to our decision.</p>"""),
    ("security", "8. Security", """        <p>We use appropriate technical and organizational measures to protect personal information, including encrypted (HTTPS) connections for this website. No method of transmission over the internet is completely secure, however, and we cannot guarantee absolute security.</p>"""),
    ("children", "9. Children", """        <p>This website is intended for business audiences and is not directed to children. We do not knowingly collect personal information from children under the age of 16.</p>"""),
    ("changes", "10. Changes to this policy", f"""        <p>We may update this Privacy Policy from time to time. The current version is always available on this page, and the effective date below shows when it was last revised.</p>
        <p><strong>Effective date:</strong> {EFFECTIVE}</p>"""),
    ("contact", "11. Contact", f"""        <p>If you have any questions about this Privacy Policy or how we handle personal information, please contact us:</p>
        <div class="legal-card">
        {ADDRESS}
        </div>"""),
]

TERMS = [
    ("acceptance", "1. Acceptance of these terms", f"""        <p>This website is operated by {LEGAL}, a Wyoming limited liability company trading as {BRAND} Consulting (&ldquo;we&rdquo;, &ldquo;us&rdquo;). By accessing or using the website, you agree to these Terms of Use. If you do not agree, please do not use the website.</p>"""),
    ("no-advice", "2. No professional advice; no client relationship", """        <p>The content of this website is provided for general information only. It does not constitute business, financial, legal, tax or other professional advice and should not be relied upon as such. Using this website or contacting us does not create a client relationship. Any engagement is governed exclusively by a separate written agreement signed by both parties.</p>"""),
    ("ip", "3. Intellectual property", f"""        <p>All content on this website, including text, graphics, logos and design, is owned by or licensed to us and is protected by copyright, trademark and other laws. &ldquo;{BRAND}&rdquo;, &ldquo;{BRAND} Consulting&rdquo; and the {BRAND} logo are trade names and marks used by us.</p>
        <p>You may view, download and print pages of this website for your own internal, non-commercial use, provided that you do not modify the content and keep all copyright and proprietary notices intact. Any other use requires our prior written permission.</p>"""),
    ("use", "4. Acceptable use", """        <p>You agree not to use the website in any way that is unlawful or that could damage, disable or impair it, including by attempting to gain unauthorized access to any systems, introducing malicious code, or using automated means to scrape or harvest content.</p>"""),
    ("links", "5. Third-party links", """        <p>The website may contain links to third-party websites. We are not responsible for the content, privacy practices or availability of those websites, and a link does not imply endorsement.</p>"""),
    ("disclaimer", "6. Disclaimer", """        <p>We take care to keep the information on this website accurate and up to date. However, the website and its content are provided &ldquo;as is&rdquo; and &ldquo;as available&rdquo;, without warranties of any kind, express or implied, including warranties of accuracy, completeness, merchantability, fitness for a particular purpose and non-infringement, to the fullest extent permitted by law.</p>"""),
    ("liability", "7. Limitation of liability", """        <p>To the fullest extent permitted by law, we are not liable for any indirect, incidental, consequential, special or punitive damages, or for any loss of profits, revenue or data, arising from your use of, or inability to use, the website or its content.</p>
        <p>Nothing in these terms excludes or limits liability that cannot be excluded or limited under applicable law.</p>"""),
    ("law", "8. Governing law and venue", """        <p>These Terms of Use are governed by the laws of the State of Wyoming, United States, without regard to its conflict-of-law rules. Any dispute arising from these terms or your use of the website shall be brought exclusively in the state or federal courts located in Wyoming, unless mandatory law provides otherwise.</p>"""),
    ("changes", "9. Changes", f"""        <p>We may revise these Terms of Use at any time by updating this page. Your continued use of the website after changes are posted constitutes acceptance of the revised terms.</p>
        <p><strong>Effective date:</strong> {EFFECTIVE}</p>"""),
    ("contact", "10. Contact", f"""        <p>Questions about these Terms of Use can be sent to:</p>
        <div class="legal-card">
        {ADDRESS}
        </div>"""),
]

NOTICE = [
    ("operator", "Website operator", f"""        <div class="legal-card">
        {ADDRESS}
        </div>"""),
    ("company", "Company information", f"""        <p><strong>Legal entity:</strong> {LEGAL}</p>
        <p><strong>Legal form:</strong> Limited liability company organized under the laws of the State of Wyoming, USA</p>
        <p><strong>Trade name:</strong> {BRAND} Consulting</p>
        <p><strong>Represented by:</strong> {OWNER}, Managing Member</p>"""),
    ("responsible", "Responsible for content", f"""        <p>{OWNER}, address as above.</p>"""),
    ("content", "Liability for content", """        <p>We prepare the content of this website with care. However, we cannot guarantee that the content is accurate, complete or current. We are not obliged to monitor transmitted or stored third-party information. If we become aware of any legal violations, we will remove the relevant content promptly.</p>"""),
    ("links", "Liability for links", """        <p>This website may contain links to external third-party websites over whose content we have no influence. The respective provider or operator is always responsible for the content of linked pages. If we become aware of legal violations, we will remove such links promptly.</p>"""),
    ("copyright", "Copyright", """        <p>The content and works on this website are subject to copyright. Reproduction, editing, distribution or any kind of use beyond the limits of copyright law require our prior written consent. Fonts used on this website (Inter and Newsreader) are licensed under the SIL Open Font License.</p>"""),
]


def build_404():
    body = """  <section class="notfound">
    <div class="wrap">
      <p class="eyebrow">Error 404</p>
      <h1 class="display">Page not found</h1>
      <p>The page you are looking for has moved or no longer exists.</p>
      <a class="btn btn-primary" href="/">Back to homepage</a>
    </div>
  </section>"""
    return page("404", "Page not found", "The page you are looking for could not be found.", body, noindex=True)


def main():
    pages = {
        "index.html": build_home(),
        "services.html": build_services(),
        "approach.html": build_approach(),
        "about.html": build_about(),
        "contact.html": build_contact(),
        "privacy.html": legal_page("privacy", "Privacy Policy", f"How {BRAND} Consulting collects, uses and protects personal information.",
                                   f"Effective {EFFECTIVE}. We collect as little personal information as possible and never sell it.", PRIVACY),
        "terms.html": legal_page("terms", "Terms of Use", f"Terms governing the use of the {BRAND} Consulting website.", f"Effective {EFFECTIVE}.", TERMS),
        "legal-notice.html": legal_page("legal-notice", "Legal Notice", f"Legal notice and company information for {BRAND} Consulting.",
                                        "Company information and statutory disclosures.", NOTICE),
        "404.html": build_404(),
    }
    for name, html in pages.items():
        (ROOT / name).write_text(html)

    urls = ["/", "/services", "/approach", "/about", "/contact", "/privacy", "/terms", "/legal-notice"]
    sitemap = "\n".join(f"  <url><loc>{URL}{u}</loc><lastmod>2026-10-17</lastmod></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap}\n</urlset>\n'
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {URL}/sitemap.xml\n")
    print("built", len(pages), "pages")


if __name__ == "__main__":
    main()
