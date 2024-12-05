import argparse
import pandas as pd
import os
import json
from enrichr_plot.plot import plot_enrichment_results

def main():
    """
    Main entry point for the enrichr_plot CLI.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Enrichr Plotting Tool")
    parser.add_argument("--modules", type=str, help="Path to the module data (JSON or CSV).", required=True)
    parser.add_argument("--expression", type=str, help="Path to the gene expression data (CSV).")
    parser.add_argument("--hubs", type=str, help="Path to the hub gene data (CSV).")
    parser.add_argument("--output", type=str, help="Output folder to save the plot.", required=True)
    parser.add_argument("--name", type=str, default="enrichment_plot", help="Name of the output file.")
    parser.add_argument("--sort", type=str, default="pvalue", help="Sort by column (e.g., 'pvalue', 'padj').")
    parser.add_argument("--terms", type=int, default=10, help="Number of terms to display in the plot.")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")

    args = parser.parse_args()

    # Load module data
    if args.modules.endswith(".json"):
        with open(args.modules) as f:
            dModules = json.load(f)
    elif args.modules.endswith(".csv"):
        dModules = pd.read_csv(args.modules).to_dict(orient="list")
    else:
        raise ValueError("Unsupported file format for modules. Use JSON or CSV.")

    # Load optional data
    df_in = pd.read_csv(args.expression) if args.expression else None
    dfHubs = pd.read_csv(args.hubs) if args.hubs else None

    # Ensure output folder exists
    os.makedirs(args.output, exist_ok=True)

    # Generate the plot
    plot_enrichment_results(
        dModules=dModules,
        df_in=df_in,
        dfHubs=dfHubs,
        name_out=args.name,
        outfolder=args.output,
        sort_by=args.sort,
        nterms=args.terms,
        verbose=int(args.verbose),
    )

    print(f"Plot saved to {os.path.join(args.output, args.name)}.pdf")
