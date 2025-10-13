"""An example of how to represent a group of acquaintances in Python."""

my_group = {
    "Jill": {
        "age": 26,
        "job": "biologist",
        "connections": {
            "friend": ["Zalika"],
            "partner": ["John"]
        }
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "connections": {
            "friend": ["Jill"],
            "landlord": ["Nash"]
        }
    },
    "John": {
        "age": 27,
        "job": "writer",
        "connections": {
            "partner": ["Jill"],
            "cousin": ["Nash"]
        }
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "connections": {
            "cousin": ["John"],
            "landlord_of": ["Zalika"]
        }
    }
}



# Functions for Stretch Goal #7

def forget(group, person1, person2):
    """Remove the connection between person1 and person2 (both directions if present)."""
    if person1 in group and person2 in group:
        for relation, people in group[person1]["connections"].items():
            if person2 in people:
                people.remove(person2)
        for relation, people in group[person2]["connections"].items():
            if person1 in people:
                people.remove(person1)


def add_person(group, name, age, job=None, relations=None):
    """Add a new person with given characteristics to the group."""
    if relations is None:
        relations = {}
    group[name] = {
        "age": age,
        "job": job,
        "connections": relations
    }


def average_age(group):
    """Calculate the mean age of the group."""
    ages = [person["age"] for person in group.values()]
    return sum(ages) / len(ages) if ages else 0



# Example usage (only runs if executed directly)

if __name__ == "__main__":
    from pprint import pprint

    print("Initial group:")
    pprint(my_group)

    # Add a new person
    add_person(my_group, "Alice", 22, "student", {"friend": ["Jill"]})
    print("\nAfter adding Alice:")
    pprint(my_group)

    # Forget Jill and John
    forget(my_group, "Jill", "John")
    print("\nAfter Jill forgets John:")
    pprint(my_group)

    # Average age
    print("\nAverage age:", average_age(my_group))
        # ---- Summary statistics using comprehension expressions ----

    # maximum age
    max_age = max(person["age"] for person in my_group.values())
    print("\nMaximum age in group:", max_age)

    # the average (mean) number of relations among members of the group
    avg_relations = sum(len(p["connections"]) for p in my_group.values()) / len(my_group)
    print("Average number of relation types per person:", avg_relations)

    # he maximum age of people in the group that have at least one relation
    max_age_with_relation = max(
        (p["age"] for p in my_group.values() if len(p["connections"]) > 0),
        default=None
    )
    print("Maximum age of people with at least one relation:", max_age_with_relation)

    # [more advanced] the maximum age of people in the group that have at least one friend
    max_age_with_friend = max(
        (p["age"] for p in my_group.values() if "friend" in p["connections"] and p["connections"]["friend"]),
        default=None
    )
    print("Maximum age of people with at least one friend:", max_age_with_friend)
