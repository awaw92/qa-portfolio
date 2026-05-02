import pytest
from django.test import Client


@pytest.mark.django_db
def test_quiz_starts_with_zero_score():
    client = Client()

    response = client.post('/', {
        'player_name': 'Test',
        'player_country': 'PL',
        'player_age': '25',
        'level': 'easy'
    })

    assert client.session['score'] == 0
