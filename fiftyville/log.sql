-- Keep a log of any SQL queries you execute as you solve the mystery.
-- To find out all kinds of columns there are in this table.
.schema crime_scene_reports

-- To find the crime scene report about the crime. It told me that the crime took place at 10:15am and all 3 witnesses mentioned the bakery, where the theft took place aswell.
SELECT * FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND year = 2021
AND day = 28
AND month = 7;

