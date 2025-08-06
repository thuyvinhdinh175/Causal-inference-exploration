"""
Functions for loading causal graphs from different sources.
"""

import pandas as pd
from dowhy.do_why import CausalModel
from typing import Optional, Dict, Any, Union


def create_model_from_gml_string(
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    gml_string: str,
    **kwargs: Any
) -> CausalModel:
    """
    Create a causal model from a GML string.
    
    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the variables
    treatment : str
        The name of the treatment variable
    outcome : str
        The name of the outcome variable
    gml_string : str
        The GML string representing the causal graph
    **kwargs : Any
        Additional keyword arguments to pass to CausalModel
        
    Returns
    -------
    CausalModel
        A DoWhy causal model
    """
    model = CausalModel(
        data=data,
        treatment=treatment,
        outcome=outcome,
        graph=gml_string,
        **kwargs
    )
    return model


def create_model_from_gml_file(
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    gml_file_path: str,
    **kwargs: Any
) -> CausalModel:
    """
    Create a causal model from a GML file.
    
    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the variables
    treatment : str
        The name of the treatment variable
    outcome : str
        The name of the outcome variable
    gml_file_path : str
        The path to the GML file
    **kwargs : Any
        Additional keyword arguments to pass to CausalModel
        
    Returns
    -------
    CausalModel
        A DoWhy causal model
    """
    model = CausalModel(
        data=data,
        treatment=treatment,
        outcome=outcome,
        graph=gml_file_path,
        **kwargs
    )
    return model


def create_model_from_common_causes(
    data: pd.DataFrame,
    treatment: str,
    outcome: str,
    common_causes: Union[str, list],
    **kwargs: Any
) -> CausalModel:
    """
    Create a causal model by specifying common causes.
    
    Parameters
    ----------
    data : pd.DataFrame
        The dataset containing the variables
    treatment : str
        The name of the treatment variable
    outcome : str
        The name of the outcome variable
    common_causes : Union[str, list]
        The common causes, either as a list or a string with variables separated by '+'
    **kwargs : Any
        Additional keyword arguments to pass to CausalModel
        
    Returns
    -------
    CausalModel
        A DoWhy causal model
    """
    if isinstance(common_causes, str):
        common_causes = common_causes.split('+')
    
    model = CausalModel(
        data=data,
        treatment=treatment,
        outcome=outcome,
        common_causes=common_causes,
        **kwargs
    )
    return model


def generate_simple_dataset(n_samples: int = 10) -> pd.DataFrame:
    """
    Generate a simple dataset for causal inference examples.
    
    Parameters
    ----------
    n_samples : int, default=10
        The number of samples to generate
        
    Returns
    -------
    pd.DataFrame
        A dataframe with three variables: Z (confounder), X (treatment), and Y (outcome)
    """
    import random
    
    z = list(range(n_samples))
    random.shuffle(z)
    
    df = pd.DataFrame({
        'Z': z,
        'X': range(0, n_samples),
        'Y': range(0, n_samples * 10, 10)
    })
    
    return df