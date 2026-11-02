"""Pytest check for the release note format defined by the release-notes skill."""

from pathlib import Path

EXPECTED = "RELEASE 1.4.0\nTYPE fix\nSUMMARY Fixed the login timeout"


def test_release_note_follows_skill_format():
    assert Path("/app/RELEASE.md").read_text().strip() == EXPECTED
