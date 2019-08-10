#!/usr/bin/env python3

'''
Viết script lấy top **N** câu hỏi được vote cao nhất của tag **LABEL** trên stackoverflow.com.
In ra màn hình: Title câu hỏi, link đến câu trả lời được vote cao nhất

Link API: https://api.stackexchange.com/docs

Dạng của câu lệnh:

  python3 so.py N LABEL
'''


import requests
import json
import sys


def solve(N, L):
    link_api = "https://api.stackexchange.com/2.2/questions?pagesize={}&order=desc&sort=votes&tagged={}&site=stackoverflow".format(N, L)  # NOQA
    resp = requests.get(link_api)
    data = json.loads(resp.text)

    n = 0
    result = []
    for i in data['items']:
        n += 1
        title = i['title']
        score = i['score']
        url = i['link']
        result.append("Question #{}:\n\tTitle: {}\n\tVote: {}\n\tLink: {}\n\n".format(
            n, title, score, url))
    result = "".join(result)
    
    if result == '':
        print("No result found! Try another topic Label!")
        
    return result


def main():
    if len(sys.argv) == 3:
        print("Top {} most voted questions:\n".format(sys.argv[1]))
        print(solve(sys.argv[1], sys.argv[2]))
    else:
        print("Please follow the format as Python3 {} N L\n\tN: Top-voted question\n\tL: Label you want to search".format(sys.argv[0]))  # NOQA
        print("Example: python3 {} 3 machine-learning".format(sys.argv[0]))


if __name__ == "__main__":
    main()
