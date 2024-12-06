# Multidimensional Knapsack Problem (MDKP)

## Overview
The **Multidimensional Knapsack Problem (MDKP)** is a classical combinatorial optimization problem that involves selecting a subset of objects from a set to:
1. Maximize the total value of the selected objects.
2. Ensure that the resource consumption of the selected objects does not exceed the capacity of any resource.

This project includes:
- A function to parse an instance of the MDKP from a structured text file.
- An efficient greedy algorithm that selects objects based on their value-to-weight ratio.

---

## Problem Description
### Inputs:
- **Objects (N):** A set of objects, where each object has:
  - A value `v_i`.
  - A resource consumption `w_{i,j}` for each resource `j`.
- **Resources (R):** A set of resources, where each resource `j` has:
  - A capacity `q_j`.

### Constraints:
- For each resource `j`, the total consumption of the selected objects must not exceed its capacity:
  \[
  \sum_{i \in S} w_{i,j} \leq q_j \quad \forall j \in R
  \]

### Objective:
Maximize the total value of the selected objects:
\[
\text{Maximize} \quad \sum_{i \in S} v_i
\]

---

## Features
1. **Instance Reader:**
   - Reads an MDKP instance from a structured text file.
   - Extracts the number of objects, number of resources, object values, resource consumption matrix, and resource capacities.

2. **Greedy Algorithm:**
   - Implements a greedy approach based on the value-to-weight ratio.
   - Selects objects to maximize the total value while respecting resource constraints.

---

## Input File Format
The input file must follow this structure:
NbrObjets NbrRessources 
<number_of_objects> <number_of_resources>
 les valeurs des objets 
<value1> 
<value2> 
... 
les quatités des resources consommées pour chaque objet (ligne)
 <consumption1_1> <consumption1_2> ... <consumption1_R> 
<consumption2_1> <consumption2_2> ... <consumption2_R>
 ... 
les capacités des ressources 
<capacity1>
<capacity2> 
...


### Example Input
NbrObjets NbrRessources 
5 3 
les valeurs des objets 
50 
40 
30 
20 
10 
les quatités des resources consommées pour chaque objet (ligne) 
10 5 8 
8 3 4 
5 6 7 
3 8 5 
2 1 3 
les capacités des ressources 
20 
15 
10

## Usage
### 1. Prerequisites
- Python 3.x installed on your system.

### 2. Running the Program
Save the code in a Python file (e.g., `mdkp_solver.py`) and prepare an input file (e.g., `instance.txt`) in the required format.

Run the program:
```bash
python mdkp_solver.py

### Example Ouput

Nombre d'objets : 5
Nombre de ressources : 3
Valeurs (index et valeurs) : [[0, 50], [1, 40], [2, 30], [3, 20], [4, 10]]
Premières 5 lignes de la matrice de consommation : [[10, 5, 8], [8, 3, 4], [5, 6, 7], [3, 8, 5], [2, 1, 3]]
Capacités : [20, 15, 10]
Optimized Total Score: 90
Final Remaining Capacities: [0, 4, 2]
Indices of Selected Objects: [0, 1, 2]
