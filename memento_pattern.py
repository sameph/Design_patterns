# simplified_memento.py

class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Originator: Setting state to '{state}'")
        self._state = state

    def save_state(self):
        return Memento(self._state)

    def restore_state(self, memento):
        self._state = memento.get_state()
        print(f"Originator: Restored state to '{self._state}'")

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._history = []

    def save(self, originator):
        print("Caretaker: Saving current state.")
        self._history.append(originator.save_state())

    def undo(self, originator):
        if not self._history:
            print("Caretaker: No saved states.")
            return
        memento = self._history.pop()
        print("Caretaker: Undoing to previous state.")
        originator.restore_state(memento)


# --- Client Code ---
if __name__ == "__main__":
    print("Memento Pattern - Simplified Demo\n")

    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("State A")
    caretaker.save(originator)

    originator.set_state("State B")
    caretaker.save(originator)

    originator.set_state("State C")

    print(f"\nCurrent state: {originator.get_state()}")
    caretaker.undo(originator)
    print(f"After undo: {originator.get_state()}")
    caretaker.undo(originator)
    print(f"After another undo: {originator.get_state()}")
