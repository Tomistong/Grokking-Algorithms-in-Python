#!/usr/bin/env python



def look_for_key(main_box):
    """Non-recursive code example."""
    pile = main_box.make_a_pile_to_look_through()
    while pile is not pile.is_empty():
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("Found the key!")


def look_for_key(box):
    """Recursive code example."""
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("Found the key!")


def countdown(i:int):
    """Bad runaway recursive example."""
    print(i)
    countdown(i-1)


def countdown(i:int):
    """Good recursive example."""
    print(i)
    if i <= 0:
        return None
    else:
        countdown(i)


def greet(name:str):
    """Simple stack example."""
    # Begin the call stack with this function
    print("Hello, " + name + "!")
    # Pause completion of this function to add `greet2` to the stack
    greet2(name)
    # Resume completion of this function and pop `greet2` from the stack
    print("Getting ready to say bye...")
    # Pause completion of this function to add `bye` to the stack
    bye()
    # Resume completion of this function and pop `bye` from the stack
    return None


def greet2(name:str):
    """Stack example function."""
    print("How are you, " + name + "?")
    return None
 

def bye():
    print("Ok bye!")
    return None


def fact(x:int):
    """Recursive call stack example."""
    # Begin call stack with current function
    if x == 1:
        # Resume completion of current function, exit recursion, and return 1
        return 1
    # Continue execution of current function
    else:
        # Pause completion of function and add recursion to stack
        return x * fact(x-1)

print(fact(3))