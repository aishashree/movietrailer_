import webbrowser

"""explains class is named as Movie"""
class Movie():      #class 

    def __init__(self,
    movie_title,
    movie_storyline,
    poster_image,
    trailer_youtube ):     
        self.title = movie_title       #instance variable
        self.storyline = movie_storyline #instance variable
        self.poster_image_url = poster_image  #instance variable
        self.trailer_youtube_url = trailer_youtube  #instance variable

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
