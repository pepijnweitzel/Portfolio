-- Keep a log of any SQL queries you execute as you solve the mystery.
-- To find out all the kinds of columns there are in this table.
.schema crime_scene_reports

-- To find the crime scene report about the crime. It told me that the crime took place at 10:15am and all 3 witnesses mentioned the bakery, where the theft took place aswell.
SELECT * FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND year = 2021
AND day = 28
AND month = 7;

-- To find out all the kinds of columns there are in this table
.schema interviews

-- To tell me more about what the witnesses said. It told me te following things:
--10 min within theft thief in his car to drive away.
--before 10:15am thief was withdrawing money from ATM on Leggett Street
--After theft called accomplice for less than minute, taking earliest flight out of fiftyville at july 29th 2021, accomplice bought flight ticket
SELECT * FROM interviews
WHERE year = 2021
AND day = 28
AND month = 7;

--To find all the kinds of columns in all the tables
.schema

-- To find the possible license plate from the thief's car
SELECT license_plate FROM bakery_security_logs
WHERE year = 2021
AND day = 28
AND month = 7
AND hour = 10
AND minute <= 25
AND activity = 'exit';

-- To find all the names from the people leaving the bakery after the theft within 10 minutes of the theft
SELECT name FROM people
WHERE licen_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021
    AND day = 28
    AND month = 7
    AND hour = 10
    AND minute <= 25
    AND activity = 'exit'
);

-- Get account number from withdrawns made at leggett street at 28-07-2021
SELECT account_number FROM atm_transactions
WHERE year = 2021
AND month = 7
AND day = 28
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';

-- Get the person id's that made an withdraw at legget street the day of the theft
SELECT person_id FROM bank_accounts
WHERE account_number IN (
    SELECT account_number FROM atm_transactions
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw'
);

-- Get the names that made an withdraw
SELECT name FROM people
WHERE id IN (
    SELECT person_id FROM bank_accounts
    	WHERE account_number IN (
            SELECT account_number FROM atm_transactions
            WHERE year = 2021
            AND month = 7
            AND day = 28
            AND atm_location = 'Leggett Street'
            AND transaction_type = 'withdraw'
)
);

-- Check for the same names in withdraw name list and people leaving bakery name list. Which gave me: Luca, Diana, Bruce
SELECT name FROM (SELECT name FROM people WHERE licen_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute <= 25 AND activity = 'exit'))
WHERE name IN (SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw')));

-- To get the numbers from the people calling for less than a minute on the day of the theft.
SELECT caller FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Get names from the people that made the call
SELECT name FROM people
WHERE phone_number IN (
    SELECT caller FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60;
);

-- Check for the same names in last made list from withdraw and leaving bakery and previously made list for simmilarities. Which gave me Bruce and Diana
SELECT name FROM (
    SELECT name FROM people
    WHERE phone_number IN (
        SELECT caller FROM phone_calls
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND duration < 60;
))
WHERE name IN (
    SELECT name FROM (SELECT name FROM people WHERE licen_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND day = 28 AND month = 7 AND hour = 10 AND minute <= 25 AND activity = 'exit'))
    WHERE name IN (SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw'))));

-- To get the earliest flight id the day after the theft: 36
SELECT id FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY hour
LIMIT 1;

-- Get Diana's passport number: 3592750733
SELECT passport_number FROM people
WHERE name = 'Diana';

-- Get Bruce's passport number: 5773159633
SELECT passport_number FROM people
WHERE name = 'Bruce';

-- Find out the passengers passports list on the flight and whether bruce's is on it. It gives back his passport number so it was Bruce who commited the crime!
SELECT passport_number FROM passengers
WHERE flight_id = 36
AND passport_number = 5773159633;

-- Find out where he went: destination id = 4
SELECT destination_airport_id FROM flights
WHERE id = 36;

-- Find out the name of the city where the airport is. He went to New York City!
SELECT city FROM airports
WHERE id = 4;

