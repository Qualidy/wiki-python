from datetime import datetime, timedelta, date


Service_Pauschale = "30 Euro"

def read_data():
        with open("./vins.txt") as f:
                vins = f.readlines()

        with open("./emails.txt") as f:
                emails = f.readlines()

        with open("./last_workshop_visit.txt") as f:
                last_workshop_visit = f.readlines()

        with open("./locations.txt") as f:
                locations = f.readlines()

        with open("./mileage_readings.txt") as f:
                mileage_readings = f.readlines()

        with open("./mileage_at_last_service.txt") as f:
                mileage_at_last_service = f.readlines()

        with open("./mobile_numbers.txt") as f:
                mobile_numbers = f.readlines()

        with open("./registration_dates.txt") as f:
                registration_dates = f.readlines()

        with open("./service_contract_durations.txt") as f:
                service_contract_durations = f.readlines()

        with open("./service_fees.txt") as f:
                service_fees = f.readlines()

        with open("./service_partner_ids.txt") as f:
                service_partner_ids = f.readlines()

        with open("./vehicle_models.txt") as f:
                vehicle_models = f.readlines()

        return vins, emails, last_workshop_visit, locations, mileage_readings, locations, mobile_numbers, registration_dates, service_contract_durations, service_fees, service_partner_ids, vehicle_models

vins, emails, last_workshop_visit, locations, mileage_readings, mileage_at_last_service, mobile_numbers, registration_dates, service_contract_durations, service_fees, service_partner_ids, vehicle_models = read_data()


def extend_service_duration(service_contract_durations, vins, vin , years):
    
    position = [i for i,x in enumerate(vins) if x == vin]
    service_contract_durations[position[0]] + years

    return service_contract_durations



if __name__ == "__main__":
      extend_service_duration(service_contract_durations, vins, "6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b" , 3) 