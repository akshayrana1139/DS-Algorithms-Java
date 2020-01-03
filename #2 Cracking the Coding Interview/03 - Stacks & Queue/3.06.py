'''
Question: Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. 
People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). 
They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.You may use the built-in LinkedList data structure.

#1: making one queue for both is not feasible as you need to check animal type.., so make two queue for animal and old..
peek at both the queue in case of oldest animal, and give the one with timestamp..

'''