from collections import defaultdict
import requests
import os

url = "https://adventofcode.com/2024/day/5/input"
session_cookie = os.environ.get("SESSION_COOKIE")
if not session_cookie:
    raise ValueError("Required env variable: SESSION_COOKIE for input requests")
cookies = dict(session=session_cookie)
r = requests.get(url, cookies=cookies)

res = r.text.strip().split('\n')

rules = [l for l in res if '|' in l]
updates = [l for l in res if not '|' in l and l.strip()]

def create_rule_dict(rules):
    rules_dict = defaultdict(list)

    for rule in rules:
        x,y = rule.split('|')
        rules_dict[x].append(y)
    return rules_dict

rules_dict = create_rule_dict(rules)

def get_true_update(update, rules_dict):
    numbers = update.split(',')
    prev = []
    for i in range(len(numbers)):
        prev.append(numbers[i])
        next = numbers[i+1:]
        curr_rul = rules_dict.get(numbers[i])
        if (curr_rul):
            for rule_number in curr_rul:
                if not (rule_number in next) and (rule_number in prev):
                    return False
    return True

true_updates = []
for update in updates:
    if (get_true_update(update, rules_dict)):
        true_updates.append(update)

middle = 0
for u in true_updates:
    n = u.split(',')
    middle+=int(n[len(n)//2])

print(middle)
