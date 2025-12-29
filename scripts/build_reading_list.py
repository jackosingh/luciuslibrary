import csv
import html
from collections import defaultdict

groups = defaultdict(list)

with open("data/reading.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        category = r.get("Category", "Uncategorized").strip() or "Uncategorized"
        groups[category].append(r)

out = []

for category in sorted(groups.keys()):
    out.append(f"<h2>{html.escape(category)}</h2>")
    out.append("<ul>")

    for r in reversed(groups[category]):
        title = html.escape(r["Title"])
        url = html.escape(r["URL"])
        desc = html.escape(r["Description"])

        out.append(f"""
        <li>
          <a href="{url}" target="_blank">{title}</a><br>
          <small>{desc}</small>
        </li>
        """)

    out.append("</ul>")

with open("nav/reading-list.html", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
