import re
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--training", nargs='+', required=True, help="Add facial structure")
args = vars(ap.parse_args())

dataset_path = "ibug_300W_large_face_landmark_dataset/"
output_dataset_path = "ibug_300W_large_face_landmark_dataset/labels_ibug_300W_custom_with_"

dataset = ['train', 'test']

coordinates_map = {
    'jaw': [0, 17],
    'right_eyebrow': [17, 22],
    'left_eyebrow': [22, 27],
    'nose': [27, 35],
    'right_eye': [36, 42],
    'left_eye': [42, 48], 
    'mouth': [48, 68]
}

LANDMARKS = set()

for arg in args['training']:
    if arg in coordinates_map.keys():
        for x in range(coordinates_map[arg][0], coordinates_map[arg][1] + 1):
            LANDMARKS.add(x)
    else:
        print("Facial doesn't exist!")
        exit()

# define "PART"
PART = re.compile("part name='[0-9]+'")
NUM = re.compile("[0-9]+")

'''creates a new xml file stored at [out_path] with the desired landmark-points.
    The input xml [in_path] must be structured like the ibug annotation xml.'''

for path in dataset:
    file = open(dataset_path + "labels_ibug_300W_" + path + ".xml", "r")
    out = open(output_dataset_path + "_".join(args['training']) + "_" + path + ".xml", "w")

    for line in file.readlines():
        finds = re.findall(PART, line)

        # find the part section
        if len(finds) <= 0:
            out.write(line)
        else:
            # we are inside the part section 
            # so we can find the part name and the landmark x, y coordinates
            name, x, y = re.findall(NUM, line)

            # if is one of the point i'm looking for, write in the output file
            if int(name) in LANDMARKS:
                out.write(f"      <part name='{name}' x='{x}' y='{y}'/>\n")

    out.close()