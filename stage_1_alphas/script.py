file_name = "alpha_10_aaradhya"

body = """
ts_backfill(liabilities/assets,63)
"""

with open(file_name, "w") as file:
    file.write(body)

print(f"File '{file_name}' created successfully.")