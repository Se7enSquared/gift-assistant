# this will hold the logic for inferring relationships

class Relationships():

    def __init__(self, recipient: object):
        self.recipient = recipient

    @property
    def is_mother(self):
        pass

    @property
    def is_father(self):
        pass

    @property
    def is_wife(self):
        pass

    @property
    def is_husband(self):
        pass

    # logic for finding mother, father, sister, brother, son, daughter
