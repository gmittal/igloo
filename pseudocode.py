# 2016 MIT Lincoln Lab IEEE Icehouse Challenge
# By Alex Gao, Gautam Mittal, and Max Wang


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

# What is given to us or what we already know about the environment
raw_environment_given_metrics = {
    known_victim_locations: [
        {x: 15, y: 20},
        {x: 200, y: 15},
        {x: 10, y: 100}
    ],
    known_hazards: [
        {
            danger_level: 3,
            name: "fire",
            location: {
                x: 15,
                y: 100
            }
        },
        {
            danger_level: 1,
            name: "gas leak",
            location: {
                x: 500,
                y: 100
            }
        },
        {
            danger_level: 2,
            name: "armed explosive",
            location: {
                x: 300,
                y: 100
            }
        },
    ]
}




# Computer assisted decision making layer for providing likelihood of suriving certain situtations from an individual standpoint
class DecisionMaking:
    # Assesses the probability of a responder being able to neutralize the threat
    def hazardNeutralizationAssessment:
        probability = 0.5
        return probability

    # Assesses survivability of trying to rescue a certain victim based on distance, hazard level, etc.
    def victimSurvivabilityAssessment:
        



# Process all raw data -- function returns inferred metrics/suggested decisions
# This influences what will finally get displayed on the HUD

# Key metrics that need to be gleaned: Individual responder sensor data and biometrics,
#  Team member information, and a computer assisted decision making layer.

# Team information is sent over both Wifi and Bluetooth radios for redudancy in the scenario
# that one of the radios becomes inaccessible or unreliable, however, if there is ever a moment
# in time where neither communication radio is available, the system will continue to display
# individual and computer assisted decision making metrics to the individual responder
def processSensorInput(sensor_data):



# A set of inferred responder metrics which can be displayed on the HUD
# These inferred metrics only contain what is most relevant at that specific time
# The inferred_metrics object will not contian any data that is not relevant at that time (all data has to be displayed or useful in some way to the responder via the HUD)
inferred__metrics = processSensorInput(raw_responder_sensor_metrics)
