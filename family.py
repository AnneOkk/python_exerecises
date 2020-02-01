class Family:
    def __init__(self, mother, father, son, daughter, weeks):
        self.mother = mother
        self.father = father
        self.son = son
        self.daughter = daughter
        self.weeks = weeks

class Vacation_Plans(Family):
    def __init__(self, mother, father, son, daughter, weeks):
        super().__init__(mother, father, son, daughter, weeks)
        self.location_= 'Portugal'
        self.alternative = ['Stay home and watch a movie', 'go to the sauna', 'Visit some Kaff around Halle',
                                                                              'just drink a nice cup of coffee',
                                                                              'go cruuuising']
    def our_family_plans(self):
        print("Sometimes, Mama, Papa, Simon & Anne plan holidays together. They have great ideas, like travelling to "
              "Portugal... ")
    def describe_alt_plans(self):
        if self.weeks < 3:
            print("... but we mostly have some nice alternatives to travelling far away, like:")
            for altern in self.alternative:
                print(f" - {altern}")
        else:
            print(f"We could travel to {self.location.title()}")

my_family = Family('Mami', 'Papa', 'Simon', 'Anne', 2)
our_plans = Vacation_Plans('Mami', 'Papa', 'Simon', 'Anne', 2)

our_plans.our_family_plans()
our_plans.describe_alt_plans()




