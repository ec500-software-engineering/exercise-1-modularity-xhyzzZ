class Analyzer:
    def __init__(self, Systolic_BP, Diastolic_BP, Heart_Rate, Heart_Oxygen_Level, Body_temp):
        self.Systolic_BP = Systolic_BP
        self.Diastolic_BP = Diastolic_BP
        self.Heart_Rate = Heart_Rate
        self.Heart_Oxygen_Level = Heart_Oxygen_Level
        self.Body_temp = Body_temp

    def Signal_Loss(self, Heart_Rate, Body_temp):
        # Signal loss judgement
        if ((int)(Heart_Rate) < 60 and (int)(Body_temp) < 36):
            return True
        return False

    def Shock_Alert(self, Heart_Rate, Body_temp):
        # Shock emergency judgement
        if ((int)(Heart_Rate) < 60 and (int)(Body_temp) >= 36):
            return True
        return False

    def Oxygen_Supply(self, Heart_Oxygen_Level):
        # Oxygen supply judgement
        if ((int)(Heart_Oxygen_Level) < 70):
            return True
        return False

    def Fever(self, Body_temp):
        # Fever judgement
        if ((float)(Body_temp) > 37.5):
            return True
        return False

    def Hypotension(self, Systolic_BP, Diastolic_BP):
        # Hypotension judgement
        if ((int)(Systolic_BP) < 90 and (int)(Diastolic_BP) < 60):
            return True
        return False

    def Hypertension(self, Systolic_BP, Diastolic_BP):
        # Hypertension judgement
        if ((int)(Systolic_BP) > 140 or (int)(Diastolic_BP) > 90):
            return True
        return False