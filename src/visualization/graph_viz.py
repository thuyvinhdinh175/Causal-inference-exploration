"""
Functions for visualizing causal graphs and treatment effects.
"""

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from typing import Optional, Dict, Any, Union
import os


def plot_causal_graph(
    graph: nx.DiGraph,
    figsize: tuple = (10, 6),
    node_size: int = 2000,
    node_color: str = 'lightblue',
    font_size: int = 12,
    save_path: Optional[str] = None
) -> None:
    """
    Plot a causal graph using NetworkX.
    
    Parameters
    ----------
    graph : nx.DiGraph
        The causal graph to plot
    figsize : tuple, default=(10, 6)
        The figure size
    node_size : int, default=2000
        The size of the nodes
    node_color : str, default='lightblue'
        The color of the nodes
    font_size : int, default=12
        The font size for node labels
    save_path : Optional[str], default=None
        If provided, save the figure to this path
    """
    plt.figure(figsize=figsize)
    pos = nx.spring_layout(graph, seed=42)  # For reproducible layout
    
    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_size=node_size,
        node_color=node_color,
        font_size=font_size,
        arrows=True,
        arrowsize=20,
        arrowstyle='->'
    )
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    
    plt.show()


def plot_treatment_outcome(
    treatment: pd.Series,
    outcome: pd.Series,
    time_var: Optional[pd.Series] = None,
    figsize: tuple = (10, 6),
    save_path: Optional[str] = None
) -> None:
    """
    Plot the relationship between treatment and outcome variables.
    
    Parameters
    ----------
    treatment : pd.Series
        The treatment variable
    outcome : pd.Series
        The outcome variable
    time_var : Optional[pd.Series], default=None
        Optional time variable for time-series data
    figsize : tuple, default=(10, 6)
        The figure size
    save_path : Optional[str], default=None
        If provided, save the figure to this path
    """
    plt.figure(figsize=figsize)
    
    if time_var is not None:
        # Time series plot
        plt.subplot(2, 1, 1)
        plt.plot(time_var, treatment, 'b-', label='Treatment')
        plt.xlabel('Time')
        plt.ylabel('Treatment')
        plt.legend()
        
        plt.subplot(2, 1, 2)
        plt.plot(time_var, outcome, 'r-', label='Outcome')
        plt.xlabel('Time')
        plt.ylabel('Outcome')
        plt.legend()
    else:
        # Scatter plot
        plt.scatter(treatment, outcome, alpha=0.6)
        plt.xlabel('Treatment')
        plt.ylabel('Outcome')
        plt.title('Treatment vs Outcome')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    
    plt.tight_layout()
    plt.show()


def plot_causal_effect(
    effect_estimates: Dict[str, float],
    ci_estimates: Optional[Dict[str, tuple]] = None,
    figsize: tuple = (10, 6),
    save_path: Optional[str] = None
) -> None:
    """
    Plot causal effect estimates with confidence intervals.
    
    Parameters
    ----------
    effect_estimates : Dict[str, float]
        Dictionary mapping method names to effect estimates
    ci_estimates : Optional[Dict[str, tuple]], default=None
        Dictionary mapping method names to confidence intervals (lower, upper)
    figsize : tuple, default=(10, 6)
        The figure size
    save_path : Optional[str], default=None
        If provided, save the figure to this path
    """
    plt.figure(figsize=figsize)
    
    methods = list(effect_estimates.keys())
    effects = list(effect_estimates.values())
    
    y_pos = range(len(methods))
    
    plt.barh(y_pos, effects, align='center', alpha=0.7)
    plt.yticks(y_pos, methods)
    
    if ci_estimates:
        for i, method in enumerate(methods):
            if method in ci_estimates:
                lower, upper = ci_estimates[method]
                plt.errorbar(
                    effects[i], i,
                    xerr=[[effects[i] - lower], [upper - effects[i]]],
                    fmt='o', color='black', capsize=5
                )
    
    plt.xlabel('Causal Effect Estimate')
    plt.title('Causal Effect Estimates by Method')
    
    if save_path:
        plt.savefig(save_path, bbox_inches='tight')
    
    plt.tight_layout()
    plt.show()