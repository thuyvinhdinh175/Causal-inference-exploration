# Causal Inference Basics

This document provides an overview of the basic concepts in causal inference.

## Causal Graphs

Causal graphs, also known as directed acyclic graphs (DAGs), are graphical models that represent causal relationships between variables. In a causal graph:

- Nodes represent variables
- Directed edges (arrows) represent causal relationships
- The absence of an edge represents the absence of a direct causal relationship

## The Four Steps of Causal Inference

DoWhy structures causal inference into four steps:

1. **Model**: Express the causal question using a formal causal graph
2. **Identify**: Determine if the causal effect can be estimated from observed data
3. **Estimate**: Use statistical methods to estimate the causal effect
4. **Refute**: Test the robustness of the estimate through sensitivity and robustness checks

## Common Causal Effects

- **Average Treatment Effect (ATE)**: The average effect of a treatment across the entire population
- **Average Treatment Effect on the Treated (ATT)**: The average effect of a treatment for those who received the treatment
- **Conditional Average Treatment Effect (CATE)**: The average treatment effect conditional on specific covariates

## Common Estimation Methods

- **Propensity Score Methods**:
  - Matching: Match treated and control units with similar propensity scores
  - Stratification: Group units into strata based on propensity scores
  - Weighting: Weight observations by the inverse of their propensity score
  
- **Instrumental Variables**: Use an instrument that affects the treatment but not the outcome directly
  
- **Regression Discontinuity**: Exploit a threshold in a running variable that determines treatment assignment

## Causal Discovery

Causal discovery algorithms attempt to learn causal structures from data. Common approaches include:

- **Constraint-based methods** (e.g., PC algorithm): Use conditional independence tests
- **Score-based methods**: Optimize a score function over possible graph structures
- **Functional causal models**: Exploit asymmetries in the data generating process

## References

1. Pearl, J. (2009). Causality: Models, Reasoning, and Inference. Cambridge University Press.
2. Morgan, S. L., & Winship, C. (2015). Counterfactuals and Causal Inference. Cambridge University Press.
3. Peters, J., Janzing, D., & Schölkopf, B. (2017). Elements of Causal Inference. MIT Press.