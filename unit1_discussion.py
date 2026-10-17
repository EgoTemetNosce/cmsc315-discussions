"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================
Class: CMSC 315
Date: 10/17/2026
Name: Roman Dilone
INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    activity = "Fitness"

    def __init__(self, name, duration):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("A session name is required.")
        if isinstance(duration, bool) or not isinstance(duration, (int, float)) or not 0 < duration < float("inf"):
            raise ValueError("Duration must be a positive, finite number.")
        self.name = name.strip()
        self._duration = duration

    def describe(self):
        return f"{self.name}: {self._duration} minutes"

    def __str__(self):
        return self.describe()


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    sport = "Muay Thai"

    def __init__(self, name, duration, focus, drills):
        super().__init__(name, duration)
        self.focus = focus
        # A new nested list belongs to each session.
        self.drills = deepcopy(drills)

    def describe(self):
        return f"{super().describe()} | {self.sport} | Focus: {self.focus}"

    def add_drill(self, drill):
        if not isinstance(drill, str) or not drill.strip():
            raise ValueError("A drill name is required.")
        self.drills.append([drill.strip()])

    def __len__(self):
        return len(self.drills)


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    first = ChildClass("Monday", 60, "Technique", [["Jab", "Cross"]])
    second = ChildClass("Wednesday", 45, "Defense", [])
    print("Class access:", ChildClass.sport)
    print("Object access:", first.sport)
    first.coach = "Coach A"
    print("First object namespace:", first.__dict__)
    print("Second object namespace:", second.__dict__)
    print("Second object has coach:", hasattr(second, "coach"))
    print("Class namespace keys:", list(ChildClass.__dict__))
    print("Inherited class variable:", ChildClass.activity)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    original = ChildClass("Pad work", 60, "Combinations", [["Jab", "Cross"]])
    shallow = copy(original)
    deep = deepcopy(original)
    original.drills[0].append("Hook")
    # A shallow copy shares the original nested data.
    # A deep copy creates independent nested data.
    print("Original drills:", original.drills)
    print("Shallow-copy drills:", shallow.drills)
    print("Deep-copy drills:", deep.drills)
    print("Shallow copy shares drills:", original.drills is shallow.drills)
    print("Deep copy shares drills:", original.drills is deep.drills)
    assert shallow.drills[0] == ["Jab", "Cross", "Hook"]
    assert deep.drills[0] == ["Jab", "Cross"]





# Student-created extension: validation and edge-case checks.
def demonstrate_validation():
    print("\n=== Validation and Edge Cases ===")
    empty = ChildClass("Beginner session", 20, "Basics", [])
    print("Empty session drill groups:", len(empty))
    assert len(empty) == 0
    for name, duration in [("", 30), ("Workout", 0), ("Workout", -5),
                           ("Workout", "sixty"), ("Workout", float("nan"))]:
        try:
            ParentClass(name, duration)
        except ValueError as error:
            print("Invalid session handled:", error)
        else:
            raise AssertionError("Invalid session was accepted.")
    try:
        empty.add_drill(" ")
    except ValueError as error:
        print("Empty drill handled:", error)
    else:
        raise AssertionError("Empty drill was accepted.")
    empty.add_drill("Basic stance")
    assert len(empty) == 1
    print("Program continued; valid drill added:", empty.drills)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.
def main():
    print("=== Unit 1 OOP Assignment ===")

    parent = ParentClass("General workout", 30)
    print(parent)
    assert parent.describe() == "General workout: 30 minutes"

    child = ChildClass("Evening training", 60, "Footwork", [])
    print(child)
    child.add_drill("Pivot practice")
    print("Drill groups:", len(child))
    assert isinstance(child, ParentClass)
    assert len(child) == 1

    demonstrate_namespaces()
    demonstrate_copying()
    demonstrate_validation()


if __name__ == "__main__":
    main()
