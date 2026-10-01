import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils import add


def test_add_fail():
    assert add(2, 3) == 6
