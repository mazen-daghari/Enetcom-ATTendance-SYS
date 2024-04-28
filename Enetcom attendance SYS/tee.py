import face_recognition

# Load known face encodings
known_face_encodings = load_known_face_encodings("known_faces")

# Load unknown face image
unknown_face_image = load_image_file("unknown_face.jpg")

# Face detection
face_locations = face_recognition.face_locations(unknown_face_image)

# Face encoding
face_encodings = face_recognition.face_encodings(unknown_face_image, face_locations)

# Face recognition
for face_encoding in face_encodings:
    # Compare to known faces
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    # Identify the matching face
    name = "Unknown"
    for face_distance, face_match in zip(face_distances, matches):
        if face_match:
            name = get_face_name(face_distance, known_face_names)
            break

    # Display the name of the recognized person
    print(f"Found {name} in the image")
