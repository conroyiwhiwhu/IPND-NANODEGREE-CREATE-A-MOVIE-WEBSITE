import fresh_tomatoes
import media

# Create instances of the Movie class to hold information of my favourite movies


lego_movie = media.Movie(
                        "Lego Movie",
                        "An ordinary Lego construction worker, thought to be the prophesied 'Special', is recruited to join a quest to stop an evil tyrant from gluing the Lego universe into eternal stasis, a journey for which he is hopelessly and hilariously under-prepared.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/The_Lego_Movie_poster.jpg/220px-The_Lego_Movie_poster.jpg",
                        "https://www.youtube.com/watch?v=fZ_JOBCLF-I"
                        )

six_days_seven_nights = media.Movie(
                         "Six Days Seven Nights",
                         "Two strangers on a flight must put aside their mutual dislike if they are to survive after crash landing on a deserted South Seas island.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/d/d2/Six_days_seven_nights.jpg/220px-Six_days_seven_nights.jpg",
                         "https://www.youtube.com/watch?v=YQ3Ux3hq3JA"
                         )

toy_story = media.Movie(
                        "Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc"
                        )

paddington = media.Movie(
                        "Paddington",
                        "The story of the comic misadventures of a young Peruvian bear who travels to the city in search of a home.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/0/06/PaddingtonPOSTER.jpg/220px-PaddingtonPOSTER.jpg",
                        "https://www.youtube.com/watch?v=7bZFr2IA0Bo"
                        )

avatar = media.Movie(
                    "Avatar",
                    "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
                    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                    )

titanic = media.Movie(
                      "Titanic",
                      "This spectacular epic re-creates the ill-fated maiden voyage of the White Star Line's $7.5 million R.M.S Titanic and the tragic sea disaster of April 15, 1912.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/2/22/Titanic_poster.jpg/220px-Titanic_poster.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0"
                      )

the_bodyguard = media.Movie(
                            "The Bodyguard",
                            "A former Secret Service agent takes on the job of bodyguard to a pop singer, whose lifestyle is most unlike a President's.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/8/8f/The_Bodyguard_1992_Film_Poster.jpg/220px-The_Bodyguard_1992_Film_Poster.jpg",
                            "https://www.youtube.com/watch?v=4JFRdJTszRM"
                            )

the_amazing_spiderman = media.Movie(
                                    "The Amazing Spiderman",
                                    "After an outcast high schooler is bitten by a genetically altered spider, he gains new-found, spider-like powers and ventures out to solve the mystery of his parent's mysterious death.",
                                    "https://upload.wikimedia.org/wikipedia/en/thumb/0/02/The_Amazing_Spider-Man_theatrical_poster.jpeg/220px-The_Amazing_Spider-Man_theatrical_poster.jpeg",
                                    "https://www.youtube.com/watch?v=oX9ZT3RbYE4"
                                    )

the_10_commandments = media.Movie(
                                  "The Ten Commandments",
                                  "The Egyptian Prince, Moses, learns of his true heritage as a Hebrew and his divine mission as the deliverer of his people.",
                                  "http://upload.wikimedia.org/wikipedia/en/d/d1/10Command56.jpg",
                                  "https://www.youtube.com/watch?v=OqCTq3EeDcY"
                                  )

above_the_rim = media.Movie(
                            "Above the Rim",
                            "Story of a promising high school basketball star and his relationships with two brothers, one a drug on hard times and now employed as a security guard.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Above_the_rim_poster.jpg/220px-Above_the_rim_poster.jpg",
                            "https://www.youtube.com/watch?v=sEsCXWD7-Cc"
                            )

# Add the instances to a list in the order to be displayed on the website.
movies = [
            lego_movie,
            six_days_seven_nights,
            toy_story,
            paddington,
            avatar,
            titanic,
            the_bodyguard,
            the_amazing_spiderman,
            the_10_commandments,
            above_the_rim
            ]
# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
