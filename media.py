import webbrowser


class Movie():
    """This class provides a way to store movie related information.

    Attributes:
        movie_title: The title of the movie.
        movie_storyline: Short summary of the movie storyline.
        poster_image: A URL to the poster image.
        trailer_youtube: A URL to the movie trailer.
    """

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        """Inits a movie class with information about the movie"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function opens a new browser and plays the
           trailer for a movie instance."""
        webbrowser.open(self.trailer_youtube_url)
