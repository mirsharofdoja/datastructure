from collections import deque
graph={

}
def search(start_node,target='elon musk'):
    search_queue=deque()
    search_queue+=graph[start_node]
    searched=set()
    while search_queue:
        person=search_queue.popleft()
        if person not in searched:
            if person==target:
                return True
            else:
                search_queue+=graph[person]
                searched.add(person)
    return False

