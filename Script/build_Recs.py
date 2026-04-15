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
    safe_title = html.escape(title)
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
            "Type": "Canon-div / Romance",
            "Description": "dsgdagd",
            "Recommendation": recommendation_cell(
                "Air - Calebski",
                "https://archiveofourown.org/works/11461545",
            ),
            "Explanation": "fdgdfsgdf",
        },
        {
            "Type": "Canon-div / Plot",
            "Description": "",
            "Recommendation": recommendation_cell(
                "To the You of 1994",
                "https://archiveofourown.org/works/51945343",
            ),
            "Explanation": "",
        },
        {
            "Type": "Postwar / Romance",
            "Description": "",
            "Recommendation": recommendation_cell(
                "The Flower Shop",
                "https://archiveofourown.org/works/7544140",
            ),
            "Explanation": "",
        },
        {
            "Type": "Postwar / Plot",
            "Description": "",
            "Recommendation": recommendation_cell(
                "The Observer Effect",
                "https://archiveofourown.org/works/32711164",
            ),
            "Explanation": "",
        },
        {
            "Type": "Intermezzo",
            "Description": "",
            "Recommendation": recommendation_cell(
                "Hunting Shadows",
                "https://archiveofourown.org/works/23468659",
            ),
            "Explanation": "",
        },
        {
            "Type": "Alternate Reality / Romance",
            "Description": "",
            "Recommendation": recommendation_cell(
                "Love Me Like You Do",
                "https://archiveofourown.org/works/9362093",
            ),
            "Explanation": "",
        },
        {
            "Type": "Alternate Reality / Plot",
            "Description": "",
            "Recommendation": recommendation_cell(
                "Flower of the North",
                "https://archiveofourown.org/works/41745237",
            ),
            "Explanation": "",
        },
    ]

    return pd.DataFrame(rows, columns=["Type", "Description", "Recommendation", "Explanation"])


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
      font-weight: 500;
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
  </style>
</head>
<body>
  {build_navbar(nav_current)}

  <div class="header-bar">
  <h1>{html.escape(title)}</h1>
  </div>

  {table_html}

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
      info: true,
      autoWidth: false,
      scrollX: true,
      orderCellsTop: true,
      columnDefs: [
        {{ targets: 0, className: "col-type", width: "10%" }},
        {{ targets: 1, className: "col-description", width: "30%" }},
        {{ targets: 2, className: "col-recommendation", width: "10%" }},
        {{ targets: 3, className: "col-explanation", width: "30%" }}
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
                                title="Hermione/Viktor Harry Potter Fanctions; Best Recommendations",
                                nav_current="")

    Path(OUTPUT_FILE).write_text(page_html, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
