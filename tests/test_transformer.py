from app.core.transformer import generate_payload

def test_generate_payload():
    list_1 = ["first string", "second string"]
    list_2 = ["other string", "another string"]
    result = generate_payload(list_1, list_2)
    expected = "FIRST STRING, OTHER STRING, SECOND STRING, ANOTHER STRING"
    assert result == expected
