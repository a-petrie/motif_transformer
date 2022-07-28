from motif import Motif

def select_last_note(motif: Motif) -> int:
    return select_note(motif, -1)     

def select_first_note(motif: Motif) -> int:
    return select_note(motif, 0)     

def select_note(motif: Motif, index: int) -> int:
    if motif.non_rest_indices() == []:
        return 0
    return motif.non_rest_indices()[index]

