# prg-xor-pdus
“PRG-based XOR construction for pseudo-deterministic Unique-SAT experiments and CNF generation”
# PRG-based XOR for Pseudo-Deterministic Unique-SAT (PDUS)

This repository contains Python code for generating XOR clauses using a pseudorandom generator (PRG) to create candidate Unique-SAT instances and encode them into CNF format.

## Features
- Generate XOR clauses from a PRG seed.
- Convert XOR clauses into CNF using Tseitin encoding.
- Example CNF output ready for SAT solvers (DIMACS format).
- Empirical evaluation of pseudo-deterministic isolation probability.

## Usage

```bash
python prg_xor_generator.py
