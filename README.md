# Legionella/Pseudomonas Biofilm Risk Modeling in Water Distribution Networks

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nikassh_bala/legionella-biofilm-msx-model/blob/main/Draft_MSX.ipynb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview
A multi-species reactive transport model of opportunistic pathogen (Legionella/Pseudomonas) dynamics in drinking water distribution networks, built on **EPANET-MSX** via **WNTR**. The model simulates suspended and biofilm-attached pathogen biomass under source-dependent organic matter loading and chlorine disinfection, then uses **global sensitivity analysis (Sobol)** to identify which kinetic parameters actually control pathogen persistence.

## Why this matters
Opportunistic pathogens like *Legionella pneumophila* proliferate in low-disinfectant, biofilm-rich zones of drinking water and premise plumbing systems — a documented cause of Legionnaires' disease outbreaks. Rather than assuming which factor (growth rate, nutrient availability, disinfectant residual) matters most, this project quantifies it directly from the model.

## Key finding
Global sensitivity analysis across 6 kinetic parameters (growth rate, substrate half-saturation, chlorine inactivation rate, wall deposition, detachment, yield) shows that **chlorine inactivation rate is the dominant control on final suspended biomass** (total-order Sobol index ≈ 0.72), far outweighing growth rate (≈ 0.13) or nutrient limitation (≈ 0.03). In this model, disinfection efficacy — not nutrient availability — is the primary lever on pathogen persistence.

*Caveat: sensitivity indices are from a modest sample size (112 model runs); the ranking is credible but confidence intervals are still wide — increasing sample size is noted as future work.*

## What's in this notebook
- **Baseline validation**: NOM-dependent, multi-source chlorine decay model (Lake and River sources with distinct organic matter and reaction rates) — confirms the reactive-transport pipeline is correct before adding biology
- **Pathogen biology model**: suspended (`Xfree`) and biofilm-attached (`Xwall`) species with coupled growth, chlorine-driven inactivation, wall deposition, and detachment kinetics, across both pipes and tanks
- **Global sensitivity analysis**: Sobol sampling and analysis (via SALib) across 6 kinetic parameters, run through 112 full EPANET-MSX simulations
- **Model export**: valid `.msx` reaction file with verified EPANET-MSX syntax

## Methods
- **WNTR** for network construction, hydraulics, and the Python interface to EPANET-MSX
- **EPANET-MSX** for multi-species bulk-phase and biofilm/wall reactive transport
- **SALib** (Sobol sampling/analysis) for global sensitivity analysis
- Supporting ML stack (scikit-learn, XGBoost, LightGBM, SHAP) reserved for downstream surrogate modeling

## How to run
Click "Open in Colab" above — the notebook mounts Google Drive and installs all dependencies (`wntr`, `numpy`, `pandas`, `matplotlib`, `shap`, `xgboost`, `lightgbm`, `scikit-learn`, `SALib`) in the first two cells. Run cells in order; the full sensitivity analysis batch (112 simulations) takes roughly 10 minutes.

## Status
Working end-to-end: validated baseline, full biology model, and sensitivity analysis all run without errors. Next steps: parameterize kinetics with literature-cited coefficients (current values are placeholders), and increase Sobol sample size to tighten confidence intervals on the sensitivity ranking.

## License
MIT
