# Python Katas & Algorithms

This directory contains a diverse collection of Python scripts, ranging from algorithmic implementations and cryptography to puzzles, theorem proving, and language feature explorations.

## 📋 Table of Contents

1.  Detailed Contents
      - [Advent of Code 2022](advent-2022)
      - [Cryptography](cryptography)
      - [Constraint Satisfaction Problems](csp)
      - [Extra & Puzzles](extra)
      - [Learning & Language Features](learning)
      - [Pattern Matching](pattern-matching)
      - [Radar Kata](radar)
      - [Z3 Theorem Prover](z3)

-----

## 🔍 Directory Overview

| Directory | General Information |
| :--- | :--- |
| **[`advent-2022/`](./advent-2022)** | Solutions and inputs for Advent of Code 2022 challenges. |
| **[`cryptography/`](./cryptography)** | Implementations of classic and modern cryptographic algorithms and PRNGs. |
| **[`csp/`](./csp)** | Solvers and algorithms for Constraint Satisfaction Problems (e.g., Map Coloring, N-Queens). |
| **[`extra/`](./extra)** | A miscellaneous collection of board game simulations, logic puzzles, and assorted scripts. |
| **[`learning/`](./learning)** | Exploratory scripts testing specific Python concepts like memory, generics, and pass-by-reference. |
| **[`pattern-matching/`](./pattern-matching)** | Standard string searching and pattern-matching algorithms. |
| **[`radar/`](./radar)** | A localized project or kata centered around radar concepts. |
| **[`z3/`](./z3)** | Experiments utilizing the Z3 Theorem Prover. |

-----

## 📂 Detailed Contents

### Advent of Code 2022

Contains scripts and data files for the 2022 Advent of Code programming challenges.

  * **[`day3.py`](./advent-2022/day3.py)** & **[`day3.md`](./advent-2022/day3.md)**: Code and documentation for Day 3.
  * **[`backpacks.txt`](./advent-2022/backpacks.txt)**: Puzzle input data.

### Cryptography

Focuses on encryption, decryption, and random number generation algorithms.

  * **[`caesar_cipher.py`](./cryptography/caesar_cipher.py)**: Implementation of the classic Caesar shift cipher.
  * **[`des_intuition.py`](./cryptography/des_intuition.py)**: Explorations into Data Encryption Standard (DES) concepts.
  * **[`mersennetwister.py`](./cryptography/mersennetwister.py)**: Implementation of the Mersenne Twister pseudorandom number generator.
  * **[`rsa.py`](./cryptography/rsa.py)**: Rivest-Shamir-Adleman (RSA) public-key cryptosystem implementation.
  * **[`rotate_string.py`](./cryptography/rotate_string.py)**: Utility for string rotation operations.

### Constraint Satisfaction Problems

Algorithms designed to solve problems defined by a set of objects whose state must satisfy a number of constraints.

  * **[`ac3.py`](./csp/ac3.py)** & **[`ac3_wiki.py`](./csp/ac3_wiki.py)**: Implementations of the AC-3 algorithm for arc consistency.
  * **[`csp.py`](./csp/csp.py)**: Core constraint satisfaction problem logic.
  * **Problem Implementations**:
      * **[`circuit_board.py`](./csp/circuit_board.py)**
      * **[`map_coloring.py`](./csp/map_coloring.py)**
      * **[`queens.py`](./csp/queens.py)** (N-Queens)
      * **[`send_more_money.py`](./csp/send_more_money.py)** (Cryptarithmetic puzzle)
      * **[`word_search.py`](./csp/word_search.py)**

### Extra & Puzzles

A grab-bag of game logic, math puzzles, and recreational programming scripts.

  * **Board Games**:
      * **[`chutes_and_ladders.py`](./extra/chutes_and_ladders.py)**
      * **[`snakes.py`](./extra/snakes.py)**
      * **[`tictactoe.py`](./extra/tictactoe.py)**
  * **Logic/Math Puzzles**:
      * **[`nonogram.py`](./extra/nonogram.py)**
      * **[`sudoku.py`](./extra/sudoku.py)**
      * **[`narcissistic.py`](./extra/narcissistic.py)**
      * **[`triplets_nextbigger.py`](./extra/triplets_nextbigger.py)**
  * **Grids & Hexagons**:
      * **[`hexagon.py`](./extra/hexagon.py)**
      * **[`hexagon_random.py`](./extra/hexagon_random.py)**
      * **[`nx_grid.py`](./extra/nx_grid.py)**
      * **[`map_triples2.py`](./extra/map_triples2.py)**
  * **Misc**:
      * **[`etc.py`](./extra/etc.py)**
      * **[`noidea.py`](./extra/noidea.py)**
      * **[`teaching.py`](./extra/teaching.py)**

### Learning & Language Features

Scripts dedicated to understanding the nuances of the Python language.

  * **[`abc_example.py`](./learning/abc_example.py)**: Demonstrations of Abstract Base Classes.
  * **[`generics.py`](./learning/generics.py)**: Usage of generics and type hinting.
  * **[`memory.py`](./learning/memory.py)**: Explorations of Python's memory management.
  * **[`passref.py`](./learning/passref.py)**: Testing pass-by-reference vs. pass-by-value behaviors.
  * **[`weird.py`](./learning/weird.py)**: Examples of Python's quirks and unexpected behaviors.

### Pattern Matching

Implementations of highly efficient string searching algorithms.

  * **[`Boyer-Moore.py`](./pattern-matching/Boyer-Moore.py)**: The Boyer-Moore string-search algorithm.
  * **[`Knuth-Morris-Pratt.py`](./pattern-matching/Knuth-Morris-Pratt.py)**: The KMP string-searching algorithm.

### Radar Kata

A specific, self-contained coding exercise.

  * **[`radar.py`](./radar/radar.py)** & **[`radar.md`](./radar/radar.md)**: Code and instructions/documentation for the radar kata.

### Z3 Theorem Prover

Scripts interacting with the Z3 solver by Microsoft Research.

  * **[`zplay.py`](./z3/zplay.py)**: Playground script for modeling and solving logic problems with Z3.
  * **[`requirements.txt`](./z3/requirements.txt)**: Dependencies needed for the Z3 environment.