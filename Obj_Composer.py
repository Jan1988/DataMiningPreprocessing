
class Composer(object):

    def __init__(self):
        # self.a_id = 0
        self.lastname = ""
        self.firstname = ""
        self.award_winner = ""
        self.year = 1900

    def __hash__(self):
        return hash((self.lastname, self.firstname, self.year))

    def __eq__(self, other):
        return (self.lastname, self.firstname, self.year) == (other.lastname, other.firstname, self.year)
