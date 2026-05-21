import os
import requests

from core.base import setup_logging

log, sep = setup_logging(os.path.splitext(os.path.basename(__file__))[0])


def fetch_public_github_data(github_username):
    """Fetch public GitHub event data."""

    if not github_username:
        log.error("GitHub username not provided.")
        return None

    try:
        response = requests.get(
            f"https://api.github.com/users/{github_username}/events/public",
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()

        log.info(f"Fetched GitHub data for {github_username}")

        return data

    except requests.RequestException as e:
        log.error(f"GitHub request failed: {e}")
        return None
