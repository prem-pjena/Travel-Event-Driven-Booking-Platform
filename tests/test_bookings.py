def test_create_booking(authorized_client):

    response = authorized_client.post(
        "/bookings?flight_id=1&seat_number=B1"
    )

    assert response.status_code == 200