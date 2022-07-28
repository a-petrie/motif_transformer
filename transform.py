from motif import Motif, Note
from itertools import groupby

def transform(motif: Motif, note_selector: callable) -> Motif:
    notes = motif.notes
    note_index = note_selector(motif)
    notes[note_index] = Note('rest', notes[note_index].get_dur())
    return Motif(collapse_ajdacent_rests(notes))

def collapse_ajdacent_rests(notes: list[Note]) -> list[Note]:
    result = []

    for k, g in group_by_note_name(notes):
        if k == "rest":
            result += [Note("rest", total_duration(g))]
        else:
            result += g
    return result

def group_by_note_name(notes: list[Note]):
    return [(k, list(g)) for k,g in groupby(notes, lambda n: n.name)]

def total_duration(notes: list[Note]):
    return sum([n.get_dur() for n in notes])
