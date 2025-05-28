CREATE VIEW available_hotel_rooms AS
SELECT
    h.hotel_id,
    h.name AS hotel_name,
    a.city,
    a.zip_code,
    a.street,
    r.room_id,
    rt.max_guests
FROM Hotel h
JOIN Address a ON a.address_id = h.address_id
JOIN Room r ON r.hotel_id = h.hotel_id
JOIN Room_Type rt ON rt.type_id = r.type_id
WHERE r.room_id NOT IN (
    SELECT b.room_id
    FROM Booking b
    WHERE NOT (
        b.check_out_date <= DATE('now') OR
        b.check_in_date >= DATE('now', '+1 day')
    )
)
