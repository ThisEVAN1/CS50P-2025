import pytest
import builtins
from project import Quiz, validate_countdown


def write_sample_csv(path, contents="question,answer\n2+2,4\n3+3,6\n"):
    p = path / "example.csv"
    p.write_text(contents)
    return str(p)


def test_quiz_init_accepts_csv(tmp_path):
    csv_path = write_sample_csv(tmp_path)
    q = Quiz(csv_path)
    assert isinstance(q, Quiz)


def test_quiz_init_rejects_non_csv(tmp_path):
    bad_file = tmp_path / "example.txt"
    bad_file.write_text("dummy")
    with pytest.raises(SystemExit):
        Quiz(str(bad_file))


def test_create_data_loads_questions(tmp_path):
    csv_path = write_sample_csv(tmp_path)
    q = Quiz(csv_path)
    q.create_data()
    assert len(q.data) == 2
    assert q.data[0]["question"] == "2+2"
    assert q.data[0]["answer"] == "4"
    assert q.data[0]["correct"] is False


def test_change_visual_data_marks_unanswered(tmp_path):
    csv_path = write_sample_csv(tmp_path)
    q = Quiz(csv_path)
    q.create_data()
    q.change_visual_data()
    assert q.visual_data[0]["answer"] == "???"


def test_change_visual_data_marks_answered(tmp_path):
    csv_path = write_sample_csv(tmp_path)
    q = Quiz(csv_path)
    q.create_data()
    q.data[0]["correct"] = True
    q.change_visual_data()
    assert q.visual_data[0]["answer"] == "4"


def test_score_counts_correct(tmp_path):
    csv_path = write_sample_csv(tmp_path)
    q = Quiz(csv_path)
    q.create_data()
    q.data[0]["correct"] = True
    assert q.score == (1, 2)


def test_validate_countdown_inf():
    assert validate_countdown("inf") > 1000


def test_validate_countdown_valid_format():
    assert validate_countdown("1:30") == 90


def test_validate_countdown_invalid_format():
    with pytest.raises(SystemExit):
        validate_countdown("badformat")


def test_prompt_marks_correct(monkeypatch, tmp_path):
    csv_path = write_sample_csv(tmp_path)
    q = Quiz(csv_path)
    q.create_data()
    monkeypatch.setattr(builtins, "input", lambda _: "4")
    q.prompt()
    assert q.data[0]["correct"] is True
