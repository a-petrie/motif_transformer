from test_utils import *

from motif import Motif
from transform import transform

# selection functions used as mocks here
def select_last_note(motif: Motif) -> int:
    return motif.non_rest_indices()[-1]


def select_first_note(motif: Motif) -> int:
    return 0


def test_last_note_deletion():
    motif = mary_had_a_little_lamb()
    expected_motif = mary_had_a_little_lamb_with_last_note_as_rest()

    transformed_motif = transform(motif, select_last_note)
    assert expected_motif.notes == transformed_motif.notes


def test_first_note_deletion():
    motif = mary_had_a_little_lamb()
    expected_motif = mary_had_a_little_lamb_with_first_note_as_rest()

    transformed_motif = transform(motif, select_first_note)
    assert expected_motif.notes == transformed_motif.notes


def test_last_note_deletion_with_rests():
    motif = mary_had_a_little_lamb_with_rest_between_notes()
    expected_motif = mary_had_a_little_lamb_with_last_note_as_rest_and_rest_between_notes()

    transformed_motif = transform(motif, select_last_note)
    assert expected_motif.notes == transformed_motif.notes


def test_first_note_deletion_with_rests():
    motif = mary_had_a_little_lamb_with_rest_between_notes()
    expected_motif = mary_had_a_little_lamb_with_first_note_as_rest_and_rest_between_notes()

    transformed_motif = transform(motif, select_first_note)
    assert expected_motif.notes == transformed_motif.notes



