import solution
import pytest

class Test:

    def test_find_pair(self):
        with open("input_file_test.txt", "w+") as input_file_test:
            input_file_test.write("2,4,6,7,9,5,4,8,9,0,5,3,2,2,4,6,8,9,5,6,9,4,2")

        pairs_found = [[6, 6], [3, 9], [4, 8], [4, 8], [5, 7]]

        test_solution = solution.FindPairs()
        result = test_solution.find_pairs(sum_up=12, input_file="input_file_test.txt", save_output=False)
        
        assert result == pairs_found

    def test_not_find_pair(self):
        with open("input_file_test.txt", "w+") as input_file_test:
            input_file_test.write("5,5,5")

        pairs_found = [[4, 5], [6, 9]]

        test_solution = solution.FindPairs()
        result = test_solution.find_pairs(sum_up=13, input_file="input_file_test.txt", save_output=False)

        assert not result == pairs_found

    def test_wrong_input(self, capsys):
        with open("input_file_test.txt", "w+") as input_file_test:
            input_file_test.write("T,e,s,t,i,n,p,u,t")

        test_solution = solution.FindPairs()
        test_solution.find_pairs(sum_up=12, input_file="input_file_test.txt", save_output=False)

        out, err = capsys.readouterr()

        assert out == "File contains letters.\n"

