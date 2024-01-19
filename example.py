from symptomtracker.tracker import SymptomTracker

tracker = SymptomTracker()
tracker.record_symptoms(1, ['Fever', 'Cough'])
print(tracker.get_patient_symptoms(1))  # Output: ['Fever', 'Cough']
tracker.clear_symptoms(1)
print(tracker.get_patient_symptoms(1))  # Output: []
