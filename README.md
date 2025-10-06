# Leaf-Integration

Leaf Integration: Area between $y=\sqrt{x}$ and $y=x^2$

## Overview

This project calculates and visualizes the area between two curves: $y = \sqrt{x}$ and $y = x^2$. The region bounded by these curves resembles a leaf shape, hence the name "Leaf Integration." The visualization demonstrates a classic calculus problem of finding the area between two functions using definite integration.

The curves intersect at two points: $(0, 0)$ and $(1, 1)$. Between these points, $\sqrt{x}$ lies above $x^2$, creating the characteristic leaf-shaped region.

## Math Background

### Finding the Intersection Points

To find where the curves intersect, we solve:
$$\sqrt{x} = x^2$$

Squaring both sides:
$$x = x^4$$
$$x^4 - x = 0$$
$$x(x^3 - 1) = 0$$

This gives us $x = 0$ or $x = 1$.

### Calculating the Area

The area between the curves is given by:
$$A = \int_{0}^{1} (\sqrt{x} - x^2) \, dx$$

Evaluating the integral:
$$A = \int_{0}^{1} x^{1/2} \, dx - \int_{0}^{1} x^2 \, dx$$

$$A = \left[\frac{x^{3/2}}{3/2}\right]_{0}^{1} - \left[\frac{x^3}{3}\right]_{0}^{1}$$

$$A = \left[\frac{2x^{3/2}}{3}\right]_{0}^{1} - \left[\frac{x^3}{3}\right]_{0}^{1}$$

$$A = \frac{2}{3} - \frac{1}{3} = \frac{1}{3}$$

**Result:** The area of the leaf-shaped region is exactly **1/3 square units**.

## Requirements

To run this project, you need:

- Python 3.7 or higher
- NumPy (for numerical computations)
- Matplotlib (for visualization)
- SciPy (for numerical integration)

Install the required packages using:
```bash
pip install numpy matplotlib
```

Or if you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/0PKunal/Leaf-Integration.git
   cd Leaf-Integration
   ```

2. Install the required dependencies:
   ```bash
   pip install numpy matplotlib
   ```

3. Run the Python script:
   ```bash
   python leaf_integration.py
   ```

The script will:
- Calculate the area between the curves numerically
- Generate a visualization showing both curves and the shaded region
- Display the calculated area value
- Save the plot as an image file

## Output Preview

The program generates a visualization showing:
- The curve $y = \sqrt{x}$ (typically in blue)
- The curve $y = x^2$ (typically in red)
- The shaded leaf-shaped region between them
- The calculated area value (≈ 0.3333 or 1/3)

<p align="center">
  <img src="Leaf_Integration.png" alt="Leaf Integration" width="400">
*Image: Visualization of the area between $y = \sqrt{x}$ and $y = x^2$*
</p>


**Mathematical Note:** This problem beautifully demonstrates how integration can compute areas of complex shapes. The result of exactly 1/3 is a precise mathematical fact, showcasing the elegance of calculus in solving geometric problems.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---
<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/0PKunal">0PKunal</a></p>
  <p>If this project helped you, please give it a ⭐️</p>
</div>
