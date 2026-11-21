import sys
import os
import textwrap
from dataclasses import dataclass

class bubble:
    def boxed_input(message, prompt_label="Input: ", width=69, indent=4):  #function for making the box style input
        os.system('cls' if os.name == 'nt' else 'clear')
        border = "|" + "-" * (width - 2) + "|"
        pad = " " * indent
        max_text_width = width - (indent * 2)

        print(border)
        print()

        # Automatically wraps each paragraph to fit cleanly inside the box width
        for paragraph in message.splitlines():
            if paragraph.strip() == "":
                print()
            else:
                wrapped_lines = textwrap.wrap(paragraph.strip(), width=max_text_width)
                for line in wrapped_lines:
                    print(f"{pad}{line}")

        # Print the prompt line, blank line, and bottom border
        print(f"{pad}{prompt_label}")
        print()
        print(border)

        # Move cursor UP 3 lines and RIGHT (indent + prompt length) spaces
        offset = indent + len(prompt_label)
        user_input = input(f"\033[3A\033[{offset}C")
        print("\033[2B")

        return user_input

    def boxed_print(message, width=69, indent=4): #function for making the box style print
        os.system('cls' if os.name == 'nt' else 'clear')
        border = "|" + "-" * (width - 2) + "|"
        pad = " " * indent
        max_text_width = width - (indent * 2)

        print(border)
        print()

        for paragraph in message.splitlines():
            if paragraph.strip() == "":
                print()
            else:
                wrapped_lines = textwrap.wrap(paragraph.strip(), width=max_text_width)
                for line in wrapped_lines:
                    print(f"{pad}{line}")

        print()
        print(border)


    # Enable ANSI escape codes on Windows
    if os.name == 'nt':
        os.system("")

    def _get_key():
        """Reads a single keypress (cross-platform: Windows, Mac, Linux)."""
        if os.name == 'nt':
            import msvcrt
            key = msvcrt.getch()
            if key in (b'\x00', b'\xe0'):  # Arrow keys prefix on Windows
                key = msvcrt.getch()
                return {b'H': 'UP', b'P': 'DOWN'}.get(key, '')
            if key == b' ':
                return 'SPACE'
            if key == b'\r':
                return 'ENTER'
        else:
            import tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
                if ch == '\x1b':  # Arrow keys prefix on Mac/Linux
                    ch2 = sys.stdin.read(2)
                    return {'[A': 'UP', '[B': 'DOWN'}.get(ch2, '')
                if ch == ' ':
                    return 'SPACE'
                if ch in ('\r', '\n'):
                    return 'ENTER'
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ''

    def boxed_multiselect(message, options, width=69, indent=4):
        os.system('cls' if os.name == 'nt' else 'clear')
        border = "|" + "-" * (width - 2) + "|"
        pad = " " * indent
        max_text_width = width - (indent * 2)

        cursor = 0
        selected = set()
        first_draw = True

        # Pre-wrap the header message lines
        header_lines = []
        for paragraph in message.splitlines():
            if paragraph.strip() == "":
                header_lines.append("")
            else:
                header_lines.extend(textwrap.wrap(paragraph.strip(), width=max_text_width))

        # Total lines the box takes up (used to redraw in place)
        total_lines = 4 + len(header_lines) + 1 + len(options)

        sys.stdout.write("\033[?25l")  # Hide terminal cursor for clean UI
        try:
            while True:
                if not first_draw:
                    # Move cursor back up to the top of the box to overwrite it
                    sys.stdout.write(f"\033[{total_lines}A")
                first_draw = False

                print(border)
                print()
                for line in header_lines:
                    print(f"{pad}{line}" if line else "")
                print()

                for i, option in enumerate(options):
                    pointer = ">" if i == cursor else " "
                    checkbox = "[x]" if i in selected else "[ ]"
                    # \033[K clears any leftover characters on the line
                    print(f"{pad}{pointer} {checkbox} {option}\033[K")

                print()
                print(border)
                sys.stdout.flush()

                key = bubble._get_key()
                if key == 'UP':
                    cursor = (cursor - 1) % len(options)
                elif key == 'DOWN':
                    cursor = (cursor + 1) % len(options)
                elif key == 'SPACE':
                    if cursor in selected:
                        selected.remove(cursor)
                    else:
                        selected.add(cursor)
                elif key == 'ENTER':
                    break
        finally:
            sys.stdout.write("\033[?25h")  # Always restore cursor visibility
            sys.stdout.flush()

        # Return the selected items in their original order
        return [options[i] for i in sorted(selected)]

player = "place_holder"
    