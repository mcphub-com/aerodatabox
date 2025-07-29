import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/aedbx-aedbx/api/aerodatabox'

mcp = FastMCP('aerodatabox')

@mcp.tool()
def flight_status(
                number: Annotated[str, Field(description='Flight number (with or without spaces, IATA or ICAO, any case formats are acceptable, e.g. KL1395, Klm 1395)')],
                withAircraftImage: Annotated[Union[bool, None], Field(description='Should include aircraft image.')] = None,
                  withLocation: Annotated[Union[bool, None], Field(description='Should include real-time positional data, e.g.: location, speed, altitude, etc., if available')] = None) -> dict: 
    '''Gets information about the status of the nearest (either in past or in future) flight or about flight departing or arriving on the day specified (local time), operated: - under specified flight number; or - by an aircraft with specified registration; or - under specified ATC-callsign; or - by an aircraft with specified Mode-S 24-bit ICAO Transponder address.'''
    url = 'https://aerodatabox.p.rapidapi.com/flights/number/%s'%number
    headers = {'x-rapidapi-host': 'aerodatabox.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'withAircraftImage': withAircraftImage,
        'withLocation': withLocation,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 204:
        return response.json()
    else:
        return {}

@mcp.tool()
def flight_history_schedule(
    number: Annotated[str, Field(description='Flight number (with or without spaces, IATA or ICAO, any case formats are acceptable, e.g. KL1395, Klm 1395)')],
    dateFromLocal: Annotated[str, Field(description='Beginning of the range of local dates of departure or arrival (in format: YYYY-MM-DD, e.g.: 2019-08-29). Maximum/minimum allowable value is determined by the current data coverage limitations and your pricing plan.')],
    dateToLocal: Annotated[str, Field(description='End of the range of local dates of departure or arrival (in format: YYYY-MM-DD, e.g.: 2019-08-29). Maximum/minimum allowable value is determined by the current data coverage limitations and your pricing plan. This date must be bigger than the dateFromLocal. The maximum difference between this date and dateFromLocal is limited and is determined by your pricing plan (ranging from 7 to 30 days as per moment of writing).')],
    dateLocalRole: Annotated[Literal['Both', 'Arrival', 'Departure', None], Field(description='If set to Both (default, recommended for best results) then the dateFromLocal and dateToLocal parameters shall be considered as both departure and arrival dates. If a flight departs OR arrives on dates within the specified range (in the local timezone of the origin or destination, respectively), it will be returned. If set to Departure then the dateFromLocal and dateToLocal parameters shall be considered as departure dates only. Only the flights departing on dates within the specified rang(in the local timezone of origin) will be returned. If set to Arrival then the dateFromLocal and dateToLocal parameters shall be considered as arrival dates only. Only the flights arriving on dates within the specified rangd (in the local timezone of destination) will be returned.')] = None) -> dict:
    '''**What is the history or schedule of a specific flight within a specific range of dates in past or in future?** This endpoint is the similar to the *Flight status* endpoints. The only difference is that instead of returning the flight data on a single day, it ** returns the list of flights operating within a selected range of dates.** All limitations and considerations applicable to *Flight status* endpoint are applicable to this endpoint as well.'''
    url = 'https://aerodatabox.p.rapidapi.com/flights/number/%s/%s/%s'%(number, dateFromLocal, dateToLocal)
    headers = {'x-rapidapi-host': 'aerodatabox.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'dateLocalRole': dateLocalRole,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fidsairport_departures_and_arrivals(
    code: Annotated[Union[str], Field(description='a 3-character IATA-code of the airport (e.g.: AMS, SFO, LAX, etc.).')],
    offsetMinutes: Annotated[Union[int, float, None], Field(description='Beginning of the search range expressed in minutes relative to the current time at the airport Default: -120')] = None,
                                        durationMinutes: Annotated[Union[int, float, None], Field(description='Length (duration) of the search range expressed in minutes Default: 720')] = None,
                                        withLeg: Annotated[Union[bool, None], Field(description='If set to true, will include movement information from airport opposite in this flight leg (airport of origin for arriving flight or airport of destination for departing flight). In this case, Movement property will be replaced with Departure and Arrival properties for each flight. Default: false.')] = None,
                                        direction: Annotated[Literal['Both', 'Arrival', 'Departure', None], Field(description='Direction of flights: Arrival, Departure or Both (default)')] = None,
                                        withCancelled: Annotated[Union[bool, None], Field(description='If set to true, result will include cancelled, divered, likely cancelled (CanceledUncertain) flights. Default: true.')] = None,
                                        withCodeshared: Annotated[Union[bool, None], Field(description='If set to true, result will include flights with all code-shared statuses. Otherwise, code-sharing flights will be excluded. For airports, where no information about code-share statuses of flights are supplied (all flights are CodeshareStatus=Unknown), complex filtering will be applied to determine which flights are likely to be operational (caution: false results are possible).')] = None,
                                        withCargo: Annotated[Union[bool, None], Field(description='If set to true, result will include cargo flights (subject to availability).')] = None,
                                        withPrivate: Annotated[Union[bool, None], Field(description='If set to true, result will include private flights (subject to availability).')] = None,
                                        withLocation: Annotated[Union[bool, None], Field(description='If set to true, each currently active flight within the result will be populated with its present real-time location, altitude, speed and track (subject to availability).')] = None) -> dict: 
    '''**What are current departures or arrivals at the airport?** or **What is the flight schedule at the airport?** or **What is flight history at the airport?** Flights may contain live updates with corresponding information related to the actual progress of the flight (including actual/estimated arrival/departure times). In this case this endpoint serves as a FIDS endpoint. Presense of live updates is subject to data coverage: not all airports have this coverage in our system. Otherwise the flight information will be limited to schedule only and will not be updated with time. Much more airports have this coverage. To check if airport is tracked and on which level, use `/health/services/airports/{icao}/feeds` endpoint. You can also use `/health/services/feeds/{service}/airports` to get the list of supported airports for this or that layer of coverage. To learn more about the data coverage, refer to https://www.aerodatabox.com/data-coverage. Returns: the list of arriving and/or departing flights scheduled and/or planned and/or commenced within a time range specified relatively to the current local time at the airport.'''
    url = 'https://aerodatabox.p.rapidapi.com/flights/airports/iata/%s'%code
    headers = {'x-rapidapi-host': 'aerodatabox.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'offsetMinutes': offsetMinutes,
        'durationMinutes': durationMinutes,
        'withLeg': withLeg,
        'direction': direction,
        'withCancelled': withCancelled,
        'withCodeshared': withCodeshared,
        'withCargo': withCargo,
        'withPrivate': withPrivate,
        'withLocation': withLocation,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def flight_departure_dates() -> dict: 
    '''**On which days the flight operates?** or **What is the flight schedule?** Get flight departure dates for a flight operated: , operated: - under specified flight number; or - by an aircraft with specified registration; or - under specified ATC-callsign; or - by an aircraft with specified Mode-S 24-bit ICAO Transponder address. Returns: Array of local departure dates in (YYYY-MM-DD).'''
    url = 'https://aerodatabox.p.rapidapi.com/flights/%7BsearchBy%7D/KL1395/dates/2020-06-01/2020-06-15'
    headers = {'x-rapidapi-host': 'aerodatabox.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search_flight_numbers_by_term(q: Annotated[str, Field(description='Search query (min. 2 non whitespace characters length)')],
                                  limit: Annotated[Union[int, float, None], Field(description='Maximum number of items to be returned (max. 100, default = 10)')] = None) -> dict: 
    '''Returns: Distinct list of available flight numbers which start with the search query.'''
    url = 'https://aerodatabox.p.rapidapi.com/flights/search/term'
    headers = {'x-rapidapi-host': 'aerodatabox.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
