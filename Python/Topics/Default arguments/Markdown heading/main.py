def heading(text, level=1):
    if level < 1:
        return f"{'#' * 1} {text}"
    elif level > 6:
        return f"{'#' * 6} {text}"
    else:
        return f"{'#' * level} {text}"
