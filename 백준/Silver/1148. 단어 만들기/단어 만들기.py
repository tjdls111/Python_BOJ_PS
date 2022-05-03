import sys
from collections import defaultdict
input=sys.stdin.readline

my_dict = []

def check(keyword, dictionary):
    keyword_idx = 0
    dictionary_idx = 0
    while keyword_idx < len(keyword) and dictionary_idx < len(dictionary):
        if keyword[keyword_idx] == dictionary[dictionary_idx]:
            keyword_idx += 1
            dictionary_idx += 1
            if keyword_idx == len(keyword):
                return True
        else:
            dictionary_idx += 1
            if dictionary_idx == len(dictionary):
                return False
    return False

while True:
    tmp = input().rstrip()
    if tmp == '-':
        break
    else:
        my_dict.append(sorted(list(tmp)))

while True:
    tmp = input().rstrip()
    sorted_tmp = sorted(list(tmp))
    if tmp == '#':
        break
    else:
        word_use_count = defaultdict(int)
        for word in my_dict: # 사전의 단어를 하나씩 보면서
            # 그 단어 만들 수 있으면
            # if word.issubset(tmp):
            if check(word,sorted_tmp):
                for w in set(word):
                    word_use_count[w] += 1
    # 0번 등장한 알파벳 고려하기
    for i in set(tmp):
        if i not in word_use_count:
            word_use_count[i] = 0

    # 젤 많이 만든 알파벳
    most_popular_cnt = max(word_use_count.values())
    least_popular_cnt = min(word_use_count.values())
    most_popular_alp = []
    least_popular_alp = []
    for key, val in word_use_count.items():
        if val == most_popular_cnt:
            most_popular_alp.append(key)
        if val == least_popular_cnt:
            least_popular_alp.append(key)

    # 출력
    print(''.join(sorted(least_popular_alp)), end=' ')
    print(least_popular_cnt,end=' ')
    print(''.join(sorted(most_popular_alp)),end=' ')
    print(most_popular_cnt)
