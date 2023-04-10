states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

stations = {}
stations["one"] = {"id", "nv", "ut"}
stations["two"] = {"wa", "id", "mt"}
stations["three"] = {"or", "nv", "ca"}
stations["four"] = {"nv", "ut"}
stations["five"] = {"ca", "az"}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)