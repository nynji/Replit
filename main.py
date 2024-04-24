

###############################################################
#            주어진 배열 안의 각 단어들을 뒤집어서 출력하기            #
###############################################################


SPACE = 1
END   = 2

## 문자열에서 ' 'or'.'을 찾는 함수. ' 'or'.'가 있다면 각 문자에 해당하는 상태 값을 반환,
## & input_index[0]을 통해 index 도출
def isSpace(array, input_index): 

    '''---------------------------------------------------------
        Problem 1
          함수가 아래 예시와 같은 기능을 할 수 있도록 block을 채워주세요. 
    ---------------------------------------------------------'''
    while True:
        input_index[0] += 1
        if array[input_index[0]] == '.':
            return END
        elif array[input_index[0]] == ' ':
            return SPACE

## isSpace를 이용하여, 문자열 안에서 단어별로 뒤집어서 출력시키는 함수.
def printInverse(array):
    previous_index = 0
    current_index = [0]
    status_flag = 0
    reversed_word = []

    while True:
        status_flag = isSpace(array, current_index)
        
        if status_flag == SPACE:
            word = array[previous_index:current_index[0]]
            reversed_word.append(word[::-1])
            
            previous_index = current_index[0]+1
            
        elif status_flag == END:
            word = array[previous_index:current_index[0]]
            reversed_word.append(word[::-1])
            break
        else:
            continue

    print(' '.join(reversed_word))


## 주어진 배열 안의 각 단어들을 뒤집어서 출력하기 
def main():
  
    A = "I am happy today."
    B = "We want to win the first prize."

    print("A 배열 안의 각 단어들을 뒤집어서 출력: ")
    printInverse(A)
    print()

    print("B 배열 안의 각 단어들을 뒤집어서 출력: ")
    printInverse(B)
    print()

if __name__ == "__main__":
    main()
