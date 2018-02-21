import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "About all the toys~",
                        "https://upload.wikimedia.org/wikipedia"
                        "/ru/a/a6/Toy_Story_1995_Poster.jpg",
                        "http://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon"
                     "Pandora on a unique mission becomes torn"
                     "between following his orders and protecting "
                     "the world he feels is his home.",
                     "https://images-na.ssl-images-amazon.com/images"
                     "/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcw"
                     "ODc5MTUwMw@@._V1_.jpg",
                     "http://www.youtube.com/watch?v=cRdxXPV9GNQ")

return_of_the_kings = media.Movie("The Lord of the Rings: "
                                  "The Return of the King",
                                  "Gandalf and Aragorn lead the World of Men "
                                  "against Sauron's army to draw "
                                  "his gaze from "
                                  "Frodo and Sam as they approach "
                                  "Mount Doom with "
                                  "the One Ring.",
                                  "https://images-na.ssl-images-amazon.com"
                                  "/images/M/MV5BYWY1ZWQ5YjMtMDE0MS0"
                                  "0NWIzLWE1M2YtOD"
                                  "YzYTk2OTNlYWZmXkEyXkFqcGdeQXVyNDUyOTg3N"
                                  "jg@._V1_SY1000_SX668_AL_.jpg",
                                  "https://www.youtube.com/watch?"
                                  "v=j3bQ6FslO6c")

game_of_thrones = media.Movie("Game of Thrones",
                              "7 powerful Houses are fighting for the Iron "
                              "Throne of 7 Kingdoms",
                              "http://4.bp.blogspot.com"
                              "/-FuP3ehGClQs/TfBm4yiOSVI"
                              "/AAAAAAAAA38/6Wgx0eijnKI/s1600/"
                              "600full-game-of-thrones-poster.jpg",
                              "http://www.youtube.com/watch?v=BpJYNVhGf1s")

x_men = media.Movie("X-MEN",
                    "Jean Grey begins to develop incredible "
                    "powers that corrupt and turn her "
                    "into a Dark Phoenix. ",
                    "https://images-na.ssl-images-amazon.com"
                    "/images"
                    "/M/MV5BZWUyMWVlMjEtNjRkYS00YjNlLThmODItY"
                    "zc1MTQ5NzBiOGM2XkEyXkFqcGdeQXVyNjY5NDczMT"
                    "k@._V1_.jpg",
                    "https://www.youtube.com/watch?v=uup2JFXH68g")

movies = [toy_story, avatar, return_of_the_kings, game_of_thrones, x_men]
fresh_tomatoes.open_movies_page(movies)
