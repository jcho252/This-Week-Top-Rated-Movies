import pytest
from MovieDb_Data import MovieDBAPI

@pytest.fixture(scope="module")
def movie_api_instance():
    return MovieDBAPI()

def test_get_data(movie_api_instance):
    data = movie_api_instance.getData()
    assert data is not None

def test_get_rank(movie_api_instance):
    ranks = movie_api_instance.get_rank()
    assert isinstance(ranks, list)
    assert len(ranks) == 10

def test_get_title(movie_api_instance):
    titles = movie_api_instance.get_title()
    assert isinstance(titles, list)
    assert len(titles) == 10

def test_get_ratings(movie_api_instance):
    ratings = movie_api_instance.get_ratings()
    assert isinstance(ratings, list)
    assert len(ratings) == 10

def test_get_release_date(movie_api_instance):
    release_dates = movie_api_instance.get_release_date()
    assert isinstance(release_dates, list)
    assert len(release_dates) == 10

def test_get_vote_count(movie_api_instance):
    vote_counts = movie_api_instance.get_vote_count()
    assert isinstance(vote_counts, list)
    assert len(vote_counts) == 10

def test_get_description(movie_api_instance):
    descriptions = movie_api_instance.get_description()
    assert isinstance(descriptions, list)
    assert len(descriptions) == 10

def test_imported_data(movie_api_instance):
    # Get data from the API
    data = movie_api_instance.getData()
    
    # Process the data
    result = movie_api_instance.moviedb_data(data)
    
    # Get expected data from the API
    expected_titles = movie_api_instance.get_title()
    expected_ratings = movie_api_instance.get_ratings()
    expected_vote_counts = movie_api_instance.get_vote_count()
    expected_release_dates = movie_api_instance.get_release_date()
    expected_ranks = range(1, len(expected_titles) + 1)  # Generate ranks starting from 1
    
    # Assertion
    assert len(result) == len(expected_titles)
    for rank, title, rating, vote_count, release_date in zip(expected_ranks, expected_titles, expected_ratings, expected_vote_counts, expected_release_dates):
        assert rank in result  # Check if the rank exists in the result dictionary
        assert result[rank] == {"title": title, "rating": rating, "release_date": release_date, "vote_count": vote_count}