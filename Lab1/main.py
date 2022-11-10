import functions

functions.generate_files()

counter = 1

while not functions.file_is_sorted():
    with open("files/file_a.txt") as file_a:
        data = file_a.read()

    print(f"Ітерація #{counter}...")

    numbers = functions.convert_to_int(data)

    series = functions.find_series(numbers)

    functions.series_to_files(series)

    functions.merge_files()

    counter += 1

print("Файл відсотован")
