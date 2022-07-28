from motif import Motif

def mary_had_a_little_lamb() -> Motif:
    notes = [
        ('B', 1),
        ('G', 1),
        ('A', 1),
        ('G', 1),
        ('B', 1),
        ('B', 1),
        ('B', 2),
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_last_note_as_rest() -> Motif:
    notes = [
        ('B', 1),
        ('G', 1),
        ('A', 1),
        ('G', 1),
        ('B', 1),
        ('B', 1),
        ('rest', 2),
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_first_note_as_rest() -> Motif:
    notes = [
        ('rest', 1),
        ('G', 1),
        ('A', 1),
        ('G', 1),
        ('B', 1),
        ('B', 1),
        ('B', 2),
    ]
    return Motif(notes)


def assert_motifs_are_equal(motif1: Motif, motif2: Motif) -> None:
    return motif1.notes == motif2.notes
