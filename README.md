# AeroDataBox MCP Server

## Overview

AeroDataBox is a comprehensive aviation and flights MCP server designed for small to medium businesses, individual developers, researchers, and students. This server provides a wide array of aviation data, including flight statuses, schedules, aircraft information, airport details, statistics, historical data, and more. It is designed for seamless integration using REST and webhooks, allowing users to easily incorporate aviation information into their systems.

## Features

### Flights 

- **Flight Status**: Retrieve information about the status of flights, either for the nearest past or future, by using flight numbers, aircraft registration, ATC call-signs, or 24-bit ICAO Mode-S addresses.
  
- **Flight History & Schedule**: Access the history or schedule of specific flights within a specified date range, providing a list of flights operating within those dates.

- **FIDS (Flight Information Display System)**: Get current departures or arrivals at airports. This includes live updates related to the actual progress of flights, subject to data coverage.

- **Flight Departure Dates**: Discover on which days a flight operates using flight numbers, aircraft registration, or other identifiers.

- **Search Flight Numbers**: Look up available flight numbers by term, ideal for implementing auto-complete features.

### Flight Alerts

- **PUSH API**: Utilize webhooks to subscribe to flights by number or airport code. Receive updates whenever flight information changes.

### Aircraft

- **Get Aircraft**: Retrieve information about aircraft using tail numbers or 24-bit ICAO Mode-S addresses.

- **Aircraft Registrations**: Access the history of current and previous registrations of an aircraft.

- **Airline Fleet**: [BETA] View the list of active aircraft in an airline's fleet.

- **Aircraft Photo**: [BETA] Obtain an aircraft image using the tail number.

- **Identify Aircraft by Photo**: [BETA] Upload a photo containing a visible tail number to identify the aircraft.

- **Search Aircraft Tail Numbers**: Look up active aircraft tail numbers by term.

### Airport

- **Get Airport**: Retrieve airport information using IATA or ICAO codes, including name, location, and more.

- **Airport Runways**: Get detailed information about airport runways.

- **Search Closest Airports**: Find airports closest to a specific location or IP geolocation.

- **Airports Free-text Search**: Implement auto-complete functionality using free-text airport search.

### Industry

- **FAA LADD Aircraft Status**: Access the status of aircraft in the FAA LADD program.

### Statistical

- **Airport & Global Delays**: View statistics on current or past flight delays and cancellations.

- **Airport Daily Routes Statistics**: Analyze daily flight routes and frequencies from a specific airport.

- **Flight Delay Statistics**: Examine detailed delay statistics for flights.

### Miscellaneous

- **Local Time at Airport**: Get the local time using IATA or ICAO airport codes.

- **Solar and Day Time at Airport**: Calculate solar events like sunrise and sunset at airports.

- **Distance Between Airports**: Compute the great-circle distance between airports.

- **Flight Time Between Airports**: Calculate theoretical and realistic flight times between airports.

- **Weather at Airport**: Access current weather and forecast information for airports.

## Is AeroDataBox Right for You?

AeroDataBox is ideal for applications that do not require exhaustive worldwide coverage or a strict service-level agreement (SLA). It is suitable for small to medium businesses, individual developers, and researchers who need reliable aviation data without the demands of mission-critical applications. 

## Support

For support, reach out via email. Before contacting, please review the documentation and must-read resources, as they address most common queries.