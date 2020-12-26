import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for name1, name2 in zip(participant, completion):
        if name1 != name2:
            return name1
    
    collections.Counter

    return participant[-1]

if __name__ == "__main__":
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    print(solution(participant, completion))

    participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
    completion = ["josipa", "filipa", "marina", "nikola"]
    print(solution(participant, completion))

    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution(participant, completion))
	