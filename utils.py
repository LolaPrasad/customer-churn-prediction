"""
Shared helper functions used across all notebooks in this project.

Notebooks import this module with:
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
    from utils import *

Keeping repeated logic (chart saving/styling, confirmation messages,
file-loading with helpful errors) in one place avoids copy-pasting the
same code into every notebook.
"""

import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Consistent chart styling used across every notebook
DEFAULT_FIGSIZE = (12, 6)
DEFAULT_DPI = 150
SOURCE_TEXT = "Source: IBM Telco Customer Churn Dataset"


def set_style():
    """Apply the consistent seaborn style used across all notebooks."""
    sns.set_style("whitegrid")
    plt.rcParams["figure.figsize"] = DEFAULT_FIGSIZE


def add_source_annotation(fig):
    """Add the dataset source credit to the bottom of a figure."""
    fig.text(0.99, 0.01, SOURCE_TEXT, ha="right", va="bottom",
              fontsize=8, color="gray", style="italic")


def format_size(num_bytes):
    """Convert a byte count into a human-readable string (KB/MB)."""
    for unit in ["B", "KB", "MB", "GB"]:
        if num_bytes < 1024:
            return f"{num_bytes:.1f}{unit}"
        num_bytes /= 1024
    return f"{num_bytes:.1f}TB"


def save_chart(fig, filepath):
    """Apply tight_layout, add source annotation, save at DEFAULT_DPI, and confirm."""
    add_source_annotation(fig)
    fig.tight_layout()
    fig.savefig(filepath, dpi=DEFAULT_DPI, bbox_inches="tight")
    size = format_size(os.path.getsize(filepath))
    print(f"✅ Saved: {filepath} ({size})")
    plt.close(fig)


def save_dataframe(df, filepath, index=False):
    """Save a DataFrame to CSV and print a confirmation message."""
    df.to_csv(filepath, index=index)
    size = format_size(os.path.getsize(filepath))
    print(f"✅ Saved: {filepath} ({size}) — {df.shape[0]} rows, {df.shape[1]} columns")


def save_joblib_object(obj, filepath):
    """Save any object with joblib and print a confirmation message."""
    import joblib
    joblib.dump(obj, filepath)
    size = format_size(os.path.getsize(filepath))
    print(f"✅ Saved: {filepath} ({size})")


def load_csv_safely(filepath, required_notebook):
    """
    Load a CSV and raise a helpful error if it is missing, telling the
    user exactly which notebook to run first to generate it.
    """
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        print(f"   Please run '{required_notebook}' first to generate this file.")
        raise


def load_joblib_safely(filepath, required_notebook):
    """Load a joblib object and raise a helpful error if it is missing."""
    import joblib
    try:
        return joblib.load(filepath)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        print(f"   Please run '{required_notebook}' first to generate this file.")
        raise


def project_path(*parts):
    """Build an absolute path from the project root, regardless of which
    notebook (running from notebooks/) calls it."""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    return os.path.join(project_root, *parts)


def annotate_vertical_bars(ax, fmt="{:.1f}%"):
    """Annotate each bar in a vertical bar chart with its value above the bar."""
    for patch in ax.patches:
        height = patch.get_height()
        x = patch.get_x() + patch.get_width() / 2
        ax.annotate(fmt.format(height), (x, height), ha="center", va="bottom", fontsize=9)


def annotate_horizontal_bars(ax, fmt="{:.1f}%"):
    """Annotate each bar in a horizontal bar chart with its value to the right of the bar."""
    for patch in ax.patches:
        width = patch.get_width()
        y = patch.get_y() + patch.get_height() / 2
        ax.annotate(fmt.format(width), (width, y), ha="left", va="center", fontsize=9)


def churn_rate_by_group(df, group_col, churn_col="Churn"):
    """Return a DataFrame of churn rate (%) by a categorical grouping column."""
    rates = df.groupby(group_col)[churn_col].mean().mul(100).round(2)
    return rates.sort_values(ascending=False)
