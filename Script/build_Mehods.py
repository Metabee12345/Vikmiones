from __future__ import annotations

import html
from pathlib import Path

import markdown

INPUT_FILE = "../Methods/Methods.md"
OUTPUT_FILE = "../Methods/index.html"
PAGE_TITLE = "Methods"
CURRENT_NAV = "Methods"

NAV_LINKS = [
    ("Recommendations", "https://metabee12345.github.io/Vikmiones/"),
    ("Results", "https://metabee12345.github.io/Vikmiones/Results/"),
    ("Methods", "https://metabee12345.github.io/Vikmiones/Methods/"),
    ("Rubric", "https://metabee12345.github.io/Vikmiones/Rubric/"),
    ("Raw Data", "https://metabee12345.github.io/Vikmiones/RawData/"),
    ("Discussion", "https://metabee12345.github.io/Vikmiones/Discussion/"),
]

def build_navbar(current_title: str = "") -> str:
    items: list[str] = []

    for label, url in NAV_LINKS:
        active_class = ' class="active"' if label == current_title else ""
        items.append(
            f'<a href="{html.escape(url, quote=True)}"{active_class}>{html.escape(label)}</a>'
        )

    return '<nav class="top-nav">' + "".join(items) + "</nav>"


def read_markdown(path: str | Path) -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Markdown file not found: {path}")
    return path.read_text(encoding="utf-8")


def markdown_to_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "toc",
        ],
    )


def build_full_page(body_html: str, title: str, nav_current: str = "") -> str:
    navbar_html = build_navbar(nav_current)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-V2XC5ZD4XL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());

  gtag('config', 'G-V2XC5ZD4XL');
</script>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>

  <style>
    body {{
      font-family: "Segoe UI", Arial, sans-serif;
      margin: 1.5rem;
      color: #000;
      line-height: 1.55;
      max-width: 1100px;
    }}

    h1, h2, h3, h4 {{
      line-height: 1.2;
    }}

    h1 {{
      margin-top: 0;
      margin-bottom: 1rem;
      font-size: 20px;
      font-weight: 700;
    }}

    h2 {{
      margin-top: 2rem;
      border-bottom: 1px solid #e5e5e5;
      padding-bottom: 0.25rem;
      font-size: 16px;
      font-weight: 700;
    }}

    h1:first-of-type {{
      font-size: 30px;
      font-weight: 700;
      margin-bottom: 1.5rem;
    }}

    p, ul, ol {{
      font-size: 16px;
    }}

    code {{
      font-family: Consolas, "Courier New", monospace;
      background: #f5f5f5;
      padding: 0.1rem 0.3rem;
      border-radius: 4px;
    }}

    pre {{
      background: #f5f5f5;
      padding: 1rem;
      overflow-x: auto;
      border-radius: 6px;
    }}

    pre code {{
      background: none;
      padding: 0;
    }}

    table {{
      border-collapse: collapse;
      width: 100%;
      margin: 1rem 0;
    }}

    th, td {{
      border: 1px solid #ddd;
      padding: 0.5rem;
      vertical-align: top;
      text-align: left;
    }}

    th {{
      background: #f7f7f7;
    }}

    blockquote {{
      margin-left: 0;
      padding-left: 1rem;
      border-left: 4px solid #ddd;
      color: #444;
    }}

    details {{
      margin-bottom: 0.75rem;
    }}

    summary {{
      cursor: pointer;
      font-weight: 600;
      padding: 0.2rem 0;
    }}

    summary:hover {{
      text-decoration: underline;
    }}

    summary::marker {{
      font-size: 0.9em;
    }}

    details details {{
      margin-left: 1rem;
    }}

    details summary {{
      cursor: pointer;
      padding: 0.2rem 0;
    }}

    details summary:hover {{
      text-decoration: underline;
    }}

    /* klikbare # headings */
    #page-content > details > summary {{
      font-size: 24px;
      font-weight: 700;
      line-height: 1.2;
    }}

    /* klikbare ## headings */
    #page-content > details > div > details > summary,
    #page-content details details > summary {{
      font-size: 20px;
      font-weight: 700;
      line-height: 1.2;
    }}

    .top-nav {{
      display: flex;
      gap: 1rem;
      align-items: center;
      padding: 0.2rem 0;
      margin-bottom: 1rem;
      margin-top: -0.95rem;
      border-bottom: 1px solid #d0d0d0;
      font-family: "Segoe UI", Arial, sans-serif;
      font-size: 16px;
      font-weight: 900;
    }}

    .top-nav a {{
      color: #333;
      text-decoration: none;
      padding: 0.15rem 0.25rem;
    }}

    .top-nav a:hover {{
      text-decoration: underline;
    }}

    .top-nav a.active {{
      color: #000;
      font-weight: 700;
    }}
  </style>
</head>
<body>
  {navbar_html}
  <div id="page-content">
    {body_html}
  </div>

  <script>
  document.addEventListener("DOMContentLoaded", function () {{
  const content = document.getElementById("page-content");

  function wrapSections(tagName) {{
    const headings = Array.from(content.querySelectorAll(tagName));

    headings.forEach((h, index) => {{
      // keep the very first h1 non-collapsible
      if (tagName === "h1" && index === 0) return;

      // skip if already inside a summary/details structure
      if (h.closest("summary")) return;

      const details = document.createElement("details");
      details.open = false;

      const summary = document.createElement("summary");
      summary.innerHTML = h.innerHTML;

      details.appendChild(summary);

      let next = h.nextSibling;

      while (next && !(next.tagName && next.tagName.match(/^H[1-6]$/))) {{
        const temp = next.nextSibling;
        details.appendChild(next);
        next = temp;
      }}

      h.replaceWith(details);
    }});
  }}

  // wrap h2 first, then h1
  wrapSections("h2");
  wrapSections("h1");
}});
</script>
</body>
</html>
"""


def main() -> None:
    md_text = read_markdown(INPUT_FILE)
    body_html = markdown_to_html(md_text)
    page_html = build_full_page(body_html, PAGE_TITLE, CURRENT_NAV)

    Path(OUTPUT_FILE).write_text(page_html, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
