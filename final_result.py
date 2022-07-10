import fuzzification
import inference
import defuzzification

cp_fuzzification = fuzzification.chest_pain_fuzzification()
bp_fuzzification = fuzzification.blood_pressure_fuzzification()
ch_fuzzification = fuzzification.cholesterol_fuzzification()
bs_fuzzification = fuzzification.blood_sugar_fuzzification()
ECG_fuzzification = fuzzification.ECG_fuzzification()
hr_fuzzification = fuzzification.heart_rate_fuzzification()
ex_fuzzification = fuzzification.exercise_fuzzification()
op_fuzzification = fuzzification.old_peak_fuzzification()
th_fuzzification = fuzzification.thallium_scan_fuzzification()
sex_fuzzification = fuzzification.sex_fuzzification()
age_fuzzification = fuzzification.age_fuzzification()
inference_engine = inference.inference()
defuzzifier = defuzzification.defuzzification()


class ProvideResult(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ProvideResult, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def get_final_result(input_dict: dict) -> str:
        print(input_dict.keys())
        fuzzy_cp = cp_fuzzification.fuzzify_chest_pain(int(input_dict['chest_pain']))
        fuzzy_bp = bp_fuzzification.fuzzify_blood_pressure(int(input_dict['blood_pressure']))
        fuzzy_ch = ch_fuzzification.fuzzify_cholesterol(int(input_dict['cholestrol']))
        fuzzy_bs = bs_fuzzification.fuzzify_blood_sugar(int(input_dict['blood_sugar']))
        fuzzy_ECG = ECG_fuzzification.fuzzify_ECG(float(input_dict['ecg']))
        fuzzy_hr = hr_fuzzification.fuzzify_heart_rate(int(input_dict['heart_rate']))
        fuzzy_ex = ex_fuzzification.fuzzify_exercise(int(input_dict['exercise']))
        fuzzy_op = op_fuzzification.fuzzify_old_peak(float(input_dict['old_peak']))
        fuzzy_th = th_fuzzification.fuzzify_thallium(int(input_dict['thallium_scan']))
        fuzzy_sex = sex_fuzzification.fuzzify_sex(int(input_dict['sex']))
        fuzzy_age = age_fuzzification.fuzzify_age(int(input_dict['age']))
        fuzzy_result = inference_engine.inference_engine(fuzzy_cp, fuzzy_bp, fuzzy_ch,
                                                         fuzzy_bs, fuzzy_ECG, fuzzy_hr,
                                                         fuzzy_ex, fuzzy_op, fuzzy_th,
                                                         fuzzy_sex, fuzzy_age)
        defuzzified_result = defuzzifier.defuzzify(fuzzy_result)
        return defuzzified_result
