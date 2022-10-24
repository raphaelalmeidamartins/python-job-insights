from src.jobs import read
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = read("tests/sorting/mocks/sort_jobs.csv")
    criterias = ["min_salary", "max_salary", "date_posted"]

    for criteria in criterias:
        sorted_jobs = read(f"tests/sorting/mocks/sort_job_by_{criteria}.csv")
        sort_by(jobs, criteria)

        assert sorted_jobs == jobs
