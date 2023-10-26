"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists."""

import time

from collections import defaultdict, deque
from queue import Queue

import memory_profiler

from tabulate import tabulate


class Solutions:
    def ladderLength_1(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)

        for word in wordList:
            word_set.add(word)

        if endWord not in word_set:
            return 0

        queue: Queue = Queue()
        queue.put(beginWord)
        level: int = 1

        while not queue.empty():
            size = queue.qsize()

            for _ in range(size):
                current_word: str = queue.get()
                word_chars: list[str] = list(current_word)

                for j in range(len(word_chars)):
                    original_char: str = word_chars[j]

                    for c in range(ord("a"), ord("z") + 1):
                        if word_chars[j] is chr(c):
                            continue

                        word_chars[j] = chr(c)
                        new_word: str = "".join(word_chars)

                        if new_word == endWord:
                            return level + 1
                        if new_word in word_set:
                            queue.put(new_word)
                            word_set.discard(new_word)

                    word_chars[j] = original_char

            level += 1
        return 0

    def ladderLength_2(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0

        transformations = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                transformations[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            current_word, level = queue.popleft()
            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]
                for next_word in transformations[pattern]:
                    if next_word == endWord:
                        return level + 1
                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

        return 0


if __name__ == "__main__":
    q = Solutions()

    beginWords = ["hit", "hit"]
    endWords = ["cog", "cog"]
    wordLists = [["hot", "dot", "dog", "lot", "log", "cog"], ["hot", "dot", "dog", "lot", "log"]]

    results = []

    for i in range(len(beginWords)):
        q = Solutions()
        result_row = []
        result_row.append(f"Test case {i + 1}")
        result_row.append(f"beginWord = {beginWords[i]}, endWord = {endWords[i]}")
        result_row.append(f"{wordLists[i]}")

        start_time_1 = time.time_ns() // 1000
        result_1 = q.ladderLength_1(beginWords[i], endWords[i], wordLists[i])
        end_time_1 = time.time_ns() // 1000
        m1 = memory_profiler.memory_usage((q.ladderLength_1, (beginWords[i], endWords[i], wordLists[i])))

        start_time_2 = time.time_ns() // 1000
        result_2 = q.ladderLength_2(beginWords[i], endWords[i], wordLists[i])
        end_time_2 = time.time_ns() // 1000
        m2 = memory_profiler.memory_usage((q.ladderLength_2, (beginWords[i], endWords[i], wordLists[i])))

        result_row.append(f"{result_1} words")
        result_row.append(f"{result_2} words")

        result_row.append(f"{end_time_1 - start_time_1} µs")
        result_row.append(f"{end_time_2 - start_time_2} µs")

        # Memory usage in MB
        result_row.append(f"{m1[0]:.2f} MB")
        result_row.append(f"{m2[0]:.2f} MB")

        results.append(result_row)

    headers = [
        "Input",
        "Word List",
        "Solution 1 Result",
        "Solution 2 Result",
        "Solution 1 Time (µs)",
        "Solution 2 Time (µs)",
        "Solution 1 Memory (MB)",
        "Solution 2 Memory (MB)",
    ]

    print(tabulate(results, headers, tablefmt="fancy_grid"))
