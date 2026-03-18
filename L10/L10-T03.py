import csv
def process_titanic_data(filename):
    try:
        male_count = 0
        female_count = 0
        ages = []
        file = open(filename, 'r')
        reader = csv.DictReader(file)
        for row in reader:
            if row['Sex'] == 'male':
                male_count += 1
            elif row['Sex'] == 'female':
                female_count += 1
            if row['Age']:
                ages.append(float(row['Age']))
        if ages:
            average_age = sum(ages) / len(ages)
            average_age_rounded = round(average_age)
        else:
            average_age_rounded = 0

        if ages:
            oldest_age = int(max(ages))
        else:
            oldest_age = 0

        print(f"The number of male passengers: {male_count}")
        print(f"The number of female passengers: {female_count}")
        print(f"The average age of passengers: {average_age_rounded}")
        print(f"The age of the oldest passenger: {oldest_age}")

    except FileNotFoundError:
        print("The file was not found. Please ensure the file 'titanic.csv' is in the correct directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_titanic_data('titanic.csv')
