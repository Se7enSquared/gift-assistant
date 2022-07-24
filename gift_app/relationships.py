
from gift_app.models import Recipient


class Relationships():

    def __init__(self, recipient: Recipient):
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

    def is_sister(self):
        pass

    def is_brother(self):
        pass


    # logic for finding mother, father, sister, brother, son, daughter
