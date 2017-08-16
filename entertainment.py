import media
import fresh_tomatoes
#List of movies
mickey_mouse = media.Movie(
    "Mickeymouse","Story of mickey mouse","https://upload.wikimedia.org/wikipedia/en/e/ed/Mickey_Mouse_film_poster.png","https://www.youtube.com/watch?v=R86XY9lmtMs")

jumanji = media.Movie(
    "Jumanji","A story of playing a game","https://upload.wikimedia.org/wikipedia/en/b/b6/Jumanji_poster.jpg","https://www.youtube.com/watch?v=5p18zqZmeiI")

angry_birds = media.Movie(
    "Angrybird","A story of a bird","https://upload.wikimedia.org/wikipedia/en/f/f9/The_Angry_Birds_Movie_poster.png","https://www.youtube.com/watch?v=QRmKa7vvct4")

spykids = media.Movie(
    "Spykids","A story of kids","https://upload.wikimedia.org/wikipedia/en/2/26/Spy_kids.jpg","https://www.youtube.com/watch?v=wAQAkfOyAEY")

finding_nemo = media.Movie(
    "FindingNemo","A story of a fish","https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg","https://www.youtube.com/watch?v=bMtzgW-FVLY")

jurassic_world = media.Movie(
    "Jurassic_World","A story of animals","https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg","https://www.youtube.com/watch?v=aJJrkyHas78")

art = media.Movie(
    "Box_art","Art using python program","boxart image","images.PNG")
# The instances are added to the list
movies = [mickey_mouse,jumanji,angry_birds,spykids,finding_nemo,jurassic_world,art]
fresh_tomatoes.open_movies_page(movies)

                
