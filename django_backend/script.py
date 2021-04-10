import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_backend.settings')
django.setup()

from responses.models import SurveyResponse

data = open('HackFest21-Data.csv')
reader = csv.reader(data)

labels = []

row1 = next(reader)
for label in row1:
    labels.append(label)

# print(labels)

SurveyResponse.objects.all().delete()
for row in reader:
    if row[0].isnumeric():
        i = 0
        new_response = SurveyResponse()
        parameterStr = ""
        for response in row:
            # print(response)
            parameterStr += f"{labels[i]}={int(response)},"
            i+=1
        # print(parameterStr)
        exec("new_response = SurveyResponse(%s)" % (parameterStr))
        new_response.save()


# new_response = SurveyResponse(Label1=123123, Label2=124135)
# new_response.save()