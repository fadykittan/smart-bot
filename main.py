import logging
from genai_manager import GenaiManager

# TODO: Configure logging
logging = logging.getLogger(__name__)

def bot():
    ai = GenaiManager()
    while True:
        message = input("Ask me anything: ")
        if message == 'stop':
            break
        response = ai.chat(message)
        print(response)

if __name__ == "__main__":
    bot()


