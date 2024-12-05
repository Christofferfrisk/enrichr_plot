import matplotlib.pyplot as plt
import seaborn as sns
import os
import pandas as pd

from enrichr_plot.utils import sort_filter_df  # Import your filtering function

def plot_enrichment_results(dModules, df_in, dfHubs, **kwargs):
    """
    Plots enrichment analysis results with bar and optional box plots.

    Parameters:
    - dModules (dict): Dictionary containing enrichment results per module.
    - df_in (pd.DataFrame): DataFrame with input data for box plots.
    - dfHubs (pd.DataFrame): DataFrame with hub gene information.
    - kwargs: Additional parameters (see detailed function signature for options).
    """
    # Default parameters
    params = {
        'df_de': None,
        'filter_go': True,
        'convertname': None,
        'ordered': None,
        'verbose': 0,
        'nHubGenes': None,
        'name_out': None,
        'outfolder': None,
        'title': None,
        'pvalue_type': 'padj',
        'figsize': (8, 3),
        'color': None,
        'nterms': 10,
        'fontsize': 10,
        'exclude_go': False,
        'sort_by': 'pvalue',
    }
    params.update(kwargs)  # Update defaults with user-specified values

    # Filter and sort modules
    significant_modules = []
    for module, df in dModules.items():
        df_filtered = sort_filter_df(df, sort_by=params['sort_by'], only_significant=True, pvalue_type=params['pvalue_type'])
        if not df_filtered.empty:
            significant_modules.append(module)

    # Create subplots
    nrows = len(significant_modules)
    fig, axs = plt.subplots(nrows=nrows, ncols=2 if df_in is not None else 1, figsize=params['figsize'], squeeze=False)

    for i, module in enumerate(significant_modules):
        df = sort_filter_df(dModules[module], sort_by=params['sort_by'], only_significant=True, pvalue_type=params['pvalue_type'])
        if df.empty:
            continue

        # Plot bar chart
        sns.barplot(x='Genes involved (%)', y='Term', data=df.head(params['nterms']), ax=axs[i, 0], color=params['color'])
        axs[i, 0].set_title(params['convertname'].get(module, module) if params['convertname'] else module)
        axs[i, 0].set_xlabel('Genes involved (%)')
        axs[i, 0].tick_params(labelsize=params['fontsize'])

        # Plot box plot (if df_in is provided)
        if df_in is not None:
            hub_genes = dfHubs[module]
            melted_df = pd.melt(df_in.loc[hub_genes].T, var_name="Gene", value_name="Expression")
            sns.boxplot(x='Gene', y='Expression', data=melted_df, ax=axs[i, 1])

    # Finalize layout
    fig.tight_layout()
    if params['name_out'] and params['outfolder']:
        os.makedirs(params['outfolder'], exist_ok=True)
        fig.savefig(os.path.join(params['outfolder'], f"{params['name_out']}.pdf"))
    return fig
