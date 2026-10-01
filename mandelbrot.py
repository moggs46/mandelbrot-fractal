import tkinter

# ----- parameters you can tweak -----
WIDTH = 700
HEIGHT = 700
# Standard Mandelbrot view window (square so pixels map 1:1)
RE_MIN = -2.0
RE_MAX = 1.0
IM_MIN = -1.5
IM_MAX = 1.5

MAX_ITER = 60  # higher values give more detail but render slower
INSIDE_COLOUR = "black"
OUTSIDE_COLOUR = "white"

# ----- recursive function: returns True if orbit is non‑divergent (stays bounded) -----
def non_divergent(z_real, z_imag, c_real, c_imag, step, limit):
    # Base cases
    if (z_real*z_real + z_imag*z_imag) > 4.0:
        return False  # divergent
    if step >= limit:
        return True   # treated as non‑divergent within our iteration budget

    # z_{n+1} = z_n^2 + c with complex arithmetic
    # (a + bi)^2 = (a^2 - b^2) + 2ab i
    next_real = (z_real*z_real - z_imag*z_imag) + c_real
    next_imag = (2.0*z_real*z_imag) + c_imag

    # Recurse
    return non_divergent(next_real, next_imag, c_real, c_imag, step + 1, limit)

# ----- map pixel (x, y) to complex plane -----
def pixel_to_complex(px, py):
    # Re axis: left -> RE_MIN, right -> RE_MAX
    # Im axis: top -> IM_MAX, bottom -> IM_MIN (note the flip for screen y increasing downward)
    c_real = RE_MIN + (px / (WIDTH - 1)) * (RE_MAX - RE_MIN)
    c_imag = IM_MAX - (py / (HEIGHT - 1)) * (IM_MAX - IM_MIN)
    return c_real, c_imag

# ----- draw the fractal -----
def main():
    window = tkinter.Tk()
    window.title("Mandelbrot Set")
    window.geometry(f"{WIDTH}x{HEIGHT}")

    canvas = tkinter.Canvas(window, width=WIDTH, height=HEIGHT, highlightthickness=0)
    canvas.pack()

    # For each pixel, treat its mapped complex number as c, seed orbit at z=0
    # If non‑divergent within MAX_ITER, draw INSIDE_COLOUR, else OUTSIDE_COLOUR
    y = 0
    while (y < HEIGHT):
        x = 0
        # Draw row‑by‑row to give visible progress
        while (x < WIDTH):
            c_real, c_imag = pixel_to_complex(x, y)
            if non_divergent(0.0, 0.0, c_real, c_imag, 0, MAX_ITER):
                colour = INSIDE_COLOUR
            else:
                colour = OUTSIDE_COLOUR
            # Draw a single pixel as a 1‑pixel line
            canvas.create_line(x, y, x+1, y, fill=colour)
            x = x + 1
        if (y % 50 == 0):
            # Refresh occasionally so the window stays responsive during drawing
            canvas.update()
        y = y + 1

    canvas.update()
    window.mainloop()

if __name__ == "__main__":
    main()
