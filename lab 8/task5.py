def convert_date_format(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Input date must be in 'YYYY-MM-DD' format")
    year, month, day = parts
    return f"{day}-{month}-{year}"
