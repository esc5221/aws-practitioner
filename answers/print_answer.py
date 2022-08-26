# print wrong answer
def print_wrong_answer():
    # open answer file
    with open('answer_3.txt', 'r') as answer_file:
        answer = answer_file.read()
        answers = answer.splitlines()

    # open my answer file
    with open('answer_3_my.txt', 'r') as my_answer_file:
        my_answer = my_answer_file.read()
        my_answers = my_answer.splitlines() 
    
    # print wrong answer
    cnt = 0
    for i in range(len(answers)):
        if answers[i] != my_answers[i]:
            print(i, 'correct: ',answers[i], '\t\t my: ',my_answers[i])
            cnt += 1
    
    print('='*50)
    print('total wrong answer: ', cnt)
    print(f'accuracy: {100-float(cnt)/float(len(answers))*100:.2f}%')

if __name__ == '__main__':
    print_wrong_answer()
