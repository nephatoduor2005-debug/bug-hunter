"""Bug Hunter - Automated Bug Bounty Hunting Tool
Version 1.0.0
"""

__version__ = "1.0.0"
__author__ = "Bug Hunter Team"

from .scanner import Scanner
from .utils.logger import Logger

__all__ = ["Scanner", "Logger"]