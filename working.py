def false_position(func, xl, xu, error_tolerance, max_iterations):

    # Evaluate the user-input function
    def f(x):
        return eval(func)

    # Check if the interval brackets a root
    if f(xl) * f(xu) >= 0:
        print("\nERROR: f(xl) and f(xu) must have opposite signs.")
        print("False Position method cannot proceed.\n")
        return

    # Table Header
    print("\n{:<10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>12} {:>14} {:>10}".format(
        "Iteration", "xl", "xu", "xr", "f(xl)", "f(xu)", "f(xr)", "f(xl)*f(xr)", "Error"
    ))
    print("-" * 115)

    xr_previous = None

    for iteration in range(1, max_iterations + 1):

        # False Position formula
        xr = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))

        # Compute relative error after first iteration
        if xr_previous is not None:
            error = abs((xr - xr_previous) / xr)
        else:
            error = None

        product = f(xl) * f(xr)  # f(xl)*f(xr)

        # Print formatted row (rounded for display only)
        print("{:<10d} {:>10.4f} {:>10.4f} {:>10.4f} {:>10.4f} {:>10.4f} {:>12.4f} {:>14.4f} {:>10}".format(
            iteration, xl, xu, xr, f(xl), f(xu), f(xr), product,
            f"{error * 100:.2f}%" if error is not None else "-"
        ))

        # Update interval based on sign change
        if product < 0:
            xu = xr
        else:
            xl = xr

        xr_previous = xr

        # Stop if error requirement is met
        if error is not None and error < error_tolerance:
            break

    # Final output summary
    print("\nFinal Result")
    print(f"Approximate Root  : {xr:.4f}")
    print(f"Approx. Error     : {error * 100:.2f}%" if error is not None else "Approx. Error : -")
    print(f"Final Interval    : [{xl:.4f}, {xu:.4f}]\n")


# ===================== USER INPUT SECTION ===================== #

print("False Position Method Calculator")
print("=" * 55)

func = input("Function: ")
xl = float(input("(xl): "))
xu = float(input("(xu): "))
error_tolerance = float(input("Relative error (decimal): "))
max_iterations = int(input("Iterations: "))

false_position(func, xl, xu, error_tolerance, max_iterations)
