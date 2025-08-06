"""
Causal inference methods and utilities.
"""

from .estimation_methods import (
    regression,
    stratification,
    matching,
    weighting,
    instrumental_variable,
    regression_discontinuity
)

__all__ = [
    'regression',
    'stratification',
    'matching',
    'weighting',
    'instrumental_variable',
    'regression_discontinuity'
]