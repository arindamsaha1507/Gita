"""Converts the data in the repo to webpages."""

import os


def read_obsidian_file(shloka_number: int) -> str:
    """Reads the contents of the Obsidian file."""

    fname = f"Obsidian/श्लोक_{shloka_number}.md"

    with open(fname, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def get_shloka(shloka_number: int) -> str:
    """Returns the shloka number in the format to be displayed on the webpage."""

    data = read_obsidian_file(shloka_number)

    lines = data.split("\n")

    end_line_index = [i for i, line in enumerate(lines) if line.startswith("##")][0]

    shloka = lines[2:end_line_index]
    shloka = "\n".join(shloka)

    print(shloka)

    return shloka


def get_chapter_and_shloka(shloka_number: int) -> tuple:
    """Returns the chapter and shloka number for the given shloka number."""

    shloka = get_shloka(shloka_number)

    start_index = shloka.find("॥") + 1
    number = shloka[start_index + 1 : -3]

    chapter, shloka = number.split("-")

    return chapter, shloka


def create_webpage(shloka_number: int) -> None:
    """Creates a webpage for the given shloka number."""

    fname = f"webpages/shloka_{shloka_number}.md"

    chapter, shloka = get_chapter_and_shloka(shloka_number)

    string = f"# अध्याय {chapter}\n\n"
    string += f"## श्लोक {shloka}\n\n"
    string += get_shloka(shloka_number).replace("\n", "<br>")
    string += "\n\n"

    with open(fname, "w", encoding="utf-8") as file:
        file.write(string)


def main():
    """Main function."""

    for i in range(1, 701):
        create_webpage(i)


if __name__ == "__main__":
    main()
