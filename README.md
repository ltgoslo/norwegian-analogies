# The Norwegian Analogy Test Set

This repository holds the Norwegian Analogy Test Set, defined for evaluating the task of analogical 
reasoning. The test set was created by semiautomatically translating and adapting the existing 
[Google analogies test set](https://arxiv.org/pdf/1301.3781.pdf) from English to Norwegian.

## Format

`norwegian-analogies.txt` comprises a total of 17,807 Norwegian analogy questions divided into 
semantic and syntactic subsets. The semantic subset includes 8,944 analogies, such as `gutt jente bror søster`. 
The syntactic subset includes 8,863 analogies, such as `dårlig dårligere stor større`. 

## Evaluation

`evaluate_analogies.py` can be used for evaluating model performance in predicting analogies.
In order for the script to work, [gensim](https://radimrehurek.com/gensim/) must be installed. 
Further, the `model` must be compatible with the original [word2vec](https://code.google.com/archive/p/word2vec/)
implementation and provided in text format. Analogy questions including a word not in the `restriction` 
most frequent words are ignored.

### Example

`python evaluate_analogies.py <model> <restriction>`

## Citing

If you publish work that uses or references this resource, please cite the following 
[master's thesis](https://www.duo.uio.no/handle/10852/61756): 

```
@MastersThesis{Stadsnes18,
  author    =     {Stadsnes, Cathrine},
  title     =     {Evaluating Semantic Vectors for Norwegian},
  school    =     {University of Oslo},
  year      =     {2018}
}
```

Or this [NIK article](http://ojs.bibsys.no/index.php/NIK/article/view/490): 

```
Evaluating Semantic Vectors for Norwegian
Cathrine Stadsnes, Lilja Øvrelid, Erik Velldal
2018
http://ojs.bibsys.no/index.php/NIK/article/view/490
```
