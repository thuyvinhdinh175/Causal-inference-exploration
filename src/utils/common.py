"""
Common utility functions for causal inference projects.
"""

import warnings
import logging
import io
import contextlib
import sys

# Define a context manager to suppress stdout and stderr
@contextlib.contextmanager
def suppress_output():
    """
    Context manager to suppress stdout and stderr output.
    
    This is useful for suppressing unwanted output from libraries during imports.
    """
    # Save the original stdout and stderr
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    # Use StringIO to trap the output
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()
    try:
        yield  # Execute the code block inside the with statement
    finally:
        # Restore the original stdout and stderr
        sys.stdout = old_stdout
        sys.stderr = old_stderr

def setup_environment(suppress_warnings=True, log_level=logging.ERROR):
    """
    Set up the environment for causal inference analysis.
    
    Parameters
    ----------
    suppress_warnings : bool, default=True
        Whether to suppress warnings
    log_level : int, default=logging.ERROR
        The logging level to set
    """
    if suppress_warnings:
        warnings.filterwarnings('ignore')
    
    logging.getLogger().setLevel(log_level)