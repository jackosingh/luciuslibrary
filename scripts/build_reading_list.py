import csv

rows = []
with open("data/reading.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

html = "<ul>\n"
for r in reversed(rows):
    html += f"""
    <li>
      <a href="{r['URL']}" target="_blank">{r['Title']}</a><br>
      <small>{r['Description']}</small>
    </li>
    """
html += "</ul>"

with open("reading.html", "w", encoding="utf-8") as f:
    f.write(html)
