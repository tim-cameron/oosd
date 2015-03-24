class MySet:

    def __init__(self, items):
        self.my_set = []
        #for x in range(0, len(items)):
        #    self.add_item(items[x])

        self.my_set = [self.add_item(items[b]) for b in range(0, len(items))]

        """Takes a list of items and builds a set with them, removing
           duplicates if necessary.
        """
        pass

    def add_item(self, item):
        if self.has_item(item) == False:
            self.my_set.append(item)
        """ Adds an item to the set if it is not already present. If the
            item is present, do nothing.
        """
        pass

    def remove_item(self, item):
        if self.has_item(item):
            self.my_set.remove(item)
        """ Removes item from the set.  Does nothing if item is not
            in the set.
        """
        pass

    def is_empty(self):
        return self.my_set.count == 0
        """Returns True is the set has no members."""
        pass

    def has_item(self, item):
        """returns True if item is in the set, False otherwise."""

        for x in range(0, len(self.my_set)):
            if self.my_set[x] == item:
                return True

        return False
        pass

    def intersection(self, otherset):
        """Returns a new set that is the intersection of self
           and otherset.
           """
        return set(self.my_set) & set(otherset)

        pass

    def union(self, otherset):
        """"Returns a new set that is the union of self and otherset"""
        return set(self.my_set) | set(otherset)
        pass

    def is_subset_of(self, otherset):
        """Returns True if self is a subset of otherset."""
        return set(self.my_set) <= set(otherset)
        pass

    def is_equal_to(self, otherset):
        """Returns True if self and otherset are equal, i.e.,
           they have the exact same members.
        """
        return self.my_set == otherset
        pass

    def is_proper_subset_of(self, otherset):
        """Returns True is self is a *proper* subset of otherset."""
        return set(self.my_set) < set(otherset)
        pass
