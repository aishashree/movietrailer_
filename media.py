import webbrowser
'''explains class is named as Movie'''


class Movie():
    '''The DocString is an constructor which initialize
    the instance and also initializing instance variable'''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    '''This DocSring is an instance method called
    by instance that is created for this class'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
