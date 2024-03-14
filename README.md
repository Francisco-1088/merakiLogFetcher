# merakiLogPuller
Obtains Meraki Event Logs for a list of networks and product types and exports them to CSV files

How to Use:
1. Edit config.py as follows
   * `api_key` should be your API Key
   * `org_name` should contain the exact name of the Organization you want to pull logs from as a string
   * `net_name` should be a comma separated list of the exact names of the networks you want to pull logs from as strings
   * `productType` should be a comma separated list of the exact names of the product types you want to pull logs from in those networks in string format. Acceptable values are `switch`, `wireless`, `appliance`, `camera`, `sensor`, `cellularGateway`, `systemsManager`.
   * `startingAfter` should be an ISO 8601 string in the format "%Y-%m-%dT00:00:00", where `%Y` is the Year, `%m` is the month, `%d` is the day, `T` is a separator, and `00:00:00` should be the starting time of day in 24H format.
   * `daysLookback` is the default number of days lookback if `startingAfter` is set to ""
2. Install the libraries in `requirements.txt` by running `pip install -r requirements.txt`
3. Run the script with `python main.py`

The script will then iterate through your list of networks and products, and produce multiple CSV files of the name `{net_name}_{product}_logs.csv`.
