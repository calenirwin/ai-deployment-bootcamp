IMU_TYPE = ["IMU Hand ","IMU Chest ","IMU Ankle "]
IMU_INFO = ["Temperature (°C)","16g Acceleration x (ms -2)","16g Acceleration y (ms -2)","16g acceleration z (ms -2)","6g Acceleration x (ms -2)"
    ,"6g Acceleration y (ms -2)","6g Acceleration z (ms -2)","Gyroscope angle 1 (rad/s)","Gyroscope angle 2 (rad/s)","Gyroscope angle 3 (rad/s)"
    ,"Magnetometer direction 1 (μT)","Magnetometer direction 2 (μT)","Magnetometer direction 3 (μT)","Orientation 1 (invalid)","Orientation 2 (invalid)"
    ,"Orientation 3 (invalid)","Orientation 4 (invalid)"]

COLUMNS_COMMON = ["Timestamp (s)","Activity ID","Heart rate (bpm)"]
IMU_HAND = [IMU_TYPE[0] + IMU_INFO[i] for i in range (len(IMU_INFO))]
IMU_CHEST = [IMU_TYPE[1] + IMU_INFO[i] for i in range (len(IMU_INFO))]
IMU_ANKLE = [IMU_TYPE[2] + IMU_INFO[i] for i in range (len(IMU_INFO))]
COLUMNS_DATASET = COLUMNS_COMMON + IMU_HAND + IMU_CHEST + IMU_ANKLE


SELECTED_FEATURES = ["16g Acceleration x (ms -2)","16g Acceleration y (ms -2)","16g acceleration z (ms -2)","6g Acceleration x (ms -2)"
    ,"6g Acceleration y (ms -2)","6g Acceleration z (ms -2)","Gyroscope angle 1 (rad/s)","Gyroscope angle 2 (rad/s)","Gyroscope angle 3 (rad/s)"]

SELECTED_FEATURES_HAND = [IMU_TYPE[0] + SELECTED_FEATURES[i] for i in range (len(SELECTED_FEATURES))]
SELECTED_FEATURES_CHEST = [IMU_TYPE[1] + SELECTED_FEATURES[i] for i in range (len(SELECTED_FEATURES))]
SELECTED_FEATURES_ANKLE = [IMU_TYPE[2] + SELECTED_FEATURES[i] for i in range (len(SELECTED_FEATURES))]
OVERALL_FEATURES = SELECTED_FEATURES_HAND + SELECTED_FEATURES_CHEST + SELECTED_FEATURES_ANKLE
SELECTED_LABELS = ["Activity ID"]
