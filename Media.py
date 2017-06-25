import webbrowser


class Movie ():
    """This class provides way to store movie storyline information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """ This function shows the object of the movie."""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This opens a link to the movie trailer when clicked"""
        webbrowser.open(self.trailer_youtube_url)
