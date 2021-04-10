
from rest_framework import serializers
from responses.models import SurveyResponse

class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        # fields=['Label1', 'Label2']
        fields = ['born_year', 'gender', 'hispanic', 'race',
         'highest_level_school', 'marital_status', 'total_people_household', 
         'under_eighteen_people_household', 'covid_vaccine', 'covid_vaccine_all_doses',
          'vaccine_opinion', 'covid_concern1', 'covid_concern2', 'covid_concern3', 'covid_concern4', 
          'covid_concern5', 'covid_concern6', 'covid_concern7', 'covid_concern8', 'covid_concern9',
           'covid_concern10', 'covid_concern11', 'covid_beliefs1', 'covid_beliefs2', 'covid_beliefs3',
            'covid_beliefs4', 'covid_beliefs5', 'covid_beliefs6', 'had_covid_doctor', 'loss_income',
             'loss_income_last_four_weeks', 'employement_last_seven_days', 'employed_by_who', 'reason_no_pay',
              'nervousness', 'worry', 'no_pleasure', 'depression', 'insurance_union', 'insurance_private',
               'insurance_medicare_disabilities', 'insurance_medicare_disability_low_income', 'insurance_military',
                'insurance_va', 'insurance_indian', 'insurance_other', 'covid_delays_care', 'covid_prevents_care',
                 'prescription_mental', 'received_counseling', 'refused_conseling']
