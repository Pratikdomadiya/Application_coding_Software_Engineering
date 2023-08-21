'''
Problem : create a pipeline execution - 3 functions - with "yield" - sum - Square - Root - (producer - consumer
functions are given).
'''

import queue
import threading
import math

# Producer function using yield: Generates numbers
def producer(limit):
    for num in range(1,limit+1):
        yield num

# Consumer function using yield: Prints processed numbers
def consumer(numbers, consumr_id):
    for num in numbers:
        print(f"Consumer {consumr_id} : Processed {num}")
        yield num

# Intermediate function using yield: Squares numbers
def square_numbers(numbers):
    for num in numbers:
        yield num ** 2

# Intermediate function using yield: Filters even numbers
def filter_even_numbers(numbers):
    for num in numbers:
        if num%2 == 0:
            yield num

# Intermediate function using yield: Calculates the sum
def calculate_sum(numbers):
    total = sum(numbers)
    return total

# Intermediate function using yield: Takes the square root
def calculate_square_root(numbers):
    for num in numbers:
        yield math.sqrt(num)


# create a producer-consumer pipeline using "yield"
numbers = producer(10)
square_numbers = square_numbers(numbers)
even_numbers = filter_even_numbers(square_numbers)
sum_of_squares = calculate_sum(even_numbers)
square_roots = calculate_square_root(sum_of_squares)


# below code snippet was given in test
# Create a thread-safe queue
data_queue = queue.Queue()

# Create a producer and consumer generator
producer = start_consumers()
producer.send(None)  # Initialize the generator
consumers = [start_consumers() for _ in range(4)]
for consumer in consumers:
    consumer.send(None)  # Initialize each consumer

# Start producer and consumer threads
def run_producer():
    for num in square_roots:
        data_queue.put(num)
    for _ in consumers:
        data_queue.put(None)  # Signal the end of data

producer_thread = threading.Thread(target=run_producer)
producer_thread.start()

# Consumer threads using yield
def run_consumer(consumer, queue):
    while True:
        item = queue.get()
        if item is None:
            break
        consumer.send(item)
    consumer.close()

consumer_threads = []
for consumer in consumers:
    consumer_thread = threading.Thread(target=run_consumer, args=(consumer, data_queue))
    consumer_threads.append(consumer_thread)
    consumer_thread.start()

# Wait for all threads to finish
producer_thread.join()
for thread in consumer_threads:
    thread.join()

print("All threads finished")