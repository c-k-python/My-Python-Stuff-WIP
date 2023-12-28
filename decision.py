import random

def make_random_decision(options):
    total_weight = sum(options.values())
    choice = random.uniform(0, total_weight)
    
    current_weight = 0
    for option, weight in options.items():
        current_weight += weight
        if current_weight > choice:
            return option

def get_user_defined_criteria():
    options = {}
    while True:
        option = input("Enter an option (or 'done' to finish): ").strip()
        if option.lower() == 'done':
            break
        weight = float(input(f"Enter the weight for '{option}': "))
        options[option] = weight
    return options

def main():
    print("Welcome to the Random Decision Maker!")
    
    options = get_user_defined_criteria()
    
    if not options:
        print("No options provided. Exiting.")
        return
    
    while True:
        input("Press Enter to make a random decision...")
        decision = make_random_decision(options)
        print(f"The random decision is: {decision}")

if __name__ == "__main__":
    main()
