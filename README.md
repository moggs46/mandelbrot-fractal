# Mandelbrot Fractal

Draws the Mandelbrot set pixel by pixel using Python and Tkinter.

## How it works
Each pixel is mapped to a complex number `c`. Starting from `z = 0`, the program repeatedly applies `z = z² + c` using a **recursive** function. If `|z|` grows larger than 2 the point escapes and is drawn white; if it stays bounded for `MAX_ITER` steps it is part of the set and drawn black. Complex multiplication is implemented by hand: `(a + bi)² = (a² − b²) + 2abi`.

## How to run
```bash
python mandelbrot.py
```
You can change the viewing window (`RE_MIN`, `RE_MAX`, `IM_MIN`, `IM_MAX`) and `MAX_ITER` at the top of the file.
