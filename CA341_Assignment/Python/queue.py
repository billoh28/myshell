import sys
import os
global data
data = ""

def enqueue_event(s):
    global data
    # Should be two spaces between s
    # Get their indexes
    index_1 = get_index(s)
    index_2 = get_index(s[index_1 + 1:]) + index_1 + 1

    start_date = s[:index_1]
    start_time = s[index_1 + 1:index_2]
    location = s[index_2 + 1:]
    
    event = "Event: Start Date -> {}, Start Time -> {}, Location -> {}\n".format(start_date, start_time, location)
    data = data + event

def enqueue_task(s):
    global data
    # Should be numerous spaces through s as there is a list at the end
    # Only need to find first three spaces
    index_1 = get_index(s)
    index_2 = get_index(s[index_1 + 1:]) + index_1 + 1
    index_3 = get_index(s[index_2 + 1:]) + index_2 + 2
    
    start_date = s[:index_1]
    start_time = s[index_1+1:index_2]
    duration = s[index_2+1:index_3]
    people = s[index_3:]
    
    task = "Task: Start Date -> {}, Start Time -> {}, Duration -> {}, People -> {}\n".format(start_date, start_time, duration, people)
    data = data + task

def dequeue():
    global data
    index = int(get_index(data, "\n"))
    data = data[index+1:]

def length(s):
    global data
    counter = 0
    for char in s:
        counter += 1
    return counter

def get_index(target, s=" "):
    global data
    i = 0
    while i<length(target) and s != target[i]:
        i += 1
    return i

def toString():
    global data
    print(data)

def length(s):
    counter = 0
    for char in s:
        counter +=1
    return counter

def lenQueue():
    global data
    counter = 0
    i = 0
    while i<length(data):
        if data[i] == "\n":
            counter += 1
        i += 1
    return counter

def help():
    s = "To add a event, enter: 'event a b c' where a is a start date, b is a start time and c is a location\nTo add a task, enter: 'task a b c d' where a is a start date, b is a start time, c is a duration and d is the people assigned to the task\nEnter 'dequeue' to dequeue the queue\nEnter 'length' to get the length of the queue\nEnter 'print' to see what's in the queue\nEnter 'q' to exit the program"
    print(s)

def main():
    print("To get help on how to use the program enter 'help'")
    cond = True
    while cond:
        s = input()
        index = get_index(s)
        cmd = s[:index]  # get index of firsts pace to find command
        if cmd == "event":
            enqueue_event(s[index+1:])

        elif cmd == "help":
            help()

        elif cmd == "task":
            enqueue_task(s[index+1:])

        elif cmd == "dequeue":
            dequeue()

        elif cmd == "length":
            print(lenQueue())

        elif cmd == "print":
            toString()

        elif cmd == "q":
            cond = False

        else:
            print("Error: invalid input")

    print("Exiting")

if __name__ == '__main__':
    data = ""
    main()
