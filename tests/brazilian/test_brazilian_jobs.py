from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    for job in read_brazilian_file("tests/mocks/brazilians_jobs.csv"):
        assert "title" in job
        assert "salary" in job
        assert "type" in job
        assert "titulo" not in job
        assert "salario" not in job
        assert "tipo" not in job
