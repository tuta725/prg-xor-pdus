from generate_xor import generate_xor_clauses, xor_to_cnf_clause

n_vars = 10
n_clauses = 5
seed = 42

clauses = generate_xor_clauses(n_vars, n_clauses, seed)
print("Generated XOR clauses:")
for c in clauses:
    print(c)

cnf_all = []
for c in clauses:
    cnf_all.extend(xor_to_cnf_clause(c[0], c[1]))

print("\nCNF clauses:")
for clause in cnf_all:
    print(clause)
