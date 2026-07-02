import pyperclip
import webbrowser


def github_search(url="https://duckduckgo.com/?t=ffab&q="):
    query = (
        "https://duckduckgo.com/?t=ffab&q="
        + "site:github.com"
        + "+"
        + pyperclip.paste()
    )
    webbrowser.open_new_tab(query)


if __name__ == "__main__":
    github_search()
