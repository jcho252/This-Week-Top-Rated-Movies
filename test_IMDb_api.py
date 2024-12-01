import pytest
from IMDb_Data import IMBDAPI

@pytest.fixture(scope="module")
def imdb_api():
    return IMBDAPI()

def test_get_data(imdb_api):
    data = imdb_api.getData()
    assert isinstance(data, dict)
    assert "data" in data

def test_get_rank(imdb_api):
    ranks = imdb_api.getRank()
    assert isinstance(ranks, list)
    assert all(isinstance(rank, int) for rank in ranks)

def test_get_title(imdb_api):
    titles = imdb_api.getTitle()
    assert isinstance(titles, list)
    assert all(isinstance(title, str) for title in titles)

def test_get_ratings(imdb_api):
    ratings = imdb_api.getRatings()
    # Check if ratings is None
    assert ratings is not None, "No ratings returned by getRatings()"
    # Check if ratings is a list
    assert isinstance(ratings, list), "Ratings is not a list"
    # Check if all elements in ratings are floats, ints, or None
    assert all(rating is None or isinstance(rating, (float, int)) for rating in ratings), "Non-float or non-int ratings found"


def test_get_release_date(imdb_api):
    release_dates = imdb_api.getReleaseDate()
    # Check if release_dates is None
    assert release_dates is not None, "No release dates returned by getReleaseDate()"
    # Check if release_dates is a list
    assert isinstance(release_dates, list), "Release dates is not a list"
    # Check if all elements in release_dates are dicts or None
    assert all(date is None or isinstance(date, dict) for date in release_dates), "Non-dict release dates found"

def test_get_vote_count(imdb_api):
    vote_counts = imdb_api.getVoteCount()
    assert isinstance(vote_counts, list)
    assert all(isinstance(count, int) for count in vote_counts)

def test_imported_data(imdb_api):
    data = imdb_api.getData()
    result = imdb_api.imbd_data(data)

    expected_titles = imdb_api.getTitle()
    expected_ratings = imdb_api.getRatings()
    expected_vote_counts = imdb_api.getVoteCount()
    expected_release_dates = imdb_api.getReleaseDate()
    expected_ranks = imdb_api.getRank()

     # Assertion
    assert len(result) == len(expected_titles)
    for rank, title, rating, vote_count, release_date in zip(expected_ranks, expected_titles, expected_ratings, expected_vote_counts, expected_release_dates):
        assert result[rank] == {"title": title, "ratings": rating, "releaseDate": release_date, "voteCount": vote_count}