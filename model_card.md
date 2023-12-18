# ModelCard for \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

## Introduction

This model card template is taken directly from Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., ... & Gebru, T. (2019, January). Model cards for model reporting. In *Proceedings of the Conference on Fairness, Accountability, and Transparency.* (pp. 220-229).

# Model Details

- **Person or organization developing model**:
Benjamin Wintersteen
- **Model date**:
12/8/23
- **Model version**:
distilbert-base-cased
- **Model type**:
Tensor Type
- **Paper or other resource for more information**:
https://arxiv.org/abs/1910.01108
- **Citation details**:
@article{Sanh2019DistilBERTAD,
  title={DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
  author={Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
  journal={ArXiv},
  year={2019},
  volume={abs/1910.01108}
}
- **License**:
apache-2.0
- **Feedback on the model**:
I thought it made lots of sense

# Intended Use

- **Primary intended uses:**
evaluating binary sentence sentiments.
- **Primary intended users:**
Folks hoping to run evaluations on sentences in a corpus
- **Out-of-scope uses:**
Text generation

# Factors

- **Relevant factors:**
epochs and amount of data finetuned on
- **Evaluation factors:**
accuracy, confidence score
# Metrics

- **Model performance measures:**
accuracy
- **Decision thresholds:**
confidence score
- **Approaches to uncertainty and variability:**
lower confidence score, binary so uncertainty will just be between two. 

# Evaluation Data

- **Datasets:**
Wikipedia, BookCorpus
- **Motivation:**
loss function
- **Preprocessing:**
lowercased and tokenized with vocab of 30,000
# Training Data

- **Datasets:**
Wikipedia, BookCorpus
- **Motivation:**
loss function
- **Preprocessing:**
90 hours

# Quantitative Analyses

- **Unitary results:**
only judged backed on accuracy
- **Intersectional results:**
There is no available comparison between the intersection of evaluated factors
# Ethical Considerations
There is some potential for bias 
# Caveats and Recommendations
