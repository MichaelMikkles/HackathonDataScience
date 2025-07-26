import pandas as pd


def load_dataset(file_path):
    """
    Loads a dataset from a CSV file using pandas.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)

# Example usage:
df = load_dataset('Dataset_Talento.csv')
print(df.head())

# Resumen del DataFrame
print(df.info())

# Estadísticas descriptivas de las columnas numéricas
print(df.describe())
