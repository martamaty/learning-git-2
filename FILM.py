
class Film:
    def __init__(self, title, year,types, views):
       self.title = title
       self.year = year
       self.types = types
       self.views = views

        # Variables
       self.current_views = 0

    def play(self, step=1):
       self.current_views += step
       

    def __str__(self):
        return f'{self.title} {self.year} {self.types} {self.views}'


class Series:
    def __init__(self, title, year, types, season,episode, views):
       self.title = title
       self.year = year
       self.types = types
       self.season = season
       self.episode = episode
       self.views = views

    def set_current_views(self, value):
       if value <= self.views:
          self.current_views = value
       
      # Variables
       self._current_views = 0

    def play(self, step=1):
       self.views += step
       return

    def __str__(self):
        return f'{self.title} {self.year} {self.types}  {self.season} {self.episode} {self.views}'

dom_z_papieru = Series(title="dom_z_papieru", year= "2019", types= "crimy", season= "02", episode="01", views=15)

dom_z_papieru.play(2)
print(dom_z_papieru.views)
