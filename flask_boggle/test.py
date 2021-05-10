from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""
        with app.test_client() as client:
            resp = client.get('/start')
            self.assertEqual(resp.status_code,200)
            self.assertIn('board',session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('nplays'))
            self.assertIn(b'High Score :',resp.data)
            self.assertIn(b'Score :',resp.data)
            self.assertIn(b'Seconds left :',resp.data)
    

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""
        with app.test_client() as client:
    
            with client.session_transaction() as sess:
                sess['board'] = [['C','A', 'T', 'T','T'],
                ['C','A', 'T', 'T','T'],
                ['C','A', 'T', 'T','T'],
                ['C','A', 'T', 'T','T'],
                ['C','A', 'T', 'T','T']]

        response = client.get('/check-word?word=cat')
        self.assertEqual(response.json['result'],'ok')

    def test_invalid_word(self):
        """Test if word is in dictionary"""
        with app.test_client() as client:
            client.get('/start')
            response = client.get('/check-word?word=impossible')
            self.assertEqual(response.json['result'],'not-on-board')

    def test_not_a_english_word(self):
        """Test if word is not a english word"""
        with app.test_client() as client:
            client.get('/start')
            response = client.get('/check-word?word=asdfglfjgkfgljk')
            self.assertEqual(response.json['result'],'not-word')
