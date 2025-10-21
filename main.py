"""
R-Squared Analysis for Machine Learning Models

This script demonstrates why R-squared (coefficient of determination) 
should not be used for machine learning models, specifically showing 
that SST ≠ SSE + SSR for non-linear models like Support Vector Regression.
"""

import pandas as pd
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt


class DataPrep:
    """Prepare sample data for demonstration."""
    
    data = [
        {'x': -1, 'y': -1},
        {'x': -1, 'y': 1},
        {'x': 0, 'y': 1},
        {'x': 0, 'y': 3},
        {'x': 1, 'y': -1},
        {'x': 1, 'y': -3}
    ]
    
    @classmethod
    def gen_df(cls):
        """Generate DataFrame from sample data."""
        return pd.DataFrame(cls.data)


class ModelFitting:
    """Fit SVR model and evaluate R-squared components."""
    
    def __init__(self, df):
        """
        Initialize and fit Support Vector Regression model.
        
        Args:
            df: DataFrame with 'x' and 'y' columns
        """
        self.mdl = SVR()
        self.mdl.fit(df[['x']], df['y'])
    
    def _predict(self, df):
        """
        Generate predictions from the fitted model.
        
        Args:
            df: DataFrame with 'x' column
            
        Returns:
            Predicted y values
        """
        return self.mdl.predict(df[['x']])

    @staticmethod
    def _diff_calc(y1, y2):
        """
        Calculate sum of squared differences.
        
        Args:
            y1: First array of values
            y2: Second array of values (or scalar)
            
        Returns:
            Sum of squared differences
        """
        return np.sum((y1 - y2) ** 2)

    def eval(self, df):
        """
        Evaluate R-squared components: SSR, SSE, and SST.
        
        For linear regression: SST = SSE + SSR
        For non-linear models: This relationship may not hold!
        
        Args:
            df: DataFrame with 'x' and 'y' columns
            
        Returns:
            Tuple of (SSR, SSE, SST)
        """
        y_hat = self._predict(df)
        y_bar = np.mean(df['y'])
        y_i = np.array(df['y'])
        
        # Total Sum of Squares
        SST = self._diff_calc(y_i, y_bar)
        
        # Error Sum of Squares (Residual)
        SSE = self._diff_calc(y_i, y_hat)
        
        # Regression Sum of Squares
        SSR = self._diff_calc(y_hat, y_bar)
        
        return SSR, SSE, SST
    
    def plot(self, df, output_path='output/svr_plot.png'):
        """
        Plot the data points and fitted regression line.
        
        Args:
            df: DataFrame with 'x' and 'y' columns
            output_path: Path where the plot will be saved
        """
        import os
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        df.plot.scatter(x='x', y='y', c='DarkBlue')
        x = np.array(range(np.min(df['x']) - 1, np.max(df['x']) + 2)).reshape(-1, 1)
        y = self.mdl.predict(x)
        plt.plot(x, y, 'r-', linewidth=2, label='SVR Prediction')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Support Vector Regression - R² Analysis')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Save the plot
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Plot saved to: {output_path}")
        plt.close()


def main():
    """Main execution function."""
    print("=" * 60)
    print("R-Squared Analysis for Non-Linear Models")
    print("=" * 60)
    print()
    
    # Generate data
    df = DataPrep.gen_df()
    print("Sample Data:")
    print(df)
    print()
    
    # Fit model and evaluate
    mdl_fitting = ModelFitting(df)
    SSR, SSE, SST = mdl_fitting.eval(df)
    
    # Display results
    print("R-Squared Components:")
    print(f"  SST (Total Sum of Squares):      {SST:.6f}")
    print(f"  SSE (Error Sum of Squares):      {SSE:.6f}")
    print(f"  SSR (Regression Sum of Squares): {SSR:.6f}")
    print()
    print(f"  SSE + SSR = {SSE + SSR:.6f}")
    print()
    
    # Check if the linear regression property holds
    if abs(SST - (SSE + SSR)) < 1e-10:
        print("✓ SST = SSE + SSR (Linear relationship holds)")
    else:
        difference = abs(SST - (SSE + SSR))
        print(f"✗ SST ≠ SSE + SSR (Difference: {difference:.6f})")
        print()
        print("This demonstrates that R² should NOT be used for")
        print("non-linear models, as the fundamental property")
        print("SST = SSE + SSR does not hold!")
    
    print()
    print("=" * 60)
    
    # Generate and save plot
    print("\nGenerating plot...")
    mdl_fitting.plot(df)


if __name__ == "__main__":
    main()
