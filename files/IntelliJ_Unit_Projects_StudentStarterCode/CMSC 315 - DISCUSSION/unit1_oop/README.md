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

**Implementation**

I have defined a class called ParentClass which will store common data among all objects. There are three class variables called category, and two instance variables called name and age. A constructor is used to assign value to the instance data whereas display_info() method displays details about each object.

Next, I defined a class named ChildClass which is an inheritance of ParentClass. It inherits properties from its parent class and includes extra class and instance variables such as school, student_id, major and courses. I have defined methods called enroll_course() and drop_course() as my student-created extension. Additionally, I have overridden the display_info() method of the parent class.

The namespace portion was also helpful as it allowed me to comprehend how the class and instance variables are structured in Python. With two objects of the student class and `dict` command, it became evident that each of the objects holds their own data. Additionally, adding an extra attribute to only one object showed that objects can have different features even when they are created from the same class.

The copying portion allowed me to compare shallow and deep copy. From there, I observed that the modifications to the nested variable affect the shallow copy but do not influence the deep copy. Thus, it became obvious why the choice of the proper copy is essential when working with mutable data.

This assignment helped me gain more knowledge about how OOP can make programs more organized, flexible and reusable. All these features can also help to create more manageable and extendable future programs.
