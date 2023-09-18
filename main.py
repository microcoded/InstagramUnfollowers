import sys
import json


def main():
    followers_list = sys.argv[-1]
    following_list = sys.argv[-2]

    followers = []
    following = []

    with open(followers_list, 'r') as followers_f:
        followers_json = json.load(followers_f)

    with open(following_list, 'r') as following_f:
        following_json = json.load(following_f)

    for item in followers_json['relationships_following']:
        value = item['string_list_data'][0]['value']
        following.append(value)

    for item in following_json:
        value = item['string_list_data'][0]['value']
        followers.append(value)

    print('These people do not follow you back:')
    [print(e) for e in following if e not in followers]


if __name__ == "__main__":
    main()
