[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/iByItA62)
# Module 4 — Core Skills Drill: Descriptive Analytics

Compute summary statistics, create distribution plots, and build a correlation heatmap from the provided sales dataset.

## Setup

```bash
pip install -r requirements.txt
```

## Tasks

Complete `drill_eda.py` with three functions:

1. `compute_summary(df)` — Summary statistics (count, mean, median, std, min, max) for numeric columns. Save to `output/summary.csv`.
2. `plot_distributions(df, columns, output_path)` — 2x2 subplot figure with histograms + KDE overlay. Save to `output/distributions.png`.
3. `plot_correlation(df, output_path)` — Annotated Pearson correlation heatmap. Save to `output/correlation.png`.

See the drills page for full specifications.

## Submit

1. Create branch `drill-4-descriptive-analytics`
2. Complete `drill_eda.py` so it generates all output files
3. Push and open a PR to `main`
4. Paste your PR URL into TalentLMS → Module 4 → Core Skills Drill

---

## License

This repository is provided for educational use only. See [LICENSE](LICENSE) for terms.

You may clone and modify this repository for personal learning and practice, and reference code you wrote here in your professional portfolio. Redistribution outside this course is not permitted.
