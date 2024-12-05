import numpy as np
import pandas as pd

def sort_filter_df(df, sort_by='padj', only_significant=True, pvalue_type='padj'):
    """
    Sorts and filters dataframes, especially for enricher analysis results.

    Parameters:
    - df: DataFrame to process.
    - sort_by: Criteria to sort the DataFrame. Options are 'padj', 'pval', 'percgenesinvolved', 'genesinvolved'.
    - only_significant: If True, filters rows where p-value type is <= 0.05.
    - pvalue_type: Type of p-value to consider. Options are 'padj' (Adjusted P-value) or 'pval' (P-value).

    Returns:
    - Processed DataFrame sorted and optionally filtered based on the given criteria.
    """
    # Map pvalue_type to DataFrame column name
    pvalue_col = 'Adjusted P-value' if pvalue_type == 'padj' else 'P-value' if pvalue_type == 'pval' else None
    if pvalue_col is None:
        raise ValueError("pvalue_type must be 'padj' or 'pval'.")

    # Filter by significance if requested
    if only_significant:
        df = df[df[pvalue_col] <= 0.05]

    # Add calculated columns
    df['-log(%s)' % pvalue_type] = -np.log(df[pvalue_col])
    df['Genes involved (%)'] = df['Overlap'].apply(lambda a: 100 * (int(a.split('/')[0]) / int(a.split('/')[1])))

    # Determine sorting
    sort_columns = {
        'percgenesinvolved': ('Genes involved (%)', False),
        'genesinvolved': ('genesinvolved', False),
        'padj': ('Adjusted P-value', True),
        'pval': ('P-value', True)
    }

    if sort_by in ['genesinvolved', 'percgenesinvolved']:
        df['genesinvolved'] = df['Overlap'].apply(lambda a: int(a.split('/')[0]))

    if sort_by in sort_columns:
        sort_col, ascending = sort_columns[sort_by]
        df = df.sort_values(by=sort_col, ascending=ascending)
    else:
        raise ValueError("Invalid sort_by value. Choose from 'padj', 'pval', 'percgenesinvolved', 'genesinvolved'.")

    return df
