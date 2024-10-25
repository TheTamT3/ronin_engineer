CREATE TABLE bookings (
    id           BIGINT PRIMARY KEY AUTO_INCREMENT,
    -- Business data
    flight_id    BIGINT    NOT NULL,
    passenger_id BIGINT    NOT NULL,
    book_date    TIMESTAMP NOT NULL,
    seat_type    VARCHAR(20) CHECK (seat_type IN ('economy', 'business')),
    -- Technical data
    create_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    create_by    VARCHAR(20),
    update_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_by    VARCHAR(20)
);