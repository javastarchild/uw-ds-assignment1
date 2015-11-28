import sys
import json
import string

# -*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    new_scores = {} # initialize another empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    exclude = set(string.punctuation)
    for json_string in tweet_file:
      parsed_json = json.loads(json_string)
      if 'text' in parsed_json.keys():
        text = parsed_json['text']
        text = ''.join(ch for ch in text if ch not in exclude)
        # print(parsed_json['id'])
        # print(text.encode('utf-8'))
        words = text.split()
        score = 0
        tmp_scores = {} # initialize another empty dictionary
        for word in words:
          if not word.startswith( ("#", "@", "http") ):
              if isEnglish(word):
                word = word.encode('utf-8')
                word = word.lower()
                # print(word)
                # find new un-scored word
                if word in scores.keys():
                  # existing word so update score
                  score = score + scores[word]
                else:
                  # new word so save for making new score
                  tmp_scores[word] = 0
      # print score
      # now set all new words just found to score of current tweet
      for word in tmp_scores.keys():
          if word in new_scores.keys():
             new_scores[word] = new_scores[word] + score
          else:
             new_scores[word] = score
    # done now print new scores
    # print(new_scores)
    for word in new_scores.keys():
        score = new_scores[word]
        print word, score
if __name__ == '__main__':
    main()
