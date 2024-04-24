class ArrayStack:
    def __init__(self, max_stack_size=100):
        self.data = []
        self.top = 0
        self.max_stack_size = max_stack_size
        
    def is_empty(self):
        ''' 1) isEmpty() 함수를 마저 작성하시오. '''
      
        return self.top == 0
      ###  block  ###
    
    def is_full(self):
        ''' 2) isFull()의 함수를 마저 작성하시오. '''
      
        return self.top == self.max_stack_size ###  block  ###
    
    def push(self, e):
        if self.is_full():
            print("스택 포화 에러")
            return 
        ''' 3) push의 함수를 마저 작성하시오. '''
        self.data.append(e)
        self.top += 1
      
        #####################################
        #               block               #
        #####################################
    
    def pop(self):
        if self.is_empty():
            print("스택 공백 에러")
            return None
        
        ''' 4) pop의 함수를 마저 작성하시오. '''
        self.top -= 1
        return self.data[self.top]
        #####################################
        #               block               #
        #####################################
    
    def peek(self):
        if self.is_empty():
            print("스택 공백 에러")
            return None
        
        ''' 5) peek의 함수를 마저 작성하시오. '''
        return self.data[self.top-1]
        ###  block  ###
    
    def display(self):
    
        print(f"[스택 항목의 수 = {self.top}] ==> ", end="")
        for i in range(0, self.top):
            print(f"data[{i}]: {self.data[i]} ", end="")
        print()