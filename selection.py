from motif import Motif
from random import choice

def select_last_note(motif: Motif) -> int:
    return select_note(motif, -1)     

def select_first_note(motif: Motif) -> int:
    return select_note(motif, 0)     

def select_random_note(motif: Motif) -> int:
    if motif.non_rest_indices() == []:
        return 0
    return choice(motif.non_rest_indices())

def select_note(motif: Motif, index: int) -> int:
    if motif.non_rest_indices() == []:
        return 0
    return motif.non_rest_indices()[index]

