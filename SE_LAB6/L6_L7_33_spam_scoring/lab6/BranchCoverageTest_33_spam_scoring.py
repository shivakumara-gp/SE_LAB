from spam_scoring import classify, filter_inbox, inbox_status, score_message


def test_score_message_word_link_and_sender_branches():
    assert score_message("", False, 0) == 0
    assert score_message("free!", False, 4) == 6
    assert score_message("hello", False, 1) == 1
    assert score_message("LOUD", False, 0) == 1
    assert score_message("HEY", False, 0) == 0
    assert score_message("free", True, 0) == 0
    assert score_message("free winner", True, 4) == 5


def test_classify_true_and_false_decisions():
    assert classify(8) == "spam"
    assert classify(7) == "suspicious"
    assert classify(3) == "clean"


def test_filter_inbox_empty_and_nonempty_paths():
    assert filter_inbox([]) == {"spam": 0, "suspicious": 0, "clean": 0}

    messages = [
        ("winner prize", False, 4),
        ("free winner", False, 1),
        ("hello", False, 0),
    ]
    assert filter_inbox(messages) == {"spam": 1, "suspicious": 1, "clean": 1}


def test_inbox_status_true_and_false_decisions():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"
    assert inbox_status({"spam": 2, "suspicious": 0, "clean": 1}) == "flooded"
    assert inbox_status({"spam": 1, "suspicious": 0, "clean": 1}) == "noisy"
    assert inbox_status({"spam": 0, "suspicious": 1, "clean": 1}) == "healthy"
