from itertools import combinations

def generate_combinations(input_string):
    all_combinations = set()

    # Generate combinations of all elements together
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            all_combinations.add(input_string[i:j])

    return sorted(all_combinations)

def main():
    # Prompt the user to input elements separated by spaces
    user_input = input("Enter all OSINT elements separated by spaces (e.g., 'hello hi nice'): when you are done, press Enter: ")

    # Remove spaces to form a continuous string
    input_string = ''.join(user_input.split())

    # Generate all combinations
    combinations = generate_combinations(input_string)

    # Write the combinations to a text file
    with open('passwords.txt', 'w') as file:
        for comb in combinations:
            file.write(comb + '\n')

    print("All possible combinations have been saved to passwords.txt")

if __name__ == "__main__":
    main()