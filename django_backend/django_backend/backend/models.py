from adaptor.model import CsvModel
from django.db import models

# Create your models here.
class myCsvModel(CsvModel):
    born_year = IntegerField()
    gender = IntegerField()
    hispanic = IntegerField()
    race = IntegerField()
    highest_level_school = IntegerField()
    marital_status = IntegerField()
    total_people_household = IntegerField()
    under_eighteen_people_household = IntegerField()
    covid_vaccine = IntegerField()
    covid_vaccine_all_doses = IntegerField()
    vaccine_opinion = IntegerField()
    covid_concern1 = IntegerField()
    covid_concern2 = IntegerField()
    covid_concern3 = IntegerField()
    covid_concern4 = IntegerField()
    covid_concern5 = IntegerField()
    covid_concern6 = IntegerField()
    covid_concern7 = IntegerField()
    covid_concern8 = IntegerField()
    covid_concern9 = IntegerField()
    covid_concern10 = IntegerField()
    covid_concern11 = IntegerField()
    covid_beliefs1 = IntegerField()
    covid_beliefs2 = IntegerField()
    covid_beliefs3 = IntegerField()
    covid_beliefs4 = IntegerField()
    covid_beliefs5 = IntegerField()
    covid_beliefs6 = IntegerField()
    had_covid_doctor = IntegerField()
    loss_income = IntegerField()
    loss_income_last_four_weeks = IntegerField()
    employement_last_seven_days = IntegerField()
    employed_by_who = IntegerField()
    reason_no_pay = IntegerField()
    telework_household = IntegerField()
    applied_unemployment_benefits = IntegerField()
    received_unemployment_benefits = IntegerField()
    received_ss_benefits = IntegerField()
    appplied_other_benefits = IntegerField()
    applied_benefits_ss_retirement = IntegerField()
    applied_benefits_ss_disability = IntegerField()
    applied_benefits_ss_survivors = IntegerField()
    applied_benefits_ssi = IntegerField()
    applied_benefits_medicare = IntegerField()
    apply_benefits_likelyhood = IntegerField()
    will_apply_benefits_ss_retirement = IntegerField()
    will_apply_benefits_ss_disability = IntegerField()
    will_apply_benefits_ss_survivors = IntegerField()
    will_apply_benefits_ssi = IntegerField()
    will_apply_benefits_medicare = IntegerField()
    covid_affects_apply_benefits = IntegerField()
    stimulus_usage = IntegerField()
    stimulus_usage_food = IntegerField()
    stimulus_usage_clothing = IntegerField()
    stimulus_usage_household_consumables = IntegerField()
    stimulus_usage_hosuehold_items = IntegerField()
    stimulus_usage_recreational = IntegerField()
    stimulus_usage_rent = IntegerField()
    stimulus_usage_mortgage = IntegerField()
    stimulus_usage_utilities = IntegerField()
    stimulus_usage_vehicle = IntegerField()
    stimulus_usage_debts = IntegerField()
    stimulus_usage_charity = IntegerField()
    stimulus_usage_savings = IntegerField()
    stimulus_usage_other = IntegerField()
    financial_difficulty = IntegerField()
    spending_changes_online = IntegerField()
    spending_changes_curbside = IntegerField()
    spending_changes_in_store = IntegerField()
    spending_changes_credit_cards = IntegerField()
    spending_changes_cash = IntegerField()
    spending_changes_no_restaurants = IntegerField()
    spending_changes_more_restaurants = IntegerField()
    spending_changes_less_pyhsical_health = IntegerField()
    spending_changes_in_person_physical_health = IntegerField()
    spending_changes_less_housekeeping = IntegerField()
    spending_changes_more_housekeeping = IntegerField()
    spending_changes_no_change = IntegerField()
    spending_changes_reason_closed = IntegerField()
    spending_changes_reason_re_opened = IntegerField()
    spending_changes_reason_covid = IntegerField()
    spending_changes_reason_anti_covid = IntegerField()
    spending_changes_reason_low_income = IntegerField()
    spending_changes_reason_increased_income = IntegerField()
    spending_changes_reason_job_insecurity = IntegerField()
    spending_changes_reason_job_security = IntegerField()
    spending_changes_reason_teleworking = IntegerField()
    spending_changes_reason_not_teleworking = IntegerField()
    spending_changes_reason_economy_concerns = IntegerField()
    spending_changes_reason_economy_unconcern = IntegerField()
    spending_changes_reason_other = IntegerField()
    spending_cope_same_income = IntegerField()
    spending_cope_credit = IntegerField()
    spending_cope_selling = IntegerField()
    spending_cope_borrowing_family = IntegerField()
    spending_cope_unemployment_benefits = IntegerField()
    spending_cope_stimulus = IntegerField()
    spending_cope_deferred_payments = IntegerField()
    spending_cope_snap = IntegerField()
    covid_less_grocery_trips = IntegerField()
    covid_less_grocery_trips_public_transport = IntegerField()
    covid_canceled_vacations = IntegerField()
    food_insecurity = IntegerField()
    child_food_insecurity = IntegerField()
    food_insecurity_reason_money = IntegerField()
    food_insecurity_reason_transportation = IntegerField()
    food_insecurity_reason_fear = IntegerField()
    food_insecurity_reason_no_deliveries = IntegerField()
    food_insecurity_reason_lack_of_availability = IntegerField()
    free_meals = IntegerField()
    free_meals_from_school = IntegerField()
    free_meals_from_food_bank = IntegerField()
    free_meals_from_meals_on_wheels = IntegerField()
    free_meals_from_church = IntegerField()
    free_meals_from_soup_kitchen = IntegerField()
    free_meals_from_other = IntegerField()
    free_meals_from_friends_family = IntegerField()
    snap = IntegerField()
    food_cost = IntegerField()
    food_out_cost = IntegerField()
    nervousness = IntegerField()
    worry = IntegerField()
    no_pleasure = IntegerField()
    depression = IntegerField()
    insurance_union = IntegerField()
    insurance_private = IntegerField()
    insurance_medicare_disabilities = IntegerField()
    insurance_medicare_disability_low_income = IntegerField()
    insurance_military = IntegerField()
    insurance_va = IntegerField()
    insurance_indian = IntegerField()
    insurance_other = IntegerField()
    covid_delays_care = IntegerField()
    covid_prevents_care = IntegerField()
    prescription_mental = IntegerField()
    received_counseling = IntegerField()
    refused_conseling = IntegerField()
    property_ownership_type = IntegerField()
    property_type = IntegerField()
    property_not_in_debt = IntegerField()
    property_not_in_debt_2 = IntegerField()
    property_payment_confidence = IntegerField()
    property_eviction_likelihood = IntegerField()
    property_foreclosure_likelihood = IntegerField()
    child_school_enrollment_public = IntegerField()
    child_school_enrollment_home = IntegerField()
    child_school_enrollment_no = IntegerField()
    child_school_covid_effect_canceled = IntegerField()
    child_school_covid_effect_online = IntegerField()
    child_school_covid_effect_online_with_paper = IntegerField()
    child_school_covid_effect_other = IntegerField()
    child_school_covid_effect_none = IntegerField()
    device_unavailability = IntegerField()
    device_provider_school = IntegerField()
    device_provider_family = IntegerField()
    device_provider_other = IntegerField()
    internet_unavailability = IntegerField()
    internet_service_provider_school = IntegerField()
    internet_service_provider_family = IntegerField()
    internet_service_provider_other = IntegerField()
    in_person_teacher_prevelance = IntegerField()
    child_self_study_hours = IntegerField()
    covid_effect_learning_time = IntegerField()
    members_planned_on_classes = IntegerField()
    class_plan_program_occupational = IntegerField()
    class_plan_program_associates = IntegerField()
    class_plan_program_bachelors = IntegerField()
    class_plan_program_graduate = IntegerField()
    class_plan_program_other_credential = IntegerField()
    class_plan_program_non_credential = IntegerField()
    covid_effect_class_plan_no_change = IntegerField()
    covid_effect_class_plan_canceled = IntegerField()
    covid_effect_class_plan_online = IntegerField()
    covid_effect_class_plan_less_classes = IntegerField()
    covid_effect_class_plan_more_classes = IntegerField()
    covid_effect_class_plan_changed_institution = IntegerField()
    covid_effect_class_plan_different_degree = IntegerField()
    class_plan_change_reason_covid_self = IntegerField()
    class_plan_change_reason_covid_caretaker = IntegerField()
    class_plan_change_reason_non_covid_caretaker = IntegerField()
    class_plan_change_reason_online = IntegerField()
    class_plan_change_reason_financial_aid = IntegerField()
    class_plan_change_reason_campus_life = IntegerField()
    class_plan_change_reason_class_uncertainty = IntegerField()
    class_plan_change_reason_expensive_covid = IntegerField()
    class_plan_change_reason_other = IntegerField()
    household_income = IntegerField()

    class Meta:
        delimiter = ",";