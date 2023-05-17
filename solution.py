class FindPairs:
    def __init__(self, sum_up=12):
        self.sum_up = sum_up

    def find_pairs(self, sum_up=12, input_file="input_file.txt", output_file="output_file.txt", save_output=True):
        sum_up = self.sum_up

        with open(input_file, "r") as input_file:
            numbers = input_file.readline()  
        
        if not numbers:
            return print("File is empty.")
        else:
            try:
                numbers = [int(x) for x in numbers.split(",")]
            except ValueError as e:
                return print("File contains letters.")

        pairs = []

        for first_number in numbers:
            numbers.remove(first_number)
            second_number = sum_up - first_number

            if second_number in numbers:
                numbers.remove(second_number)
                pair = [first_number, second_number]
                pair.sort()
                pairs.append(pair)

        if save_output:
            with open(output_file, "w+") as output_file:
                output_file.write(str(pairs))

        return pairs

if __name__ == "__main__":
    run = FindPairs()
    run.find_pairs()