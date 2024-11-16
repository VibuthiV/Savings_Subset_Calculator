from itertools import combinations

def find_savings_options(expenses, target):
    exact_matches = []
    closest_match = None
    closest_sum = 0
    
    # Generate all combinations of expenses
    for i in range(1, len(expenses) + 1):
        for subset in combinations(expenses, i):
            subset_sum = sum(subset)
            if subset_sum == target:
                exact_matches.append(subset)
            elif subset_sum < target and subset_sum > closest_sum:
                closest_sum = subset_sum
                closest_match = subset

    return exact_matches, closest_match, closest_sum

def display_results(exact_matches, closest_match, closest_sum, target):
    # Display exact savings options
    if exact_matches:
        print(f"\n🎉 Exact ways to reach your savings goal of {target}:")
        for idx, subset in enumerate(exact_matches, 1):
            print(f"Option {idx}: Expenses to cut {subset} (Total savings: {sum(subset)})")
    else:
        print(f"\nNo exact match found for a savings goal of {target}.")
    
    # Display closest savings option if exact matches aren’t found
    if closest_match:
        print(f"\n💡 Closest option without exceeding your target:")
        print(f"{closest_match} (Total savings: {closest_sum})")

def main():
    print("Welcome to the Savings Optimizer!")
    
    # Collect monthly expenses from the user
    expenses = []
    print("Enter your monthly expenses one by one (type 'done' to finish):")
    while True:
        inp = input("> ")
        if inp.lower() == 'done':
            break
        try:
            expense = float(inp)
            if expense <= 0:
                print("Please enter a positive expense amount.")
            else:
                expenses.append(expense)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Prompt the user to set a savings target
    while True:
        try:
            target = float(input("Enter your savings target: "))
            if target <= 0:
                print("Please enter a positive savings target.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Find and display savings options
    exact_matches, closest_match, closest_sum = find_savings_options(expenses, target)
    display_results(exact_matches, closest_match, closest_sum, target)

if __name__ == "__main__":
    main()
