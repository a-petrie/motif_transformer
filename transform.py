from motif import Motif

def transform(motif: Motif, note_selector: callable) -> Motif:
    notes = motif.notes
    note_index = note_selector(motif)
    notes[note_index] = ('rest', get_note_duration(notes[note_index]))
    return Motif(notes)

def get_note_duration(note) -> float:
    return note[1]

