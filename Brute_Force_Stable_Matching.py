import itertools

def is_stable(pairings, men_preferences, women_preferences):
    n = len(pairings)
    #print("pairings",pairings)
    for i in range(n):
        #print("----------------")
        #print("this is i",i)
        man1, woman1 = pairings[i]
        #print(pairings[i])
        for j in range(i + 1, n):
            #print("****----------------")
            #print("this is j",j)
            man2, woman2 = pairings[j]
            #print(pairings[j])
            if (
                men_preferences[man1].index(woman1) > men_preferences[man1].index(woman2) and
                women_preferences[woman2].index(man1) > women_preferences[woman2].index(man2)
            ):
                return False
    return True

def brute_force_stable_matching(men_preferences, women_preferences):
    n = len(men_preferences)
    men = list(range(n))
    best_matching = None

    # All possible permutations of pairings between men and women.
    for perm in itertools.permutations(range(n)):
        pairings = [(i, perm[i]) for i in men]
        print("pairings",pairings)    
        
        if is_stable(pairings, men_preferences, women_preferences):
            best_matching = pairings

    return best_matching

men_preferences = [
    [0, 5, 4, 1, 3, 2, 6],  
    [0, 3, 2, 1, 6, 5, 4], 
    [6, 5, 4, 0, 1, 3, 2],
    [3, 2, 0, 1, 4, 6, 5],
    [2, 1, 0, 3, 4, 5, 6],
    [6, 5, 4, 3, 2, 1, 0],
    [5, 6, 3, 4, 2, 1, 0]   
]

women_preferences = [
    [1, 5, 4, 0, 3, 2, 6],  
    [0, 1, 4, 3, 2, 5, 6],  
    [4, 2, 0, 1, 3, 6, 5],
    [3, 2, 0, 1, 4, 6, 5],
    [1, 2, 3, 0, 6, 5, 4],
    [6, 5, 4, 0, 1, 3, 2],
    [5, 4, 3, 6, 2, 1, 0]
]

matching = brute_force_stable_matching(men_preferences, women_preferences)

if matching is not None:
    print("Stable Matching:")
    for man, woman in matching:
        print(f"Man {man} is paired with Woman {woman}")
else:
    print("No stable matching.")
