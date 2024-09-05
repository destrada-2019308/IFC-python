
def centerWindow(window, height, width):
    width = window.winfo_screenwidth()
    height = window.winfo_screenheigth()
    x = int((width/2) - (width/2))
    y = int((height/2) - (height/2))

    return window.geometry(f"{width}x{height}+{x}+{y}")