# Design Pattern Implementation Assignment

## Task
Implement one structural, one behavioral, and one creational design pattern in your preferred language. Each implementation includes client code demonstrating its usage.

---

## Implemented Patterns

### 1. Creational Pattern — Singleton (Borg Variation)
**File:** `singleton_pattern.py`  
The `Singleton` class ensures that all instances share the same internal state .



### 2. Behavioral Pattern — Memento
**File:** `memento_pattern.py`  
The `Originator` class can save and restore its state using `Memento` objects. The `Caretaker` handles saving and undoing changes.



### 3. Structural Pattern — Decorator
**File:** `decorator_pattern.py`  
Add dynamic features to coffee objects without changing their class by using wrappers (decorators).

---

## ▶How to Run

1. **Clone this repository or download the files.**

2. **Run each pattern independently:**

```bash
python singleton_pattern.py
python memento_pattern.py
python decorator_pattern.py
