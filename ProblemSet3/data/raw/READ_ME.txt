READ_ME

Potential Transshipments 20180723 (potential_transshipment_20180723.csv)
--------------------------------------------
Description:
Events where a transshipment vessel and a fishing vessel were within 500 meters 
of each other for greater than 2 hours, travelling at speeds of less than 2 knots, 
while 10 nautical miles from a coastal anchorage.

There are nine (9) columns.

  fishing_vessel_mmsi:          unique vessel identifier for fishing vessel, integer
  transshipment_vessel_mmsi:    unique vessel identifier for transshipment vessel, integer
  start_time:                   datetime when event began (UTC), timestamp
  end_time:                     datetime when event ended (UTC), timestamp
  mean_latitude:                average latitude of the event in decimal degrees, float
  mean_longitude:               average longitude of event in degrees, float
  duration_hr:                  duration of the event in hours, float
  median_distance_km:           median distance between vessels during event in kilometers, float
  median_speed_knots:           median speed of vessels during event in knots, float


Loitering Events 20180723 (loitering_events_20180723.csv)
--------------------------------------------
Description:
Events where a transshipment vessel travelled at speeds of less than 2 knots, for 
longer than 8 hours, while more than 20 nautical miles the shore.

There are nine (9) columns.

  transshipment_mmsi:     unique vessel identifier for transshipment vessel, integer
  starting_latitude:      starting latitude of the event in decimal degrees, float
  starting_longitude:     starting longitude of the event in decimal degrees, float
  ending_latitude:        ending latitude of the event in decimal degrees, float
  ending_longitude:       ending longitude of the event in decimal degrees, float
  starting_timestamp:     datetime when event began (UTC), timestamp
  ending_timestamp:       datetime when event ended (UTC), timestamp
  median_speed_knots:     median speed of vessels during event in knots, float
  mean_longitude:         average longitude of event in degrees, float
  total_event_duration:	  duration of the event in hours, float


Transshipment Vessels 20180723 (transshipment_vessels_20180723.csv)
--------------------------------------------
Description:
Database of cargo vessels capable of transshipping at sea and 
transporting fish (referred to as transshipment vessels).

There are six (6) columns.

  mmsi:                         unique vessel identifier for transshipment vessel, integer
  shipname:                     transshipment vessel name, string
  callsign:                     transshipment vessel radio call sign, string
  fleet_iso3:                   transshipment vessel fleet, as ISO3, string
  fleet_name:                   transshipment vessel fleet, as name, string                         
  imo:                          transshipment vessel imo number, integer




These files were downloaded from: http://globalfishingwatch.org/datasets-and-code/


For more details on the creation of this database please see: Miller, NA, A. 
Roan, T. Hochberg, J. Amos, DA. Kroodsma. 2018. Identifying global patterns of 
transshipment behavior. Frontiers in Marine Science. doi: 10.3389/fmars.2018.00240  
(https://www.frontiersin.org/articles/10.3389/fmars.2018.00240/abstract)



Unless otherwise stated, Global Fishing Watch data is licensed under a Creative 
Commons Attribution-ShareAlike 4.0 International license and code under an Apache 
2.0 license.

