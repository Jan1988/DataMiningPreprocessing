
class MovieWithGenres(object):

    def __init__(self):
        self.m_id = -1
        self.title = ""
        self.genres = ""
        self.year = 1900

    def __hash__(self):
        return hash((self.title, self.year))

    def __eq__(self, other):
        return (self.title, self.year) == (other.title, self.year)
