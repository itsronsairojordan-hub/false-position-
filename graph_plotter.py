import numpy as np
import matplotlib.pyplot as plt
import math

def false_position(func, xl, xu, error_tolerance, max_iterations):

    # ✅ function evaluator (safe eval)
    def f(x):
        allowed = {
            "exp": np.exp,
            "np": np,
            "e": math.e,
            "math": math,
            "x": x
        }
        return eval(func, {"__builtins__": None}, allowed)

    # ✅ Check if xl and xu bracket a root
    if f(xl) * f(xu) >= 0:
        print("\nERROR: f(xl) and f(xu) must have opposite signs.")
        return

    print("\n{:<10} {:>12} {:>12} {:>12} {:>12} {:>12} {:>12}".format(
        "Iter", "xl", "xu", "xr", "f(xl)", "f(xu)", "Error (%)"
    ))
    print("-" * 90)

    xr_previous = None
    xr_points = []
    xl_points = []
    xu_points = []

    # Store initial bounds
    xl_initial = xl
    xu_initial = xu
    
    for iteration in range(1, max_iterations + 1):
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))  # False Position formula
        xr_points.append(xr)
        xl_points.append(xl)
        xu_points.append(xu)

        error = abs((xr - xr_previous) / xr) * 100 if xr_previous else None

        print("{:<10d} {:>12.6f} {:>12.6f} {:>12.6f} {:>12.6f} {:>12.6f} {:>12}".format(
            iteration, xl, xu, xr, f(xl), f(xu),
            f"{error:.6f}%" if error is not None else "-"
        ))

        # update bounds
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

        if error is not None and error < error_tolerance:
            break

        xr_previous = xr

    print("\nFinal Root Approximation:", xr)

    # -------- GRAPH SECTION ---------
    x_vals = np.linspace(xl_initial - abs(xu_initial - xl_initial), 
                         xu_initial + abs(xu_initial - xl_initial), 10000)
    y_vals = f(x_vals)

    # Calculate y limits first
    y_margin = (max(y_vals) - min(y_vals)) * 0.2
    y_min = min(y_vals) - y_margin
    y_max = max(y_vals) + y_margin

    plt.figure(figsize=(10, 7))
    
    # Draw axes (x-axis and y-axis)
    plt.axhline(0, color="black", linewidth=1.5)
    plt.axvline(0, color="black", linewidth=1.5)
    
    plt.plot(x_vals, y_vals, label=f"f(x) = {func}", linewidth=2)
    
    # Plot vertical lines for all xl and xu values (INFINITE - from y_min to y_max)
    colors_xl = plt.cm.Blues(np.linspace(0.3, 0.9, len(xl_points)))
    colors_xu = plt.cm.Reds(np.linspace(0.3, 0.9, len(xu_points)))
    
    for i, (xl_val, xu_val) in enumerate(zip(xl_points, xu_points)):
        alpha = 0.4 + (0.6 * i / max(1, len(xl_points) - 1))
        # Draw lines from bottom to top of plot
        plt.vlines(xl_val, y_min, y_max, colors=colors_xl[i], linestyles='--', 
                  linewidth=1.5, alpha=alpha, label=f'xl (iter {i+1})' if i < 3 else '')
        plt.vlines(xu_val, y_min, y_max, colors=colors_xu[i], linestyles='--', 
                  linewidth=1.5, alpha=alpha, label=f'xu (iter {i+1})' if i < 3 else '')
    
    # Plot xr points
    plt.scatter(xr_points, [0]*len(xr_points), color="green", s=80, 
               zorder=5, label="xr values", edgecolors='black', linewidth=1)
    
    # Mark final root
    plt.scatter([xr], [0], color="lime", s=200, marker='*', 
               zorder=6, label="Final Root", edgecolors='black', linewidth=1.5)
    
    plt.title("False Position Method Visualization", fontsize=14, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', fontsize=9)
    
    # Set limits after drawing everything
    plt.ylim(y_min, y_max)
    plt.tight_layout()
    plt.show()


# ================ USER INPUT ================
print("False Position Method Calculator with Graph")
print("=" * 55)

func = input("Enter the function in terms of x (example: x**3 - 4*x + 1): ")
xl = float(input("Enter the lower bound (xl): "))
xu = float(input("Enter the upper bound (xu): "))
error_tolerance = float(input("Enter acceptable error % (example: 0.01 for 0.01%): "))
max_iterations = int(input("Enter maximum number of iterations: "))

false_position(func, xl, xu, error_tolerance, max_iterations)