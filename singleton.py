# singleton.py

class Singleton:
    _instance = None  
    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("Returning existing instance...")
        return cls._instance

    def __init__(self):
        self.value = 0

    def set_value(self, val):
        self.value = val

    def get_value(self):
        return self.value


# --- Client Code ---
if __name__ == "__main__":
    print("Singleton Pattern Demo\n")

    s1 = Singleton()
    s1.set_value(42)
    print(f"s1 value: {s1.get_value()}")

    s2 = Singleton()
    print(f"s2 value: {s2.get_value()}")  

    print(f"s1 ID: {id(s1)}")
    print(f"s2 ID: {id(s2)}")
    print("s1 and s2 refer to the same object:", s1 is s2)
