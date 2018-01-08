# The Norwegian Analogy Test Set

This repository holds the Norwegian Analogy Test Set, created for the purpose of evaluating 
distributional semantic models. The test set was created through the translation and modification 
of the original Google Analogy Test Set developed by T. Mikolov, K. Chen, G. Corrado and J. Dean, 
[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf).

## Format

The test set ```norwegian-analogies.txt``` is a list of 17,807 Norwegian analogy 
questions, divided into subsets of 8,944 semantic and 8,863 syntactic questions, 
such as ```gutt jente bror søster``` and ```dårlig dårligere stor større```.

## Evaluation

The script ```evaluate_analogies.py``` can be used for evaluating model performance in predicting analogies.
In order for the script to work, [gensim](https://radimrehurek.com/gensim/) must be installed. 
Further, the `<model>` must be compatible with the original [word2vec](https://code.google.com/archive/p/word2vec/)
implementation and provided in text format (or one can modify the script). 
The second argument `<vocabulary restriction>` limits the number of analogy questions considered, for example 30000. 
Questions including a word not in this number of most frequent words are ignored.

### Example

```python evaluate_analogies.py <model> <vocabulary restriction>```
