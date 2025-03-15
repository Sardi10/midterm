"""Module providing a function python version."""
# tests/test_generated_data.py
def test_generated_records(fake_records):
    """
    Test that the fake_records fixture generates records with the correct structure.
    This test will only exercise the loop in the fixture when --num_records > 0.
    """
    # Ensure fake_records is a list
    assert isinstance(fake_records, list)

    if fake_records:
        for record in fake_records:
            # Each record should be a tuple of (a, b, op, expected)
            assert isinstance(record, tuple), "Record should be a tuple"
            assert len(record) == 4, "Record must have 4 elements"
            a, b, op, expected = record
            # Check that a and b are integers
            assert isinstance(a, int), "a should be an integer"
            assert isinstance(b, int), "b should be an integer"
            # Check that op is one of the allowed operations
            assert op in ['+', '-', '*', '/'], f"Unexpected operation: {op}"
            # For division, expected should be a float; otherwise, int or float is acceptable
            if op == '/':
                assert isinstance(expected, float), "Expected result for division should be a float"
            else:
                assert isinstance(expected, (int, float)), "Expected result should be a number"
    else:
        # When --num_records is not provided or <= 0, the fixture returns an empty list.
        assert fake_records == []
