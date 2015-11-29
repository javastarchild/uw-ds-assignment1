import sys
import json
import string

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def main():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    state_scores = {} # initialize another empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    exclude = set(string.punctuation)
    for json_string in tweet_file:
      country = ""
      state = ""
      parsed_json = json.loads(json_string)
      if 'place' in parsed_json.keys():
        if parsed_json['place'] and 'country_code' in parsed_json['place'].keys():
          country = parsed_json['place']['country_code']
        if parsed_json['place'] and 'full_name' in parsed_json['place'].keys():
          full_name = parsed_json['place']['full_name'].split(", ")
          if len(full_name) >= 2:
              state = full_name[1]
      if len(state) == 2 and country == 'US':      
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
                  if state in state_scores.keys():
                      state_scores[state] += score
                  else:
                      state_scores[state] = score
                  
    print max(state_scores, key=state_scores.get)

if __name__ == '__main__':
    main()
