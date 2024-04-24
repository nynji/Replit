from Node import Node
from LinkedQueue import LinkedQueue
'''
    "LinkedQueue.py"이용하여 문제에서 원하는 LinkedQueue 데이터 구조 만들기.
    - "LinkedQueue.py"에서 class 'LinkedQueue'는 "Node.py"에서의 'Node' class를 가지고 있다. 
    - "LinkedQueue.py"에서 "num_dequeue(num: int)" 라는 함수가 정의되어 있다.
        -> 문제) num_dequeue(num: int)을 구현하여라.
    - 아래에 출력과 같은 데이터 구조를 구현하고자 한다. block안을 채워 나머지 source 코드를 완성하여라. 
    - 각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''


def main():
  que = LinkedQueue()

  for i in range(1, 10):
    que.enqueue(Node(i))

  que.display()

  
  que.num_dequeue(1)
  que.num_dequeue(1)
  que.num_dequeue(1)

  ## 1.4) 이 시점 que은 데이터 구조는 다음과 같음.
  ## -> [큐 내용] :  < 1> < 2> < 3> < 4> < 5> < 6> < 7> < 8> < 9>
  ## LinkedQueue::dequeue()를 이용하여 다음과 같은 데이터 구조를 갖도록 만들어라.
  ## -> [큐 내용] :  < 4> < 5> < 6> < 7> < 8> < 9>
  ################################################
  #                    block                     #
  ################################################

  que.display()

  ## 1.5) 최종적으로 큐의 데이터 구조과 다음과 같이 될 수 있도록 코드를 구현하여라.
  ## 출력결과: [큐 내용] :  < 4> < 6> < 8>
  ## hint) 문제는 LinkedQueue::num_dequeue()함수를 먼저 구현하시면 쉽게 풀 수 있습니다.
  ################################################
  #                    block                     #
  ################################################
  que.num_dequeue(2)
  que.num_dequeue(3)
  que.num_dequeue(4)

  que.display()


if __name__ == "__main__":
  main()
