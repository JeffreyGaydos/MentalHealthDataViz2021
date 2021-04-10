
from rest_framework import serializers
from responses.models import SurveyResponse

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['born_year','gender','hispanic','race','highest_level_school','marital_status',
        'total_people_household','under_eighteen_people_household','covid_vaccine',
        'covid_vaccine_all_doses','vaccine_opinion','covid_concern1','covid_concern2',
        'covid_concern3','covid_concern4','covid_concern5','covid_concern6','covid_concern7',
        'covid_concern8','covid_concern9','covid_concern10','covid_concern11','covid_beliefs1',
        'covid_beliefs2','covid_beliefs3','covid_beliefs4','covid_beliefs5','covid_beliefs6','had_covid_doctor',
        'loss_income','loss_income_last_four_weeks','employement_last_seven_days','employed_by_who','reason_no_pay',
        'telework_household','applied_unemployment_benefits','received_unemployment_benefits','received_ss_benefits',
        'appplied_other_benefits','applied_benefits_ss_retirement','applied_benefits_ss_disability','applied_benefits_ss_survivors',
        'applied_benefits_ssi','applied_benefits_medicare','apply_benefits_likelyhood','will_apply_benefits_ss_retirement',
        'will_apply_benefits_ss_disability','will_apply_benefits_ss_survivors','will_apply_benefits_ssi','will_apply_benefits_medicare',
        'covid_affects_apply_benefits','stimulus_usage','stimulus_usage_food','stimulus_usage_clothing','stimulus_usage_household_consumables',
        'stimulus_usage_hosuehold_items','stimulus_usage_recreational','stimulus_usage_rent','stimulus_usage_mortgage','stimulus_usage_utilities',
        'stimulus_usage_vehicle','stimulus_usage_debts','stimulus_usage_charity','stimulus_usage_savings','stimulus_usage_other','financial_difficulty',
        'spending_changes_online','spending_changes_curbside','spending_changes_in_store','spending_changes_credit_cards','spending_changes_cash',
        'spending_changes_no_restaurants','spending_changes_more_restaurants','spending_changes_less_pyhsical_health',
        'spending_changes_in_person_physical_health','spending_changes_less_housekeeping','spending_changes_more_housekeeping',
        'spending_changes_no_change','spending_changes_reason_closed','spending_changes_reason_re_opened','spending_changes_reason_covid',
        'spending_changes_reason_anti_covid','spending_changes_reason_low_income','spending_changes_reason_increased_income','spending_changes_reason_job_insecurity',
        'spending_changes_reason_job_security','spending_changes_reason_teleworking','spending_changes_reason_not_teleworking','spending_changes_reason_economy_concerns',
        'spending_changes_reason_economy_unconcern','spending_changes_reason_other','spending_cope_same_income','spending_cope_credit','spending_cope_selling',
        'spending_cope_borrowing_family','spending_cope_unemployment_benefits','spending_cope_stimulus','spending_cope_deferred_payments','spending_cope_snap',
        'covid_less_grocery_trips','covid_less_grocery_trips_public_transport','covid_canceled_vacations','food_insecurity','child_food_insecurity',
        'food_insecurity_reason_money','food_insecurity_reason_transportation','food_insecurity_reason_fear','food_insecurity_reason_no_deliveries',
        'food_insecurity_reason_lack_of_availability','free_meals','free_meals_from_school','free_meals_from_food_bank','free_meals_from_meals_on_wheels',
        'free_meals_from_church','free_meals_from_soup_kitchen','free_meals_from_other','free_meals_from_friends_family','snap','food_cost','food_out_cost',
        'nervousness','worry','no_pleasure','depression','insurance_union','insurance_private','insurance_medicare_disabilities','insurance_medicare_disability_low_income',
        'insurance_military','insurance_va','insurance_indian','insurance_other','covid_delays_care','covid_prevents_care','prescription_mental','received_counseling',
        'refused_conseling','property_ownership_type','property_type','property_not_in_debt','property_not_in_debt_2','property_payment_confidence',
        'property_eviction_likelihood','property_foreclosure_likelihood','child_school_enrollment_public','child_school_enrollment_home','child_school_enrollment_no',
        'child_school_covid_effect_canceled','child_school_covid_effect_online','child_school_covid_effect_online_with_paper','child_school_covid_effect_other',
        'child_school_covid_effect_none','device_unavailability','device_provider_school','device_provider_family','device_provider_other','internet_unavailability',
        'internet_service_provider_school','internet_service_provider_family','internet_service_provider_other','in_person_teacher_prevelance','child_self_study_hours',
        'covid_effect_learning_time','members_planned_on_classes','class_plan_program_occupational','class_plan_program_associates','class_plan_program_bachelors',
        'class_plan_program_graduate','class_plan_program_other_credential','class_plan_program_non_credential','covid_effect_class_plan_no_change',
        'covid_effect_class_plan_canceled','covid_effect_class_plan_online','covid_effect_class_plan_less_classes','covid_effect_class_plan_more_classes',
        'covid_effect_class_plan_changed_institution','covid_effect_class_plan_different_degree','class_plan_change_reason_covid_self',
        'class_plan_change_reason_covid_caretaker','class_plan_change_reason_non_covid_caretaker','class_plan_change_reason_online',
        'class_plan_change_reason_financial_aid','class_plan_change_reason_campus_life','class_plan_change_reason_class_uncertainty',
        'class_plan_change_reason_expensive_covid','class_plan_change_reason_other','household_income']

class SurveyResponseAgeDepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = ['born_year', 'depression']