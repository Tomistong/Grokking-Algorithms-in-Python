#!/usr/bin/env python

# Import libraries
from collections import deque


def person_is_buyer(name):
    """If a person's name ends in 'm', then they will buy a CS:GO skin."""
    return name[-1] == 'm'


# Graph model expressed as a hash table
graph = {}
# Make a node, 'me', and connect to neighbors of my Steam Friends list
graph['me'] = ['doppelganger', 'boromirnw', 'phattyla']

# Graph book example
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def search(name):
    # use the Python implementation of a queue: `deque`
    search_queue = deque()
    # add all neighbors to the search queue
    search_queue += graph[name]
    searched = []
    # while the search queue isn't empty...
    while search_queue:
        person = search_queue.popleft() # grab the first person off the list
        if not person in searched:
            # check if the person is a skin buyer
            if person_is_buyer(person):
                # the person is a skin buyer
                print(f'{person} loves buying CS:GO skins!')
                return True
            else:
                # add their neighbors to the search queue
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')