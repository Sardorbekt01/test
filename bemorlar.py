class NoSuchPatient(Exception):
    pass

class NoSuchDoctor(Exception):
    pass

class Person:
    def __init__(self, first_name, last_name, ssn):
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

class Doctor(Person):
    def __init__(self, first_name, last_name, ssn, doctor_id, specialization):
        super().__init__(first_name, last_name, ssn)
        self.doctor_id = doctor_id
        self.specialization = specialization

class Patient(Person):
    def __init__(self, first_name, last_name, ssn):
        super().__init__(first_name, last_name, ssn)

class Clinic:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def addPatient(self, patient):
        self.patients.append(patient)
``
    def addDoctor(self, doctor):
        self.doctors.append(doctor)

    def getPatient(self, ssn):
        for patient in self.patients:
            if patient.ssn == ssn:
                return patient
        raise NoSuchPatient("Bemor topilmadi")

    def getDoctor(self, doctor_id):
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                return doctor
        raise NoSuchDoctor("Shifokor topilmadi")

# Test qismi
if __name__ == "__main__":
    clinic = Clinic()

    # Bemorlarni qo'shamiz
    patient1 = Patient("Ismoil", "Ismoilov", "1234567890")
    patient2 = Patient("Sobir", "Sobirov", "9876543210")

    clinic.addPatient(patient1)
    clinic.addPatient(patient2)

    # Shifokorlarni qo'shamiz
    doctor1 = Doctor("Davron", "Davronov", "1111111111", 1, "Terapevt")
    doctor2 = Doctor("Nigora", "Nigorova", "2222222222", 2, "Kardiolog")

    clinic.addDoctor(doctor1)
    clinic.addDoctor(doctor2)

    try:
        # Bemorlardan malumot olish
        patient = clinic.getPatient("1234567890")
        print(f"Bemor: {patient.first_name} {patient.last_name}")

        # Shifokorlardan malumot olish
        doctor = clinic.getDoctor(2)
        print(f"Shifokor: {doctor.first_name} {doctor.last_name}, ID: {doctor.doctor_id}, Mutaxassisligi: {doctor.specialization}")

        # Topilmaydigan bemorni izlash
        clinic.getPatient("9999999999")

    except NoSuchPatient as e:
        print(f"Xatolik: {e}")

    except NoSuchDoctor as e:
        print(f"Xatolik: {e}")
