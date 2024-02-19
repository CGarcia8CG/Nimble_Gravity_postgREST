-- Create a new database 
CREATE DATABASE ces_data;

-- Connect to the new database
\c ces_data;

-- Drop tables if they exist
DROP TABLE IF EXISTS ces_woman CASCADE;
DROP TABLE IF EXISTS ces_data_nonsupervisory CASCADE;
DROP TABLE IF EXISTS ces_data_total_private CASCADE;
DROP ROLE IF EXISTS anonymous;

-- Create ces_woman table
CREATE TABLE ces_woman (
    series text,
    period text,
    sector text,
    women integer
);

-- Create ces_data_nonsupervisory table
CREATE TABLE ces_data_nonsupervisory (
    series text,
    period text,
    sector text,
    employ integer
);

-- Create ces_data_total_private table
CREATE TABLE ces_data_total_private (
    series text,
    period text,
    sector text,
    employ integer
);
