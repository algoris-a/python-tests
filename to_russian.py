from transformers import pipeline

def translate_user_input(prompt_message):
    """
    Function to read prompts from the user (english).
    :param prompt_message: The message to display to the user.
    :return: Translated input (russian).
    """

    # Define the translation pipeline
    translator = pipeline(task="translation_en_to_ru", model="Helsinki-NLP/opus-mt-en-ru")

    # Read the user input
    user_input = input(prompt_message)
    if user_input.strip().lower() == "q":
        return "q"
    
    # Translate the user input to Russian
    translations = translator(user_input, clean_up_tokenization_spaces=True)
    # Print the translated text
    print(f"Translated to Russian: {translations[0]['translation_text']}")
    # Return translated text
    return translations[0]['translation_text']

# Example usage
if __name__ == "__main__":
    # to_ru = translate_user_input("EN>: ")
    # print(f"RU>: {to_ru}")

    while True:
        to_ru = translate_user_input("EN ('Q' to stop)>: ")
        if to_ru == "q":
            print("Exiting...")
            break