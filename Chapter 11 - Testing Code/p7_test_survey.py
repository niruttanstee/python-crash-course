# Using unittest and assert methods to test AnonymousSurvey
import unittest
from p5_survey import AnonymousSurvey

class TestAnonymouseSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        # We'll use assertIn(item, list) Verify that item in list.
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses) # Gets the my_survey list
    
    # Let's create a function to test more than one responses and check that
    # it's stored correctly.
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
    
        
if __name__ == '__main__':
    unittest.main()