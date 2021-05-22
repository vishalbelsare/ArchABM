
from .AerosolModel import AerosolModel
import math
class AerosolModelColorado(AerosolModel):
    """Aerosol transmission estimator"""

    def __init__(self, params):
        self.params = params


    def get_person_risk(self, params):
        """Calculate the transmission risk of an individual in a room"

        Args:
            params (Parameters): dictionary of model parameters
        """
        pass

    def get_place_risk(self, params):
        """Calculate the risk in air quality of a place

        Args:
            params (Parameters): dictionary of model parameters
        """
        pass
        
    def get_risk(self, inputs):
        """Calculate the transmission risk of an individual in a room 
        and the dosis thrown into the air.

        Args:
            inputs (Parameters): dictionary of model inputs
        """

        params = self.params

        length = 8
        width = 6
        height = 3
        area = width * length
        volume = width * length * height

        pressure = 0.95
        temperature = 20
        relative_humidity = 50
        background_co2 = 415

        event_duration = 50 / 60 # h
        num_people = 10

        repetitions = 180
        ventilation = 3
        decay_rate = 0.62
        deposition_rate = 0.3
        additional_measures = 0

        loss_rate = ventilation + decay_rate + deposition_rate + additional_measures

        ventilation_person = volume * (ventilation + additional_measures) * 1000 / 3600 / num_people

        infective_people = 1
        fraction_immune = 0
        susceptible_people = (num_people - infective_people) * (1 - fraction_immune)

        density_area_person = area / (0.305**2) / num_people
        density_people_area = num_people / area
        density_volume_person = volume / num_people

        breathing_rate = 0.52
        breathing_rate_relative = breathing_rate / (0.0048*60)
        emission_co2_person = 0.005
        emission_co2 = emission_co2_person * num_people / pressure * (273.15 + temperature) / 273.15

        quanta_exhalation = 25
        quanta_enhancement = 1
        quanta_exhalation_relative = quanta_exhalation / 2

        mask_efficiency_exhalation = 50 / 100
        mask_efficiency_inhalation = 30 / 100
        people_with_masks = 100 / 100

        probability_infective = 0.20 / 100
        hospitalization_rate = 20 / 100
        death_rate = 1 / 100

        net_emission_rate = quanta_exhalation * (1 - mask_efficiency_exhalation*people_with_masks) * infective_people * quanta_enhancement
        quanta_concentration = net_emission_rate / loss_rate / volume * (1 - (1/loss_rate/event_duration)*(1-math.exp(-loss_rate * event_duration)))
        quanta_inhaled_per_person = quanta_concentration * breathing_rate * event_duration * (1- mask_efficiency_inhalation*people_with_masks)

        probability_infection = 1- math.exp(-quanta_inhaled_per_person)
        probability_hospitalization = probability_infection * hospitalization_rate
        probability_death = probability_infection * death_rate

        infection_risk = breathing_rate_relative * quanta_exhalation_relative * \
            (1 - mask_efficiency_exhalation * people_with_masks) * \
            (1 - mask_efficiency_inhalation * people_with_masks) * \
            event_duration * susceptible_people / (loss_rate * volume) * \
            (1 - (1 - math.exp(- loss_rate * event_duration))/(loss_rate*event_duration))
        infection_risk_relative = infection_risk / susceptible_people

        co2_mixing_ratio = (emission_co2 * 3.6 / ventilation / volume * \
            (1- (1/ventilation/event_duration) * (1 - math.exp(- ventilation * event_duration)))) * 1e6 + background_co2
        co2_concentration = (co2_mixing_ratio - background_co2) * 40.9 / 1e6 * 44 * 298 / (273.15 + temperature)*pressure
        co2_reinhaled_grams = co2_concentration * breathing_rate * event_duration
        co2_reinhaled_ppm = (co2_mixing_ratio - background_co2) * event_duration
        co2_probability_infection_= co2_reinhaled_ppm / 1e4 / probability_infection
        co2_inhale_ppm = (co2_mixing_ratio - background_co2) * event_duration * 0.01 / probability_infection + background_co2




        







                



        
