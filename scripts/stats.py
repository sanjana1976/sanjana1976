"""Render a pastel GitHub stats card (numbers + top languages) to an SVG.

Runs in the snake workflow; needs GITHUB_TOKEN and a username argument.
"""
import json
import os
import sys
import urllib.request

PALETTE = ["#ff8fb8", "#b9a2ff", "#ffad85", "#7fdcc0", "#ffe08a", "#8ccfff"]

QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      contributionCalendar { totalContributions }
    }
    repositories(ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC, first: 100) {
      totalCount
      nodes {
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""


def fetch(login, token):
    body = json.dumps({"query": QUERY, "variables": {"login": login}}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=body,
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["data"]["user"]


# Markup and notebooks aren't what I write day to day
SKIP = {"HTML", "CSS", "SCSS", "Jupyter Notebook", "Makefile", "Dockerfile", "Shell", "Batchfile", "PowerShell"}


def top_languages(user, n=6):
    # every repo gets one equal vote split by its byte shares, so one repo with
    # committed node_modules can't drown out everything else
    totals = {}
    for repo in user["repositories"]["nodes"]:
        edges = [e for e in repo["languages"]["edges"] if e["node"]["name"] not in SKIP]
        repo_total = sum(e["size"] for e in edges)
        for edge in edges:
            name = edge["node"]["name"]
            totals[name] = totals.get(name, 0) + edge["size"] / repo_total
    ranked = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)[:n]
    total = sum(size for _, size in ranked) or 1
    return [(name, size / total) for name, size in ranked]


def render(user):
    cc = user["contributionsCollection"]
    stats = [
        ("contributions (1y)", cc["contributionCalendar"]["totalContributions"]),
        ("commits (1y)", cc["totalCommitContributions"]),
        ("pull requests (1y)", cc["totalPullRequestContributions"]),
        ("public repos", user["repositories"]["totalCount"]),
    ]
    langs = top_languages(user)

    rows = []
    for i, (label, value) in enumerate(stats):
        y = 78 + i * 30
        color = PALETTE[i]
        rows.append(
            f'<g class="row" style="animation-delay:{0.15 * i:.2f}s">'
            f'<circle cx="32" cy="{y - 5}" r="5" fill="{color}"/>'
            f'<text class="lbl" x="46" y="{y}">{label}</text>'
            f'<text class="num" x="232" y="{y}" text-anchor="end" fill="{color}">{value:,}</text></g>'
        )

    bar, legend, x = [], [], 268.0
    width = 200
    for i, (name, share) in enumerate(langs):
        w = share * width
        color = PALETTE[i % len(PALETTE)]
        bar.append(f'<rect x="{x:.1f}" y="66" width="{w:.1f}" height="10" fill="{color}"/>')
        x += w
        lx = 268 + (i % 2) * 104
        ly = 104 + (i // 2) * 26
        legend.append(
            f'<circle cx="{lx + 5}" cy="{ly - 4}" r="4.5" fill="{color}"/>'
            f'<text class="lang" x="{lx + 15}" y="{ly}">{name} <tspan class="pct">{share * 100:.0f}%</tspan></text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="495" height="195" viewBox="0 0 495 195" role="img" aria-label="GitHub stats">
  <defs>
    <clipPath id="bar"><rect x="268" y="66" width="{width}" height="10" rx="5"/></clipPath>
  </defs>
  <style>
    .title {{ font: 700 16px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: #ff8fb8; }}
    .sub {{ font: 600 11px ui-monospace, SFMono-Regular, Consolas, Menlo, monospace; fill: #b9a2ff; letter-spacing: .12em; }}
    .lbl {{ font: 500 13.5px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: #d9c7cf; }}
    .num {{ font: 700 15px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; }}
    .lang {{ font: 500 12.5px -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; fill: #d9c7cf; }}
    .pct {{ fill: #8f7b85; }}
    .row {{ animation: in .5s ease-out backwards; }}
    @keyframes in {{ from {{ opacity: 0; transform: translateX(-8px); }} }}
    .grow {{ transform-box: fill-box; transform-origin: left; animation: grow 1.2s cubic-bezier(.2,.7,.2,1) backwards; }}
    @keyframes grow {{ from {{ transform: scaleX(0); }} }}
  </style>
  <rect x="1" y="1" width="493" height="193" rx="16" fill="#141016" stroke="#2e2429" stroke-width="2"/>
  <text class="title" x="26" y="38">&#10047; Sanjana's GitHub stats</text>
  {''.join(rows)}
  <line x1="250" y1="58" x2="250" y2="172" stroke="#3a2a32"/>
  <text class="sub" x="268" y="54">TOP LANGUAGES</text>
  <g clip-path="url(#bar)"><g class="grow">{''.join(bar)}</g></g>
  {''.join(legend)}
</svg>
"""


if __name__ == "__main__":
    login, out = sys.argv[1], sys.argv[2]
    svg = render(fetch(login, os.environ["GITHUB_TOKEN"]))
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
