import json

def extract_features_from_tsv(tsv_file):
    features = []
    with open(tsv_file, 'r') as f:
        for line in f:
            id, geojson_str = line.strip().split('\t')
            try:
                geojson_data = json.loads(geojson_str)
                features.append(geojson_data)
            except json.JSONDecodeError:
                print("Failed to parsing data:", line)
    return {"type": "FeatureCollection", "features": features}

def write_featurecollection_to_geojson(feature_collection, output_file):
    with open(output_file, 'w') as f:
        json.dump(feature_collection, f)

if __name__ == "__main__":
    tsv_file = "id_4.tsv" # change file name
    output_geojson_file = "output/output_id_4.geojson" # change output name
    print("Opening file and generating feature, please wait...")
    feature_collection = extract_features_from_tsv(tsv_file)
    print("Writing feature collection, please wait...")
    write_featurecollection_to_geojson(feature_collection, output_geojson_file)
    print("Done.")
