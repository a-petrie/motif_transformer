from test_utils import *

from motif import Motif
from transform import transform
from selection import *

import pytest

from random import seed

test_data = [
        ( 
            mary_had_a_little_lamb(),
            mary_had_a_little_lamb_with_last_note_as_rest(),
            select_last_note 
        ),
        (
            mary_had_a_little_lamb(),
            mary_had_a_little_lamb_with_first_note_as_rest(),
            select_first_note
        ),
        (
            mary_had_a_little_lamb_with_rest_between_notes(),
            mary_had_a_little_lamb_with_last_note_as_rest_and_rest_between_notes(),
            select_last_note
        ),
        (
            mary_had_a_little_lamb_with_rest_between_notes(),
            mary_had_a_little_lamb_with_first_note_as_rest_and_rest_between_notes(),
            select_first_note
        ),
        (
            mary_had_a_little_lamb_off_beats(),
            mary_had_a_little_lamb_off_beats_and_last_note_as_rest(),
            select_last_note
        ),
        (
            mary_had_a_little_lamb_off_beats(),
            mary_had_a_little_lamb_off_beats_and_first_note_as_rest(),
            select_first_note
        ),
        (
            Motif([Note("rest", 4)]),
            Motif([Note("rest", 4)]), 
            select_first_note
        ),
        (
            Motif([Note("rest", 4)]),
            Motif([Note("rest", 4)]),
            select_last_note
        ),
        (
            Motif([Note("rest", 4)]),
            Motif([Note("rest", 4)]),
            select_random_note
        ),
        (
            mary_had_a_little_lamb(),
            mary_had_a_little_lamb_with_fifth_note_as_rest(),
            select_random_note
        ),
        (
            mary_had_a_little_lamb_with_rest_between_notes(),
            mary_had_a_little_lamb_rests_expected_random(),
            select_random_note
        ),
        (
            mary_had_a_little_lamb_off_beats(),
            mary_had_a_little_lamb_off_beats_expected_random(),
            select_random_note
        ),
    ]

@pytest.mark.parametrize("initial,expected,note_selector", test_data)
def test_motif_deletions(initial: Motif, expected: Motif, note_selector: callable) -> None:
    seed(42)
    transformed = transform(initial, note_selector)
    assert transformed.notes == expected.notes


