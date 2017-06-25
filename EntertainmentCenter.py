import fresh_tomatoes
import Media

# a list of my 6 favorite movies
Finding_Nemo = Media.Movie(
    "Finding Nemo",
    "Little fish gets lost trying to be brave.",
    "http://www.pixartalk.com/wp-content/uploads/2009/06/nemoteaser.jpg",
    "https://www.youtube.com/watch?v=wZdpNglLbt8")
Up = Media.Movie(
    "Up",
    "A story of alittle man who likes balloons",
    "http://www.impawards.com/2009/posters/up.jpg",
    "https://www.youtube.com/watch?v=pkqzFUhGPJg")
Dark_Knight = Media.Movie(
    "Dark Knight",
    "Batman and the Joker battle it out",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")
Ted = Media.Movie(
    "Ted", "The story talking Teddy Bear that is VERY naughty",
    "https://images-na.ssl-images-amazon.com/images/I/61hYEm-udhL._SY550_.jpg",
    "https://www.youtube.com/watch?v=6h0wTgErTEw")
Deadpool = Media.Movie(
    "Deadpool",
    "Guy turns superhero, also not your average love story",
    "http://nerdist.com/wp-content/uploads/2015/07/Deadpool-poster.jpg",
    "https://www.youtube.com/watch?v=M_5twa6PH9k")
Gone_Girl = Media.Movie(
    "Gone Girl",
    "Crazy wife fakes death and frames husband.\
    Also Neil Patrick Harris is naked.",
    "http://www.impawards.com/2014/posters/gone_girl_ver2_xlg.jpg",
    "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")
movies = [Finding_Nemo, Up, Dark_Knight, Ted, Deadpool, Gone_Girl]
# this will open the website into webbrowser that will show the 6 movies.
fresh_tomatoes.open_movies_page(movies)
