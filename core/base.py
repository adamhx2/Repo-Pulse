from typing import Optional
import logging


def setup_logging(script_name: str = "talos", level: int = logging.INFO):
    """
    Returns (log, sep)
    - log: logger scoped to script_name
    - sep: helper to print nice section separators
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    log = logging.getLogger(script_name)

    def sep(title: Optional[str] = None):
        line = "=" * 60
        if title:
            log.info(line)
            log.info(title)
            log.info(line)
        else:
            log.info(line)

    return log, sep
