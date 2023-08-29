"""
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

# Parasetamol-nimistä (eli Panadol® tai Tylenol®) särky/kuumelääkettä voidaan
# annostella aikuiselle potilaalle 15 mg painokiloa kohden kuuden tunnin
# välein, mutta 24 tunnissa ei saa ylittää 4000 mg kokonaisannosta.
MAX_DOSE = 4000
TIME_PER_DOSE = 6
DOSE_SIZE = 15


def calculate_dose(weight, time_from_dose, total_24hr_dose):
    """
    :param weight: int, weight of person
    :param time_from_dose: int, time from previous dose
    :param total_24hr_dose: int, the total 24hr dose
    :return: returns the dose of paracetamol that should be given tot the
    patient
    """
    weight = int(weight)
    time_from_dose = int(time_from_dose)
    dose_to_give = DOSE_SIZE * weight
    total_24hr_dose = int(total_24hr_dose)

    new_total_24hr_dose = total_24hr_dose + dose_to_give
    if time_from_dose < TIME_PER_DOSE:
        return 0
    elif new_total_24hr_dose > MAX_DOSE:
        return MAX_DOSE - total_24hr_dose
    else:
        return dose_to_give


def main():
    weight = input("Patient's weight (kg): ")
    time_from_dose = input("How much time has passed from the previous dose"
                           " (full hours): ")
    total_24hr_dose = input("The total dose for the last 24 hours (mg): ")
    paracetamol_amount = calculate_dose(weight, time_from_dose,
                                        total_24hr_dose)
    print(f"The amount of Parasetamol to give to the patient:"
          f" {paracetamol_amount}")

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
    main()
