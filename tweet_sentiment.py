import sys
import json
import string

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
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
        words = text.split(" ")
        score = 0
        for word in words:
          if not word.startswith("#"):
            if not word.startswith("@"):
              word = word.encode('utf-8')
              word = word.lower()
              # print(word)
              if word in scores.keys():
                score = score + scores[word]
      print score

if __name__ == '__main__':
    main()
