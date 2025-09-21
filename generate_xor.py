"""
PRG-based XOR Construction for Pseudo-Deterministic Unique-SAT
Author: Uthit Lakkaew
"""

import random

def prg(seed, length):
    random.seed(seed)
    return [random.randint(0, 1) for _ in range(length)]

def generate_xor_clauses(n_vars, n_clauses, seed):
    bits = prg(seed, n_clauses)
    clauses = []
    for i in range(n_clauses):
        k = random.randint(2, min(5, n_vars))
        vars_indices = random.sample(range(1, n_vars+1), k)
        parity = bits[i]
        clauses.append((vars_indices, parity))
    return clauses

def xor_to_cnf_clause(vars_indices, parity, aux_start=1000):
    cnf = []
    if len(vars_indices) == 2:
        x1, x2 = vars_indices
        if parity == 0:
            cnf = [[x1, x2], [-x1, -x2]]
        else:
            cnf = [[x1, -x2], [-x1, x2]]
    elif len(vars_indices) == 3:
        x1, x2, x3 = vars_indices
        b = parity
        cnf = [
            [x1, x2, b],
            [x1, -x2, -b],
            [-x1, x2, -b],
            [-x1, -x2, b]
        ]
    else:
        aux = aux_start
        prev = vars_indices[0]
        for i in range(1, len(vars_indices)-1):
            cnf.append([prev, vars_indices[i], aux])
            prev = aux
            aux += 1
        cnf.append([prev, vars_indices[-1], parity])
    return cnf

if __name__ == "__main__":
    n_vars = 10
    n_clauses = 5
    seed = 42
    clauses = generate_xor_clauses(n_vars, n_clauses, seed)
    print("Generated XOR clauses:", clauses)
    cnf_all = []
    for c in clauses:
        cnf_all.extend(xor_to_cnf_clause(c[0], c[1]))
    print("CNF clauses:", cnf_all)
