import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    # This class provides a way to store movie related information

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # initialize instance of class Movie
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # opens a webbrowser and play the movie's trailer via youtube

    def show_trailer(self):
        """Plays the movie's trailer in a new browser window"""
        webbrowser.open(self.trailer_youtube_url)
