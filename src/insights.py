from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs = read(path)
    return set(map(lambda job: job["job_type"], jobs))


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return list(filter(lambda job: job["job_type"] == job_type, jobs))


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs = read(path)
    return set(filter(None, map(lambda job: job["industry"], jobs)))


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return list(filter(lambda job: job["industry"] == industry, jobs))


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    return max(
        int(job["max_salary"]) for job in jobs if job["max_salary"].isnumeric()
    )


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    return min(
        int(job["min_salary"]) for job in jobs if job["min_salary"].isnumeric()
    )


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if not (
        "min_salary" in job.keys()
        and "max_salary" in job.keys()
        and isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
        and job["min_salary"] >= 0
        and job["max_salary"] >= 0
    ):
        raise ValueError("Salary is not valid")
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError("Minimum salary is greater than maximum salary")
    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return [
        job
        for job in jobs
        if (
            ("min_salary" in job.keys() and "max_salary" in job.keys())
            and (
                isinstance(job["min_salary"], int)
                and isinstance(job["max_salary"], int)
            )
            and (job["min_salary"] >= 0 and job["max_salary"] >= 0)
            and int(job["min_salary"]) < int(job["max_salary"])
            and isinstance(salary, int)
            and matches_salary_range(job, salary)
        )
    ]
