import streamlit as st

def main():
    """Streamlit app for Pythonic and OWASP best practices."""
    # Streamlit page config
    st.set_page_config(
        page_title="Python Best Practices Guide",
        page_icon="🐍",
        layout="wide",
    )

    # Sidebar
    st.sidebar.title("Contents")
    st.sidebar.markdown(
        """
        - [Pythonic Practices](#pythonic-practices)
        - [OWASP Security Guidelines](#owasp-security-guidelines)
        """
    )

    # Header
    st.title("🐍 Python Best Practices Guide")
    st.markdown("This guide provides an overview of **Pythonic coding principles** and **OWASP security guidelines** for writing clean, efficient, and secure Python code.")

    # Pythonic Practices
    st.header("Pythonic Practices")
    st.subheader("1. Code Readability")
    st.markdown(
        """
        - Follow **PEP 8** standards for code formatting.
        - Use meaningful variable and function names.
        - Write small, focused functions to keep code modular and reusable.
        """
    )

    st.subheader("2. Use Python Built-ins")
    st.markdown(
        """
        - Use Python's built-in functions whenever possible (e.g., `sum()`, `any()`, `all()`).
        - Prefer list comprehensions over `for` loops for creating new lists:
          ```python
          # Example
          squares = [x**2 for x in range(10)]
          ```
        """
    )

    st.subheader("3. Handle Exceptions Gracefully")
    st.markdown(
        """
        - Always catch specific exceptions instead of using a generic `except` clause:
          ```python
          try:
              result = 10 / 0
          except ZeroDivisionError as e:
              print(f"Error: {e}")
          ```
        """
    )

    st.subheader("4. Use `with` Statement for File Operations")
    st.markdown(
        """
        - Avoid manual file closing; use `with` for safe resource management:
          ```python
          with open("example.txt", "r") as file:
              content = file.read()
          ```
        """
    )

    # OWASP Security Guidelines
    st.header("OWASP Security Guidelines")
    st.subheader("1. Validate User Input")
    st.markdown(
        """
        - Never trust user input. Validate all inputs for length, format, and allowed characters.
        - Use libraries like `cerberus` or `pydantic` for data validation:
          ```python
          from pydantic import BaseModel, ValidationError

          class UserInput(BaseModel):
              username: str
              age: int
          
          try:
              user = UserInput(username="Alice", age="25")
          except ValidationError as e:
              print(e)
          ```
        """
    )

    st.subheader("2. Protect Sensitive Data")
    st.markdown(
        """
        - Never hardcode sensitive information like passwords or API keys in code.
        - Use environment variables and libraries like `python-decouple` or `dotenv`:
          ```python
          from decouple import config
          DATABASE_PASSWORD = config("DB_PASSWORD")
          ```
        """
    )

    st.subheader("3. Use Secure Libraries")
    st.markdown(
        """
        - Keep libraries up to date and avoid deprecated packages.
        - Check for vulnerabilities using tools like `Safety` or `Bandit`:
          ```bash
          pip install safety
          safety check
          ```
        """
    )

    st.subheader("4. Avoid Command Injection")
    st.markdown(
        """
        - Never use user input directly in system commands:
          ```python
          import os

          # Bad
          os.system(f"rm -rf {user_input}")

          # Good
          import subprocess
          subprocess.run(["rm", "-rf", user_input], check=True)
          ```
        """
    )

    st.subheader("5. Implement Logging Securely")
    st.markdown(
        """
        - Avoid logging sensitive information.
        - Use Python's `logging` module instead of `print` for better control:
          ```python
          import logging
          
          logging.basicConfig(level=logging.INFO)
          logging.info("This is a log message")
          ```
        """
    )

    # Footer
    st.markdown("---")
    st.text("Made with ❤️ using Python and Streamlit | OWASP Secure")

if __name__ == "__main__":
    main()
