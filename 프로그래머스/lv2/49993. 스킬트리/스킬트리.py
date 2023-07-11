def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list=list(skill)
        
        for y in skills:
            if y in skill:
                if y!=skill_list.pop(0):
                    break
        else:
            answer+=1   
    return answer