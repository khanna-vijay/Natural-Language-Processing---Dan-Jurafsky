# Chapter 8

__8.1__ Find one tagging error in each of the following sentences that are tagged with the Penn Treebank tagset:
1. ```I/PRP need/VBP a/DT flight/NN from/IN Atlanta/NN```
2. ```Does/VBZ this/DT flight/NN serve/VB dinner/NNS```
3. ```I/PRP have/VB a/DT friend/NN living/VBG in/IN Denver/NNP```
4. ```Can/VBP you/PRP list/VB the/DT nonstop/JJ afternoon/NN flights/NNS```

/// RESPONSE

__8.2__ Use the Penn Treebank tagset to tag each word in the following sentences from Damon Runyon’s short stories. You may ignore punctuation. Some of these are quite difficult; do your best.
1. It is a nice night.
2. This crap game is over a garage in Fifty-second Street. . .
3. . . . Nobody ever takes the newspapers she sells . . .
4. He is a tall, skinny guy with a long, sad, mean-looking kisser, and a mournful voice.
5. . . . I am sitting in Mindy’s restaurant putting on the gefillte fish, which is a dish I am very fond of, . . .
6. When a guy and a doll get to taking peeks back and forth at each other, why there you are indeed.

/// RESPONSE

__8.3__ Now compare your tags from the previous exercise with one or two friend’s answers. On which words did you disagree the most? Why?

/// RESPONSE

__8.4__ Implement the “most likely tag” baseline. Find a POS-tagged training set, and use it to compute for each word the tag that maximizes $p(t|w)$. You will need to implement a simple tokenizer to deal with sentence boundaries. Start by assuming that all unknown words are NN and compute your error rate on known and unknown words. Now write at least five rules to do a better job of tagging unknown words, and show the difference in error rates.

/// RESPONSE

__8.5__ Build a bigram HMM tagger. You will need a part-of-speech-tagged corpus. First split the corpus into a training set and test set. From the labeled training set, train the transition and observation probabilities of the HMM tagger directly on the hand-tagged data. Then implement the Viterbi algorithm so you can decode a test sentence. Now run your algorithm on the test set. Report its error rate and compare its performance to the most frequent tag baseline.

/// RESPONSE

__8.6__ Do an error analysis of your tagger. Build a confusion matrix and investigate the most frequent errors. Propose some features for improving the performance of your tagger on these errors.

/// RESPONSE

__8.7__ Develop a set of regular expressions to recognize the character shape features described on page 176.

/// RESPONSE

__8.8__ The BIO and other labeling schemes given in this chapter aren’t the only possible one. For example, the B tag can be reserved only for those situations where an ambiguity exists between adjacent entities. Propose a new set of BIO tags for use with your NER system. Experiment with it and compare its performance with the schemes presented in this chapter.

/// RESPONSE

__8.9__ Names of works of art (books, movies, video games, etc.) are quite different from the kinds of named entities we’ve discussed in this chapter. Collect a list of names of works of art from a particular category from a Web-based source (e.g., gutenberg.org, amazon.com, imdb.com, etc.). Analyze your list and give examples of ways that the names in it are likely to be problematic for the techniques described in this chapter.

/// RESPONSE

__8.10__ Develop an NER system specific to the category of names that you collected in the last exercise. Evaluate your system on a collection of text likely to contain instances of these named entities.

/// RESPONSE



