# Testing a class.

# Similar to testing a function as much of the work involves testing the
# behaviour of the methods in the class.

# There are a few differences however. Let's consider a class that helps
# administer anonymous surveys.

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store response."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_responses):
        """Store a single response to the survey."""
        self.responses.append(new_responses)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
            
# We'll test the class by making a program that uses the class in language_survey