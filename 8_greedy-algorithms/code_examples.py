#!/usr/bin/env python


# Television station example
# Set of states
states_needed = set(
    [
        "mt", "wa", "or",
        "id", "nv", "ut",
        "ca", "az"
    ]
)
# List of stations
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])
# List of final stations
final_stations = set()
while states_needed:
    # Pick the station that covers the most uncovered states
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        # Get intersection of states not covered AND states covered by station
        covered = states_needed & states_for_station
        # Check if intersection covers more states than the current best station
        if len(covered) > len(states_covered):
            # Set the current station as our new best station
            best_station = station
            # Update the states covered to the intersection
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
print(final_stations)