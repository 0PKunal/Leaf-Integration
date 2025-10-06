# Modules for calculation and ploting
import numpy as np
import matplotlib.pyplot as plt

# Define x range
x = np.linspace(0, 1, 250)

# Define curves
y1 = np.sqrt(x)   # upper curve
y2 = x**2         # lower curve

# Plot creation
plt.figure(figsize=(6, 6))
plt.plot(x, y1, 'g-', linewidth=2, label=r'$y=\sqrt{x}$')
plt.plot(x, y2, 'b-', linewidth=2, label=r'$y=x^2$')

# Filling the leaf area between the curves
plt.fill_between(x, y1, y2, color='mediumseagreen', alpha=0.4)

# Labels and title
plt.title(r'Leaf Integration: Area between $y=\sqrt{x}$ and $y=x^2$', fontsize=13)
plt.xlabel(r'x$\longrightarrow$')
plt.ylabel(r'y$\longrightarrow$')

# Grid, legend, and axis limits
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.axis('equal')
plt.tight_layout()

# Showing the plot
plt.show()
