/*extended_hotel*/
CREATE VIEW
    extended_hotel AS
SELECT
    Hotel.*,
    Address.*
FROM
    Hotel
    JOIN Address on Address.address_id = Hotel.address_id;

/*extended_hotel_room*/
CREATE VIEW
    extended_hotel_room AS
SELECT
    Hotel.*,
    Address.*,
    (
        SELECT
            MAX(Room_Type.max_guests)
        FROM
            Room
            JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE
            Room.hotel_id = Hotel.hotel_id
    ) AS max_guests
FROM
    Hotel
    JOIN Address ON Address.address_id = Hotel.address_id;

/*extended_hotel_room_booking*/
CREATE VIEW extended_hotel_room_booking AS
SELECT
    Hotel.*,
    Address.*,
    Room.room_id,
    (
        SELECT Room_Type.max_guests
        FROM Room_Type
        WHERE Room_Type.type_id = Room.type_id
    ) AS max_guests,
    Booking.*
FROM
    Hotel
    JOIN Address ON Address.address_id = Hotel.address_id
    LEFT JOIN Room ON Room.hotel_id = Hotel.hotel_id
    LEFT JOIN Booking ON Booking.room_id = Room.room_id

/*extended_room*/
CREATE VIEW
    extended_room AS
SELECT
    Room.*,
    STRING_AGG (Facilities.facility_id, ', ') AS facilities_list,
    Room_Type.*
FROM
    Room
    LEFT JOIN Room_Facilities ON Room_Facilities.room_id = Room.room_id
    Left JOIN Facilities on Facilities.facility_id = Room_Facilities.facility_id
    JOIN Room_Type ON Room_Type.type_id = Room.type_id
GROUP BY
    Room.room_id
ORDER BY
    Room.room_id;

/*Example Query for getting Rooms in Date Range*/
SELECT
    Room.*
FROM
    Room
    JOIN Booking on Booking.room_id = Room.room_id
WHERE
    Room.room_id NOT in (
        SELECT
            Booking.room_id
        FROM
            Booking
        Where
            (
                Booking.check_in_date BETWEEN '2025-06-01' AND '2025-06-05'
            )
            OR (
                Booking.check_out_date BETWEEN '2025-06-01' AND '2025-06-05'
            )
            OR (
                Booking.check_in_date <= '2025-06-01'
                AND Booking.check_out_date >= '2025-06-05'
            )
    )

/* view to create an invoice */
CREATE VIEW booking_view AS
SELECT *
FROM Booking b
LEFT JOIN Guest g ON b.guest_id = g.guest_id
LEFT JOIN Address a ON g.address_id = a.address_id
LEFT JOIN Room r ON b.room_id = r.room_id
LEFT JOIN Hotel h ON r.hotel_id = h.hotel_id