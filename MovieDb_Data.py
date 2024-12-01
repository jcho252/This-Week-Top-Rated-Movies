import requests
import json

class MovieDBAPI:
    
    def __init__(self):
        self.movieInfo = None
        self.url = "https://api.themoviedb.org/3/trending/movie/week?language=en-US"

        self.headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ODMzODVkYWRjZDdiNDkyOWM2Y2U5MGQyODIyYjQ5YyIsInN1YiI6IjY1ZjlmZDZhYmQ5OTBjMDE4NjIyZDQ1OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.q5tGzFXlj5qK9uRmce45dPz1LqWdqtTnVn4-bOEapSs"
        }

    def getData(self):
        response = requests.get(self.url, headers=self.headers)
        self.movieInfo = json.loads(response.text)
        return self.movieInfo

    def get_rank(self):
        ranks = []
        for movie in self.movieInfo["results"][:10]:
            rank = movie["vote_average"]
            ranks.append(rank)
        return ranks

    def get_title(self):
        titles = []
        for movie in self.movieInfo["results"][:10]:
            title = movie["title"]
            titles.append(title)
        return titles
    
    def get_ratings(self):
        ratings = []
        for movie in self.movieInfo["results"][:10]:
            rating = movie["vote_average"]
            ratings.append(rating)
        return ratings
    
    def get_release_date(self):
        release_dates = []
        for movie in self.movieInfo["results"][:10]:
            release_date = movie["release_date"]
            release_dates.append(release_date)
        return release_dates
    
    def get_vote_count(self):
        vote_counts = []
        for movie in self.movieInfo["results"][:10]:
            vote_count = movie["vote_count"]
            vote_counts.append(vote_count)
        return vote_counts

    def get_description(self):
            descriptions = []
            for movie in self.movieInfo["results"][:10]:  # Only top 10 movies
                description = movie["overview"]
                descriptions.append(description)
            return descriptions
    
    def moviedb_data(self,data):
        ranks = self.get_rank()
        titles = self.get_title()
        ratings = self.get_ratings()
        release_dates = self.get_release_date()
        vote_counts = self.get_vote_count()

        data_dict = {}

        for i in range(len(ranks)):
            data_dict[i + 1] = {
                "title": titles[i],
                "rating": ratings[i],
                "release_date": release_dates[i],
                "vote_count": vote_counts[i],
            }

        return data_dict

# Create an instance of the MovieDbAPI class
movie_db = MovieDBAPI()
data = movie_db.getData()
finalresult = movie_db.moviedb_data(data)

#Output for MovieDb API data
'''
for rank, info in finalresult.items():
    print(f"Rank: {rank}")
    print(f"Title: {info['title']}")
    print(f"Rating: {info['rating']}")
    print(f"Release Date: {info['release_date']}")
    print(f"Vote Count: {info['vote_count']}")
    print("-------------------------")
    '''