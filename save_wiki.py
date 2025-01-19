import wikipediaapi


def save_wikipedia_page_to_file(keyword: str, filename: str, language: str = 'ja'):
    """
    Searches for a Wikipedia page and saves its content to a text file.

    :param keyword: The title of the Wikipedia page to search for.
    :param filename: The name of the file where the content will be saved.
    :param language: The language of the Wikipedia (default is 'en' for English).
    """
    # Define a user agent to comply with Wikipedia's policy
    user_agent = "MyWikipediaApp/1.0 (https://example.com; myemail@example.com)"

    # Initialize Wikipedia API with a user agent
    wiki_wiki = wikipediaapi.Wikipedia(language=language, user_agent=user_agent)

    # Get the page
    page = wiki_wiki.page(keyword)

    if page.exists():
        # Save the content to a file
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"Title: {page.title}\n\n")
            file.write(page.text)
        print(f"Page '{keyword}' has been saved to '{filename}'.")
    else:
        print(f"The page '{keyword}' does not exist on Wikipedia in the {language} language.")


# Example usage
save_wikipedia_page_to_file(keyword="スプラトゥーン3", filename="output_wikipedia.txt")
