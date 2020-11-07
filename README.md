# generate_shortest_path
using a web form ,submit city names and a path would be generated that would give the most efficient (flat) route 

Libraries needed 
  (1)Django 1.4.1
  (2)geopy
  (3)pprint
  (4)numpy

for travelling salesman problem 2 methods are used 
  (1)tsp1 is the most accurate but most time consuming
  (2)tsp3 is a soft approximation .
  tsp1 supports both back to base and one way while tsp3 only supports back to base .
  (i am using tsp3 because of compute limitation on my ailing laptop)

additional features to be added:
  (1)markers and path highlighted on map
  (2)a history section to remember the past (upto) 9 searches

additional notes:
  If anyone knows how to work with djinja on js , i would like your help as i was unable to get the markers to shop up on map(openlayers API)
