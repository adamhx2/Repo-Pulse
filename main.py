import os
from workflows.cli import main as run
from workflows.github import fetch_public_github_data
from core.base import setup_logging
from dotenv import load_dotenv
from pprint import pformat

load_dotenv()
log, sep = setup_logging(os.path.splitext(os.path.basename(__file__))[0])

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")


def main():
    github_data = fetch_public_github_data(GITHUB_USERNAME)
    log.info(pformat(github_data))


if __name__ == "__main__":
    main()
