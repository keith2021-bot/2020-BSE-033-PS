import unittest
from symptomtracker.tracker import SymptomTracker

class TestSymptomTracker(unittest.TestCase):
    def test_record_symptoms(self):
        tracker = SymptomTracker()
        tracker.record_symptoms(1, ['Fever', 'Cough'])
        self.assertEqual(tracker.get_patient_symptoms(1), ['Fever', 'Cough'])

    def test_clear_symptoms(self):
        tracker = SymptomTracker()
        tracker.record_symptoms(1, ['Headache', 'Fatigue'])
        tracker.clear_symptoms(1)
        self.assertEqual(tracker.get_patient_symptoms(1), ['Headache', 'Fatigue'])

if __name__ == '__main__':
    unittest.main()
