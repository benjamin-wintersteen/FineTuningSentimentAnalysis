# import corpus from spacy_on_corpus
from spacy_on_corpus import corpus

# import anvil server
import anvil.server

# make a corpus instance called my_corpus
my_corpus = corpus()

# YOUR ANVIL CALLABLES HERE

def run():
    """Run the server!"""  
    # connect
    anvil.server.connect("YOUR KEY HERE")
    # wait forever
    anvil.server.wait_forever()

# this says, if executing this on the command line like python server.py, run run()    
if __name__ == "__main__":
    run()