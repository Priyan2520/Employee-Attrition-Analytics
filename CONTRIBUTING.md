# Contributing to Employee Attrition Analytics

Thank you for reviewing this project. Contributions, feedback, and suggestions are welcome to help improve this repository. To keep the project clean and professional, please adhere to the following guidelines:

## Code of Conduct
Please maintain a respectful and professional tone in all communications, issues, and pull requests.

## How Can I Contribute?

### Reporting Bugs
If you find an error in the Python scripts or Power BI data models:
1. Open an **Issue** with a descriptive title.
2. Provide a clear description of the bug, including steps to reproduce it and error messages.

### Suggesting Enhancements
To suggest improvements to the data model, visualizations, or documentation:
1. Open an **Issue** outlining the suggestion.
2. Explain the business value of the enhancement.

### Pull Requests (PRs)
To submit changes:
1. Fork the repository and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes in your branch, ensuring clean code and updated documentation.
3. Verify that the Python scripts run with zero errors:
   ```bash
   python data/data_cleaning.py
   python notebooks/generate_charts.py
   ```
4. Commit your changes with clear, professional messages:
   ```bash
   git commit -m "feat: add salary band distribution to Power BI guide"
   ```
5. Push to your fork and submit a **Pull Request** to the `main` branch of this repository.

## Formatting & Code Standards

### Python
*   Follow **PEP 8** style guidelines.
*   Keep functions focused, well-documented, and modular.
*   Ensure all charts use consistent corporate color hex codes.

### Power BI / DAX
*   Format DAX formulas using capital letters for functions (e.g., `CALCULATE`, `DIVIDE`, `AVERAGE`).
*   Organize all metrics and measures inside the `_Measures` table.
*   Design visualizations in line with the established corporate theme: Deep Navy (`#0F172A`), Teal (`#0D9488`), and Slate Grey (`#64748B`).

---
Developed by **Priya Pradeep Nakate** | Data Analytics Intern, SyntecxHub.
