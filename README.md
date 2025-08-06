# Causal Inference Exploration using DoWhy and CDT

This repository contains my exploration of causal inference using the DoWhy library and Causal Discovery Toolbox (CDT). DoWhy is a Python library that aims to spark causal thinking and analysis by combining causal inference and machine learning techniques, while CDT provides tools for automated causal discovery.

## Contents

- Jupyter notebooks demonstrating various causal inference techniques
- Implementation of propensity score stratification for estimating causal effects
- Analysis of treatment effects with detailed comments explaining the methodology
- Automated causal discovery using CDT

## Key Features

- Structured approach to causal inference using the four-step process: model, identify, estimate, and refute
- Implementation of backdoor adjustment via propensity score stratification
- Automated causal relationship discovery using CDT
- Detailed comments explaining each step of the causal inference process
- Visualization of causal graphs and treatment effects

## Project Structure

```
causal-inference-exploration/
├── data/                      # Data files and datasets
│   ├── raw/                   # Original, immutable data
│   └── processed/             # Cleaned, transformed data
├── src/                       # Source code
│   ├── discovery/             # Causal discovery algorithms
│   ├── inference/             # Causal inference methods
│   ├── utils/                 # Utility functions
│   └── visualization/         # Plotting and visualization
├── notebooks/                 # Jupyter notebooks for examples and tutorials
│   ├── discovery/             # Causal discovery examples
│   ├── inference/             # Causal inference examples
│   └── case_studies/          # Real-world applications
├── examples/                  # Example Python scripts and data
│   └── graphs/                # Example graph files
├── docs/                      # Documentation
│   ├── theory/                # Theoretical background
│   └── images/                # Images and diagrams
├── environment.yml            # Conda environment file
├── requirements.txt           # Pip requirements file
└── README.md                  # Project overview
```

## Getting Started

To use this repository:

1. Clone the repository
2. Install R and required R packages:
   ```R
   install.packages(c("pcalg", "bnlearn", "glmnet"))
   ```
   <!-- Note: kpcalg is excluded due to compatibility issues -->
3. Install Python dependencies: `pip install -r requirements.txt`
4. Explore the Jupyter notebooks in the `notebooks` directory
5. Run the example scripts in the `examples` directory: `python examples/basic_example.py`

## Dependencies

### Python Libraries
- DoWhy
- CDT (Causal Discovery Toolbox)
- NumPy
- Pandas
- Matplotlib
- Jupyter
- NetworkX
- Scikit-learn

### R Libraries
- pcalg
- bnlearn
- glmnet

## License

This project is licensed under the MIT License - see the LICENSE file for details.# causal-inference-exploration
