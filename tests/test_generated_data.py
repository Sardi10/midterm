# tests/test_generated_data.py
def test_generated_records(fake_records):
    # This test simply prints out the fake records for demonstration.
    if fake_records:
        for record in fake_records:
            a, b, op, expected = record
            print(f"Record: {a} {op} {b} = {expected}")
    assert True
