import sys
import json
import operator
import string

def main():
    tweet_file = open(sys.argv[1])
    hashtags_counts = {} # initialize empty dictionary
    for json_string in tweet_file:
      parsed_json = json.loads(json_string)
      if 'entities' in parsed_json.keys():
        hashtags = parsed_json['entities']['hashtags']
        # print(parsed_json['id'])
        for hashtag in hashtags:
            # print hashtag
            text = hashtag['text']
            if text in hashtags_counts.keys():
              # existing hashtag so update count
              hashtags_counts[text] += 1
            else:
              # new hashtag so save with count = 1
              hashtags_counts[text] = 1
    sorted_hashtags = sorted(hashtags_counts.items(), key=operator.itemgetter(1), reverse=True)
    for item in sorted_hashtags[:10]:
      print item[0], item[1]
if __name__ == '__main__':
    main()
