class Person:
    """A class to represent an individual."""

    def __init__(self, name, age, job):
        """Create a new Person with the given name, age and job."""
        self.name = name
        self.age = age
        self.job = job


class Group:
    """A class that represents a group of individuals and their connections."""

    def __init__(self):
        """Create an empty group."""
        self.members = []
        self.connections = {}

    def size(self):
        """Return how many people are in the group."""
        return len(self.members)

    def contains(self, name):
        """Check whether the group contains a person with the given name."""
        return any(member.name == name for member in self.members)

    def _get_person(self, name):
        """Return Person object by name (internal helper)."""
        for member in self.members:
            if member.name == name:
                return member
        raise ValueError(f"{name} is not in the group")

    def add_person(self, name, age, job):
        """Add a new person with the given characteristics to the group."""
        if self.contains(name):
            raise ValueError(f"{name} already exists in the group")
        person = Person(name, age, job)
        self.members.append(person)
        self.connections[name] = {}

    def number_of_connections(self, name):
        """Find the number of connections that a person in the group has"""
        if name not in self.connections:
            raise ValueError(f"{name} is not in the group")
        return len(self.connections[name])

    def connect(self, name1, name2, relation, reciprocal=True):
        """Connect two given people in a particular way.
        Optional reciprocal: If true, will add the relationship from name2 to name1 as well
        """
        if not self.contains(name1) or not self.contains(name2):
            raise ValueError("Both people must exist in the group")
        self.connections[name1][name2] = relation
        if reciprocal:
            self.connections[name2][name1] = relation

    def forget(self, name1, name2):
        """Remove the connection between two people."""
        if name1 in self.connections:
            self.connections[name1].pop(name2, None)
        if name2 in self.connections:
            self.connections[name2].pop(name1, None)

    def average_age(self):
        """Compute the average age of the group's members."""
        all_ages = [person.age for person in self.members]
        return sum(all_ages) / self.size()


if __name__ == "__main__":
    # Start with an empty group...
    my_group = Group()

    # Add group members (same as Part 2)
    my_group.add_person("Jill", 26, "biologist")
    my_group.add_person("Zalika", 28, "artist")
    my_group.add_person("John", 27, "writer")
    my_group.add_person("Nash", 34, "chef")

    # Add connections (same as Part 2)
    my_group.connect("Jill", "Zalika", "friend")
    my_group.connect("Jill", "John", "partner")
    my_group.connect("Nash", "John", "cousin")
    my_group.connect("Nash", "Zalika", "landlord", reciprocal=False)
    # If you want the reciprocal label for Zalika->Nash:
    my_group.connect("Zalika", "Nash", "tenant", reciprocal=False)

    # Forget Nash and John's connection
    my_group.forget("Nash", "John")

    assert my_group.contains("John"), "John should be in the group"
    assert my_group.size() == 4, "Group should have 4 members"
    assert my_group.average_age() == 28.75, "Average age of the group is incorrect!"
    assert my_group.number_of_connections("Nash") == 1, "Nash should only have one relation"
    print("All assertions have passed!")

