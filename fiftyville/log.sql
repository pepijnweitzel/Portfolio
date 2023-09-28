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

