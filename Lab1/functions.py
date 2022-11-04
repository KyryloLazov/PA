def generate_files():
    import random
    with open("files/file_a.txt", "w") as file_a:
        nums = []
        for i in range(30): #1_800_000
            num = random.randint(1, 100) #2_000_000
            nums.append(num)
        file_a.write(" ".join([str(i) for i in nums]))

        print("Файл згенерован")

def convert_to_int(data) -> list[int]:
    numbers = [int(num) for num in data.split(' ')]

    return numbers

def find_series(numbers: list[int]) -> list:
    if len(numbers) == 1:
        return [numbers]

    #Усі серії
    all_series = []
    #Поточна
    this_series = []

    for i in range(1, len(numbers)):
        #Попоредне число менше
        if numbers[i - 1] <= numbers[i]:
            this_series.append(numbers[i - 1])
        else:
            #Додаємо число у поточну серію
            this_series.append(numbers[i - 1])
            #Поточну серію додоаємо до усіх
            all_series.append(this_series)
            #Обнуляємо поточну
            this_series = []

        #Якщо ітерована остання серія
        if i == len(numbers) - 1:
            this_series.append(numbers[i])
            all_series.append(this_series)
            this_series = []

    return all_series

def series_to_files(series: list):
    file_b = open("files/file_b.txt", "w")
    file_c = open("files/file_c.txt", "w")

    for i in range(len(series)):
        string_to_write = ""

        for j in range(len(series[i])):
            #Уникнення від пробілів у кінці файлу
            #Якщо і та j - останні індекси
            #або і-передостанній, а j останній індекси
            if (i == len(series)-1 and j == len(series[i]) - 1) or (i == len(series) - 2 and j == len(series[i]) - 1):
                string_to_write += f"{series[i][j]}"
            else:
                string_to_write += f"{series[i][j]} "

        if i % 2 == 0:
            file_b.write(string_to_write)
        else:
            file_c.write(string_to_write)

    file_b.close()
    file_c.close()

def clear_file():
    file_a = open("files/file_a.txt", "w")
    file_a.write("")
    file_a.close()

def merge_files():
    with open("files/file_b.txt") as b:
        file_b = b.read()
        print(file_b)

    with open("files/file_c.txt") as c:
        file_c = c.read()
        print(file_c)

    numbers_b = convert_to_int(file_b)
    numbers_c = convert_to_int(file_c)

    series_b = find_series(numbers_b)
    series_c = find_series(numbers_c)

    clear_file()

    if(len(series_b) >= len(series_c)):
        longest_series = series_b
    else:
        longest_series = series_c

    if (len(series_b) < len(series_c)):
        shortest_series = series_b
    else:
        shortest_series = series_c

    for i in range(len(longest_series)):
        longest_series_elements = longest_series[i]

        #Якщо і менше за довжину кортших серій
        if i < len(shortest_series):
            shortest_series_elements = shortest_series[i]
        else:
            shortest_series_elements = []

        joined_list = longest_series_elements + shortest_series_elements
        joined_list.sort()

        with open("files/file_a.txt", "a") as file_a:
            #Запис числе у файл
            file_a.write(" ".join([str(i) for i in joined_list]))
            #Якщо і!=len(longest_series) - 1: ставимо пробіл
            file_a.write(" " if i != len(longest_series) - 1 else "")

def file_is_sorted() -> bool:
    with open("files/file_a.txt") as file_a:
        data = file_a.read()

    numbers = convert_to_int(data)

    for i in range(1, len(numbers)):
        if numbers[i - 1]>numbers[i]:
            return False

    return True