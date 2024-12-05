"""
enrichr_plot: A Python package for enrichment analysis visualization and filtering.

Modules:
- utils: Contains functions for sorting and filtering DataFrames.
- plot: Provides visualization functions for enrichment results.

Public API:
- sort_filter_df: Sorts and filters DataFrames for enrichment analysis.
- plot_enrichment_results: Generates bar and line plots for enrichment results.
"""

# Import core functionality
from .utils import sort_filter_df
from .plot import plot_enrichment_results

__version__ = "1.0.0"
__author__ = "Christoffer Frisk"
__license__ = "MIT"
__description__ = "A tool for enrichment analysis visualization and filtering."


__all__ = [
    "sort_filter_df",
    "plot_enrichment_results",
]
