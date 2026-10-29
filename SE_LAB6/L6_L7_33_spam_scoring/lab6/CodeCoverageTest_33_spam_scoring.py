from spam_scoring import classify, filter_inbox, inbox_status, score_message


def test_score_message_spam_and_high_link_count():
    assert score_message("free winner", False, 4) == 8


def test_score_message_uppercase_known_sender_and_score_floor():
    assert score_message("HELLO", True, 0) == 0


def test_score_message_known_sender_with_positive_score():
    assert score_message("urgent winner", True, 4) == 5


def test_classify_all_labels():
    assert classify(8) == "spam"
    assert classify(4) == "suspicious"
    assert classify(3) == "clean"


def test_filter_inbox_counts_each_class():
    messages = [
        ("free winner", False, 4),
        ("free winner", False, 1),
        ("hello there", False, 0),
    ]
    assert filter_inbox(messages) == {"spam": 1, "suspicious": 1, "clean": 1}


def test_inbox_status_all_outcomes():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"
    assert inbox_status({"spam": 2, "suspicious": 0, "clean": 1}) == "flooded"
    assert inbox_status({"spam": 1, "suspicious": 0, "clean": 1}) == "noisy"
    assert inbox_status({"spam": 0, "suspicious": 1, "clean": 1}) == "healthy"
