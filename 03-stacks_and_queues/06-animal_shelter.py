#------------------------------------------------------Question------------------------------------------------------#

# An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. 

# Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. 

#--------------------------------------------------------Tips--------------------------------------------------------#

# You may use the built-in Linked list data structure.

# 022 - We could consider keeping a single linked list for dogs and cats, and then iterating
#       through it to find the first dog (or cat). What is the impact of doing this?
# 056 - Let's suppose we kept separate lists for dogs and cats. How would we find the oldest
#       animal of any type? Be creative!
# 063 - Think about how you'd do it in real life. You have a list of dogs in chronological order and
#       a list of cats in chronological order. What data would you need to find the oldest animal?
#       How would you maintain this data?

#------------------------------------------------------Solution------------------------------------------------------#

# This would make dequeueAny easy, but dequeueDog and dequeueCat would require iteration through
# the queue to find the first dog or cat. This would increase the complexity of the solution and decrease the
# efficiency.

# An alternative approach that is simple, clean and efficient is to simply use separate queues for dogs and
# cats, and to place them within a wrapper class called An imalQueue. We then store some sort of timestamp
# to mark when each animal was enqueued. When we call dequeueAny, we peek at the heads of both the
# dog and cat queue and return the oldest.

from LinkedList import LinkedList

# TODO WIP

class Animal:
    def __init__(self, name):
        self.name = name
        self.order = 0

    def __str__(self):
        return self.name

    def setOrder(self, order):
        self.order = order

    def getOrder(self):
        return self.order

    def isOlderThan(self, animal):
        return self.order < animal.getOrder()


class AnimalQueue():
    def __init__(self):
        self.cats = LinkedList()
        # self.cats.order = 0
        self.dogs = LinkedList()
        # self.dogs.order = 0

    def enqueue(self, animal):
        # Order is used as a sort of timestamp, so that we can compare the insertion order of a dog to a cat.
        animal.setOrder(animal.order)
        animal.order += 1

        if isinstance(animal.__class__, Cat):
            self.cats.add(animal)
        else: #if isinstance(animal.__class__, Dog):
            self.dogs.add(animal)
        # else: exit(0)

    def dequeueAny(self):
        # Look at tops of dog and cat queues, and pop the queue with the oldest value.
        if len(self.cats) == 0: 
            return Dog.dequeueDogs(self)
        elif len(self.dogs) == 0: 
            return Cat.dequeueCats(self)
        
        cat = self.cats.peek()
        dog = self.dogs.peek()
        if (cat.isOlderThan(dog)):
            return self.dequeueCats()
        else: 
            return self.dequeueDogs()

class Cat(Animal):
    def dequeueCats(self):
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat

class Dog(Animal):
    def dequeueDogs(self):
        dog = self.dogs[0]
        self.dogs = self.dogs[1:]
        return dog


# class AnimalShelter():
#     def __init__(self):
#         self.cats, self.dogs = [], []

#     def enqueue(self, animal):
#         if animal.__class__ == Cat: self.cats.append(animal)
#         elif animal.__class__ == Dog: self.dogs.append(animal)
#         else: exit(0)

#     def dequeueAny(self):
#         if len(self.cats) == 0: 
#             return self.dequeueDog()
#         elif len(self.dogs) == 0: 
#             return self.dequeueCat()

#     def dequeueCat(self):
#         if len(self.cats) == 0: 
#             return None
#         cat = self.cats[0]
#         self.cats = self.cats[1:]
#         return cat

#     def dequeueDog(self):
#         if len(self.dogs) == 0: 
#             return None
#         dog = self.dogs[0]
#         self.dogs = self.dogs[1:]
#         return dog

#--------------------------------------------------------Tests-------------------------------------------------------#

import unittest

class Test(unittest.TestCase):


    def testAnimalShelter(self):
        shelter = AnimalQueue()
        shelter.enqueue(Cat("Charlie"))
        shelter.enqueue(Cat("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(str(shelter.dequeueAny()), "Charlie")
        self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAny()), "Garfield")
        self.assertEqual(str(shelter.dequeueDog()), "Pluto")
        self.assertEqual(str(shelter.dequeueDog()), "Clifford")
        self.assertEqual(str(shelter.dequeueCat()), "Tony")
        self.assertEqual(str(shelter.dequeueCat()), "None")
        self.assertEqual(str(shelter.dequeueAny()), "Blue")
        self.assertEqual(str(shelter.dequeueAny()), "None")

if __name__ == "__main__":
  unittest.main()