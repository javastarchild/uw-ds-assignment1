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
    tweet_file = open(sys.argv[1])
    terms_counts = {} # initialize empty dictionary
    exclude = set(string.punctuation)
    total_terms = 0
    for json_string in tweet_file:
      parsed_json = json.loads(json_string)
      if 'text' in parsed_json.keys():
        text = parsed_json['text']
        text = ''.join(ch for ch in text if ch not in exclude)
        # print(parsed_json['id'])
        # print(text.encode('utf-8'))
        words = text.split()
        for word in words:
          if not word.startswith( ("#", "@", "http") ):
              if isEnglish(word):
                word = word.encode('utf-8')
                word = word.lower()
                # print(word)
                # find new words
                # increment total words counter
                total_terms += 1
                if word in terms_counts.keys():
                  # existing word so update count
                  terms_counts[word] += 1
                else:
                  # new word so save with count = 1
                  terms_counts[word] = 1
      # print terms_counts
    # done now print counts / total terms
    # print terms_counts
    # print 'Count = ', total_terms
    for word in terms_counts.keys():
        freq = terms_counts[word] / float(total_terms)
        print word, freq
if __name__ == '__main__':
    main()
