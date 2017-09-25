class Primes:

    def is_prime(self, num, update=True):
        if update is True:
            self._gen_primes_(num)
        
        for prime in self.primes:
            if prime >= num**(0.5)+1:
                return True
            if num % prime == 0:
                return False
        return True

            

    def _gen_primes_(self, max_val):
        if max_val > self.max_val:
            i = self.max_val
            while i < max_val:
                i += 1
                if self.is_prime(i, update=False) is True:
                    self.primes.append(i)
            self.max_val = max_val
                



    def __init__(self, max_val):
        self.primes = [2,3]
        self.max_val = 3
        self._gen_primes_(max_val)


primes = Primes(10000)



class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self, node):
        if str(node) in self.nodes.keys():
            return
        self.nodes[str(node)] = set([])
    def add_conn(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.nodes[str(node1)].add(node2)
        self.nodes[str(node2)].add(node1)
    def neighbors(self, node):
        return self.nodes[str(node)]


def get_valid(graph):
    valid = [node for node, neighbors in graph.nodes.items() if len(neighbors) > 3]
    valid.sort()
    return valid


def test(node, neighbors, graph, left):
    if left == 0:
        return []
    
    neighbors = [n for n in graph.nodes[str(node)] if n in neighbors]
    
    
    if len(neighbors) < left:
        return None
    
    result = []
    for i in range(0, len(neighbors)):
        temp = neighbors[:]
        cur = temp.pop(i)
        val = test(cur, set(temp), graph, left - 1)
        if val is not None:
            return [neighbors[i]] + val
        temp = temp[:i] + [cur] + temp[i:]
        
    
    if len(result) > 0:
        return result
    return None

def splits(num, checker):
    if not checker.is_prime(num):
        return []

    num = str(num)
    
    if len(num) == 2:
        if int(num[0]) in checker.primes:
            if int(num[1]) in checker.primes:
                if checker.is_prime(int(num[1] + num[0])) is True:
                    return [(int(num[0]), int(num[1]))]

    result = []
    for i in range(1, len(num)-1):
        if not num[i] is "0":
            if int(num[:i]) in checker.primes:
                if int(num[i:]) in checker.primes:
                    if checker.is_prime(int(num[i:] + num[:i])):
                        result.append((int(num[:i]), int(num[i:])))
    return result

def answer():
    g = Graph()
    count = 10
    while count < 10000000:
        count += 1
        
        for split in splits(count, primes):
            print(count)
            g.add_conn(split[0],split[1])
            
        valid = get_valid(g)
        for v in valid:
            ans = test(v, g.neighbors(v), g, 4)
            if ans is not None:
                print([v] + ans)

   
            


answer()


