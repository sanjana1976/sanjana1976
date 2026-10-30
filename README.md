<a href="https://sanjana1976.github.io/personal_web/">
  <img src="assets/banner.svg" alt="Sanjana Kalarickal, backend engineer focused on speed" width="100%">
</a>

<p align="center">
  <a href="https://sanjana1976.github.io/personal_web/"><img src="https://img.shields.io/badge/website-sanjana1976.github.io-ff8fb8?style=flat-square&labelColor=1a1418" alt="Website"></a>
  <a href="https://www.linkedin.com/in/s1976"><img src="https://img.shields.io/badge/LinkedIn-s1976-ff8fb8?style=flat-square&logo=linkedin&logoColor=white&labelColor=1a1418" alt="LinkedIn"></a>
  <a href="mailto:skalarickal@ucsd.edu"><img src="https://img.shields.io/badge/email-skalarickal@ucsd.edu-ff8fb8?style=flat-square&logo=gmail&logoColor=white&labelColor=1a1418" alt="Email"></a>
  <a href="https://sanjana1976.github.io/personal_web/Sanjana_Kalarickal_Resume.pdf"><img src="https://img.shields.io/badge/r%C3%A9sum%C3%A9-PDF-ff8fb8?style=flat-square&logo=readthedocs&logoColor=white&labelColor=1a1418" alt="Résumé"></a>
</p>

<p align="center">
  <img src="assets/whoami.svg" alt="curl localhost:8080/whoami returns a JSON profile" width="760">
</p>

### ⚡ how I build

I work on backends where latency is a feature. In practice that means profiling before optimizing, keeping hot paths warm, fanning independent work out in parallel, and making every write idempotent so a retry is boring instead of a double-charge.

### 🌸 featured work

<p align="center">
  <a href="https://github.com/sanjana1976/LitAgent_Phase2"><img src="assets/card-litsynth.svg" alt="LitSynth" width="49%"></a>
  <a href="https://github.com/sanjana1976/PR_Check"><img src="assets/card-downstream.svg" alt="Downstream" width="49%"></a>
  <a href="https://github.com/sanjana1976/menu-translator"><img src="assets/card-menubuddy.svg" alt="Menu Buddy" width="49%"></a>
  <a href="https://github.com/sanjana1976/RAG-pipeline"><img src="assets/card-docsearch.svg" alt="Smart Document Search" width="49%"></a>
</p>

<details>
<summary><b>🔍 How they work under the hood</b> <sub>(click to expand)</sub></summary>
<br>

**[LitSynth](https://github.com/sanjana1976/LitAgent_Phase2)**: an autonomous research agent. It breaks a question into sub-queries, searches arXiv, Semantic Scholar, DBLP and Crossref in parallel, extracts each paper's claims and flags where sources contradict each other. It runs as a checkpointed LangGraph state machine that fans retrieval, extraction and contradiction checks across workers (6.5 min → ~70 s). A writer/critic loop retracts any claim that fails a citation whitelist.

**[Downstream](https://github.com/sanjana1976/PR_Check)**: builds a monorepo's module dependency graph and walks reverse import edges to find everything a PR can break and who should review it. It parses with oxc-parser and resolves imports itself (tsconfig paths, workspaces, package exports) with zero I/O in the core. Edges are stored in compact CSR arrays, and 12 golden fixtures pin it to the TypeScript compiler's own resolver.

**[Menu Buddy](https://github.com/sanjana1976/menu-translator)**: React + Express. Menu photos go through a vision-model extraction pipeline with a strict JSON schema. Results are cached by image hash, so a repeat scan is instant and free. The API layer adds request IDs, upload validation, timeouts and rate limiting.

**[Smart Document Search](https://github.com/sanjana1976/RAG-pipeline)**: transcripts are chunked, embedded with gte-small and shortlisted from a FAISS index, then re-ranked with ColBERT-style token-level scoring on BERT. That catches matches pooled embeddings miss.

</details>

### 🧭 where I've shipped

| | what I built | the number |
|:--|:--|:--|
| ♟️ **Y STEM and Chess**<br><sub>SWE Intern · Jun 2026 – now</sub> | Real-time puzzle trainer on Socket.io, where the server pushes puzzles to a whole lesson and an LLM tutor reads the live board state. Also ported video sessions from Angular to React on Agora. | signup coverage **10% → 87%** |
| 🎙️ **CSES Innovate · AIDE**<br><sub>Co-Team Lead · Aug 2025 – now</sub> | Voice-to-code for VS Code: a speech → intent → codegen pipeline of three fine-tuned Hugging Face models served locally behind FastAPI, with warm inference on CPU only. | **3–5 min → 2–5 s**, 98.8% accuracy |
| 💳 **Brainworks Academy**<br><sub>Full-Stack Intern · Mar – May 2026</sub> | Stripe checkout with idempotency keys, and async webhooks with timeouts and de-duplication, so late or repeated events can't corrupt orders. | 55 live orders, **0 double-charges** |

### 🧰 toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,java,ts,js,nodejs,express,fastapi,postgres,supabase,mongodb,sqlite,react&perline=12" alt="Python, Java, TypeScript, JavaScript, Node.js, Express, FastAPI, PostgreSQL, Supabase, MongoDB, SQLite, React"><br>
  <img src="https://skillicons.dev/icons?i=tailwind,electron,aws,vercel,docker,githubactions,git,pytorch&perline=12" alt="Tailwind, Electron, AWS, Vercel, Docker, GitHub Actions, Git, PyTorch">
</p>
<p align="center"><sub>plus LangGraph · Hugging Face · FAISS · Socket.io · Stripe · pytest · Vitest · JUnit</sub></p>

### 🐍 my commits, eaten daily

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/snake-light.svg">
  <img alt="A snake eating my contribution graph" src="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/snake-light.svg">
</picture>

<br>

<p align="center">
  <sub>ask me about: shaving p99s · why your webhook fired twice · fan-out vs. one big prompt</sub><br><br>
  <img src="https://komarev.com/ghpvc/?username=sanjana1976&label=visitors&color=ff8fb8&style=flat-square" alt="profile views">
</p>
