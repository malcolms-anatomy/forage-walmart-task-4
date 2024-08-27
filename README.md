# Data Munging Task

This project involves data munging and database insertion using Python. The main script, `data_munging.py`, performs the following tasks:

1. **Data Reading**: Reads data from CSV files containing shipping information.
2. **Data Merging**: Merges the data from multiple CSV files into a single DataFrame.
3. **Database Insertion**: Inserts the processed data into a SQLite database.

## Files

- `data_munging.py`: The main script that performs data munging and database insertion.
- `README.md`: This file.
- `data/`: Directory containing the CSV files used in the script.
  - `shipping_data_0.csv`: Contains shipping data with columns `origin_warehouse`, `destination_store`, `product`, `on_time`, `product_quantity`, and `driver_identifier`.
  - `shipping_data_1.csv`: Contains shipment information with columns `shipment_identifier`, `product`, and `on_time`.
  - `shipping_data_2.csv`: Contains additional shipment information with columns `shipment_identifier`, `origin_warehouse`, `destination_store`, and `driver_identifier`.
- `shipment_database.db`: The SQLite database where the processed data is stored.

## Setup

1. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\Activate`

