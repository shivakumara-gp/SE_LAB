from hypothesis import given, strategies as st
from spam_scoring import sender_domain, first_link, shout_ratio


@given(st.text() | st.none())
def test_sender_domain_no_crash(s):
    try:
        res = sender_domain(s)
    except Exception as e:
        assert False, f"sender_domain crashed with {type(e).__name__}: {e}"
    if res is not None:
        assert isinstance(res, str)


@given(st.text() | st.none())
def test_first_link_no_crash(s):
    try:
        res = first_link(s)
    except Exception as e:
        assert False, f"first_link crashed with {type(e).__name__}: {e}"
    if res is not None:
        assert isinstance(res, str)
        assert res.startswith("http")


@given(st.text() | st.none())
def test_shout_ratio_no_crash(s):
    try:
        res = shout_ratio(s)
    except Exception as e:
        assert False, f"shout_ratio crashed with {type(e).__name__}: {e}"
    assert isinstance(res, float)
    assert 0.0 <= res <= 1.0