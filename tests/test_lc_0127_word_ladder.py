from questions.lc_0127_word_ladder import Solutions


class TestWordLadder:
    def setup_method(self) -> None:
        self.solutions = Solutions()

    def test_ladderLength_1(self) -> None:
        s = self.solutions

        # Example 1
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        assert s.ladderLength_1(beginWord, endWord, wordList) == 5

        # Example 2
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        assert s.ladderLength_1(beginWord, endWord, wordList) == 0

        # Example 3
        beginWord = "a"
        endWord = "z"
        wordList = ["b", "c", "d"]
        assert s.ladderLength_1(beginWord, endWord, wordList) == 0

        # Example 4
        beginWord = "cat"
        endWord = "dog"
        wordList = ["rat", "bat", "bag", "fag", "fog", "dog"]
        assert s.ladderLength_1(beginWord, endWord, wordList) == 6

    def test_ladderLength_2(self) -> None:
        s = self.solutions

        # Example 1
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        assert s.ladderLength_2(beginWord, endWord, wordList) == 5

        # Example 2
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        assert s.ladderLength_2(beginWord, endWord, wordList) == 0

        # Example 3
        beginWord = "a"
        endWord = "z"
        wordList = ["b", "c", "d"]
        assert s.ladderLength_2(beginWord, endWord, wordList) == 0

        # Example 4
        beginWord = "cat"
        endWord = "dog"
        wordList = ["rat", "bat", "bag", "fag", "fog", "dog"]
        assert s.ladderLength_2(beginWord, endWord, wordList) == 6
