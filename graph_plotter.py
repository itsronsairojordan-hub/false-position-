import numpy as np 
import matplotlib.pyplot as plt
import math

def false_position(func, xl, xu, error_tolerance, max_iterations):

    # function evaluator 
    def f(x):
        allowed = {
            "exp": np.exp,
            "np": np,
            "e": math.e,
            "math": math,
            "sin": np.sin,
            "cos": np.cos,
            "tan": np.tan,
            "pi": np.pi,
            "x": x
            }
        return eval(func, {"__builtins__": None}, allowed)


    # check if xl and xu bracket a root
    if f(xl) * f(xu) >= 0:
        print("\nERROR: f(xl) and f(xu) must have opposite signs.")
        return

    print("\n{:<10} {:>10} {:>10} {:>10} {:>12} {:>12} {:>12} {:>12} {:>10}".format(
        "Iter", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "f(xl)*f(xr)", "Error (%)"
    ))
    print("-" * 110)

    xr_previous = None
    xr_points = []
    xl_points = []
    xu_points = []
    xl_initial = xl
    xu_initial = xu

    iteration = 1
    while True:  # loop until error tolerance OR iteration limit is met

        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu)) # eto yung formula for false pos

        xr_points.append(xr)
        xl_points.append(xl)
        xu_points.append(xu)

        error = abs((xr - xr_previous) / xr) * 100 if xr_previous else None

        print(
        "{:<10d} {:>10.4f} {:>10.4f} {:>10.4f} {:>12.4f} {:>12.4f} {:>12.4f} {:>12.4f} {:>10}".format(
            iteration, xl, xu, xr, f(xl), f(xu), f(xr), f(xl) * f(xr),
            f"{error:.2f}%" if error is not None else "-"
            )
        )

        # update bounds based on sign test
        if f(xl) * f(xr) < 0:
            xu = xr
        else:
            xl = xr

    # stopping condition 1 → if ever na mareach niya yun error tolerance
        if error is not None and error <= error_tolerance:
            break

    # stopping condition 2 → if ever na mareach yung iterattion na ininput ng user (unless set to 0 tuloy tuloy lang hanggang mameet si error tolerance)
        if max_iterations != 0 and iteration >= max_iterations:
            break

        xr_previous = xr
        iteration += 1


    print("\nFinal Root Approximation:", xr.round(4))

    # -------- GRAPH SECTION ---------
    # Generate x and y values
    x_vals = np.linspace(xl_initial - abs(xu_initial - xl_initial),
                         xu_initial + abs(xu_initial - xl_initial), 10000)
    
    y_vals = f(x_vals) #Takes all x_vals and plugs them into the function f(x). Returns a list (array) of y values that correspond to each x.

    y_margin = (max(y_vals) - min(y_vals)) * 0.2 # Para hindi dikit na dikit yung graph sa frame.
    y_min = min(y_vals) - y_margin
    y_max = max(y_vals) + y_margin

    plt.figure(figsize=(10, 7)) #Opens a new plot window with size 10 inches wide × 7 inches tall.

    plt.axhline(0, color="black", linewidth=1.5)
    plt.axvline(0, color="black", linewidth=1.5)# axhline(0) draws horizontal line at y = 0 (x-axis) and axvline(0) draws vertical line at x = 0 (y-axis)

    plt.plot(x_vals, y_vals, label=f"f(x) = {func}", linewidth=2) # Plots the function f(x)

    # Plot ONLY the final xl and xu values
    plt.vlines(xl, y_min, y_max, color="blue", linestyles="--", linewidth=2, label="Last xl")
    plt.vlines(xu, y_min, y_max, color="red", linestyles="--", linewidth=2, label="Last xu")

# Plot ONLY the final xr (estimated root)
    plt.scatter([xr], [0], color="lime", s=200, marker=".", edgecolors="black", linewidth=1.5, label="Final xr")


    plt.scatter([xr], [0], color="lime", s=200, marker='*',
                zorder=6, edgecolors='black', linewidth=1.5)

    plt.title("False Position Method Visualization", fontsize=14, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("f(x)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', fontsize=9)

    plt.ylim(y_min, y_max)
    plt.tight_layout()
    plt.show()


print("False Position Method Calculator with Graph")
print("=" * 55)

func = input("Enter the function in terms of x (example: x**3 - 4*x + 1): ")
xl = float(input("Enter the lower bound (xl): "))
xu = float(input("Enter the upper bound (xu): "))
error_tolerance = float(input("Enter acceptable error % (example: 0.01 for 0.01%): "))
max_iterations = int(input("Enter maximum number of iterations: "))

false_position(func, xl, xu, error_tolerance, max_iterations)
