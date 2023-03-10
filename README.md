# UOCIS322 - Project 5 #
kiem@uoregon.edu
Kie MacPherson
## Outline
This is a web-based application designed to calculate and display open and close times for respective KM/mile checkpoints for the RUSA ACP brevet. It also now uses a Mongo Database to be able to store input/field data as well as "Display" and "Insert" buttons and functionality.

## Algorithm
All open times for each passed control are added up as length from the prior control divided by the maximum speed for that control. If a control is not passed, the remainder is divided instead.

(length from prior control to next control / max speed) +
(length from prior control to next control / max speed) + ... + (remainder / max speed)

The closed times are the same but with max speed replaced with minimum speed. There is an oddity where the closing time within the first 60 km is based on 20 km/hr plus 1 hour.

The table is as follows:

Control location (km)	Minimum Speed (km/hr)	Maximum Speed (km/hr)
0 - 200										15												34
200 - 400									15												32
400 - 600									15												30
600 - 1000								11.428										28
1000 - 1300								13.333										26

## How to use start

run docker:
docker build -t image-name .
//where image-name is your choice of the docker image name.

run image:
docker run -d -p forwardedport:5000 image-name

to run in your browser go to:
http://localhost:forwardedport

where forwardedport is a port to forward to e.g. (5001); but do not use 5000.

## How to use tests:
to see docker containers:
docker ps

run tests:
docker exec $(ID of container from docker ps)
