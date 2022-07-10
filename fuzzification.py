class chest_pain_fuzzification:
    def __init__(self):
        pass

    def typical_angina(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def atypical_angina(self, x):
        if x == 2:
            return 1
        else:
            return 0

    def non_anginal_pain(self, x):
        if x == 3:
            return 1
        else:
            return 0

    def asymptomatic(self, x):
        if x == 4:
            return 1
        else:
            return 0

    def fuzzify_chest_pain(self, cp):
        return dict(
            typical_anginal=self.typical_angina(cp),
            atypical_anginal=self.atypical_angina(cp),
            non_anginal_pain=self.non_anginal_pain(cp),
            asymptomatic=self.asymptomatic(cp)
        )


class blood_pressure_fuzzification:
    def __init__(self):
        pass

    def blood_pressure_low(self, x):
        if 0 <= x <= 111:
            return 1.0
        elif 111 < x <= 134:
            return (-1.0 / 23) * x + 134 / 23.0
        else:
            return 0.0

    def blood_pressure_medium(self, x):

        if 127 <= x <= 139:
            return (1.0 / 12) * x - 127 / 12.0
        elif 139 < x <= 153:
            return (-1.0 / 14) * x + 153 / 14.0
        else:
            return 0.0

    def blood_pressure_high(self, x):

        if 142 <= x <= 157:
            return (1.0 / 15) * x - 142 / 15.0
        elif 157 < x <= 172:
            return (-1.0 / 15) * x + 172 / 15.0
        else:
            return 0.0

    def blood_pressure_very_high(self, x):

        if 0 <= x <= 154:
            return 0.0
        elif 154 < x <= 171:
            return (1.0 / 17) * x - 154 / 17.0
        else:
            return 1.0

    def fuzzify_blood_pressure(self, bp):
        return dict(
            low=self.blood_pressure_low(bp),
            medium=self.blood_pressure_medium(bp),
            high=self.blood_pressure_high(bp),
            very_high=self.blood_pressure_very_high(bp)
        )


class cholesterol_fuzzification:
    def __init__(self):
        pass

    def cholesterol_low(self, x):
        if 0 <= x <= 151:
            return 1.0
        elif 151 < x <= 197:
            return (-1.0 / 46) * x + 197 / 46.0
        else:
            return 0.0

    def cholesterol_medium(self, x):

        if 188 <= x <= 215:
            return (1.0 / 27) * x - 188 / 27.0
        elif 215 < x <= 250:
            return (-1.0 / 35) * x + 250 / 35.0
        else:
            return 0.0

    def cholesterol_high(self, x):

        if 217 <= x <= 263:
            return (1.0 / 46) * x - 217 / 46.0
        elif 263 < x <= 307:
            return (-1.0 / 44) * x + 307 / 44.0
        else:
            return 0.0

    def cholesterol_very_high(self, x):

        if 0 <= x <= 281:
            return 0.0
        elif 281 < x <= 347:
            return (1.0 / 66) * x - 281 / 66.0
        else:
            return 1.0

    def fuzzify_cholesterol(self, chl):
        return dict(
            low=self.cholesterol_low(chl),
            medium=self.cholesterol_medium(chl),
            high=self.cholesterol_high(chl),
            very_high=self.cholesterol_very_high(chl)
        )


class blood_sugar_fuzzification:
    def __init__(self):
        pass

    def blood_sugar_veryhigh(self, x):
        if 120 <= x:
            return 1
        if 105 <= x < 120:
            return 0.067 * x - 7
        else:
            return 0

    def fuzzify_blood_sugar(self, bloodSugar):
        return dict(
            true=self.blood_sugar_veryhigh(bloodSugar),
            false=1 - self.blood_sugar_veryhigh(bloodSugar)
        )


class ECG_fuzzification:
    def __init__(self):
        pass

    def ECG_normal(self, x):
        if -0.5 <= x <= 0:
            return 1.0
        elif 0 < x <= 0.4:
            return (-1.0 / 0.4) * x + 1.0
        else:
            return 0.0

    def ECG_abnormal(self, x):
        if 0.2 <= x <= 1:
            return (1.0 / 0.8) * x - 0.2 / 0.8
        elif 1 < x <= 1.8:
            return (-1.0 / 0.8) * x + 1.8 / 0.8
        else:
            return 0.0

    def ECG_hypertrophy(self, x):
        if -0.5 <= x <= 1.4:
            return 0.0
        elif 1.4 < x <= 1.9:
            return (1.0 / 0.5) * x - 1.4 / 0.5
        else:
            return 0

    def fuzzify_ECG(self, ECG):
        return dict(
            normal=self.ECG_normal(ECG),
            abnormal=self.ECG_abnormal(ECG),
            hypertrophy=self.ECG_hypertrophy(ECG)
        )


class heart_rate_fuzzification:
    def __init__(self):
        pass

    def heart_rate_low(self, x):

        if 0 <= x <= 100:
            return 1.0
        elif 100 < x <= 141:
            return (-1.0 / 41) * x + 141 / 41.0
        else:
            return 0.0

    def heart_rate_medium(self, x):

        if 111 <= x <= 152:
            return (1.0 / 41) * x - 111 / 41.0
        elif 152 < x <= 194:
            return (-1.0 / 42) * x + 194 / 42.0
        else:
            return 0.0

    def heart_rate_high(self, x):

        if 0 <= x <= 152:
            return 0.0
        elif 152 < x <= 210:
            return (1.0 / 58) * x - 152 / 58.0
        else:
            return 1.0

    def fuzzify_heart_rate(self, hr):
        return dict(
            low=self.heart_rate_low(hr),
            medium=self.heart_rate_medium(hr),
            high=self.heart_rate_high(hr)
        )


class exercise_fuzzification:
    def __init__(self):
        pass

    def true(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def false(self, x):
        if x == 0:
            return 1
        else:
            return 0

    def fuzzify_exercise(self, ex):
        return dict(
            true=self.true(ex),
            false=self.false(ex)
        )


class old_peak_fuzzification:
    def __init__(self):
        pass

    def old_peak_low(self, x):
        if 0 <= x <= 1:
            return 1.0
        elif 1 < x <= 2:
            return (-1.0) * x + 2.0
        else:
            return 0.0

    def old_peak_risk(self, x):
        if 1.5 <= x <= 2.8:
            return (1.0 / 1.3) * x - 1.5 / 1.3
        elif 2.8 < x <= 4.2:
            return (-1.0 / 1.4) * x + 4.2 / 1.4
        else:
            return 0.0

    def old_peak_terrible(self, x):
        if 0 <= x <= 2.5:
            return 0.0
        elif 2.5 < x <= 4:
            return (1.0 / 1.5) * x - 2.5 / 1.5
        else:
            return 1.0

    def fuzzify_old_peak(self, op):
        return dict(
            low=self.old_peak_low(op),
            risk=self.old_peak_risk(op),
            terrible=self.old_peak_terrible(op)
        )


class thallium_scan_fuzzification:
    def __init__(self):
        pass

    def normal(self, x):
        if x == 3:
            return 1
        else:
            return 0

    def medium(self, x):
        if x == 6:
            return 1
        else:
            return 0

    def high(self, x):
        if x == 7:
            return 1
        else:
            return 0

    def fuzzify_thallium(self, th):
        return dict(
            normal=self.normal(th),
            medium=self.medium(th),
            high=self.high(th)
        )


class sex_fuzzification:
    def __init__(self):
        pass

    def male(self, x):
        if x == 0:
            return 1
        else:
            return 0

    def female(self, x):
        if x == 1:
            return 1
        else:
            return 0

    def fuzzify_sex(self, sex):
        return dict(
            male=self.male(sex),
            female=self.female(sex)
        )


class age_fuzzification:
    def __init__(self):
        pass

    def age_young(self, x):
        if 0 <= x <= 29:
            return 1.0
        elif 29 < x <= 38:
            return (-1.0 / 9.0) * x + 38.0 / 9.0
        else:
            return 0.0

    def age_mild(self, x):
        if 33 <= x <= 38:
            return (1.0 / 5.0) * x - 33.0 / 5.0
        elif 38 < x <= 45:
            return (-1.0 / 7.0) * x + 45.0 / 7.0
        else:
            return 0.0

    def age_old(self, x):
        if 40 <= x <= 48:
            return (1.0 / 8.0) * x - 40.0 / 8.0
        elif 48 < x <= 58:
            return (-1.0 / 10.0) * x + 58.0 / 10.0
        else:
            return 0.0

    def age_very_old(self, x):
        if 0 <= x <= 52:
            return 0.0
        elif 52 < x <= 60:
            return (1.0 / 8.0) * x - 52.0 / 8.0
        else:
            return 1.0

    def fuzzify_age(self, age):
        return dict(
            young=self.age_young(age),
            mild=self.age_mild(age),
            old=self.age_old(age),
            very_old=self.age_very_old(age)
        )


class output_sick_fuzzification:
    def __init__(self):
        pass

    def outputsick_healthy(self, x):
        if 0 <= x <= 0.25:
            return 1.0
        elif 0.25 < x <= 1:
            return (-1.0 / 0.75) * x + 1 / 0.75
        else:
            return 0.0

    def outputsick_sick1(self, x):
        if 0 <= x <= 1:
            return 1.0 * x
        elif 1 < x <= 2:
            return (-1.0) * x + 2
        else:
            return 0.0

    def outputsick_sick2(self, x):
        if 1 <= x <= 2:
            return 1.0 * x - 1
        elif 2 < x <= 3:
            return (-1.0) * x + 3.0
        else:
            return 0.0

    def outputsick_sick3(self, x):
        if 2 <= x <= 3:
            return 1.0 * x - 2.0
        elif 3 < x <= 4:
            return -1.0 * x + 4.0
        else:
            return 0

    def outputsick_sick4(self, x):
        if 0 <= x <= 3:
            return 0.0
        elif 3 < x <= 3.75:
            return (1.0 / 0.75) * x - 3.0 / 0.75
        else:
            return 1.0
