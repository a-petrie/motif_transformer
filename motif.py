class Note:

    name: str
    dur: float

    def __init__(self, name, dur):
        self.name = name
        self.dur = dur

    def is_rest(self) -> bool:
        return self.name == "rest"

    def get_dur(self) -> float:
        return self.dur

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.dur == other.dur

    def __str__(self) -> str:
        return f"({self.name}, {self.dur})"

class Motif:

    notes: list[Note]

    def __init__(self, notes: list[Note]):
        self.notes = notes

    def non_rest_indices(self) -> list[int]:
        return [i for i, n in enumerate(self.notes) if not n.is_rest()]

