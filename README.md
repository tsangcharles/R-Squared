# Why You Should Not Use R² for Machine Learning

A practical demonstration of why the coefficient of determination (R²) is not suitable for evaluating non-linear machine learning models.

## Overview

This project demonstrates a fundamental issue with using R² (R-squared) for machine learning models: **the key property SST = SSE + SSR does not hold for non-linear models**.

In classical linear regression, R² is defined as:

$$R^2 = 1 - \frac{SSE}{SST} = \frac{SSR}{SST}$$

where:
- **SST** (Total Sum of Squares): $\sum(y_i - \bar{y})^2$
- **SSE** (Error Sum of Squares): $\sum(y_i - \hat{y}_i)^2$
- **SSR** (Regression Sum of Squares): $\sum(\hat{y}_i - \bar{y})^2$

A crucial property of linear regression is that **SST = SSE + SSR**, which allows R² to be interpreted as "the percentage of variation in the response variable explained by the regressors."

However, for non-linear models (such as Support Vector Regression, Neural Networks, or Gradient Boosting), this property **does not necessarily hold**, making R² less meaningful and potentially misleading.

## What This Project Shows

This project uses a simple dataset with Support Vector Regression (SVR) to demonstrate that:

1. The model fits the data reasonably well
2. Despite this, **SST ≠ SSE + SSR**
3. Therefore, the traditional interpretation of R² breaks down

### Sample Output

```
SST (Total Sum of Squares):      22.666667
SSE (Error Sum of Squares):      13.501234
SSR (Regression Sum of Squares):  3.847891

SSE + SSR = 17.349125

✗ SST ≠ SSE + SSR (Difference: 5.317542)
```

This demonstrates that the fundamental decomposition property does not hold for non-linear models!

## Project Structure

```
R_Squared/
├── main.py          # Main Python script with analysis
├── setup.sh         # Setup script for virtual environment
├── README.md        # This file
├── .gitignore       # Git ignore file
├── output/          # Generated plots (created when you run main.py)
│   └── svr_plot.png
└── main.ipynb       # Original Jupyter notebook (deprecated)
```

## Setup

### Prerequisites

- Python 3.7 or higher
- Bash shell (Linux/macOS/WSL/Git Bash)

### Installation

1. Clone or download this repository

2. Run the setup script to create a virtual environment and install dependencies:

   ```bash
   bash setup.sh
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

### Manual Setup (Alternative)

If you prefer to set up manually or are on Windows:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (Command Prompt):
.\venv\Scripts\activate.bat

# Install dependencies
pip install pandas scikit-learn numpy matplotlib
```

## Usage

After activating the virtual environment, simply run:

```bash
python main.py
```

This will:
1. Generate the sample dataset
2. Fit a Support Vector Regression model
3. Calculate SST, SSE, and SSR
4. Display the results showing that SST ≠ SSE + SSR
5. Generate and save a visualization plot to `output/svr_plot.png`

## Dependencies

- **pandas**: Data manipulation and analysis
- **scikit-learn**: Machine learning library (SVR model)
- **numpy**: Numerical computing
- **matplotlib**: Plotting and visualization

## Key Takeaways

1. **R² works well for linear regression** because SST = SSE + SSR, giving it a clear interpretation

2. **R² is problematic for non-linear models** because the decomposition property breaks down

3. **For machine learning models**, prefer alternative metrics such as:
   - Mean Squared Error (MSE)
   - Root Mean Squared Error (RMSE)
   - Mean Absolute Error (MAE)
   - Cross-validated performance scores

## Technical Details

### The Sample Data

The project uses a simple 6-point dataset:

| x  | y  |
|----|----|
| -1 | -1 |
| -1 |  1 |
|  0 |  1 |
|  0 |  3 |
|  1 | -1 |
|  1 | -3 |

This small dataset makes it easy to see the effects while keeping the computation simple.

### Why SST ≠ SSE + SSR for Non-Linear Models

In linear regression, the predicted values lie on a linear hyperplane, which creates an orthogonal decomposition of the total variation. This geometric property ensures SST = SSE + SSR.

For non-linear models, the predictions don't lie on a linear subspace, breaking the orthogonality and thus the decomposition property. The model can still make good predictions, but the mathematical foundation for R² interpretation is lost.

## References

This project was inspired by the common confusion around using R² for machine learning models. While many sources mention that "R² doesn't work for non-linear models," few provide concrete examples. This project aims to fill that gap with a clear, reproducible demonstration.

## License

This project is provided as-is for educational purposes.

## Author

Created as a demonstration for a blog post on why R² should not be used for machine learning model evaluation.

---

**Questions or feedback?** Feel free to open an issue or reach out!
