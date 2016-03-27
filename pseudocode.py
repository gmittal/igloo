
# Assume sensor input is given, this is all raw data returned by the various sensors
# Assume this data is updated in real time
raw_responder_sensor_metrics = {
    heart_rate: 120,
    microphone: "raw microphone data as an encoded string",
    barometer: 20,
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
# These inferred metrics only contain what is most relevant at that specific time
# The inferred_metrics object will not contian any data that is not relevant at that time (all data has to be displayed or useful in some way to the responder via the HUD)
inferred__metrics = processSensorInput(raw_responder_sensor_metrics)
