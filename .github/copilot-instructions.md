# Copilot Instructions for Foodhub Data Analysis Project

## Overview
This project focuses on data analysis for the Foodhub platform, utilizing Python for data manipulation and analysis. The architecture is designed to facilitate easy data ingestion, processing, and visualization.

## Project Structure
- **foodhub_order.csv**: Contains the order data used for analysis.
- **PYF_Project_Learner_Notebook_Full_Code.ipynb**: Jupyter notebook with the full code for data analysis.
- **README.md**: Provides an overview of the project and setup instructions.

## Key Components
- **Data Ingestion**: Data is loaded from `foodhub_order.csv` using pandas. Ensure that the CSV file is in the correct format.
- **Data Processing**: The notebook contains functions for cleaning and processing the data. Look for functions prefixed with `process_`.
- **Visualization**: Use libraries like Matplotlib and Seaborn for visualizing data trends. Check the notebook for examples.

## Developer Workflows
- **Running the Notebook**: Use Jupyter Notebook to run the analysis. Ensure all dependencies are installed via `pip install -r requirements.txt`.
- **Testing**: While there are no formal tests, ensure that the notebook runs without errors after any changes.
- **Debugging**: Use print statements or logging to debug issues in the notebook. Check the output cells for errors.

## Conventions and Patterns
- **Function Naming**: Functions are named using snake_case. This is consistent throughout the notebook.
- **Documentation**: Each function should have a docstring explaining its purpose and parameters.

## Integration Points
- **External Dependencies**: Ensure that all required libraries are installed. Use the `requirements.txt` file for reference.
- **Data Flow**: The data flows from the CSV file into the notebook, where it is processed and visualized. Ensure that the data format remains consistent.

## Examples
- To load data, use:
  ```python
  import pandas as pd
  data = pd.read_csv('foodhub_order.csv')
  ```
- For visualization:
  ```python
  import seaborn as sns
  sns.lineplot(data=data, x='date', y='sales')
  ```

## Conclusion
These instructions should help AI agents understand the structure and workflows of the Foodhub Data Analysis project. For any unclear sections, please provide feedback for improvement.