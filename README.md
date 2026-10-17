
# Completed Implementation: Muay Thai Training Sessions

## Implementation Documentation
I modeled training sessions with the original ParentClass and ChildClass names so the completed code remained easy to compare with the starter.

- I created ParentClass with the class variable activity, the instance variables name and _duration, a constructor, and describe().
- I created ChildClass with inheritance, the class variable sport, the instance variables focus and drills, add_drill(), and an overridden describe(). I used super() to reuse the parent's initialization and description.
- I used _duration to signal an internal attribute by Python convention. This convention did not prevent outside access. I validated duration in the constructor.
- I implemented __str__ to provide readable object output and __len__ to return the number of drill groups.
- I displayed two instance namespaces using __dict__. I accessed sport through both the class and an object, added coach to only one object, and displayed the child class namespace keys.
- I demonstrated shallow and deep copying with a nested list of drills. After I added Hook to the original combination, the shallow copy also contained Hook. The deep copy retained only Jab and Cross.
- I added validation and edge-case checks as my student-created extension. I caught ValueError so invalid entries did not stop the demonstration.

## Verification
I ran the program with Python 3 and all assertions passed. I checked a parent description, inheritance, adding a drill, an empty drill list, a blank session name, zero and negative durations, a text duration, a NaN duration, and a blank drill. The empty list returned a length of zero. Invalid values produced clear messages. A valid drill was added after a failed entry, which demonstrated recovery.

## Memory and Growth
I stored drills in nested lists. Storage grew with the number of drill groups and their contents. Appending a group took amortized O(1) time; len() took O(1) time. A shallow object copy created a separate instance but shared the nested drills. A deep copy duplicated the nested data, so its time and additional memory grew with the copied data. The constructor also deep-copied the supplied drills to prevent separate sessions from sharing the caller's mutable list.

## Real-World Application
I used Muay Thai training as a practical scenario. A general workout supplied common session information, while a specialized session added a focus and drill combinations. This organization supported future specialized workouts without duplicating the shared code. The same pattern could organize general security events and specialized alerts in a cybersecurity application.

## Submission Status
I completed and locally verified the implementation. The student still needed to run and review the files, commit and push them, insert the actual repository link in the discussion post, and respond to two classmates.

---

## Original Assignment Instructions
# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.