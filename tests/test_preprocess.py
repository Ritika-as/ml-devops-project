from src.preprocess import clean_data

def test_clean_data():
    data = [1, None, 3]
    result = clean_data(data)
    assert None not in result
