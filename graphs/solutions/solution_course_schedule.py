'''Solution: Course Schedule (Challenge 3)'''
def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * num_courses
    
    def has_cycle(course):
        if color[course] == BLACK:
            return False
        if color[course] == GRAY:
            return True
        color[course] = GRAY
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        color[course] = BLACK
        return False
    
    return not any(has_cycle(i) for i in range(num_courses))
