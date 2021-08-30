#!/Users/nabinniroula/anaconda3/bin/python
""" Here, we will work on Python Queues. """
import queue
# To use FIFO queues, use Queue() class with queue module
# q1 = queue.Queue()  # This gives infinite queue, use a number to have a size of the queue
q2 = queue.Queue(5)
# put an item into this queue
q2.put(9)
print(q2)
print(q2.qsize())
print(q2.empty())
print(q2.full())
print(q2.get())
print(q2.empty())
print(f"The size of queue after get() method is called is {q2.qsize()}.")