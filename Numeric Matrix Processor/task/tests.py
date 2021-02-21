import string
from collections import namedtuple

from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

TestClue = namedtuple("TestClue", ["answer", "feedback"])


class CalcTest(StageTest):
    ERROR_STRING = "ERROR"

    def generate(self) -> List[TestCase]:
        return [
            TestCase(
                stdin=
                '3 3\n'
                '1 2 3\n'
                '4 5 6\n'
                '7 8 9\n'
                '3\n'
                ,
                attach=TestClue(
                    answer=
                    '3 6 9\n'
                    '12 15 18\n'
                    '21 24 27\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '2 3\n'
                '1 2 3\n'
                '4 5 6\n'
                '0\n'
                ,
                attach=TestClue(
                    answer=
                    '0 0 0\n'
                    '0 0 0\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '5 5\n'
                '1 4 6 7 8\n'
                '1 9 5 2 2\n'
                '1 4 3 5 7\n'
                '1 4 6 4 1\n'
                '1 4 5 7 1\n'
                '5\n'
                ,
                attach=TestClue(
                    answer=
                    '5 20 30 35 40\n'
                    '5 45 25 10 10\n'
                    '5 20 15 25 35\n'
                    '5 20 30 20 5\n'
                    '5 20 25 35 5\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '1 1\n'
                '1\n'
                '1\n'
                ,
                attach=TestClue(
                    answer=
                    '1\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '1 1\n'
                '0\n'
                '1\n'
                ,
                attach=TestClue(
                    answer=
                    '0\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '3 2\n'
                '1 2\n'
                '8 1\n'
                '9 1\n'
                '10\n'
                ,
                attach=TestClue(
                    answer=
                    '10 20\n'
                    '80 10\n'
                    '90 10\n'
                    ,
                    feedback=
                    ''
                )
            ),
        ]

    def is_equal_matrices(self, actual: list, expected: list) -> bool:
        if len(actual) != len(expected):
            return False
        for actual_line, expected_line in zip(actual, expected):
            if len(actual_line) != len(expected_line):
                return False
            else:
                for actual, expected in zip(actual_line, expected_line):
                    try:
                        if abs(float(actual) - float(expected)) > 0.01:
                            return False
                    except ValueError:
                        raise WrongAnswer("Looks like your matrix contains not only numbers!")
        return True

    def check(self, reply: str, attach) -> CheckResult:
        reply = reply.strip()
        answer = str(attach.answer).strip()
        if answer == self.ERROR_STRING:
            return CheckResult(reply == self.ERROR_STRING, f'Expected output:\n{answer}\nYour output:\n{reply}')
        else:
            characters = set(string.ascii_lowercase)
            actual = [line.split() for line in reply.splitlines() if line and characters.isdisjoint(line)]
            expected = list(map(str.split, answer.split("\n")))
            return CheckResult(self.is_equal_matrices(expected, actual), attach.feedback)


if __name__ == '__main__':
    CalcTest("processor.processor").run_tests()
