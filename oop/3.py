class Patient:
    def __init__(self, name, age, gender, patient_id, medical_history=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.patient_id = patient_id
        self.medical_history = medical_history if medical_history is not None else []

    def add_medical_record(self, condition: str):
        self.medical_history.append(condition)
        print(f"Added '{condition}' to medical history.")

    def get_summary(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Gender": self.gender,
            "Patient ID": self.patient_id,
            "Medical History": self.medical_history or "No records"
        }


class Inpatient(Patient):
    def __init__(self, name, age, gender, patient_id, admission_date, room_number, medical_history=None):
        super().__init__(name, age, gender, patient_id, medical_history)
        self.admission_date = admission_date
        self.room_number = room_number

    def discharge(self):
        """Clear admission details."""
        self.admission_date = None
        self.room_number = None
        print("Patient discharged. Room cleared.")

    def get_summary(self):
        """Override to include admission details."""
        summary = super().get_summary()
        summary.update({
            "Admission Date": self.admission_date or "Not admitted",
            "Room Number": self.room_number or "No room assigned"
        })
        return summary


class Outpatient(Patient):
    def __init__(self, name, age, gender, patient_id, last_visit_date, doctor_consulted, medical_history=None):
        super().__init__(name, age, gender, patient_id, medical_history)
        self.last_visit_date = last_visit_date
        self.doctor_consulted = doctor_consulted

    def schedule_follow_up(self, date):
        self.last_visit_date = date
        print(f"Follow-up scheduled on {date} with Dr. {self.doctor_consulted}.")

    def get_summary(self):
        """Override to include outpatient details."""
        summary = super().get_summary()
        summary.update({
            "Last Visit Date": self.last_visit_date,
            "Doctor Consulted": self.doctor_consulted
        })
        return summary


# ---------- Example Usage ----------
# Inpatient
inpatient = Inpatient("John Doe", 45, "Male", "P001", "2025-08-01", "Room 101")
inpatient.add_medical_record("Diabetes")
print(inpatient.get_summary())
inpatient.discharge()
print(inpatient.get_summary())

# Outpatient
outpatient = Outpatient("Jane Smith", 30, "Female", "P002", "2025-07-20", "Dr. Adams")
outpatient.add_medical_record("Flu")
print(outpatient.get_summary())
outpatient.schedule_follow_up("2025-09-15")
print(outpatient.get_summary())
