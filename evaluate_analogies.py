# -*- coding: utf-8 -*- 

import sys
import logging
from gensim.models.keyedvectors import KeyedVectors

def evaluate_analogies(model, analogies, restriction):
	""" Compute accuracy on the analogy test set. """

	accuracy = model.accuracy(analogies, restrict_vocab=int(restriction), case_insensitive=True)

	sem_correct = sum((len(accuracy[i]['correct']) for i in range(5)))
	sem_incorrect = sum(len(accuracy[i]['incorrect']) for i in range(5))
	sem_total = sem_correct + sem_incorrect	
	sem_accuracy = (sem_correct/sem_total)*100
	result_sem = 'Semantic: {}/{}, '.format(sem_correct, sem_total), 'Accuracy: {0:.1f}%'.format(sem_accuracy)
	logging.info(result_sem)

	syn_correct = sum((len(accuracy[i]['correct']) for i in range(5, len(accuracy)-1)))
	syn_incorrect = sum((len(accuracy[i]['incorrect']) for i in range(5, len(accuracy)-1)))
	syn_total = syn_correct + syn_incorrect
	syn_accuracy = (syn_correct/syn_total)*100
	result_syn = 'Syntactic: {}/{}, '.format(syn_correct, syn_total), 'Accuracy: {0:.1f}%'.format(syn_accuracy)
	logging.info(result_syn)

def main():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	
	analogies = 'norwegian-analogies.txt' 
	model_path = sys.argv[1]
	restriction = sys.argv[2] # Questions including a word not in the 'restriction' most frequent words are ignored
	
	model = KeyedVectors.load_word2vec_format(model_path, binary=False)
	evaluate_analogies(model, analogies, restriction)

if __name__ == '__main__':
    main()