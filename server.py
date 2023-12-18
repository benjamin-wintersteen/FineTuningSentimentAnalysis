# import corpus from spacy_on_corpus
from spacy_on_corpus import corpus

# import anvil server
import anvil.server

# make a corpus instance called my_corpus
my_corpus = corpus()
my_corpus = corpus.build_corpus('creator.jsonl', my_corpus= my_corpus)

# YOUR ANVIL CALLABLES HERE
@anvil.server.callable
def get_doc_sentiment_markdown(doc_id):
    """Gets markdown of sentiments
        :param doc_id: the id of a spaCy doc made from the text in the document
        :type doc: str
        :returns: a markdown table
        :rtype: string
        """
    return my_corpus.render_doc_sentiments(doc_id)
def run():
    """Run the server!"""  
    # connect
    anvil.server.connect("server_UVAGO47DXC6B5WUYDX5MBGFK-MJL5RFG3YNWLGHEB")
    # wait forever
    anvil.server.wait_forever()


# this says, if executing this on the command line like python server.py, run run()    
if __name__ == "__main__":
    run()