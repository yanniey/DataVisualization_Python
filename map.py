from geojson import dumps
import geojson as g

import parse
from parse import parse, MY_FILE
import parse as p


def create_map(data_file):
	# define type of GeoJSON that we want to create
	# features are points, multi-points, linestrings etc.
	geo_map = {"type": "FeatureCollection"}

	# define empty list to store all points on the graph
	item_list = []
	# iterare over data_file to create GeoJSON document
	# using enumerate() so that we get both the line and the line number(index)

	for index, line in enumerate(data_file):
		# skip any zero coordinates because we can't map them on the graph
		if line["X"] =="0" or line ["Y"]=="0":
			continue
		# setup a new dictionary for each iteration
		# this data dictionary is temporary. We will append it to the item_list in each iteration
		data = {}
		# assign line items to appropriate GeoJSON fields
		data["type"] = "Feature"
		data["id"] = index
		data["properties"]={"title":line["Category"],
							"description":line["Descript"],
							"date":line["Date"]
		}
		data["geometry"] = {"type":"Point",
							"coordinates":(line["X"],line["Y"])
		}
		# add data dictionary to item_list
		item_list.append(data)
		
	# for each point in item_list, add the point to our dictionary. setdefault creates a key called "features" that has a value type of an empty list. Append point to this list with each iteration.
		for point in item_list:
			#setdefault is a method for features(from GeoJSON)
			geo_map.setdefault("features",[]).append(point)

	# now that all data is parsed into GeoJSON, write to a file so that we can load it to gist.github.com
		with open("file_sf.geojson","w") as f:
			f.write(g.dumps(geo_map))
			# dumps()prints geo_map into a GeoJSON recognizable file

def main():
	data = p.parse(p.MY_FILE,",")

	return create_map(data)

if __name__ =="__main__":
	main()