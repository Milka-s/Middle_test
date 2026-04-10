import pytest
from main import PopulationAnalyzer


@pytest.fixture
def analyzer(tmp_path):
    test_file = tmp_path / "test_data.txt"
    test_file.write_text(
        "Ukraine, 603628, 41000000\n"
        "France, 551695, 67000000\n"
        "Poland, 312685, 38000000",
        encoding="utf-8")

    return PopulationAnalyzer(str(test_file))


def test_read_file(analyzer):
    data = analyzer.read_file()
    assert len(data) == 3
    assert data[0]['name'] == "Ukraine"
    assert data[0]['area'] == 603628.0


@pytest.mark.parametrize("sort_type, reverse, expected_first", [
    ("area", False, "Poland"),
    ("area", True, "Ukraine"),
    ("population", False, "Poland"),
    ("population", True, "France")
])
def test_sorting(analyzer, sort_type, reverse, expected_first):
    analyzer.read_file()
    if sort_type == "area":
        sorted_data = analyzer.sort_by_area(reverse=reverse)
    else:
        sorted_data = analyzer.sort_by_population(reverse=reverse)
    assert sorted_data[0]['name'] == expected_first
