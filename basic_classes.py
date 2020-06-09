
class Movies:

    price_of_a_ticket = 8

    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def introduction():
        intro = "\nWelcome! Here you can check out some of my favorite movies!"
        print(intro)

    def basic_info_set(self):
        return self.title + ' was directed by ' + self.director + '. Year of the release: ' + str(self.year)

    def how_old(self):
        time_passed = 2020 - self.year
        if time_passed == 1:
            word = "year"
        else:
            word = "years"
        return self.title + ' was released ' + str(time_passed) + ' ' + word + ' ago.' 


movie_1 = Movies("Donnie Darko", "Richard Kelly", 2001)
movie_2 = Movies("Requiem For A Dream", "Darren Aronofsky", 2000)
movie_3 = Movies("Parasite", "Bong Joon-ho", 2019)
movie_4 = Movies("The Others", "Alejandro Amenábar", 2011)
movie_5 = Movies("Irrational Man", "Woody Allen", 2015)

Movies.introduction()
print("Average price of a ticket in cinemas:", Movies.price_of_a_ticket)
print(movie_2.basic_info_set())
print(movie_1.basic_info_set())
Movies.price_of_a_ticket = 10
print("Average price of a ticket in cinemas:", Movies.price_of_a_ticket)
print(movie_3.how_old())
print(movie_5.how_old())