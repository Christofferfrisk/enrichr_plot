import pandas as pd
from enrichr_plot.utils import sort_filter_df

# Example DataFrame
data = {
    "Adjusted P-value": [0.01, 0.2, 0.03, 0.04],
    "P-value": [0.005, 0.1, 0.015, 0.02],
    "Overlap": ["5/100", "10/200", "8/150", "15/300"]
}
df = pd.DataFrame(data)

# Apply the function
processed_df = sort_filter_df(df, sort_by='padj', only_significant=True)
print(processed_df)
