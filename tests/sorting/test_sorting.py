import pytest
from src.sorting import sort_by

jobs = [
    {
        "min_salary": 1000,
        "max_salary": 2000,
        "date_posted": "2022-01-01",
    },
    {
        "min_salary": 2000,
        "max_salary": 3000,
        "date_posted": "2021-01-01",
    },
    {
        "min_salary": 3000,
        "max_salary": 4000,
        "date_posted": "2020-01-01",
    },
    {
        "min_salary": "",
        "max_salary": 5000,
        "date_posted": "2019-01-01",
    },
    {
        "min_salary": 5000,
        "max_salary": "",
        "date_posted": "2018-01-01",
    },
    {
        "min_salary": 6000,
        "max_salary": 7000,
        "date_posted": "",
    },
]

sorted_min_salary = [jobs[0], jobs[1], jobs[2], jobs[4], jobs[5], jobs[3]]
sorted_max_salary = [jobs[5], jobs[3], jobs[2], jobs[1], jobs[0], jobs[4]]
sorted_date_posted = [jobs[0], jobs[1], jobs[2], jobs[3], jobs[4], jobs[5]]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == sorted_min_salary
    sort_by(jobs, "max_salary")
    assert jobs == sorted_max_salary
    sort_by(jobs, "date_posted")
    assert jobs == sorted_date_posted
    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
