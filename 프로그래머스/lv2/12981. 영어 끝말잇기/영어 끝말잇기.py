def solution(n, words):
    answer = []
    res = []
    for i in range(1,len(words)):
        if words.count(words[i])==2 or words[i][0]!=words[i-1][-1]:	
            for j in range(len(words)):
                if words[j]==words[i]:
                    res.append(j)
            answer.append(max(res)%n+1)
            answer.append(max(res)//n+1)
            break
    if len(res)==0:
        answer=[0,0]
    return answer

######## more compacted version ########
# Rather than appending the index of same words to the list, 
# adding conditional statements to check if the same word has ever appeared before the word appears.

def solution(n, words):
    answer = []
    res = []
    for i in range(1,len(words)):
        if words[i] in words[:i] or words[i][0]!=words[i-1][-1]:	
            return [i%n+1, i//n+1]
    else:
        return [0,0]
