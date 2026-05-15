from __future__ import annotations

import html
from pathlib import Path

import pandas as pd

OUTPUT_FILE = "../index.html"

NAV_LINKS = [
    ("Recommendations", "https://metabee12345.github.io/Vikmiones/"),
    ("Results", "https://metabee12345.github.io/Vikmiones/Results/"),
    ("Methods", "https://metabee12345.github.io/Vikmiones/Methods/"),
    ("Rubric", "https://metabee12345.github.io/Vikmiones/Rubric/"),
    ("Raw Data", "https://metabee12345.github.io/Vikmiones/RawData/"),
    ("Discussion", "https://metabee12345.github.io/Vikmiones/Discussion/"),
]

def recommendation_cell(title: str, url: str) -> str:
    # safe_title = html.escape(title)
    safe_title = title
    safe_url = html.escape(url, quote=True)

    return (
        f'<div class="rec-cell">'
        f'  <a class="rec-title" href="{safe_url}" target="_blank" rel="noopener noreferrer">'
        f'    {safe_title}'
        f'  </a>'
        f'</div>'
    )

def build_dataframe() -> pd.DataFrame:
    rows = [
        {
            "sort_order": 2,
            "Type": "Canon-Divergence / <br> Plot-focus",
            "Description": '<strong class="smallfattext">Hermione and Viktor meet during or slightly before GoF</strong>. <br>'+
                           "We see how events unfold when they stay together. <br>"+
                           "There is a good romance, but the main focus is on how <br>"+
                           "Hermione's romantic choice affects the war and larger HP-plot.",
            "Recommendation": recommendation_cell(
                "Alignment - FastNeutrons",
                "https://archiveofourown.org/works/73628601",
            ),
            "Explanation": '<strong class="smallfattext">The one single canon-divergence vikmione in the dataset that is truely complete </strong> (covering full GoF-DH). It also holds the single highest <br>'+
                           "Quality score of the entire dataset. Other complete canon-divergences either miss their sequel after GoF, or are not vikmione-centric. <br>"+
                           "Looks can be Deceiving, for example, is a magnificent work. But it is a canon-divergence with a vikmione-endgame. It is not <br>"+
                           "a true vikmione-centric canon-divergence, unlike Alignment.",
        },
        {
            "sort_order": 1,
            "Type": "Canon-Divergence / <br> Romance-focus",
            "Description": '<strong class="smallfattext">Hermione and Viktor meet during or slightly before GoF</strong>. <br>'+
                           "We see how events unfold when they stay together. <br>"+
                           "Effects on the larger HP plot are present, but the main <br>"+
                           "focus is on the development of the relationship.",
            "Recommendation": recommendation_cell(
                "Air - Calebski",
                "http://archiveofourown.org/works/18766738",
            ),
            "Explanation": '<strong class="smallfattext">An iconic work, and without a doubt the best romance-oriented canon-divergence for Hermione/Viktor</strong>. Both its quality score and <br>'+
            "absolute number of hits are at the top of it's category. Another big advantage is that the story continues to the end of Ootp, which is further <br>"+
            "into the HP-plot than any other romance-oriented canon-divergence in the dataset. It is still WIP, but our dataset does not contain Complete <br>"+
            "works in this category other then 'A life in Letters', which is not a longfic.",
        },
        {
            "sort_order": 4,
            "Type": "Post-War / <br> Plot-focus",
            "Description": '<strong class="smallfattext">Hermione and Viktor reconnect after Voldemort is defeated</strong>, <br>'+
                           "usually connected to themes like trauma, safety and healing. <br>"+
                           "There is a good romance, but the main focus is on how <br>"+
                           "Hermione's choices affects the larger wizarding world.",
            "Recommendation": recommendation_cell(
                "Debts of Honor - sareliz",
                "http://archiveofourown.org/works/23132749",
            ),
            "Explanation": '<strong class="smallfattext">An iconic work, by far the highest Quality score of all plot/postwar works</strong>, and the second-ranked work in the database in absolute <br>'+
                           "number of hits. There is a massive plot and a beautiful romance about healing after the war with Voldemort. It is WIP, but it stops <br>"+
                           "at a very natural point, so that it could be considered finished."
        },
        {
            "sort_order": 3,
            "Type": "Post-War / <br> Romance-focus",
            "Description": '<strong class="smallfattext">Hermione and Viktor reconnect after Voldemort is defeated</strong>. <br>'+
                           "Effects on the larger world are present, but the main <br>"+
                           "focus is on the development of the relationship, <br>"+
                           "usually connected to themes like trauma, safety and healing.",
            "Recommendation": recommendation_cell(
                "Letter of Survival - Buddybee13",
                "http://archiveofourown.org/works/56968588",
            ),
            "Explanation": '<strong class="smallfattext">The best combination between popularity and quality score in this category</strong>. However, the category is difficult as the better <br>'+
                           'postwar-works usually have a stronger plot-focus. Letters of Survival is the best one is this category, but The Flower Shop - paigevlindsay is <br>'+
                           'also a good option if you prefer less heavy themes.'
        },
        {
            "sort_order": 5,
            "Type": "Intermezzo",
            "Description": '<strong class="smallfattext"> A story that can be inserted </strong> into the canonical <br>'+
                           "HP-plot without breaking or changing it. Usually spanning <br>"+
                           "a limited amount of time and romance-focussed.",
            "Recommendation": recommendation_cell(
                "Hunting Shadows - TangentiaLives",
                "http://archiveofourown.org/works/23468659",
            ),
            "Explanation": '<strong class="smallfattext">A wonderful story about Hermione travelling to Bulgaria between PoS and GoF.</strong> Its quality score is close to Light to fight the shadows, <br>'+
                           "but it's hits and popularity are way larger, hence the recommendation. It also has a notable plot beyond just romance."
        },
        {
            "sort_order": 7,
            "Type": "Alternate Reality / <br> Plot-focus",
            "Description": '<strong class="smallfattext">Hermione and Viktor meet in a setting that is not <br>'+
                           "directly related to the canonical main HP-plot</strong>. <br>"+
                           "There is a good romance, but the main focus is on how <br>"+
                           "Hermione's romantic choice affects the larger world.",
            "Recommendation": recommendation_cell(
                "Hermione Granger and the silent country </br> - Callmesalticidae",
                "https://archiveofourown.org/works/27111157",
            ),
            "Explanation": '<strong class="smallfattext">By far the best Quality score for this type of works</strong> in the database. Alternatives are either quite philosophical, or the characters <br>'+
                           "and setting no longer feel like the Harry Potter world. Hermione studies at beauxbatons in a heavily altered setting w.r.t. canon."
        },
        {
            "sort_order": 6,
            "Type": "Alternate Reality / <br> Romance-focus",
            "Description": '<strong class="smallfattext">Hermione and Viktor meet in a setting that is not <br>'+
                           "directly related to the canonical main HP-plot</strong>. <br>"+
                           "Effects on the larger world are present, but the main <br>"+
                           "focus is on the development of the relationship.",
            "Recommendation": recommendation_cell(
                "A Year Abroad - paigevlindsay",
                "https://archiveofourown.org/works/7933567",
            ),
            "Explanation": '<strong class="smallfattext">The top quality score in this category and complete.</strong> The number of these type of works is not very broad in the dataset (only 3). <br>'+
                           "One has a low Quality score and another is WIP, leaving this one as our recommendation. Hermione travels to Durmstrang as part <br>"+
                           "of an exchange-program after the war is over. The war and HP-plot have been massively altered to generate space for the exchange-program."
        },
    ]

    return pd.DataFrame(rows, columns=["sort_order", "Type", "Description", "Recommendation", "Explanation"])


def build_html_table(df: pd.DataFrame) -> str:
    return df.to_html(
        index=False,
        escape=False,  # needed so URL links stay clickable
        table_id="ficTable",
        classes="display nowrap compact",
        border=0,
    )


def build_navbar(current_title: str = "") -> str:
    items = []

    for label, url in NAV_LINKS:
        active_class = ' class="active"' if label == current_title else ""
        items.append(
            f'<a href="{html.escape(url, quote=True)}"{active_class}>{html.escape(label)}</a>'
        )

    return '<nav class="top-nav">' + "".join(items) + "</nav>"

def build_full_page(table_html: str, title: str = "Summary Table", nav_current: str = "") -> str:
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

  <link rel="stylesheet" href="https://cdn.datatables.net/1.13.8/css/jquery.dataTables.min.css">

  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 1.5rem;
    }}

    h1 {{
      margin-bottom: 1rem;
    }}

    .table-container {{
      overflow-x: auto;
    }}

    table.dataTable {{
      width: 100% !important;
      font-size: 12px;
    }}

    table.dataTable thead th {{
      font-size: 16px;
      font-weight: 600;
      font-family: "Segoe UI", Arial, sans-serif;
      color: #000000;
      white-space: nowrap;
    }}

    table.dataTable tbody td {{
      font-size: 13px;
      font-weight: 300;
      font-family: "Segoe UI", Arial, sans-serif;
      color: #000000;
      vertical-align: top;
      white-space: nowrap;
    }}

    .header-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1rem;
    }}

    .header-bar h1 {{
      margin: 0;
    }}

    .filters {{
      display: flex;
      gap: 1.5rem;
      align-items: flex-start;
    }}

    .filters > div {{
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .filters select {{
      min-width: 200px;
      height: 5.5em;
      font-size: 13px;
    }}

    a {{
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}

    .top-nav {{
      display: flex;
      gap: 1rem;
      align-items: center;
      padding: 0.45rem 0;
      margin-bottom: 1rem;
      margin-top: -1rem;
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

    td.col-type {{
      font-size: 18px !important;
      font-weight: 600;
    }}

    td.col-description {{
      font-size: 13px !important;
      font-weight: 300;
    }}

    td.col-recommendation {{
      font-size: 18px !important;
      font-weight: 500;
    }}

    td.col-explanation {{
      font-size: 13px !important;
      font-weight: 300;
    }}

    #ficTable thead th:nth-child(1) {{
      font-size: 20px;
      font-weight: 700;
    }}

    #ficTable thead th:nth-child(2) {{
      font-size: 20px;
      font-weight: 700;
    }}

    #ficTable thead th:nth-child(3) {{
      font-size: 20px;
      font-weight: 700;
    }}

    #ficTable thead th:nth-child(4) {{
      font-size: 20px;
      font-weight: 700;
    }}

    .introduction {{
      font-size: 18px;
      color: #000000;
      font-weight: 400;
      margin-bottom: 2rem;
    }}

    .flagtext {{
      font-size: 18px;
      color: #000000;
      font-weight: 400;
      margin-top: 1rem;
      margin-bottom: 2rem;
    }}

    .smallfattext {{
      font-weight: 700;
    }}
  </style>
</head>
<body>
  {build_navbar(nav_current)}

  <div class="header-bar">
  <h1>{html.escape(title)}</h1>
  </div>

  <h1 class="introduction">
  Hermione/Viktor fanfiction recommendations, including canon-divergence, post-war, and AU longfics. This guide helps you find the best Vikmione fics with summaries, filters, and structured analysis.
  <br>
  Click a title to open the fic, or use the <strong class="smallfattext"><a href="https://metabee12345.github.io/Vikmiones/Results/">Results</a></strong> to browse the full list of fics (filters available).
  </h1>

  {table_html}

  <div class="flagtext">
  All recommendations are based on a <strong class="smallfattext">structured quality <a href="https://metabee12345.github.io/Vikmiones/Rubric/">rubric</a></strong> with high internal consistency (Cronbach α = 0.78, Spearman = 0.92, Average fluctuation = 5.7%).
  <br>
  <br>
  You can browse the full list of all analysed fics <a href="https://metabee12345.github.io/Vikmiones/Results/">here</a>, or read about the <a href="https://metabee12345.github.io/Vikmiones/Methods/">analysis method</a> and <a href="https://metabee12345.github.io/Vikmiones/Discussion/">statistical analysis</a>.
  </div>

  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  <script src="https://cdn.datatables.net/1.13.8/js/jquery.dataTables.min.js"></script>

  <script>
  $(document).ready(function() {{
    const table = $('#ficTable');

    const dataTable = table.DataTable({{
      paging: true,
      pageLength: -1,
      lengthMenu: [[-1], ["All"]],
      searching: true,
      ordering: true,
      order: [[0, "asc"]],
      info: true,
      autoWidth: false,
      scrollX: true,
      orderCellsTop: true,
      language: {{
        search: "Search (title, tags, themes):"
      }},
      columnDefs: [
        {{ targets: 0, visible: false }},
        {{ targets: 1, className: "col-type", width: "12%" }},
        {{ targets: 2, className: "col-description", width: "25%" }},
        {{ targets: 3, className: "col-recommendation", width: "12%" }},
        {{ targets: 4, className: "col-explanation", width: "51%" }}
      ]
    }});

  }});
</script>
</body>
</html>
"""


def main() -> None:

    # Read table:
    df = build_dataframe()
    df = df.fillna("")

    table_html = build_html_table(df)
    page_html = build_full_page(table_html,
                                title="Hermione/Viktor Fic Guide; Best Recommendations & Hidden Gems",
                                nav_current="")

    Path(OUTPUT_FILE).write_text(page_html, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
