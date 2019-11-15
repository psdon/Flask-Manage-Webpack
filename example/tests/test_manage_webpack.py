def test_index(client):
    resp = client.get("/")

    data = resp.data

    assert b"main_css" in data
    assert b"main_js" in data
    assert b"bg.dbb383786757dec129cb96c035b943b5.jpg" in data
