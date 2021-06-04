import dlib

training_path = "ibug_300W_large_face_landmark_dataset/labels_ibug_300W_custom_with_mouth_right_eye_left_eye_train.xml"
testing_path = "ibug_300W_large_face_landmark_dataset/labels_ibug_300W_custom_with_mouth_right_eye_left_eye_test.xml"

model_path = "model/custom_landmark_model.dat"

print("[INFO] evaluating shape predictor on training dataset...")
error = dlib.test_shape_predictor(training_path, model_path)
print("[INFO] error for training dataset: {}".format(error))

print("[INFO] evaluating shape predictor on testing dataset...")
error = dlib.test_shape_predictor(testing_path, model_path)
print("[INFO] error for testing dataset: {}".format(error))