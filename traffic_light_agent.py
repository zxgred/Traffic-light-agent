# Task 1: Table-driven agent for a traffic light responder
table = {
    "Red": "Stop",
    "Yellow": "Slow Down",
    "Green": "Go",
    
}


def traffic_light_agent(percept):
    """Return the action stored in the lookup table for this percept."""
    return table.get(percept, "Unknown percept")


percept_sequence = ["Red", "Green", "Yellow", "Red", "Flashing Red"]

print("Percept\t\tAction")
for percept in percept_sequence:
    print(f"{percept}\t\t{traffic_light_agent(percept)}")