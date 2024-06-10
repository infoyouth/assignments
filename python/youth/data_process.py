def process_data(data: list) -> list:
    """Function to process a list of data."""
    return [d * 2 for d in data]

if __name__ == "__main__":
    sample_data = [1, 2, 3, 4, 5]
    print(process_data(sample_data))

