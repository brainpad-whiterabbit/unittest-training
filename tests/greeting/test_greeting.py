import datetime

import pytest

import greeting.greeting as greeting_module


@pytest.mark.parametrize(
    "now_time, expected",
    [
        (datetime.time(5, 0, 0), "Good morning!"),
        (datetime.time(11, 59, 59), "Good morning!"),
        (datetime.time(12, 0, 0), "Good afternoon!"),
        (datetime.time(17, 59, 59), "Good afternoon!"),
        (datetime.time(18, 0, 0), "Good evening!"),
        (datetime.time(21, 59, 59), "Good evening!"),
        (datetime.time(22, 0, 0), "Good night!"),
        (datetime.time(4, 59, 59), "Good night!"),
    ],
)
def test_get_greeting_returns_expected_message_for_fixed_times(
    monkeypatch, now_time, expected
):
    class FixedDateTime(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(
                2026, 1, 1, now_time.hour, now_time.minute, now_time.second, tzinfo=tz
            )

    monkeypatch.setattr(greeting_module.datetime, "datetime", FixedDateTime)

    assert greeting_module.get_greeting() == expected


def test_get_greeting_uses_current_time_when_none(monkeypatch):
    class FixedDateTime(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 1, 1, 12, 0, 0, tzinfo=tz)

    monkeypatch.setattr(greeting_module.datetime, "datetime", FixedDateTime)

    assert greeting_module.get_greeting() == "Good afternoon!"
