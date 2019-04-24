class Dinglemouse(object):

    def __init__(self, queues, capacity):
        self.capacity = capacity
        # self.people = []
        self.ix = 0
        self.capsule = []
        self.nosOfPeople = 0

        self.queues = []
        for ix, i in enumerate(queues):
            self.queues.append(list(i))
            # self.people.extend(list(i))

            for ii in i:
                if ii != ix:
                    self.nosOfPeople += 1

        print(self.nosOfPeople)

        
    def theLift(self):
        while(self.nosOfPeople>0):
            self.goUp()
            self.goDown()


    def goUp(self):
        __import__('pudb').set_trace()
        while(self.ix<=6):
            self.ix += 1
            self.takePeople()
            self.givePeople()


    def goDown(self):
        while(self.ix>=0):
            self.ix -= 1
            self.takePeople()
            self.givePeople()


    def takePeople(self):
        __import__('pudb').set_trace()
        while(len(self.queues[self.ix]) != 0):
            self.capsule.append(self.queues[self.ix].pop())
            if (len(self.capsule) == self.capacity):
                break

            
    def givePeople(self):
        __import__('pudb').set_trace()
        for i in self.capsule:
            if i==self.ix:
                self.capsule.remove(i)
                self.queues[self.ix].remove(i)
                self.nosOfPeople -= 1

