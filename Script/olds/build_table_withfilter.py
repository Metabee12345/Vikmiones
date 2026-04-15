from __future__ import annotations

import html
from pathlib import Path

import pandas as pd


INPUT_FILE = "./Vikmione beoordeling.xlsx"
SHEET_NAME = "Summary"
OUTPUT_FILE = "index.html"

COLUMN_ORDER = [
    "Titel",
    "Author",
    "URL",
    "Status",
    "Wordcount(k)",
    "Vikmione Type",
    "Focus",
    "Total Hits",
    "Years since Publication",
    "Popularity Score",
    "Execution Score",
    "Plot Summary",
    "Strongest Point",
    "Weakest Point",
    "War solution",
]


def make_url_clickable(df: pd.DataFrame) -> pd.DataFrame:
    """Convert only the URL column into clickable links."""
    df = df.copy()

    if "URL" not in df.columns:
        return df

    def render_url(value: object) -> str:
        if pd.isna(value):
            return ""
        url = str(value).strip()
        if not url:
            return ""
        safe_url = html.escape(url, quote=True)
        return f'<a href="{safe_url}" target="_blank" rel="noopener noreferrer">{safe_url}</a>'

    df["URL"] = df["URL"].apply(render_url)
    return df


def reorder_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Keep known columns in the requested order, then append any unexpected extras."""
    existing = [col for col in COLUMN_ORDER if col in df.columns]
    extras = [col for col in df.columns if col not in existing]
    return df[existing + extras]


def build_select_options(df: pd.DataFrame, column_name: str) -> str:
    """Build HTML <option> tags from unique values in a column."""
    if column_name not in df.columns:
        return ""

    values = sorted(
        v for v in df[column_name].dropna().astype(str).str.strip().unique() if v
    )

    return "\n".join(
        f'<option value="{html.escape(v, quote=True)}">{html.escape(v)}</option>'
        for v in values
    )


def build_html_table(df: pd.DataFrame) -> str:
    return df.to_html(
        index=False,
        escape=False,  # needed so URL links stay clickable
        table_id="ficTable",
        classes="display nowrap compact",
        border=0,
    )


def build_full_page(table_html: str, title: str = "Summary Table", vikmione_type_options: str = "") -> str:
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
      font-size: 14px;
      font-weight: 300;
      font-family: "Segoe UI", Arial, sans-serif;
      color: #000000;
      vertical-align: top;
      white-space: nowrap;
    }}

    thead select {{
      width: 100%;
      min-width: 140px;
      height: 5.5em;
      font-size: 12px;
      font-family: "Segoe UI", Arial, sans-serif;
      box-sizing: border-box;
      margin-top: 4px;
    }}

    a {{
      text-decoration: none;
    }}

    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>

  <div class="table-container">
    {table_html}
  </div>

  <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
  <script src="https://cdn.datatables.net/1.13.8/js/jquery.dataTables.min.js"></script>

  <script>
  $(document).ready(function() {{
    const table = $('#ficTable');

    // Voeg een tweede rij toe aan de tabelheader
    table.find('thead').prepend(`
      <tr>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th>
          <select id="vikmione-type-filter" multiple>
            {vikmione_type_options}
          </select>
        </th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
        <th></th>
      </tr>
    `);

    const dataTable = table.DataTable({{
      paging: true,
      pageLength: -1,
      lengthMenu: [[-1, 10, 25, 50, 100], ["All", 10, 25, 50, 100]],
      searching: true,
      ordering: true,
      info: true,
      autoWidth: false,
      scrollX: true,
      orderCellsTop: true
    }});

    const vikmioneTypeColIdx = 5;

    $.fn.dataTable.ext.search.push(function(settings, data, dataIndex) {{
      if (settings.nTable.id !== 'ficTable') return true;

      const selected = $('#vikmione-type-filter').val();

      if (!selected || selected.length === 0) {{
        return true;
      }}

      const cellValue = (data[vikmioneTypeColIdx] || '').toString().trim();
      return selected.includes(cellValue);
    }});

    $('#vikmione-type-filter').on('change', function() {{
      dataTable.draw();
    }});
  }});
</script>
</body>
</html>
"""


def main() -> None:
    input_path = Path(INPUT_FILE)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Read table:
    df = pd.read_excel(input_path, sheet_name=SHEET_NAME)
    df = df.fillna("")

    # Remove benchmarks:
    df = df[df["Vikmione Type"] != "Not a Vikmione"]

    # Reorder columns:
    df = reorder_columns(df)
    df = make_url_clickable(df)

    # Rename columns:
    df = df.rename(columns={"Execution Score": "Quality(%)"})
    df = df.rename(columns={"Popularity Score": "Popularity"})
    df = df.rename(columns={"Years since Publication": "Years"})

    # Make columns filterable:
    vikmione_type_options = build_select_options(df, "Vikmione Type")

    table_html = build_html_table(df)
    page_html = build_full_page(table_html,
                                title="Summary Table",
                                vikmione_type_options=vikmione_type_options)

    Path(OUTPUT_FILE).write_text(page_html, encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
