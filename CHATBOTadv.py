from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import LevenshteinDistance
from chatterbot.response_selection import get_first_response

class AdvancedChatBot:
    def __init__(self):
        # Create a new chatbot instance
        self.chatbot = ChatBot(
            'AdvancedBot',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            input_adapter='chatterbot.input.TerminalAdapter',
            output_adapter='chatterbot.output.TerminalAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'statement_comparison_function': LevenshteinDistance,
                    'response_selection_method': get_first_response,
                    'default_response': 'I am sorry, but I do not understand.',
                },
                {
                    'import_path': 'chatterbot.logic.MathematicalEvaluation',
                }
            ],
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace',
                'chatterbot.preprocessors.unescape_html',
            ],
            database_uri='sqlite:///database.db'  # Use SQLite as a database
        )

        # Create a new trainer
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)

        # Train the chatbot on English language data
        self.trainer.train('chatterbot.corpus.english')

    def get_response(self, user_input):
        # Get a response from the chatbot
        response = self.chatbot.get_response(user_input)
        return str(response)

    def chat(self):
        print("Chatbot: Hello! I'm your advanced chatbot.")
        while True:
            user_input = input("You: ")

            # Check if the user wants to exit
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye!")
                break

            # Get a response from the chatbot
            response = self.get_response(user_input)
            print("Chatbot:", response)

# Create an instance of the AdvancedChatBot class
advanced_chatbot = AdvancedChatBot()

# Start the chat loop
advanced_chatbot.chat()
