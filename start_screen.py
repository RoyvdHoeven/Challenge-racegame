import re
import time

from bs4 import BeautifulSoup
from colorama import init

init()

# !Do not change ansi_escape value!
ansi_escape = re.compile(r'\x1b\[[0-9;]*m')


def visible_len(text) -> int:
    return len(ansi_escape.sub('', text))


def rgb_to_ansi(r, g, b) -> str:
    return f"\033[38;2;{r};{g};{b}m"


def html_to_ansi(file_path) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

        container = soup.find("div", class_="ascii-container")
        output = ""

        for element in container.children:

            if element.name == "span":
                style = element.get("style", "")
                text = element.text
                match = re.search(r"rgb\((\d+), \s*(\d+), \s*(\d+)\)", style)

                if match:
                    r, g, b = map(int, match.groups())
                    output += rgb_to_ansi(r, g, b) + text

            elif element.string:
                output += element.string

        output += "\033[0m"
        return output


def overlay_line(base_line, overlay, start_x) -> str:
    result = []
    visible_index = 0
    i = 0

    while i < len(base_line):
        if base_line[i] == "\033":
            end = i
            while end < len(base_line) and base_line[end] != "m":
                end += 1
            end += 1
            result.append(base_line[i:end])
            i = end
        else:
            if start_x <= visible_index < start_x + len(overlay):
                result.append(overlay[visible_index - start_x])
            else:
                result.append(base_line[i])
            visible_index += 1
            i += 1

    return "".join(result)


def build_welcome_box(width, height, message) -> list[str]:
    inner_width = width - 2
    padding = (inner_width - len(message)) // 2

    box = [
        "╔" + "═" * inner_width + "╗",
        "║" + " " * inner_width + "║",
        "║" + " " * padding + message + " " * (inner_width - padding - len(message)) + "║",
        "║" + " " * inner_width + "║",
        "╚" + "═" * inner_width + "╝"
    ]

    return box


def welcome_message(html_file_path):
    ansi_art = html_to_ansi(html_file_path)
    art_lines = ansi_art.splitlines()

    box_width = 80
    box_height = 5
    message = "WELCOME TO [ Terminal Racer ]"

    max_width = max(visible_len(line) for line in art_lines)
    art_lines = [line + " " * (max_width - visible_len(line)) for line in art_lines]

    start_x = (max_width - box_width) // 2
    start_y = (len(art_lines) - box_height) // 2

    welcome_box = build_welcome_box(box_width, box_height, message)

    for i, box_line in enumerate(welcome_box):
        art_lines[start_y + i] = overlay_line(art_lines[start_y + i], box_line, start_x)

    print("\n".join(art_lines))
    time.sleep(1)


if __name__ == "__main__":
    welcome_message()

# Welcome box message old
"""
        print("╔════════════════════════════════════════════════════════════════════════════════╗")
        print("║                                                                                ║")
        print("║▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄║")
        print("║                                                                                ║")
        print("║                        WELCOME TO [ Terminal Racer ]                           ║")
        print("║                                                                                ║")
        print("║▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄║")
        print("║                                                                                ║")
        print("╚════════════════════════════════════════════════════════════════════════════════╝")
    """
