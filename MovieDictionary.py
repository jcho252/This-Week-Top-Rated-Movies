from MovieDb_Data import MovieDBAPI
from IMDb_Data import IMBDAPI

class MovieDictionary:

    def __init__(self):
        self.imdb_api = IMBDAPI()
        self.movie_db_api = MovieDBAPI()
        self.combined_data = {}

    def add_imdb_data(imdb_data, combined_data):
        if not isinstance(imdb_data ,dict):
            raise ValueError("imdb_data must be a dictionary")
        
        for rank, info in imdb_data.items():
            title = info['title']
            if not title:
                raise ValueError(f"Title Mising for rank {rank}")
            
            rating = info.get('ratings')  # Get the rating value or None if it doesn't exist
            if rating is not None:  # Check if rating exists
                rating = round(rating, 2)  # Round the rating to the hundredth decimal
                rating_str = f"{rating:.2f}"  # Format the rating with exactly two decimal places
            else:
                rating_str = "N/A"  # Set to 'N/A' if rating is None
            
            release_date_dict = info['releaseDate']
            month = str(release_date_dict['month']).zfill(2)  # Add leading zero if necessary
            day = str(release_date_dict['day']).zfill(2)  # Add leading zero if necessary
            release_str = f"{month}-{day}-{release_date_dict['year']}"

            combined_data[title] = {
                'rank': rank,
                'rating': rating_str,
                'release_date': release_str,
                'vote_count_imdb': info.get('voteCount', 0),
                'vote_count_moviedb': 0  # Initialize with zero, will be updated later
            }
         

    def add_moviedb_data(movie_db_data, combined_data):
        for rank, info in movie_db_data.items():
            title = info['title']
            rating = round(info['rating'], 2)  # Round the rating to the hundredth decimal
            rating_str = f"{rating:.2f}"  # Format the rating with exactly two decimal places
            
            # Split release_date and format as month-day-year
            release_date_parts = info['release_date'].split('-')
            month = release_date_parts[1].zfill(2)  # Add leading zero if necessary
            day = release_date_parts[2].zfill(2)  # Add leading zero if necessary
            release_str = f"{month}-{day}-{release_date_parts[0]}"
            
            if title in combined_data:
                combined_data[title]['vote_count_moviedb'] = info.get('vote_count', 0)
            else:
                combined_data[title] = {
                    'rank': rank,
                    'rating': rating_str,
                    'release_date': release_str,
                    'vote_count_imdb': 0,  # Initialize with zero
                    'vote_count_moviedb': info.get('vote_count', 0)
                }

    def add_vote_counts(combined_data):
        for title, info in combined_data.items():
            total_vote_count = info['vote_count_imdb'] + info['vote_count_moviedb']
            info['total_vote_count'] = total_vote_count

    def sort_combined_data(self):
        return sorted(self.combined_data.items(), key=lambda x: x[1]['rating'], reverse=True)

    # Create instances of the IMDb and MovieDB APIs
    imdb_api = IMBDAPI()
    movie_db_api = MovieDBAPI()

    # Get movie data from IMDb
    imdb_data = imdb_api.imbd_data(imdb_api.getData())

    # Get movie data from MovieDB
    movie_db_data = movie_db_api.moviedb_data(movie_db_api.getData())

    # Combine movie data from both sources into a single dictionary
    combined_data = {}

    # Add IMDb data to combined dictionary
    add_imdb_data(imdb_data, combined_data)

    # Add MovieDB data to combined dictionary
    add_moviedb_data(movie_db_data, combined_data)

    # Add vote counts
    add_vote_counts(combined_data)

    def sort_key(item):
        rating = item[1]['rating']
        if rating == 'N/A':
            return float('-inf')  # Assign a large negative value for 'N/A' ratings
        else:
            return float(rating)

    # Sort the combined dictionary by rating in descending order
    sorted_movies = sorted(combined_data.items(), key=sort_key, reverse=True)

    # Output the sorted list of movies with rank numbers, release dates, ratings, and total vote counts
    for index, (title, info) in enumerate(sorted_movies, start=1):
        print(f"Rank: {index}")
        print(f"Title: {title}")
        print(f"Rating: {info['rating']}")
        print(f"Release Date: {info['release_date']}")
        print(f"Total Vote Count: {info['total_vote_count']}")
        print('=' * 30)
