# Chem Bench — Exam Prep Site

A single-file study site covering your uploaded course materials:

- **D-CHM 214** — Mineral Processing & Extractive Metallurgy
- **D-CHM 211** — Analytical Chemistry II
- **D-CHM 215** — Indigenous Food & Beverage Production
- **CHM 213** — Separation & Purification Techniques
- **Lab 1** — Minerals & Mineral Ores (practical)
- **CHM 212** — Characteristics of Ionic Compounds (assignment notes)

Each course has three tabs: **Notes** (organized key points), **Flashcards**
(flip cards you can mark "known" — saved in your browser), and a **Quiz**
(multiple choice with instant feedback and a saved best score).

## Run it locally
Just open `index.html` in any browser — no build step, no dependencies.

## Put it on GitHub Pages
1. Create a new GitHub repo (e.g. `chem-bench`).
2. Add `index.html` (and this README) to the repo and push:
   ```
   git init
   git add index.html README.md
   git commit -m "Add exam prep site"
   git branch -M main
   git remote add origin https://github.com/<your-username>/chem-bench.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Source → Deploy from a branch → main / (root)** → Save.
4. Your site will be live at `https://<your-username>.github.io/chem-bench/`.

## Notes
- Progress (mastered flashcards, best quiz scores) is stored in your
  browser's `localStorage`, per device/browser — it won't sync across
  devices unless you add a backend later.
- To add more courses later, open `index.html`, find the `COURSES` array
  near the top of the `<script>` block, and copy one course object as a
  template (accent color, notes, cards, quiz).
