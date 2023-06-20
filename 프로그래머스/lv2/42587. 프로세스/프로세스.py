def solution(priorities, location):
    answer = 0
    while priorities:
        if location==0:
            for i in range(1,len(priorities)):
                if priorities[0]<priorities[i]:
                    priorities.append(priorities[0])
                    priorities.pop(0)
                    location=len(priorities)-1
                    break
            else:
                answer+=1
                return answer
        else:
            for i in range(1,len(priorities)):
                if priorities[0]<priorities[i]:
                    priorities.append(priorities[0])
                    priorities.pop(0)
                    break
            else:
                priorities.pop(0)
                answer+=1
            location-=1
            
                    