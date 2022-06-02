import pytest
from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/jobs.csv", "test") == 2687
    assert count_ocurrences("src/jobs.csv", "salary") == 598
    assert count_ocurrences("src/jobs.csv", "job") == 3454
    assert count_ocurrences("src/jobs.csv", "python") == 1639
    assert count_ocurrences("src/jobs.csv", "medical") == 1639
    with pytest.raises(FileNotFoundError):
        count_ocurrences("src/test.csv", "test")
