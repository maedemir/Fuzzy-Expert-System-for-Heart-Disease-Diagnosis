class inference:
    def __init__(self):
        pass
    def inference_engine(self, chest_pain, blood_pressure, cholesterol,
                  blood_sugar, ECG, heart_rate, exercise,
                  old_peak, thallium, sex, age):
        output = {'sick1': [], 'sick2': [], 'sick3': [], 'sick4': [], 'healthy': []}

        output['sick4'].append(min(age['very_old'], chest_pain['atypical_anginal']))   # Rule 1
        output['sick4'].append(min(heart_rate['high'], age['old']))    # Rule 2
        output['sick3'].append(min(sex['male'], heart_rate['medium']))     # Rule 3
        output['sick2'].append(min(sex['female'], heart_rate['medium']))   # Rule 4
        output['sick3'].append(min(chest_pain['non_anginal_pain'], blood_pressure['high']))    # Rule 5
        output['sick2'].append(min(chest_pain['typical_anginal'], heart_rate['medium']))     # Rule 6
        output['sick3'].append(min(blood_sugar['true'], age['mild']))         # Rule 7
        output['sick2'].append(min(blood_sugar['false'], blood_pressure['very_high']))        # Rule 8
        output['sick1'].append(max(chest_pain['asymptomatic'], age['very_old']))   # Rule 9
        output['sick1'].append(max(blood_pressure['high'], heart_rate['low']))  # Rule 10
        output['healthy'].append(chest_pain['typical_anginal'])    # Rule 11
        output['sick1'].append(chest_pain['atypical_anginal'])     # Rule 12
        output['sick2'].append(chest_pain['non_anginal_pain'])     # Rule 13
        output['sick3'].append(chest_pain['asymptomatic'])     # Rule 14
        output['sick4'].append(chest_pain['asymptomatic'])     # Rule 15
        output['sick1'].append(sex['female'])  # Rule 16
        output['sick2'].append(sex['male'])    # Rule 17
        output['healthy'].append(blood_pressure['low'])    # Rule 18
        output['sick1'].append(blood_pressure['medium'])    # Rule 19
        output['sick2'].append(blood_pressure['high'])      # Rule 20
        output['sick3'].append(blood_pressure['high'])      # Rule 21
        output['sick4'].append(blood_pressure['very_high'])     # Rule 22
        output['healthy'].append(cholesterol['low'])    # Rule 23
        output['sick1'].append(cholesterol['medium'])   # Rule 24
        output['sick2'].append(cholesterol['high'])     # Rule 25
        output['sick3'].append(cholesterol['high'])     # Rule 26
        output['sick4'].append(cholesterol['very_high'])    # Rule 27
        output['sick2'].append(blood_sugar['true'])     # Rule 28
        output['healthy'].append(ECG['normal'])     # Rule 29
        output['sick1'].append(ECG['normal'])      # Rule 30
        output['sick2'].append(ECG['abnormal'])     # Rule 31
        output['sick3'].append(ECG['hypertrophy'])  # Rule 32
        output['sick4'].append(ECG['hypertrophy'])    # Rule 33
        output['healthy'].append(heart_rate['low'])     # Rule 34
        output['sick1'].append(heart_rate['medium'])    # Rule 35
        output['sick2'].append(heart_rate['medium'])    # Rule 36
        output['sick3'].append(heart_rate['high'])      # Rule 37
        output['sick4'].append(heart_rate['high'])     # Rule 38
        output['sick2'].append(exercise['true'])    # Rule 39
        output['healthy'].append(old_peak['low'])   # Rule 40
        output['sick1'].append(old_peak['low'])     # Rule 41
        output['sick2'].append(old_peak['terrible'])      # Rule 42
        output['sick3'].append(old_peak['terrible'])      # Rule 43
        output['sick4'].append(old_peak['risk'])    # Rule 44
        output['healthy'].append(thallium['normal'])    # Rule 45
        output['sick1'].append(thallium['normal'])  # Rule 46
        output['sick2'].append(thallium['medium'])  # Rule 47
        output['sick3'].append(thallium['high'])    # Rule 48
        output['sick4'].append(thallium['high'])    # Rule 49
        output['healthy'].append(age['young'])      # Rule 50
        output['sick1'].append(age['mild'])     # Rule 51
        output['sick2'].append(age['old'])      # Rule 52
        output['sick3'].append(age['old'])      # Rule 53
        output['sick4'].append(age['very_old'])     # Rule 54
        return dict(
            outputsick_sick1=max(output['sick1']),
            outputsick_sick2=max(output['sick2']),
            outputsick_sick3=max(output['sick3']),
            outputsick_sick4=max(output['sick4']),
            outputsick_healthy=max(output['healthy'])
        )
