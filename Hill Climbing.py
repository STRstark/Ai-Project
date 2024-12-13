import random 

INFINITY = 100000
MAX_ITERATION = 1000

# The Values are not Correct, so the code amy never give an existing path :)
nodes = [
    "Tehran", "Isfahan", "Mashhad", "Shiraz", "Tabriz", "Ahvaz", "Kermanshah",
    "Karaj", "Qom", "Hamedan", "Yazd", "Kerman", "Ardabil", "Zanjan", "Sanandaj",
    "Urmia", "Rasht", "Sari", "Bandar Abbas", "Qazvin", "Semnan", "Birjand",
    "Bojnord", "Gorgan", "Khorramabad", "Ilam", "Bushehr", "Zahedan", "Yasuj",
    "Arak", "Mahabad", "Dezful"
]

edges = [
    ("Tehran", "Karaj", 50), ("Tehran", "Qom", 140), ("Tehran", "Semnan", 216),
    ("Karaj", "Qazvin", 100), ("Qom", "Isfahan", 275), ("Isfahan", "Shiraz", 481),
    ("Isfahan", "Yazd", 310), ("Yazd", "Kerman", 370), ("Shiraz", "Bandar Abbas", 577),
    ("Kerman", "Zahedan", 555), ("Kerman", "Bandar Abbas", 485), ("Mashhad", "Bojnord", 270),
    ("Mashhad", "Birjand", 500), ("Mashhad", "Semnan", 570), ("Ardabil", "Tabriz", 215),
    ("Tabriz", "Urmia", 149), ("Tabriz", "Zanjan", 286), ("Zanjan", "Hamedan", 264),
    ("Hamedan", "Sanandaj", 121), ("Sanandaj", "Kermanshah", 133), ("Kermanshah", "Ilam", 131),
    ("Ilam", "Khorramabad", 175), ("Khorramabad", "Ahvaz", 318), ("Ahvaz", "Dezful", 151),
    ("Dezful", "Yasuj", 252), ("Yasuj", "Shiraz", 200), ("Khorramabad", "Arak", 227),
    ("Arak", "Qom", 167), ("Rasht", "Sari", 307), ("Sari", "Gorgan", 150), ("Gorgan", "Bojnord", 330),
]

# Normalization of the graphs weights
epsilon = 0.01

Max_Edge = max(edge[2] for edge in edges)
Min_Edge = min(edge[2] for edge in edges)

normalized_edges = {
    (start, end): epsilon + ((distance - Min_Edge) / (Max_Edge - Min_Edge)) * (1 - epsilon)
    for start, end, distance in edges
}

normalized_edges.update({
    (end, start): weight for (start, end), weight in normalized_edges.items()
})

#helper functions

def createInitialRoute():
    current_solution = nodes[:]
    random.shuffle(current_solution)
    return current_solution

def Distace(current_solution):
    distace = 0
    for i in range( len(current_solution)-1):
        start = current_solution[i]
        end = current_solution[i+1]
        if normalized_edges.get((start , end)) is not None :
            distace +=normalized_edges.get((start , end))
        else:
            return 'inf'

def GetNeighbors(current_solution) :
    neighbors = []
    for i in range(len(current_solution)):
        for j in range(i+1 , len(current_solution)):
            neighbor = current_solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors
            
# main function : 

def hill_climbing():
    current_solution = createInitialRoute()
    current_Dis = Distace(current_solution)
    
    for _ in range(MAX_ITERATION) :
        neighbors = GetNeighbors(current_solution)
        next = min(neighbors , key=Distace)
        next_dist = Distace(next)
        
        if next_dist >= current_Dis:
            break
        
        current_solution , current_Dis = next , next_dist
        
    return current_solution , current_Dis


solution , cost = hill_climbing()

print(solution , cost)