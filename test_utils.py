from motif import Motif, Note


def mary_had_a_little_lamb() -> Motif:
    notes = [
        Note('B', 1),
        Note('G', 1),
        Note('A', 1),
        Note('G', 1),
        Note('B', 1),
        Note('B', 1),
        Note('B', 2),
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_last_note_as_rest() -> Motif:
    notes = [
        Note('B', 1),
        Note('G', 1),
        Note('A', 1),
        Note('G', 1),
        Note('B', 1),
        Note('B', 1),
        Note('rest', 2),
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_first_note_as_rest() -> Motif:
    notes = [
        Note('rest', 1),
        Note('G', 1),
        Note('A', 1),
        Note('G', 1),
        Note('B', 1),
        Note('B', 1),
        Note('B', 2),
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_rest_between_notes() -> Motif:
    notes = [
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('G', 0.5),
        Note('rest', 0.5),
        Note('A', 0.5),
        Note('rest', 0.5),
        Note('G', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 1.5),
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_last_note_as_rest_and_rest_between_notes() -> Motif:
    notes = [
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('G', 0.5),
        Note('rest', 0.5),
        Note('A', 0.5),
        Note('rest', 0.5),
        Note('G', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 2.5)
    ]
    return Motif(notes)


def mary_had_a_little_lamb_with_first_note_as_rest_and_rest_between_notes() -> Motif:
    notes = [
        Note('rest', 1),
        Note('G', 0.5),
        Note('rest', 0.5),
        Note('A', 0.5),
        Note('rest', 0.5),
        Note('G', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 0.5),
        Note('B', 0.5),
        Note('rest', 1.5),
    ]
    return Motif(notes)


