# Practical-4 (Gradient Descent Algorithm)

### 0. Import libraries:
```python3
import numpy as np
import matplotlib.pyplot as plt
```
### 1. Define the function and its derivative
```python3
def f(x):
    return (x + 3)**2

def grad_f(x):
    return 2 * (x + 3)
```

### 2. Initialize parameters
```python3
x_current = 2.0
learning_rate = 0.1
tolerance = 1e-6
max_iterations = 100

history = [x_current]
converged = False
```

### 3. Gradient Descent loop
```python3
for i in range(max_iterations):
    gradient = grad_f(x_current)
    x_next = x_current - learning_rate * gradient

    history.append(x_next)

    print(f"Iteration {i+1}: x = {x_next:.6f}, "
          f"f(x) = {f(x_next):.6f}")

    if abs(x_next - x_current) < tolerance:
        x_current = x_next
        converged = True
        print(f"\nConverged after {i+1} iterations.")
        break

    x_current = x_next
```

### 4. Print the result
```python3
if not converged:
    print("\nMaximum iterations reached.")

print("Minimum point x =", x_current)
print("Minimum function value y =", f(x_current))
```

### 5. Plot convergence
```python3
plt.plot(history, [f(x) for x in history], marker="o")
plt.xlabel("x values")
plt.ylabel("f(x)")
plt.title("Gradient Descent Convergence")
plt.grid(True)
plt.show()
```
