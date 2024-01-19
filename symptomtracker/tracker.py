class SymptomTracker:
    def __init__(self):
        self.patient_symptoms = {}

    def record_symptoms(self, patient_id, symptoms):
        if patient_id not in self.patient_symptoms:
            self.patient_symptoms[patient_id] = []
        self.patient_symptoms[patient_id].extend(symptoms)

    def get_patient_symptoms(self, patient_id):
        return self.patient_symptoms.get(patient_id, [])

    def clear_symptoms(self, patient_id):
        if patient_id in self.patient_symptoms:
            del self.patient_symptoms[patient_id]
