# Static Code Analysis Issues

Line numbers refer to the original `movie_reviews.py` analyzed by the `*_report_before.txt` reports.

## 1. High Severity

### Weak MD5 Hash for Review IDs

- **Tool:** Bandit
- **Code:** B324
- **Lines:** 45–46
- **Problem:** MD5 is a weak hash for security-sensitive use.
- **Fix:** Replace MD5 with SHA-256 if a stronger hash is appropriate. Since this is only a review identifier, document that it is not used for security.

## 2. Medium Severity

### Listening on All Network Interfaces

- **Tool:** Bandit
- **Code:** B104
- **Line:** 4
- **Problem:** `0.0.0.0` allows the service to listen on all network interfaces.
- **Fix:** Use `127.0.0.1` for local-only use, or make the host configurable if external access is required.

## 3. Other Findings

### Hardcoded Moderator Password

- **Tool:** Bandit
- **Code:** B105
- **Line:** 6
- **Problem:** A password is stored directly in source code and may be exposed when the file is shared.
- **Fix:** Remove it if unused, or load the secret from an environment variable or secure configuration.

### Standard Random Generator

- **Tool:** Bandit
- **Code:** B311
- **Line:** 41
- **Problem:** `random.choice` is unsuitable for security-sensitive decisions. In this program it only selects a featured movie, so the selection is not security-sensitive.
- **Fix:** Keep `random` for this non-security use and document the context, or use `secrets.choice` if the selection becomes security-sensitive.

### Missing Module and Function Docstrings

- **Tool:** Pylint
- **Codes:** C0114, C0116
- **Lines:** 1, 11, 16, 26, 34, 39, 45, 48, 54, 58
- **Problem:** The module and functions do not describe their purpose, inputs, or results.
- **Fix:** Add a module docstring and concise docstrings for each function.

### Names Do Not Follow Python Naming Conventions

- **Tool:** Pylint
- **Code:** C0103
- **Lines:** 8, 11, 16, 26, 34, 39, 45, 48, 54; arguments at 16 and 45
- **Problem:** Function and argument names use camelCase rather than snake_case. Pylint also flags `featured` as not following its expected naming style.
- **Fix:** Rename functions and arguments to snake_case, and give the mutable `featured` variable a consistent lower-case name.

### Unnecessary `else` After `return`

- **Tool:** Pylint
- **Code:** R1705
- **Lines:** 28–30
- **Problem:** The `else` branch is unnecessary because the `if` branch already returns.
- **Fix:** Remove `else` and place the fallback return after the `if` block.

### Global Statement

- **Tool:** Pylint
- **Code:** W0603
- **Line:** 40
- **Problem:** `pickFeatured` changes module-level state with `global`, making the function harder to reason about and test.
- **Fix:** Return the selected title without changing global state, or encapsulate the state in an object if it needs to persist.

### Index Loop Could Use `enumerate`

- **Tool:** Pylint
- **Code:** C0200
- **Lines:** 50–51
- **Problem:** The loop uses `range(len(titles))` to access both an index and a title.
- **Fix:** Iterate with `enumerate(titles, start=1)`.

### Missing Whitespace Around an Operator

- **Tool:** Flake8
- **Code:** E225
- **Line:** 35
- **Problem:** An operator has no surrounding whitespace.
- **Fix:** Add spaces around the operator.

### Missing Blank Line Before a Top-Level Function

- **Tool:** Flake8
- **Code:** E302
- **Line:** 48
- **Problem:** There is not enough blank-line separation before the function definition.
- **Fix:** Add the required blank lines before the function.

### Inline Comment Spacing

- **Tool:** Flake8
- **Code:** E261
- **Line:** 70
- **Problem:** The inline comment does not have enough spaces before it.
- **Fix:** Add at least two spaces before the inline comment.

### Missing Whitespace After a Comma

- **Tool:** Flake8
- **Code:** E231
- **Line:** 72
- **Problem:** A comma is not followed by whitespace.
- **Fix:** Add a space after the comma.
