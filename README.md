# Finetuning Transformer Models

# Project 5

## Name

## Class year

## Extension(s) - Describe your extension(s) here

## Resources - Who or what did you use to finish this project deliverable?

-----------------------------------------------------------------------------------------------------------------------------------------------
*Please do not edit below this line!*
-----------------------------------------------------------------------------------------------------------------------------------------------

## Project Description

The goals of this assignment are:
* To work with the object oriented version of our corpus code.
* To modify a web app that we can use to analyze text data.
* To finetune a transformer model and write a model card for it.

Here are the steps you should do to successfully complete this project:
1. Check out the assignment from Github. 
2. Make a codespace with at least 8GB of RAM (preferably more!).
3. Copy your `spacy_on_corpus.py` from project 4b.
4. Copy the anvil callable functions and your API key from project 4b into the file `server.py`.
5. Complete all the instructions in this notebook. Make sure to answer all questions, and to commit the notebook in a "run" state!
6. Edit the README.md file. Provide your name, your class year, links to/descriptions of any extensions and a list of resources you used. 
7. Commit your code often. We will take the last commit before the deadline as your submission of the project.

Possible extensions (from least points to most points):
* Modify the `render_document_sentiment` method you implemented for this project to have a third column, `Aspect`. Fill it with the first keyphrase extracted from the sentence using the keyphrase extraction algorithm from project 4b, or with the first noun chunk in the sentence. Explain whether this is better than the baseline implementation for this project, and why.
* Finetune a different model (other than distilbert-cased) for the sentence sentiment task.
* Finetune a transformer model for a different NLP task. Add it to your web app.
* Your other ideas are welcome! If you'd like to discuss one with Dr Stent, feel free.

## Project 5 Rubric

- [] File spacy_on_corpus.py is complete with new functionality and is commented. (4 points)
- [] File server.py is complete with new functionality and is commented. (4 points)
- [] Notebook is code-complete and committed in a run state. (4 points)
- [] All requested screenshots are provided in notebook. (1 point)
- [] All ten questions are answered. (5 points)
- [] Model card is completed. (5 points)
- [] Student made meaningful commit messages. (1 pt)
- [] Readme has student's name, class year and resources student used. (1 pt)
- [] Extension (1-2 points for a start; 3-4 points for a complete extension; 5 points for a surprising and creative extension)

### Comments from grader
