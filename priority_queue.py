class QueueElement:
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, element, priority):
        queue_element = QueueElement(element, priority)
        added = False

        for index in range(len(self.items)):
            if queue_element.priority < self.items[index].priority:
                self.items.insert(index, queue_element)
                added = True
                break

        if added is False:
            self.items.insert(1, queue_element)

    def print(self):
        for i in range(len(self.items)):
            print(self.items[i].element + ' - ' + str(self.items[i].priority))


priorityQueue = PriorityQueue()
priorityQueue.enqueue('Jan', 2)
priorityQueue.enqueue('Mommy', 4)
priorityQueue.enqueue('Nanay', 3)
priorityQueue.enqueue('Jamie', 1)
priorityQueue.enqueue('Isabelle', 1)
priorityQueue.print()


