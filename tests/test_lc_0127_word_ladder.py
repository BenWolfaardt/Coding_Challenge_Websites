import pytest

from questions.lc_0127_word_ladder import Solutions


class TestWordLadder:
    def setup_method(self) -> None:
        self.solutions = Solutions()

    @pytest.mark.parametrize(
        "beginWord, endWord, wordList, expected",
        [
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
            ("a", "z", ["b", "c", "d"], 0),
            ("cat", "dog", ["rat", "bat", "bag", "fag", "fog", "dog"], 6),
        ],
    )
    def test_ladderLength_1(self, beginWord: str, endWord: str, wordList: list[str], expected: str) -> None:
        s = self.solutions
        assert s.ladderLength_1(beginWord, endWord, wordList) == expected

    @pytest.mark.parametrize(
        "beginWord, endWord, wordList, expected",
        [
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
            ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
            ("a", "z", ["b", "c", "d"], 0),
            ("cat", "dog", ["rat", "bat", "bag", "fag", "fog", "dog"], 6),
        ],
    )
    def test_ladderLength_2(self, beginWord: str, endWord: str, wordList: list[str], expected: str) -> None:
        s = self.solutions
        assert s.ladderLength_2(beginWord, endWord, wordList) == expected
