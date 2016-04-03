# 2016 MIT Lincoln Lab IEEE Icehouse Challenge
# By Alex Gao, Gautam Mittal, and Max Wang
# Assume all placeholder data objects are updated in real time by sensors

import math
import numpy as np
from utils import *

Victims = 0
Responders = 0

# Assume sensor input is given, this is all raw data returned by the various sensors
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
    },
    equipment: [ # equipment is entered via phone interface before mission
        "first aid kit",
        "infrared camera",
        "external oxygen apparatus",
        "shoring kit"
    ]
}

# What is given to us or what we already know about the environment
# This information can change depending on (but is not reliant on) external communications from other responders
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


# Requires a network connection (either bluetooth or Wifi) in order to know about
# other responders' metrics
raw_external_responder_metrics = {
    "responder1": {
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
    },

    "responder2": {
            heart_rate: 90,
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
    },
}

# Computer assisted decision making layer for providing likelihood of surviving certain known situtations from an individual standpoint
class DecisionMaking:
    # Assesses the probability of a responder being able to neutralize the threat
    def hazardNeutralizationAssessment(singleHazardData, equipmentList):
        probability = 0.5
        return probability

    # Assesses survivability of trying to rescue a certain victim based on distance, hazard level, etc.
    def victimResponderSurvivabilityAssessment(victimLocation, responderLocation, completeHazardData):
        victimToResponderDistance = math.sqrt(((victimLocation["x"]-responderLocation["x"])**2)+((victimLocation["y"]-responderLocation["y"])**2))

        # Find the hazard closest to the victim (probably what's most likely affecting them)
        hazardDisplacement = []
        for hazard in completeHazardData:
            victimToHazardDistance = math.sqrt(((victimLocation["x"]-hazard["location"]["x"])**2)+((victimLocation["y"]-hazard["location"]["y"])**2))
            hazardDisplacement.append(victimToHazardDistance)
        hazardDisplacement.sort()
        closestHazardDisplacement = hazardDisplacement[0] # closest hazard

        hazardDistances = []
        for hazard in completeHazardData:
            #A* or other similar pathfinding algorithms
        hazardDistances.sort()
        optimalHazardDistance = hazardDistances[0]

        # Find the danger level of the closest hazard
        closestHazardDangerLevel = 0
        for hazard in completeHazardData:
            victimToHazardDistance = math.sqrt(((victimLocation["x"]-hazard["location"]["x"])**2)+((victimLocation["y"]-hazard["location"]["y"])**2))
            if victimToHazardDistance == closestHazardDisplacement:
                closestHazardDangerLevel = hazard["danger_level"]
                break


        # The probability of survival for the victim and responder is contingent on three variables:
        # Distance the hazard is away from the victim, distance the victim is from the responder, and the danger level of the hazard

        # Absolute worst case scenario values
        maxPossibleDangerLevel = 3
        minPossibleVictimHazardDistance = 1
        maxPossibleResponderDistance = 100 # the maxPossibleResponderDistance isn't actually this, this just a placeholder value,
                                           # it should be calculated using the given dimensions of the room, and then should be equal to the length of the diagonal of the game room

        # a really high surival constant means high chance of death, a really low number means very low chance of death
        zero_survival_constant = maxPossibleDangerLevel*(maxPossibleResponderDistance-minPossibleVictimHazardDistance)

        survival_probability = 1


#Markov Decision Process
#State = Room
#Action = Moving into Room
#Transitions = Probability of 1 of moving into Room specified by Action
#Reward = Progress
#   When Reward -> -50, then worker dies
#   Reward similar to Exposure
#   Tech changes Reward for each applicable hazard in room.
#



#Value Iteration function for Markov Decision Process (MDP) and Partially Observable Markov Decision Process (POMDP) that returns optimal policy given state, rewards, and threshold
#Initialize value function V(s) arbitrarily for all states s
#repeat until convergence
#for each state s
#   V(s) := max Q-value for a state-action pair, with Bellman Equation
#see http://burlap.cs.brown.edu/tutorials/cpl/p1.html
#and https://www.cs.ubc.ca/~kevinlb/teaching/cs322%20-%202008-9/Lectures/DT4.pdf
#important http://aima.cs.berkeley.edu/python/mdp.html


class MDP:
    """A Markov Decision Process, defined by an initial state, transition model,
    and reward function. Gamma is for algorithms. Based off of Artificial Intelligence: A Modern Approach by Peter Norvig"""

    def __init__(self, init, actlist, terminals, gamma=.9):
        update(self, init=init, actlist=actlist, terminals=terminals,
               gamma=gamma, states=set(), reward={})

    def R(self, state):
        "Return a numeric reward for this state."
        return self.reward[state]

    def T(state, action):
        """Transition model.  From a state and an action, return a list
        of (result-state, probability) pairs."""
        abstract

    def actions(self, state):
        """Set of actions that can be performed in this state.  By default, a
        fixed list of actions, except for terminal states. Override this
        method if you need to specialize by state."""
        if state in self.terminals:
            return [None]
        else:
            return self.actlist



#Partially Observable Monte-Carlo Planning
#used for POMDP
#Online, partially observable, can be deterministic

function Search(h)
    repeat
        if h is empty then
            s != I
        else
            s != B(h)
        end if
        Simulate(s, h, 0)
    until Timeout()
    return argmaxV(hb)
end

function Rollout(s, h, depth)

function Simulate(s, h, depth)




# Process all raw data -- function returns inferred metrics/suggested decisionsr
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
# The inferred_metrics object will not contian any data that is not relevant at that
# time (all data has to be displayed or useful in some way to the responder via the HUD)
inferred__metrics = processSensorInput(raw_responder_sensor_metrics)
