"""
HTML crawler configuration loader.
"""

import yaml
from pathlib import Path


class HTMLConfigLoader:
    """
    Load HTML crawler sources configuration.
    """

    def __init__(self, config_path):
        self.config_path = Path(config_path)


    def load(self):
        """
        Load yaml config.

        Returns:
            list
        """

        if not self.config_path.exists():
            return []


        with open(
            self.config_path,
            "r",
            encoding="utf-8"
        ) as f:

            data = yaml.safe_load(f)


        if not data:
            return []


        return data.get(
            "sources",
            []
        )
