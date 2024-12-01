import pytest
from IMDb_Data import IMBDAPI
from MovieDb_Data import MovieDBAPI
from MovieDictionary import MovieDictionary

@pytest.fixture
def imdb_api_instance():
    return IMBDAPI()

@pytest.fixture
def moviedb_api_instance():
    return MovieDBAPI()

@pytest.fixture
def movie_dict_instance():
    return MovieDictionary()

@pytest.fixture
def test_combined_data_structure(combined_data):
    assert isinstance(combined_data, dict)
    # Add more assertions as needed to ensure the structure of combined_data is correct
    assert all(isinstance(movie_info, dict) for movie_info in combined_data.values())
    assert all('rank' in movie_info for movie_info in combined_data.values())
    assert all('rating' in movie_info for movie_info in combined_data.values())
    assert all('release_date' in movie_info for movie_info in combined_data.values())
    assert all('vote_count_imdb' in movie_info for movie_info in combined_data.values())
    assert all('vote_count_moviedb' in movie_info for movie_info in combined_data.values())

def test_sorted_movies_sorting(movie_dict_instance):
    sorted_movies = movie_dict_instance.sort_combined_data()
    # Check if the sorting is done correctly
    assert sorted_movies == sorted(sorted_movies, key=lambda x: x[1]['rating'], reverse=True)
    # Add more assertions to ensure correct sorting based on other criteria

def test_total_vote_count_calculation(movie_dict_instance):
    for movie_info in movie_dict_instance.combined_data.values():
        assert 'total_vote_count' in movie_info
        assert isinstance(movie_info['total_vote_count'], int)
        assert movie_info['total_vote_count'] == movie_info['vote_count_imdb'] + movie_info['vote_count_moviedb']

def test_release_date_format(movie_dict_instance):
    for movie_info in movie_dict_instance.combined_data.values():
        release_date = movie_info['release_date']
        assert isinstance(release_date, str)
        assert len(release_date.split('-')) == 3
