# Polymorphism

All this talk of interfaces demonstrates flexibility in programming. Flexibility in programming is a broad philosophy, but what’s worth remembering is that we want to implement forms that are familiar in our programs so that usage is expected. For example, let’s think of the + operator. It’s easy to think of it as a single function that “adds” whatever is on the left with whatever is on the right, but it does many different things in different contexts:

```python
# For an int and an int, + returns an int
2 + 4 == 6

# For a float and a float, + returns a float
3.1 + 2.1 == 5.2

# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"

# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]
```

Look at all the different things that + does! The hope is that all of these things are, for the arguments given to them, the intuitive result of adding them together. Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data.

Polymorphism is an abstract concept that covers a lot of ground, but defining class hierarchies that all implement the same interface is a way of introducing polymorphism to our code.

## Instructions

1. In script.py a few different types of data are provided. Call len() on each of them.

Is the same operation happening for each? How is it different? How is it similar? Does using len() to refer to these different operations make sense?
