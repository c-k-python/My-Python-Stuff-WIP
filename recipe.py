import random

def suggest_random_recipe():
    recipes = [
        {
            "name": "Spaghetti Bolognese",
            "ingredients": ["spaghetti", "ground beef", "onions", "tomato sauce", "garlic", "herbs", "Parmesan cheese"],
            "instructions": ["Cook spaghetti according to package instructions.", "Brown ground beef with onions and garlic.", "Add tomato sauce and herbs. Simmer for 20 minutes.", "Serve sauce over cooked spaghetti. Top with Parmesan cheese."]
        },
        {
            "name": "Chicken Alfredo Pasta",
            "ingredients": ["fettuccine pasta", "chicken breasts", "butter", "heavy cream", "Parmesan cheese", "garlic", "salt", "pepper"],
            "instructions": ["Cook fettuccine pasta according to package instructions.", "Season and cook chicken breasts in butter until done.", "In a separate pan, heat garlic in butter, add heavy cream, and simmer.", "Stir in Parmesan cheese until melted. Season with salt and pepper.", "Combine pasta, sliced chicken, and Alfredo sauce. Serve hot."]
        },
        # Add more recipes as needed
    ]

    random_recipe = random.choice(recipes)
    
    print(f"\nRecipe: {random_recipe['name']}")
    print("Ingredients:")
    for ingredient in random_recipe['ingredients']:
        print(f"- {ingredient}")
    
    print("\nInstructions:")
    for i, instruction in enumerate(random_recipe['instructions'], start=1):
        print(f"{i}. {instruction}")

if __name__ == "__main__":
    print("Welcome to the Random Recipe Suggester!")
    
    while True:
        input("\nPress Enter for a random recipe suggestion (type 'exit' to quit): ")
        
        user_input = input("Do you want a recipe suggestion? (yes/no): ").lower()
        
        if user_input == 'no':
            print("Exiting the Random Recipe Suggester.")
            break
        elif user_input != 'yes':
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        suggest_random_recipe()
