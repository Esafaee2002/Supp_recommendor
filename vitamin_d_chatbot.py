"""Simple Vitamin D recommendation chatbot.

This script interacts with the user via the command line, asking a few
health and lifestyle questions. At the end it offers a basic suggestion
on whether the user might need vitamin D supplementation.

It is designed to demonstrate the kind of logic that could later be
powered by an AI service such as MedGemma.
"""

def ask_yes_no(question: str) -> bool:
    """Prompt the user with a yes/no question until they respond correctly."""
    while True:
        answer = input(f"{question} (yes/no): ").strip().lower()
        if answer in {"yes", "no"}:
            return answer == "yes"
        print("Please respond with 'yes' or 'no'.")


def main() -> None:
    print("Welcome to the Vitamin D Chatbot!")
    print(
        "I'll ask a few questions to help determine if you might benefit from extra vitamin D."\
    )

    exposure = ask_yes_no(
        "Do you get at least 15 minutes of direct sunlight per day?"
    )
    diet = ask_yes_no(
        "Do you regularly eat vitamin D rich foods like fatty fish or fortified dairy?"
    )
    age_above_50 = ask_yes_no("Are you older than 50 years?")
    symptoms = ask_yes_no("Are you experiencing bone pain or muscle weakness?")

    # Simple scoring system
    risk_score = int(not exposure) + int(not diet) + int(age_above_50) + int(symptoms)

    if risk_score >= 2:
        recommendation = (
            "You may benefit from vitamin D supplementation. "
            "Consider discussing this with your healthcare provider."
        )
    else:
        recommendation = "You likely do not need additional vitamin D at this time."

    print(recommendation)
    print(
        "\nNote: This chatbot is for demonstration purposes and does not provide medical advice."
    )


if __name__ == "__main__":
    main()
