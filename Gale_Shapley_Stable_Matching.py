male_preferences = {
    'm1': ['w1', 'w6', 'w5', 'w2', 'w4', 'w3', 'w7'],
    'm2': ['w1', 'w4', 'w3', 'w2', 'w7', 'w6', 'w5'],
    'm3': ['w7', 'w6', 'w5', 'w1', 'w2', 'w4', 'w3'],
    'm4': ['w4', 'w3', 'w1', 'w2', 'w5', 'w7', 'w6'],
    'm5': ['w3', 'w2', 'w1', 'w4', 'w5', 'w6', 'w7'],
    'm6': ['w7', 'w6', 'w5', 'w4', 'w3', 'w2', 'w1'],
    'm7': ['w6', 'w7', 'w4', 'w5', 'w3', 'w2', 'w1']
}

female_preferences = {
    'w1': ['m2', 'm6', 'm5', 'm1', 'm4', 'm3', 'm7'],
    'w2': ['m1', 'm2', 'm5', 'm4', 'm3', 'm6', 'm7'],
    'w3': ['m5', 'm3', 'm1', 'm2', 'm4', 'm7', 'm6'],
    'w4': ['m4', 'm3', 'm1', 'm2', 'm5', 'm7', 'm6'],
    'w5': ['m2', 'm3', 'm4', 'm1', 'm7', 'm6', 'm5'],
    'w6': ['m7', 'm6', 'm5', 'm1', 'm2', 'm4', 'm3'],
    'w7': ['m6', 'm5', 'm4', 'm7', 'm3', 'm2', 'm1']
}

matched_couples = []
unmatched_men = []


def get_unmatched_men():
    for man in male_preferences.keys():
        unmatched_men.append(man)


def stable_matching():
    while len(unmatched_men) > 0:
        for man in unmatched_men:
            start_match(man)


def start_match(man):
    for woman in male_preferences[man]:
        current_match = [match for match in matched_couples if woman in match]

        if len(current_match) == 0:
            matched_couples.append([man, woman])
            unmatched_men.remove(man)
            break

        elif len(current_match) > 0:
            current_man = female_preferences[woman].index(current_match[0][0])
            potential_man = female_preferences[woman].index(man)

            if current_man < potential_man:
                continue
            else:
                unmatched_men.remove(man)
                unmatched_men.append(current_match[0][0])
                current_match[0][0] = man
                break


def main():
    get_unmatched_men()
    stable_matching()
    return matched_couples


if __name__ == "__main__":
    print(main())