## Utility Functions for Data Analysis and Visualization

import matplotlib.pyplot as plt
import seaborn as sns


def setup_plot_theme():
  """Applies a consistent styling theme to all Matplotlib/Seaborn plots."""
  sns.set_theme(style="whitegrid")
  plt.rcParams.update({
      "figure.autolayout": True,
      "figure.dpi": 300,
  })