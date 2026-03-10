# A function that colors the provided text (ONLY FOR THE TERMINAL)
def color(
    text: str, fg: str | None = None,
    bg: str | None = None, bold: bool | str = False,
    end_fg: str | None = None, end_bg: str | None = None,
    end_bold: bool | str = False, reset: bool = True
) -> str:

    # Sets to store temporary values
    bold = '1' if bold else '0'
    end_bold = '1' if end_bold else '0'
    fg = fg.replace(" ", "") if fg else None
    bg = bg.replace(" ", "") if bg else None
    end_fg = end_fg.replace(" ", "") if end_fg else None
    end_bg = end_bg.replace(" ", "") if end_bg else None
    ends = ''

    # Checks if chosen color should continue after the provided text
    if reset:
        ends = '\033[0m'
    if end_fg and end_bg:
        ends = f'\033[{end_bold};38;2;{end_fg};48;2;{end_bg}m'
    elif end_fg:
        ends = f'\033[{end_bold};38;2;{end_fg}m'
    elif end_bg:
        ends = f'\033[{end_bold};48;2;{end_bg}m'

    # Checks if both foreground and background should be changed
    if fg and bg:
        return f'\033[{bold};38;2;{fg};48;2;{bg}m{text}{ends}'
    elif fg:
        return f'\033[{bold};38;2;{fg}m{text}{ends}'
    elif bg:
        return f'\033[{bold};48;2;{bg}m{text}{ends}'

    return f'\033[{bold}m{text}{ends}'
