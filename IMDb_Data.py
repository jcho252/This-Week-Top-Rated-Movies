import json
import http.client

class IMBDAPI:

    def __init__(self):

        self.movieInfo = None

        self.conn = http.client.HTTPSConnection("imdb188.p.rapidapi.com")
        self.headers = {
            'X-RapidAPI-Key': "d9fd9f74d6msh2d6a91965ff58bdp13ef81jsnd578a886ecb5",
            'X-RapidAPI-Host': "imdb188.p.rapidapi.com"
        }

    def getData(self):
        self.conn.request("GET", "/api/v1/getWeekTop10", headers=self.headers)
        res = self.conn.getresponse()
        data = res.read().decode("utf-8")
        self.movieInfo= json.loads(data)

        return self.movieInfo

    def getRank(self):
        ranks = []
        for movie in self.movieInfo["data"]:
            ranks.append(movie["chartMeterRanking"]["currentRank"])
        return ranks
    def getTitle(self):
            titles = []
            for movie in self.movieInfo["data"]:
                titles.append(movie["titleText"]["text"])
            return titles

    def getRatings(self):
        ratings = []
        for movie in self.movieInfo['data']:
            ratings.append(movie["ratingsSummary"]["aggregateRating"])
        return ratings

    def getReleaseDate(self):
        releaseDates = []
        for movie in self.movieInfo["data"]:
            releaseDates.append(movie["releaseDate"])
        return releaseDates

    def getVoteCount(self):
        votecount = []
        for movie in self.movieInfo["data"]:
            votecount.append(movie["ratingsSummary"]["voteCount"])
        return votecount

    def imbd_data(self, data):

        titles = self.getTitle()
        ratings = self.getRatings()
        voteCounts = self.getVoteCount()
        releaseDates = self.getReleaseDate()
        ranks = self.getRank()

        data_dict = {}

        for rank, title, rating, voteCount, releaseDate in zip(ranks, titles, ratings, voteCounts, releaseDates):
            data_dict[rank]= {

                "title" : title,
                "ratings" : rating,
                "releaseDate" : releaseDate,
                "voteCount" : voteCount
    }
        return data_dict

imdb_api = IMBDAPI()
finalData = imdb_api.getData()
result = imdb_api.imbd_data(finalData)

#Output for the IMDb API data
'''
for rank, movie_info in result.items():
    print(f"Rank: {rank}")
    print(f"Title: {movie_info['title']}")
    print(f"Ratings: {movie_info['ratings']}")
    print(f"Release Date: {movie_info['releaseDate']}")
    print(f"Vote Count: {movie_info['voteCount']}")
    print("=" * 30)
    '''