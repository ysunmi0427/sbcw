import math

class Vector:

    def __init__(self, *elements):
        if len(elements) >= 2:
            self.elements = elements
        else:
            raise ValueError('At least two elements are required') 

    def __repr__(self):
        return f'{list(self.elements)}'

    def __len__(self):
        return len(self.elements)

    def __neg__(self):
        return Vector(*[-e for e in self.elements])

    def __add__(self, other):
        if len(self.elements) == len(other.elements):
            return Vector(*[self.elements[l] + other.elements[l] for l in range(len(self.elements))])
        else:
            raise ValueError(f'A vector of size {len(self.elements)} is expected')
    
    def __sub__(self, other):
        if len(self.elements) == len(other.elements):
            return Vector(*[self.elements[l] - other.elements[l] for l in range(len(self.elements))])
        else:
            raise ValueError(f'A vector of size {len(self.elements)} is expected')

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(*[e * other for e in self.elements])
        elif len(self.elements) == len(other.elements):
            return sum([self.elements[l] * other.elements[l] for l in range(len(self.elements))])
        else:
            raise ValueError(f'A vector of size {len(self.elements)} is expected')

    def __truediv__(self, other):
        if isinstance(other, Vector):
            raise TypeError("unsupported operand type(s) for /: 'Vector' and 'Vector'")
        else:
            return Vector(*[e / other for e in self.elements])
    
    def __floordiv__(self, other):
        if isinstance(other, Vector):
            raise TypeError("unsupported operand type(s) for /: 'Vector' and 'Vector'")
        else:
            return Vector(*[e // other for e in self.elements])

    def __eq__(self, other):
        return all([x == y for x, y in zip(self.elements, other.elements)])

class Range(object):
    # Problem 2.1
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start
        if step == 0:
            raise ValueError('`step` cannot be zero')
    def __iter__(self):
        return self
    def __next__(self):
        # Generalized version
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else:
            self.current += self.step
            return self.current - self.step
  
    # Problem 2.2
    def __reversed__(self):
        # simpler than below but.. lol
        # return reversed(list(Range(self.start, self.stop, self.step)))
        length = math.ceil((self.stop - self.start) / self.step)
        return Range(self.start + self.step * (length-1), self.start-1, -self.step)