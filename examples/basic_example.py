"""
A basic example demonstrating the usage of the causal inference modules.
"""

import sys
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import setup_environment
from src.discovery import generate_simple_dataset, create_model_from_gml_string
from src.visualization import plot_causal_graph, plot_treatment_outcome, plot_causal_effect
from src.inference import regression, stratification, matching, weighting

# Set up the environment
setup_environment()

# Generate a simple dataset
df = generate_simple_dataset(n_samples=100)
print("Generated dataset:")
print(df.head())

# Create a causal model using a GML string
gml_string = """graph[directed 1 
                node[id "Z" label "Z"]  
                node[id "X" label "X"]
                node[id "Y" label "Y"]      
                edge[source "Z" target "X"]    
                edge[source "Z" target "Y"]     
                edge[source "X" target "Y"]]"""

model = create_model_from_gml_string(
    data=df,
    treatment='X',
    outcome='Y',
    gml_string=gml_string
)

# View the model
print("\nCausal Model:")
model.view_model()

# Convert the model's graph to a NetworkX graph for visualization
G = nx.DiGraph()
G.add_node("Z")
G.add_node("X")
G.add_node("Y")
G.add_edge("Z", "X")
G.add_edge("Z", "Y")
G.add_edge("X", "Y")

# Visualize the causal graph
print("\nVisualizing the causal graph:")
plot_causal_graph(G)

# Visualize the relationship between treatment and outcome
print("\nVisualizing treatment-outcome relationship:")
plot_treatment_outcome(df['X'], df['Y'])

# Identify the causal effect
identified_estimand = model.identify_effect()
print("\nIdentified Estimand:")
print(identified_estimand)

# Estimate the causal effect using different methods
print("\nEstimating causal effects:")

# Using regression
regression_estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.linear_regression"
)
print("Regression estimate:", regression_estimate.value)

# Using propensity score stratification
stratification_estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.propensity_score_stratification"
)
print("Stratification estimate:", stratification_estimate.value)

# Using propensity score matching
matching_estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.propensity_score_matching"
)
print("Matching estimate:", matching_estimate.value)

# Using inverse propensity weighting
weighting_estimate = model.estimate_effect(
    identified_estimand,
    method_name="backdoor.propensity_score_weighting"
)
print("Weighting estimate:", weighting_estimate.value)

# Plot the causal effect estimates
effect_estimates = {
    "Regression": regression_estimate.value,
    "Stratification": stratification_estimate.value,
    "Matching": matching_estimate.value,
    "Weighting": weighting_estimate.value
}

print("\nPlotting causal effect estimates:")
plot_causal_effect(effect_estimates)

# Refute the estimates
print("\nRefuting estimates:")
refutation = model.refute_estimate(
    identified_estimand, 
    regression_estimate,
    method_name="random_common_cause"
)
print(refutation)

print("\nDone!")