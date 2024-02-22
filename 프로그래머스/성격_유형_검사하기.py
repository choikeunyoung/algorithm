def solution(survey, choices):
    answer_list = ["RT", "CF", "JM", "AN"]
    survey_dict = {}
    
    for answers in answer_list:
        for ans in answers:
            survey_dict[ans] = 0
    
    point = [3, 2, 1, 0 , 1, 2 ,3]
    survey_length = len(survey)
    
    for i in range(survey_length):
        if choices[i]-1 < 3:
            survey_dict[survey[i][0]] += point[choices[i]-1]
        elif choices[i]-1 > 3:
            survey_dict[survey[i][1]] += point[choices[i]-1]
    
    answer = ''

    for ans in answer_list:
        if survey_dict[ans[0]] > survey_dict[ans[1]]:
            answer += ans[0]
        elif survey_dict[ans[0]] < survey_dict[ans[1]]:
            answer += ans[1]
        else:
            if ans[0] > ans[1]:
                answer += ans[1]
            else:
                answer += ans[0]

    return answer