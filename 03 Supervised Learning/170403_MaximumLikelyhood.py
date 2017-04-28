sample_memo = '''
Milt, we're gonna need to go ahead and move you downstairs into storage B. We have some new people 
coming in, and we need all the space we can get. So if you could just go ahead and pack up your stuff 
and move it down there, that would be terrific, OK?
Oh, and remember: next Friday... is Hawaiian shirt day. So, you know, if you want to, go ahead and wear 
a Hawaiian shirt and jeans.
Oh, oh, and I almost forgot. Ahh, I'm also gonna need you to go ahead and come in on Sunday, too...
Hello Peter, whats happening? Ummm, I'm gonna need you to go ahead and come in tomorrow. So if you could be here 
around 9 that would be great, mmmk... oh oh! and I almost forgot ahh, I'm also gonna need you to 
go ahead and come in on Sunday too, kay. We ahh lost some people this week and ah, we sorta need to play 
catch up.
'''


#
#   Maximum Likelihood Hypothesis
#
#
#   In this quiz we will find the maximum likelihood word based on the preceding word
#
#   Fill in the NextWordProbability procedure so that it takes in sample text and a word,
#   and returns a dictionary with keys the set of words that come after, whose values are
#   the number of times the key comes after that word.
#
#   Just use .split() to split the sample_memo text into words separated by spaces.

#def NextWordProbability(sampletext, word):
    #a = sampletext.split

def NextWordProbability(sampletext,word):
    words = sampletext.split(' ')
    dict = {}
    for index, val in enumerate(words):
        next_w = words[index + 1]
        if val == word:
            if next_w in dict:
                dict[next_w] += 1
            else:
                dict[next_w] = 1

        if index == len(words) - 2:
            sum_all = 0
            for i in dict:
                sum_all = sum_all + dict[i]

            for key in dict:
                dict[key] = (float)(dict[key]) / sum_all
            return dict


a = NextWordProbability(sample_memo, 'be')

def NextWordProbability2(sampletext,word):
    total_words = sampletext.split()
    new_dict = {}

    for i in range(len(total_words) - 1):
        if total_words[i] == word:
            new_dict[total_words[i+1]] = new_dict.get(total_words[i+1],0) + 1

    sum_all = 0

    for i in new_dict:
        sum_all = sum_all + new_dict[i]

    for key in new_dict:
        new_dict[key] = (float)(new_dict[key])/sum_all
    return new_dict

a1 = NextWordProbability2(sample_memo, 'be')

print a
print a1