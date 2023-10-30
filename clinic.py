class Doctor:
    def __init__(self, id, surname, name, specialization, num_patients):
        self.id = id
        self.surname = surname
        self.name = name
        self.specialization = specialization
        self.num_patients = num_patients

    def __str__(self):
        return f"{self.surname} {self.name}"

    def get_specialization(self):
        return self.specialization

    def get_num_patients(self):
        return self.num_patients


class Hospital:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def idle_doctors(self):
        idle_doctors = [doctor for doctor in self.doctors if doctor.get_num_patients() == 0]
        idle_doctors.sort(key=lambda doctor: (doctor.surname, doctor.name))
        return [str(doctor) for doctor in idle_doctors]

    def busy_doctors(self):
        busy_doctors = [doctor for doctor in self.doctors if doctor.get_num_patients() > 0]
        busy_doctors.sort(key=lambda doctor: (doctor.surname, doctor.name))
        return [str(doctor) for doctor in busy_doctors]

    def doctors_by_num_patients(self):
        sorted_doctors = sorted(self.doctors, key=lambda doctor: doctor.get_num_patients(), reverse=True)
        return [f"{doctor.get_num_patients()}: {doctor.id} {doctor.surname} {doctor.name}" for doctor in sorted_doctors]

    def count_patients_per_specialization(self):
        specialization_count = {}
        for doctor in self.doctors:
            specialization = doctor.get_specialization()
            specialization_count[specialization] = specialization_count.get(specialization, 0) + 1
        sorted_specializations = sorted(specialization_count.items(), key=lambda item: (-item[1], item[0]))
        return [f"{count} - {specialization}" for specialization, count in sorted_specializations]

# Usage example:
if __name__ == "__main__":
    hospital = Hospital()
    doctor1 = Doctor(1, "Smith", "John", "Cardiologist", 5)
    doctor2 = Doctor(2, "Johnson", "Mary", "Dermatologist", 10)
    doctor3 = Doctor(3, "Williams", "James", "Cardiologist", 8)
    doctor4 = Doctor(4, "Brown", "Anna", "Dermatologist", 3)
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)
    hospital.add_doctor(doctor3)
    hospital.add_doctor(doctor4)

    print("Idle Doctors:")
    print(hospital.idle_doctors())

    print("\nBusy Doctors:")
    print(hospital.busy_doctors())

    print("\nDoctors by Number of Patients:")
    print(hospital.doctors_by_num_patients())

    print("\nCount of Patients per Specialization:")
    print(hospital.count_patients_per_specialization())
