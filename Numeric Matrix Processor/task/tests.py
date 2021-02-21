import re
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
                '4 5\n'
                '1 2 3 4 5\n'
                '3 2 3 2 1\n'
                '8 0 9 9 1\n'
                '1 3 4 5 6\n'
                '4 5\n'
                '1 1 4 4 5\n'
                '4 4 5 7 8\n'
                '1 2 3 9 8\n'
                '1 0 0 0 1\n'
                ,
                attach=TestClue(
                    answer=
                    '2 3 7 8 10\n'
                    '7 6 8 9 9\n'
                    '9 2 12 18 9\n'
                    '2 3 4 5 7\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '2 3\n'
                '1 4 5\n'
                '4 5 5\n'
                '4 5\n'
                '0 1 0 4 5\n'
                '1 7 8 9 4\n'
                '1 2 3 5 6\n'
                '1 3 4 3 8\n'
                ,
                attach=TestClue(
                    answer=
                    'ERROR\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '4 5\n'
                '4 2 3 4 5\n'
                '3 5 3 2 1\n'
                '8 0 9 9 1\n'
                '1 3 4 5 9\n'
                '4 5\n'
                '1 1 4 4 5\n'
                '4 4 5 7 8\n'
                '1 2 3 9 8\n'
                '1 0 0 0 1\n'
                ,
                attach=TestClue(
                    answer=
                    '5 3 7 8 10\n'
                    '7 9 8 9 9\n'
                    '9 2 12 18 9\n'
                    '2 3 4 5 10\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '1 1\n'
                '1\n'
                '1 1\n'
                '2\n'
                ,
                attach=TestClue(
                    answer=
                    '3\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '1 2\n'
                '3 4\n'
                '1 2\n'
                '5 6\n'
                ,
                attach=TestClue(
                    answer=
                    '8 10\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '2 1\n'
                '1\n'
                '2\n'
                '2 1\n'
                '2\n'
                '1\n'
                ,
                attach=TestClue(
                    answer=
                    '3\n'
                    '3\n'
                    ,
                    feedback=
                    ''
                )
            ),
            TestCase(
                stdin=
                '2 1\n'
                '2\n'
                '1\n'
                '1 2\n'
                '1 2\n'
                ,
                attach=TestClue(
                    answer=
                    'ERROR\n'
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


def convert():
    inputs = []
    outputs = []
    for filename in sorted(os.listdir("cases")):
        if filename.startswith("input") and re.match(r"^input\d+$", filename):
            with open("cases/" + filename) as f:
                inputs.append(f.read())
        if filename.startswith("output") and re.match(r"^output\d+$", filename):
            with open("cases/" + filename) as f:
                feedback = f.readline()
                outputs.append(TestClue(f.read(), feedback))

    print('[')
    for inp, out in zip(inputs, outputs):
        print('    TestCase(')
        print('        stdin=')
        for line in inp.splitlines():
            print('        \'' + line + '\\n\'')
        print('        ,')
        print('        attach=TestClue(')
        print('            answer=')
        for line in out.answer.splitlines():
            print('            \'' + line + '\\n\'')
        print('            ,\n'
              '            feedback=')
        print('            \'' + out.feedback.strip() + '\'')
        print('        )')
        print('    ),')
    print(']')
