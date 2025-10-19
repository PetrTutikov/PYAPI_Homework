def merge_files_by_line_count(filenames, output_file):
    files_data = []

    # Читаем файлы
    for fname in filenames:
        with open(fname, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            files_data.append((fname, len(lines), lines))

    # Сортируем
    files_data.sort(key=lambda x: x[1])

    # Запись
    with open(output_file, 'w', encoding='utf-8') as out:
        for fname, line_count, lines in files_data:
            out.write(f"{fname}\n")
            out.write(f"{line_count}\n")
            out.writelines(lines)
            out.write("\n")


# Проверка
filenames = ['1.txt', '2.txt', '3.txt']
output_file = 'result.txt'

merge_files_by_line_count(filenames, output_file)
