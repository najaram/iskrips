class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)


def hot_potato(list_names, num):

    queue = Queue()

    for i in range(num):
        queue.enqueue(list_names[i])

    while queue.size() > 1:
        for j in range(num):
            queue.enqueue(queue.dequeue())
        eliminated = queue.dequeue()
        print(eliminated + ' was eliminated.')

    return queue.dequeue()


names = ['jan', 'jamie', 'isa', 'maye', 'nanay', 'kuya razel', 'mommy', 'daddy']
champion = hot_potato(names, 8)
print('The champion is ' + champion)

