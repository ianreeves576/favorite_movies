"""This program has information of favorite movies and then opens a webpage.
The webpage will display the movie poster, allow the user to click on it, and
play the trailer. """

import fresh_tomatoes
import media

# The following instances are listed displaying favorite movies by title,
# storyline, poster URL, and Youtube link. step_brothers = media.Movie(
step_brothers = media.Movie(
    "Step Brothers",
    "Step Brothers learn to live under the same roof",
    "https://upload.wikimedia.org/wikipedia/en/d/d9/StepbrothersMP08.jpg",  # NOQA
    "https://www.youtube.com/watch?v=CewglxElBK0")

karate_kid = media.Movie(
    "Karate Kid",
    "Kid in dangerof being hurt learns karate "
    "to defend himself from enemies",
    "https://upload.wikimedia.org/wikipedia/en/a/a9/Karate_kid.jpg",
    "https://www.youtube.com/watch?v=n7JhKCQnEqQ")

the_fast_and_the_furious = media.Movie(
    "The Fast and The Furious",
    "Speed-junkies race cars to see who is the ultimate winner",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/Fast_and_Furious_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=2TAOizOnNPo")

forrest_gump = media.Movie(
    "Forrest Gump",
    "A man with a mission to keep on running",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

iron_man = media.Movie(
    "Iron Man",
    "A bomb engineer creates an iron suit to protect the United States",
    "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
    "https://www.youtube.com/watch?v=8hYlB38asDY")

harry_potter_sorc_stone = media.Movie(
    "Harry Potter and the Sorcerer's Stone",
    "A kid that's a wizard in his blood and heart",
    "https://upload.wikimedia.org/wikipedia/en/b/bf/Harry_Potter_and_the_Sorcerer%27s_Stone.jpg",  # NOQA
    "https://www.youtube.com/watch?v=VyHV0BRtdxo")

# The favorite movies are put into a list (array) and then we open the page.
movies = [
    step_brothers, karate_kid, the_fast_and_the_furious, forrest_gump,
    iron_man, harry_potter_sorc_stone]
fresh_tomatoes.open_movies_page(movies)
