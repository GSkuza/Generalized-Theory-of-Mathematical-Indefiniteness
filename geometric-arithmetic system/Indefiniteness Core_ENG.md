# indefiniteness_core.py Documentation

## English Version

### Introduction

Runtime primitives for the Generalized Theory of Mathematical Indefiniteness (GTMØ). This module offers two public objects:

-   `O`: The unique *ontological singularity* (Ø).
-   `AlienatedNumber`: A symbolic placeholder for *alienated numbers* (ℓ∅).

### Design Goals

The rewrite of this module aimed for:

-   **Singleton safety**: `O is O` holds true even under import reloads and pickling/unpickling.
-   **Fail-fast strict mode**: Setting the environment variable `GTM_STRICT=1` makes any arithmetic with `O` or `AlienatedNumber` raise a `SingularityError` instead of silently resulting in `O`.
-   **Compatibility**: Retains the original public API (e.g., `O_empty_singularity` representation, absorbing arithmetic operators) to ensure existing notebooks and scripts continue to work.
-   **Pythonic integration**: Implements `__bool__`, `__eq__`, and hashing, and derives from `numbers.Number` for smoother interoperability with numeric libraries.
-   **Typed**: Full `mypy` support and is PEP 561 ready.

### Public API

#### 1. `O` / `Singularity` (Ontological Singularity Ø)

-   **Description**: Represents the unique ontological singularity (Ø) in GTMØ. It acts as an absorbing element in arithmetic operations.
-   **Instance**: The primary way to access the singularity is via the `O` constant.
    ```python
    from indefiniteness_core import O
    ```
-   **Singleton**: `O` is a true singleton. The expression `O is O` will always be `True`, even across module reloads or pickling/unpickling processes.
-   **Representation**: `repr(O)` yields the string `"O_empty_singularity"`.
-   **Boolean Value**: In a boolean context, `O` evaluates to `False` (i.e., `bool(O)` is `False`).
-   **Arithmetic Behavior**:
    -   **Default Mode**: Any arithmetic operation involving `O` (e.g., `O + 5`, `5 * O`) results in `O`.
    -   **Strict Mode**: If Strict Mode is enabled (see Configuration), such operations will raise a `SingularityError`.
-   **Type**: `O` is an instance of the `Singularity` class, which inherits from `numbers.Number`.
-   **Hashing & Equality**: `O` is hashable. `O == O` is `True`. `O` is only considered equal to itself.

#### 2. `AlienatedNumber` (Alienated Numbers ℓ∅)

-   **Description**: A symbolic placeholder for "alienated numbers" (ℓ∅). These are not intended for meaningful arithmetic; operations involving them typically collapse to `O`.
-   **Instantiation**:
    ```python
    from indefiniteness_core import AlienatedNumber
    an_num = AlienatedNumber(identifier: str | int | float | None = None)
    ```
    -   The `identifier` is optional. If not provided, it defaults to `"anonymous"`.
-   **Representation**: `repr(AlienatedNumber("my_id"))` yields the string `"l_empty_num(my_id)"`.
-   **Arithmetic Behavior**:
    -   **Default Mode**: Any arithmetic operation involving an `AlienatedNumber` instance (e.g., `an_num + 5`) results in `O`.
    -   **Strict Mode**: If Strict Mode is enabled, such operations will raise a `SingularityError`.
-   **Type**: The `AlienatedNumber` class inherits from `numbers.Number`.
-   **Hashing & Equality**: `AlienatedNumber` instances are hashable. Two instances are considered equal if they are both `AlienatedNumber`s and their `identifier` attributes are equal.
-   **Domain-specific Methods**:
    -   `psi_gtm_score() -> float`: Returns an epistemic *purity* score. A value approaching 1.0 signifies maximal indefiniteness. Default return value: `0.999_999_999`.
    -   `e_gtm_entropy() -> float`: Returns cognitive *entropy*. A value approaching 0.0 signifies maximal epistemic certainty. Default return value: `1e-9`.

#### 3. `SingularityError`

-   **Description**: An `ArithmeticError` subclass. It is raised when arithmetic operations involving `O` or an `AlienatedNumber` are performed while **Strict Mode** is active.

### Configuration

#### Strict Mode

-   **Enabling**: To enable Strict Mode, set the environment variable `GTM_STRICT` to `1` before running your Python script (e.g., `GTM_STRICT=1 python your_application.py`).
-   **Behavior**: When Strict Mode is enabled, any arithmetic operation that would normally result in `O` due to the involvement of `O` or an `AlienatedNumber` will instead raise a `SingularityError`. This provides a "fail-fast" mechanism.

### JSON Encoding API

-   The `Singularity` and `AlienatedNumber` classes are equipped with a `to_json()` method for convenient serialization to JSON-compatible string representations.
    -   `O.to_json()` returns the string `"\"O_empty_singularity\""`.
    -   `AlienatedNumber("example_id").to_json()` returns the string `"\"l_empty_num(example_id)\""`.

### Usage Examples

```python
import os
from indefiniteness_core import O, AlienatedNumber, SingularityError

# Default behavior (absorbing)
result1 = O + 10
print(f"O + 10 = {result1}")  # Output: O_empty_singularity

an_num = AlienatedNumber("example")
result2 = an_num * 5
print(f"AlienatedNumber * 5 = {result2}")  # Output: O_empty_singularity

print(f"Is O falsy? {not O}")  # Output: True
print(f"O is O: {O is O}")      # Output: True
print(f"O as JSON: {O.to_json()}") # Output: "\"O_empty_singularity\""
print(f"an_num as JSON: {an_num.to_json()}") # Output: "\"l_empty_num(example)\""


# Strict Mode Example (requires GTM_STRICT=1 environment variable)
if os.getenv("GTM_STRICT", "0") == "1":
    print("\nStrict Mode is ON")
    try:
        result_strict = O / 2
        print(f"O / 2 in strict mode = {result_strict}") # This line won't be reached
    except SingularityError as e:
        print(f"Strict mode caught an error for 'O / 2': {e}")

    try:
        result_an_strict = an_num - 7
        print(f"AlienatedNumber - 7 in strict mode = {result_an_strict}") # This line won't be reached
    except SingularityError as e:
        print(f"Strict mode caught an error for 'AlienatedNumber - 7': {e}")
else:
    print("\nStrict Mode is OFF (set GTM_STRICT=1 to enable)")
