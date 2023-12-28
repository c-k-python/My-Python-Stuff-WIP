import random

def generate_theme_based_app_idea():
    themes = [
        "Randomization",
        "Timezone",
        "Optimization",
    ]

    app_ideas = {
        "Randomization": [
            "Diverse Data Dice Roller - Generates random data sets for statistical analysis",
            "Decision Engine - Helps users make random decisions based on user-defined criteria",
            "Variety Playlist Creator - Creates diverse music playlists based on user preferences",
            "Art Prompt Generator - Inspires artists with random prompts for creative projects",
            "Recipe Roulette - Suggests random recipes for cooking enthusiasts",
        ],
        "Timezone": [
            "Global Meeting Scheduler - Finds optimal meeting times across different timezones",
            "Jetsetter's Companion - Assists frequent travelers in managing multiple timezone schedules",
            "World Clock Widget - Displays a customizable world clock with timezone conversions",
            "Virtual Flight Assistant - Plans flights considering timezones and layovers",
            "International Event Planner - Coordinates events across global timezones",
        ],
        "Optimization": [
            "Efficient Disk Organizer - Optimizes file storage and arrangement for faster access",
            "Memory Boost Pro - Enhances system performance by optimizing RAM usage",
            "Energy Saver Plus - Optimizes CPU usage and power settings for improved energy efficiency",
            "Website Speed Analyzer - Analyzes and suggests improvements for website loading speed",
            "Network Traffic Optimizer - Manages and prioritizes internet traffic for improved connectivity",
        ],
    }

    theme = random.choice(themes)
    category = random.choice(list(app_ideas.keys()))
    
    # Get the list of ideas for the selected category
    ideas = app_ideas[category]
    
    # Check if there are remaining ideas for the category
    if not ideas:
        return "No more ideas for this category. Try another theme."

    # Select a random idea
    idea = random.choice(ideas)

    # Remove the selected idea from the list
    ideas.remove(idea)

    result = f"Theme: {theme}\nCategory: {category}\nApp Idea: {idea}"
    print(result)
    return result

if __name__ == "__main__":
    # Keep generating ideas until there are no more ideas left
    while True:
        theme_based_app_idea = generate_theme_based_app_idea()
        if "No more ideas" in theme_based_app_idea:
            print("All ideas exhausted. Press Enter to exit.")
            input()  # Wait for user input before exiting
            break
        else:
            input("Press Enter for the next idea...")
