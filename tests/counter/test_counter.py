from src.counter import count_ocurrences


def test_counter():
    file_path = "src/jobs.csv"

    with open(file_path) as file:
        read_data = file.read()

        expected_results = {
            "python": read_data.lower().lower().count("python"),
            "javascript": read_data.lower().lower().count("javascript"),
        }

        words = [
            "Python",
            "PyThon",
            "PYTHON",
            "python",
            "JavaScript",
            "Javascript",
            "JAVASCRIPT",
            "javascript",
        ]

        for word in words:
            assert expected_results[word.lower()] == count_ocurrences(
                file_path, word
            )
