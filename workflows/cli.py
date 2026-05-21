# import argparse

# from .export import export_activity_json
# from .github import fetch_public_github_data
# from .summary import summarize_activity
import os
from core.base import setup_logging

log, sep = setup_logging(os.path.splitext(os.path.basename(__file__))[0])


def main():
    """Run the Repo Pulse CLI."""
    pass
