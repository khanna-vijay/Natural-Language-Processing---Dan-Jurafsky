import math

import nltk
nltk.download('brown')
from nltk.corpus import brown

def collect_probabilities(_samples):
    # collect frequency of tag types
    tag_freq = {}
    # collect frequency of words under a tag
    word_per_tag_freq = {}
    # bigram based on tag types
    bigram = {}
    # initial probability distributions
    pi = {}
    total_start = 0
    samples_len = len(_samples)

    # generate tag_freq, pi, and word_per_tag_freq first
    for i in range(samples_len):
        sample = _samples[i]
        has_next = i + 1 < samples_len

        # collect data for pi
        if has_next:
            if _samples[i + 1][1] not in pi:
                pi.update({_samples[i + 1][1]: 2})
            else:
                pi[_samples[i + 1][1]] += 1
            total_start += 1

        # count tag for tag_freq
        if sample[1] not in tag_freq:
            tag_freq.update({sample[1]: 2})
            word_per_tag_freq.update({sample[1]: {sample[0]: 2}})
        else:
            tag_freq[sample[1]] += 1
            if sample[0] not in word_per_tag_freq[sample[1]]:
                word_per_tag_freq[sample[1]].update({sample[0]: 2})
            else:
                word_per_tag_freq[sample[1]][sample[0]] += 1

    # create a matrix for bigram
    for tag_0 in tag_freq:
        bigram.update({tag_0: {}})
        for tag_1 in tag_freq:
            bigram[tag_0].update({tag_1: 1})

    # generate bigram counts
    for i in range(samples_len):
        sample = _samples[i]
        has_next = i + 1 < samples_len

        if has_next:
            next_sample = _samples[i + 1]
            bigram[sample[1]][next_sample[1]] += 1

    return tag_freq, word_per_tag_freq, bigram, pi

def viterbi(_samples, _tag_freq, _word_per_tag_freq, _bigram, _init_dist):

    # process every sentence in the test set
    # use '.' as indicator that a sentence is over
    test_size = len(_samples)
    current_index = 0
    is_correct = 0
    while current_index < test_size:

        # find the boundry of a sentence
        sentence = []
        hidden_state = []
        last_token = ''
        while last_token != '.' and current_index < test_size:
            sentence.append(_samples[current_index][0])
            hidden_state.append(_samples[current_index][1])
            last_token = sentence[-1]
            current_index += 1

        # sentence is collected at this point

        # initialization step
        path_probability = {}
        backpointer = {}
        for tag in init_dist:

            path_probability.update({tag: []})
            backpointer.update({tag: [0]})

            # initial distribution of this tag
            pi_tag = init_dist[tag]

            # b_word is the probability of the word being generated by this tag
            if sentence[0] in _word_per_tag_freq[tag]:
                b_word = _word_per_tag_freq[tag][sentence[0]] / _tag_freq[tag]
            else:
                b_word = 2.2250738585072014e-100

            path_probability[tag].append(math.log(pi_tag * b_word, 10))

        # recursion step
        T = len(sentence)
        for i in range(1, T):
            for tag in init_dist:

                if sentence[i] in _word_per_tag_freq[tag]:
                    b_word = _word_per_tag_freq[tag][sentence[i]] / _tag_freq[tag]
                else:
                    b_word = 2.2250738585072014e-100

                # search the maximum value of
                # viterbi[s', t-1] * a(s|s') *b_s(o_t)
                best_trans_prob = -2.2250738585072014e+308
                best_trans_tag = ''
                for prev_tag in init_dist:

                    if prev_tag in _bigram and tag in _bigram[prev_tag]:
                        transitional_prob = _bigram[prev_tag][tag] / _tag_freq[prev_tag]
                    else:
                        transitional_prob = 2.2250738585072014e-100

                    prob = path_probability[prev_tag][i - 1] + math.log(transitional_prob * b_word, 10)

                    if prob > best_trans_prob:
                        best_trans_prob = prob
                        best_trans_tag = prev_tag

                # print(f'max_val: {max_val}')
                path_probability[tag].append(best_trans_prob)
                backpointer[tag].append(best_trans_tag)

        # termination step
        best_path_prob = -2.2250738585072014e+308
        best_path_pointer = None
        for tag in init_dist:
            if path_probability[tag][T - 1] > best_path_prob:
                best_path_prob = path_probability[tag][T - 1]
                best_path_pointer = tag

        predictions = [best_path_pointer]

        for i in reversed(range(1, T)):
            prev_tag = predictions[-1]
            predictions.append(backpointer[prev_tag][i])

        predictions.reverse()
        print(f'sentence:       {sentence}')
        print(f'hidden s:       {hidden_state}')
        print(f'predictions:    {predictions}')

        for i in range(len(predictions)):
            if predictions[i] == hidden_state[i]: is_correct += 1

    print(f'accuracy: {is_correct / test_size}')


if __name__ == "__main__":

    CORPUS = brown.tagged_words(categories='news', tagset='universal')
    CORPUS_SIZE = len(brown.tagged_words(categories='news'))

    CUT_OFF = math.floor(CORPUS_SIZE * 0.75)

    # section off training and testing lists from corpus
    training_list = CORPUS[:CUT_OFF]
    testing_list = CORPUS[CUT_OFF:]

    tag_frequency, word_per_tag_frequency, tag_bigram, init_dist = collect_probabilities(training_list)
    print(init_dist)
    viterbi(testing_list, tag_frequency, word_per_tag_frequency, tag_bigram, init_dist)






