# here we creat first class of python

class PartyAnimal:
    x = 0

    def party(animal):
        animal.x = animal.x + 1
        print('So far ', animal.x)

an = PartyAnimal()

an.party()
an.party()
an.party()


#  here is how to explain the example above: first the class is like a package, in the package, we need an
# object, then what activity that object can do. here, we call object, which is x in example instance. and
# his activity which is party(), then store all this information into constructor which is an in the example,
#  then if you want to know which activity that an has, then call the activity of an by using: an.party(), here
# we only have one activity which is party(). then we print it three times, which leads to the result, why we got
#  so far 1, so far 2, so far 3