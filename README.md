# Norwegian Analogy Test Set

This repository holds the Norwegian Analogy Test Set, created for the purpose of evaluating 
distributional semantic models. The test set was created through the translation and modification 
of the original Google Analogy Test Set developed by T. Mikolov, K. Chen, G. Corrado and J. Dean, 
[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf).

The test set - ```norwegian-analogies.txt``` - is a list of 17,807 Norwegian analogy 
questions, divided into subsets of 8,944 semantic and 8,863 syntactic questions, 
such as ```gutt jente bror søster``` and ```dårlig dårligere stor større```.

The script - ```eval.py``` - can be used for evaluating model performance in predicting analogies.
