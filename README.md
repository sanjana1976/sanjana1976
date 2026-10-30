<a href="https://sanjana1976.github.io/personal_web/">
  <img src="assets/banner.svg" alt="Backend Developer, Sanjana Kalarickal" width="100%">
</a>

<p align="center">
  <a href="https://sanjana1976.github.io/personal_web/"><img src="assets/btn-website.svg" alt="Website" height="44"></a>
  <a href="https://www.linkedin.com/in/s1976"><img src="assets/btn-linkedin.svg" alt="LinkedIn" height="44"></a>
  <a href="https://sanjana1976.github.io/personal_web/Sanjana_Kalarickal_Resume.pdf"><img src="assets/btn-resume.svg" alt="Résumé" height="44"></a>
  <a href="mailto:skalarickal@ucsd.edu"><img src="assets/btn-email.svg" alt="Email me" height="44"></a>
</p>

### About me 🌷

- Computer Science at **[UC San Diego](https://ucsd.edu)**, graduating Dec 2027
- Specializing in backend systems, with a research interest in **tail latency across multi-tier systems**, especially pipelines where AI models and agents sit on the critical path
- Currently:
  - **AIDE** at CSES Innovate: voice-to-code for VS Code (**3–5 min → 2–5 s**, CPU only); now writing the research paper and running the study
  - Prev. full-stack SWE at **Y STEM and Chess**, summer '26

---

### Things I've built 🛠️

<p align="center">
  <a href="https://github.com/sanjana1976/LitAgent_Phase2"><img src="assets/card-litsynth.svg" alt="LitSynth" width="49%"></a>
  <a href="https://github.com/sanjana1976/PR_Check"><img src="assets/card-downstream.svg" alt="Downstream" width="49%"></a>
  <a href="https://github.com/sanjana1976/menu-translator"><img src="assets/card-menubuddy.svg" alt="Menu Buddy" width="49%"></a>
  <a href="https://github.com/sanjana1976/RAG-pipeline"><img src="assets/card-docsearch.svg" alt="Smart Document Search" width="49%"></a>
</p>

<details>
<summary>🔍 <b>How they work under the hood</b></summary>
<br>

**[LitSynth](https://github.com/sanjana1976/LitAgent_Phase2)**: an autonomous research agent. It breaks a question into sub-queries, searches arXiv, Semantic Scholar, DBLP and Crossref in parallel, extracts each paper's claims and flags where sources contradict each other. It runs as a checkpointed LangGraph state machine that fans retrieval, extraction and contradiction checks across workers (6.5 min → ~70 s). A writer/critic loop retracts any claim that fails a citation whitelist.

**[Downstream](https://github.com/sanjana1976/PR_Check)**: builds a monorepo's module dependency graph and walks reverse import edges to find everything a PR can break and who should review it. It parses with oxc-parser and resolves imports itself (tsconfig paths, workspaces, package exports) with zero I/O in the core. Edges are stored in compact CSR arrays, and 12 golden fixtures pin it to the TypeScript compiler's own resolver.

**[Menu Buddy](https://github.com/sanjana1976/menu-translator)**: React + Express. Menu photos go through a vision-model extraction pipeline with a strict JSON schema. Results are cached by image hash, so a repeat scan is instant and free. The API layer adds request IDs, upload validation, timeouts and rate limiting.

**[Smart Document Search](https://github.com/sanjana1976/RAG-pipeline)**: transcripts are chunked, embedded with gte-small and shortlisted from a FAISS index, then re-ranked with ColBERT-style token-level scoring on BERT. That catches matches pooled embeddings miss.

</details>

---

### GitHub stats 📊

<p align="center">
  <img src="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/stats.svg" alt="GitHub stats and top languages" width="49%">
  <img src="https://streak-stats.demolab.com?user=sanjana1976&background=141016&border=ff8fb8&stroke=3a2a32&ring=ff8fb8&fire=ffad85&currStreakNum=fbf4f7&sideNums=fbf4f7&currStreakLabel=ff8fb8&sideLabels=b9a2ff&dates=8f7b85&border_radius=16" alt="Contribution streak" width="49%">
</p>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/snake-light.svg">
  <img alt="A snake eating my contribution graph" src="https://raw.githubusercontent.com/sanjana1976/sanjana1976/output/snake-light.svg">
</picture>

<details>
<summary>🧰 <b>Full toolbox</b></summary>
<br>
<p align="center">
  <img src="https://skillicons.dev/icons?i=py,java,ts,js,nodejs,express,fastapi,postgres,supabase,mongodb,sqlite,react&perline=12" alt="Python, Java, TypeScript, JavaScript, Node.js, Express, FastAPI, PostgreSQL, Supabase, MongoDB, SQLite, React"><br>
  <img src="https://skillicons.dev/icons?i=tailwind,electron,aws,vercel,docker,githubactions,git,pytorch&perline=12" alt="Tailwind, Electron, AWS, Vercel, Docker, GitHub Actions, Git, PyTorch">
</p>
<p align="center"><sub>plus LangGraph · Hugging Face · FAISS · Socket.io · Stripe · pytest · Vitest · JUnit</sub></p>
</details>

<p align="center">
  <sub>ask me about: shaving p99s · why your webhook fired twice · fan-out vs. one big prompt</sub>
</p>

<details>
<summary><sub><code>$ curl whoami</code></sub></summary>
<br>
<p align="center"><img src="assets/whoami.svg" alt="curl localhost:8080/whoami returns a JSON profile" width="720"></p>
</details>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=sanjana1976&label=visitors&color=ff8fb8&style=flat-square" alt="profile views">
</p>
