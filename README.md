# [LeetCode](https://leetcode.com/problemset/all/) `Python` Challenge Solutions

## Table of Contents

- **Overview**
- **Solution Details**
- **TODOs**

### Overview

| Question | Solution                                        | Test             | Difficulty | Solved  |
|:--------:|:-----------------------------------------------:|:----------------:|:----------:|:-------:|
| [127]    | [Word Ladder][127.1]                            | [Tests][127.2]   | Hard       |    ✓    |

[127]:      https://leetcode.com/problems/word-ladder/
[127.1]:    questions/lc_0127_word_ladder.py
[127.2]:    tests/test_lc_0127_word_ladder.py

### Solution Details

> Important to note that each time the `Python` code is run, it's execution time can differ quite significantly. This is partly due to:

- **Just-In-Time Compilation (JIT)**: Python is an interpreted language, which means that Python code is executed line by line.
- **Dynamic Typing**: Python is dynamically typed, and variable types can change during runtime. This dynamic nature can affect execution times due to the need for dynamic type checking and conversion.
- **Garbage Collection**: Python uses automatic memory management with garbage collection. The timing and frequency of garbage collection can introduce variations in execution times, particularly in memory-intensive programs.
- **Caching**: Python bytecode is often cached, which can lead to variations depending on whether the cached bytecode is used or needs to be regenerated.

> Regarding Big **O** and Memory footprint in the below sections - note that these values are those receivd in the LeetCode submissions.

- Should you want to see more details and *your machines* performance you can run the code in the `if __name__ == "__main__":` section.
- Run the code a few times to see how much of a difference can be observed due to the aforementioned issues.

#### 127 Word Ladder

The general approach to this question is using a Bredth First Search (BFS) as well as hashing the list to improve the performance. We, however, approached it differently and imporved this performance even further. Below a summary

- Solution 1: BFS & HashMap (`set`).
- Solution 2: Optimised Solution 1 by precomputing valid transformations using a wildcard character approach.

| Solution  | Time (ms) | Memory (MB) | Big **O**      |
|----------:|:---------:|:-----------:|---------------|
| **1**     | 437       | 18          | **O**(N * M^2) |
| **2**     | 119       | 20.1        | **O**(N * M)   |

> Big **O** - where N is the number of words in the word list, and M is the length of each word.

### TODOs

- [ ] Explain how to setup env
