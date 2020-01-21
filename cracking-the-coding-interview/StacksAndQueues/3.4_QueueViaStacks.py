"""
3.4:  Queue via Stacks: 
        Implement a MyQueue class which implements a queue using two stacks.

	Idea:
	The idea here is to use stack2 which takes care of dequeue and stack1 will take care of enqueue. 
	In this way when we want to dequeue at some point of time we check if stack1 has elems. 
	if it has elems then we do a pop for every elem in stack1 and copy it in the stack2. 
	and then pop from stack2 which now has the 0th elem of stack1.
	Now again if we add elems we add it to stack1. Stack1 is pure stack and Stack2 is as well but elems in stack2 are reverse of stack1. 
	which makes it queue.

	Time Complexity:
	Push O(1)
	Pop O(1) amortized. because even if we have pop after each elem its O(1) process - pop from stack1 -> push to stack2 -> pop from stack2
		Now if we pop after pushing 100 elements. then we have a forloop for 100 pops and then for next 99 pops it will be O(1)
	
	Space Complexity:
		Other than the space for Stack1 and Stack2 its O(1)
"""


class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, data):
        self.stack1.append(data)

    def pop(self):
        if len(self.stack2) == 0:
            if len(self.stack1) != 0:
                for num in self.stack1[::-1]:
                    self.pushStack2(self.popStack1())
            else:
                return "No More Elements"
        return self.stack2.pop()

    def pushStack2(self, num):
        self.stack2.append(num)

    def popStack1(self):
        return self.stack1.pop()


if __name__ == "__main__":
    q = QueueWithTwoStacks()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    print(q.stack1, q.stack2)
    print(q.pop())
    print(q.stack1, q.stack2)
    q.push(6)
    q.push(7)
    print(q.pop())
    print(q.stack1, q.stack2)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.stack1, q.stack2)
