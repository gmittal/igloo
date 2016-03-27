
# Assume sensor input is given, this is all raw data returned by the various sensors
# Assume this data is updated in real time
raw_responder_sensor_metrics = {
    heart_rate: 120,
    microphone: "raw microphone data as an encoded string"
    accelerometer: {
        glasses: {
            x: 140,
            y: 150,
            z: 10,
            gyro: 100
        },
        phone: {
            x: 140,
            y: 150,
            z: 10,
            gyro: 100
        }
    },
    location: {
        x: 10,
        y: 20
    }
}

# Process all raw data -- function returns inferred metrics/suggested decisions
# This influences what will finally get displayed on the HUD
def processSensorInput(sensor_data):
    # Do something here


# A set of inferred responder metrics which can be displayed on the HUD
inferred_responder_metrics = processSensorInput(raw_responder_sensor_metrics)
