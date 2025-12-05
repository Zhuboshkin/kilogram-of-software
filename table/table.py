import pandas as pd
# Если не грузится эта библиотека:
# 1) открой терминал
# 2) вставь pip install pandas openpyxl
import os
import operator
from datetime import datetime

# -----------------------------------------------------------
#                  ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
# -----------------------------------------------------------
current_table = None       # текущая таблица
current_filename = None    # имя загруженного файла

# -----------------------------------------------------------
#                  ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ
# -----------------------------------------------------------
def auto_detect_types(df):
    """Автоопределение типов столбцов по значениям"""
    types = {}
    for col in df.columns:
        sample = df[col].dropna()
        if sample.empty:
            types[col] = str
            continue
        val = sample.iloc[0]
        if isinstance(val, int):
            types[col] = int
        elif isinstance(val, float):
            types[col] = float
        elif isinstance(val, bool):
            types[col] = bool
        elif isinstance(val, datetime):
            types[col] = datetime
        else:
            types[col] = str
    return types


def check_numeric(df, col):
    """Проверка, что столбец числовой"""
    if df[col].dtype not in [int, float, bool]:
        raise TypeError(f"Столбец '{col}' не числовой для арифметической операции")

# -----------------------------------------------------------
#                  ЗАГРУЗКА И СОХРАНЕНИЕ
# -----------------------------------------------------------
def load_table(*filenames, auto_type=False):
    """Загрузка таблицы из одного или нескольких файлов (csv/pkl/xlsx)"""    
    global current_table, current_filename
    tables = []

    for fname in filenames:
        if not os.path.exists(fname):
            raise FileNotFoundError(f"Файл '{fname}' не найден!")
        ext = os.path.splitext(fname)[1].lower()
        if ext == ".csv":
            df = pd.read_csv(fname)
        elif ext == ".pkl":
            df = pd.read_pickle(fname)
        elif ext in [".xls", ".xlsx"]:
            df = pd.read_excel(fname)
        else:
            raise ValueError(f"Неизвестный формат файла '{fname}'")
        tables.append(df)

    # Проверка структуры столбцов
    columns_set = set(tables[0].columns)
    for t in tables[1:]:
        if set(t.columns) != columns_set:
            raise ValueError("Несоответствие структуры столбцов между файлами!")

    current_table = pd.concat(tables, ignore_index=True)

    if auto_type:
        types = auto_detect_types(current_table)
        for col, t in types.items():
            try:
                current_table[col] = current_table[col].astype(t, errors='ignore')
            except:
                pass

    current_filename = os.path.splitext(os.path.basename(filenames[0]))[0]
    print("Таблица успешно загружена:\n")
    print_table()


def save_table(max_rows=None):
    """Сохраняет таблицу в csv, txt и pickle, можно разбивать на несколько файлов по max_rows"""
    global current_table, current_filename

    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return

    if current_filename is None:
        current_filename = "table"

    # Если max_rows не указан — сохраняем в один файл
    if max_rows is None or len(current_table) <= max_rows:
        current_table.to_csv(f"{current_filename}.csv", index=False, encoding="utf-8")
        current_table.to_csv(f"{current_filename}.txt", index=False, sep="\t", encoding="utf-8")
        current_table.to_pickle(f"{current_filename}.pkl")
        print(f'Таблица успешно сохранена как {current_filename}.csv, {current_filename}.txt, {current_filename}.pkl')
    else:
        # Разбиваем на несколько файлов
        total_rows = len(current_table)
        parts = (total_rows + max_rows - 1) // max_rows
        for i in range(parts):
            part_table = current_table.iloc[i*max_rows : (i+1)*max_rows]
            fname = f"{current_filename}_part{i+1}"
            part_table.to_csv(f"{fname}.csv", index=False, encoding="utf-8")
            part_table.to_csv(f"{fname}.txt", index=False, sep="\t", encoding="utf-8")
            part_table.to_pickle(f"{fname}.pkl")
            print(f'Файл {fname} сохранён ({len(part_table)} строк)')

# -----------------------------------------------------------
#                  ОСНОВНЫЕ ОПЕРАЦИИ
# -----------------------------------------------------------
def print_table(table=None):
    """Вывод таблицы с разделителями между столбцами и строками"""
    global current_table
    if table is None:
        table = current_table
    if table is None:
        print("Таблица не загружена!")
        return

    col_widths = [max(len(str(x)) for x in [col]+list(table[col].fillna(''))) for col in table.columns]
    line = "+".join("-"*(w+2) for w in col_widths)
    header = "|".join(f" {col.ljust(col_widths[i])} " for i, col in enumerate(table.columns))

    print(line)
    print(header)
    print(line)

    for idx, row in table.iterrows():
        row_str = "|".join(f" {str(row[col]).ljust(col_widths[i])} " for i, col in enumerate(table.columns))
        print(row_str)
        print(line)

# -----------------------------------------------------------
#                  ВЫБОРКА СТРОК
# -----------------------------------------------------------
def get_rows_by_number(start, stop=None, copy_table=False):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return None
    if stop is None:
        result = current_table.iloc[start:start+1]
    else:
        result = current_table.iloc[start:stop+1]
    print(result)
    if copy_table:
        current_table = result.copy()
        print("Текущая таблица заменена выбранными строками!")
    return result.copy() if copy_table else result

def get_rows_by_index(*values, copy_table=False):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return None
    col = current_table.columns[0]
    result = current_table[current_table[col].isin(values)]
    if copy_table:
        current_table = result.copy()
        print("Текущая таблица заменена выбранными строками!")
    return result.copy() if copy_table else result

# -----------------------------------------------------------
#                  РАБОТА СО СТОЛБЦАМИ
# -----------------------------------------------------------
def get_column_types(by_number=True):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return None

    types = {}
    for i, col in enumerate(current_table.columns):
        dtype = current_table[col].dtype
        if dtype == "int64":
            t = int
        elif dtype == "float64":
            t = float
        elif dtype == "bool":
            t = bool
        elif dtype == "datetime64[ns]":
            t = datetime
        else:
            t = str
        key = i if by_number else col
        types[key] = t
    print(types)
    return types

def set_column_types(types_dict, by_number=True):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return
    for key, t in types_dict.items():
        column = current_table.columns[key] if by_number else key
        try:
            current_table[column] = current_table[column].astype(t)
        except Exception as e:
            print(f"Ошибка преобразования столбца '{column}':", e)

# -----------------------------------------------------------
#                  ЧТЕНИЕ/ЗАПИСЬ ЗНАЧЕНИЙ
# -----------------------------------------------------------
def get_values(column=0):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return None
    if isinstance(column, int):
        if column < 0 or column >= len(current_table.columns):
            print(f"Ошибка: столбца с индексом {column} нет!")
            return None
        col = current_table.columns[column]
    else:
        if column not in current_table.columns:
            print(f"Ошибка: столбца с именем '{column}' нет!")
            return None
        col = column
    result = list(current_table[col])
    print(result)
    return result

def get_value(column=0):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return None
    if len(current_table) != 1:
        print("Ошибка: таблица должна содержать одну строку!")
        return None
    if isinstance(column, int):
        if column < 0 or column >= len(current_table.columns):
            print(f"Ошибка: столбца с индексом {column} нет!")
            return None
        col = current_table.columns[column]
    else:
        if column not in current_table.columns:
            print(f"Ошибка: столбца с именем '{column}' нет!")
            return None
        col = column
    result = current_table.iloc[0][col]
    print(result)
    return result

def set_values(values, column=0):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return
    if isinstance(column, int):
        if column < 0 or column >= len(current_table.columns):
            print(f"Ошибка: столбца с индексом {column} нет!")
            return None
        col = current_table.columns[column]
    else:
        if column not in current_table.columns:
            print(f"Ошибка: столбца с именем '{column}' нет!")
            return None
        col = column
    current_table[col] = values
    print("Значения установлены.")

def set_value(value, column=0):
    global current_table
    if current_table is None:
        print("Ошибка: таблица не загружена!")
        return
    if len(current_table) != 1:
        print("Ошибка: таблица должна содержать одну строку!")
        return
    if isinstance(column, int):
        if column < 0 or column >= len(current_table.columns):
            print(f"Ошибка: столбца с индексом {column} нет!")
            return None
        col = current_table.columns[column]
    else:
        if column not in current_table.columns:
            print(f"Ошибка: столбца с именем '{column}' нет!")
            return None
        col = column
    current_table.at[current_table.index[0], col] = value
    print("Значение установлено.")

# -----------------------------------------------------------
#                  РАСШИРЕННЫЕ ФУНКЦИИ (АРИФМЕТИКА, СКЛЕИВАНИЕ)
# -----------------------------------------------------------
def concat(table1, table2):
    return pd.concat([table1, table2], ignore_index=True)

def split(table, row_number):
    part1 = table.iloc[:row_number].copy()
    part2 = table.iloc[row_number:].copy()
    return part1, part2

def merge_tables(table1, table2, by_number=True):
    if by_number:
        merged = pd.concat([table1.reset_index(drop=True), table2.reset_index(drop=True)], axis=1)
    else:
        merged = pd.merge(table1, table2, on=table1.columns[0], how='outer')
    return merged

def add(table, col1, col2, result_col):
    check_numeric(table, col1)
    check_numeric(table, col2)
    table[result_col] = table[col1] + table[col2]

def sub(table, col1, col2, result_col):
    check_numeric(table, col1)
    check_numeric(table, col2)
    table[result_col] = table[col1] - table[col2]

def mul(table, col1, col2, result_col):
    check_numeric(table, col1)
    check_numeric(table, col2)
    table[result_col] = table[col1] * table[col2]

def div(table, col1, col2, result_col):
    check_numeric(table, col1)
    check_numeric(table, col2)
    table[result_col] = table[col1] / table[col2]

# -----------------------------------------------------------
#                  СРАВНЕНИЯ И ФИЛЬТРАЦИЯ
# -----------------------------------------------------------
def parse_value(v):
    try:
        return int(v)
    except: pass
    try:
        return float(v)
    except: pass
    try:
        return datetime.fromisoformat(v)
    except: pass
    return v

def compare(table, col1, col2, op):
    if col2 in table.columns:
        right = table[col2]
    else:
        right = parse_value(col2)
    left = table[col1]
    return op(left, right)

def eq(table, col1, col2): return compare(table, col1, col2, operator.eq)
def ne(table, col1, col2): return compare(table, col1, col2, operator.ne)
def gr(table, col1, col2): return compare(table, col1, col2, operator.gt)
def ls(table, col1, col2): return compare(table, col1, col2, operator.lt)
def ge(table, col1, col2): return compare(table, col1, col2, operator.ge)
def le(table, col1, col2): return compare(table, col1, col2, operator.le)

def filter_rows(table, bool_list, copy_table=False):
    if len(bool_list) != len(table):
        raise ValueError("Длина списка должна совпадать с количеством строк")
    result = table[bool_list]
    if copy_table:
        return result.copy()
    else:
        table.drop(table.index, inplace=True)
        for idx, row in result.iterrows():
            table.loc[len(table)] = row
        return table
# -----------------------------------------------------------
#                  КОНСОЛЬНЫЙ ИНТЕРФЕЙС
# -----------------------------------------------------------
print("Программа запущена. Команды:")
print("  load_table file1 file2 ... auto_type=True/False")
print("  save_table max_rows=N")
print("  print_table")
print("  get_rows_by_number a b t/f")
print("  get_rows_by_index val1 val2 ...")
print("  get_column_types t/f")
print("  set_column_types col=тип(int/float/bool/str/datetime)")
print("  get_values column")
print("  get_value column (если 1 строка)")
print("  set_values val1,val2,... column")
print("  set_value column значение")
print("  concat")
print("  split row_number")
print("  add/sub/mul/div col1 col2 result_col")
print("  eq/gr/ls/ge/le/ne col1 col2")
print("  filter_rows bool_list (t/f)")
print("  merge_tables by_number=True/False")
print("  exit\n")

type_map = {"int": int, "float": float, "bool": bool, "str": str, "datetime": datetime}

# -----------------------------------------------------------
#                  ЦИКЛ КОМАНД
# -----------------------------------------------------------
while True:
    command = input(">>> ").strip()
    if not command:
        continue
    parts = command.split()
    cmd = parts[0].lower()

    try:
        # ------------------ ВЫХОД ------------------
        if cmd == "exit":
            print("Выход...")
            break

        # ------------------ ЗАГРУЗКА / СОХРАНЕНИЕ ------------------
        elif cmd == "load_table":
            files = [p for p in parts[1:] if not p.lower().startswith("auto_type")]
            auto_type = any("auto_type=true" in p.lower() or "auto_type=t" in p.lower() for p in parts)
            load_table(*files, auto_type=auto_type)

        elif cmd == "save_table":
            max_rows = None
            for p in parts[1:]:
                if p.startswith("max_rows="):
                    max_rows = int(p.split("=")[1])
            save_table(max_rows)

        elif cmd == "print_table":
            print_table()

        # ------------------ ВЫБОРКА СТРОК ------------------
        elif cmd == "get_rows_by_number":
            if len(parts) == 2:
                get_rows_by_number(int(parts[1]))
            elif len(parts) == 3:
                get_rows_by_number(int(parts[1]), int(parts[2]))
            elif len(parts) == 4:
                copy_table = parts[3].lower() in ["t", "true"]
                get_rows_by_number(int(parts[1]), int(parts[2]), copy_table)
            else:
                print("Использование: get_rows_by_number start [stop] [copy]")

        elif cmd == "get_rows_by_index":
            copy_table = False
            vals = []
            for p in parts[1:]:
                if p.lower() in ["t", "true", "f", "false"]:
                    copy_table = p.lower() in ["t", "true"]
                else:
                    vals.append(p)
            get_rows_by_index(*vals, copy_table=copy_table)

        # ------------------ РАБОТА СО СТОЛБЦАМИ ------------------
        elif cmd == "get_column_types":
            by_number = True
            if len(parts) == 2 and parts[1].lower() in ["f", "false"]:
                by_number = False
            get_column_types(by_number)

        elif cmd == "set_column_types":
            mapping = {}
            for part in parts[1:]:
                if "=" not in part:
                    print("Формат: set_column_types 0=int 2=str ...")
                    continue
                col, tp = part.split("=")
                if tp not in type_map:
                    print("Тип должен быть int, float, bool, str или datetime")
                    continue
                mapping[int(col)] = type_map[tp]
            set_column_types(mapping)

        elif cmd == "get_values":
            if len(parts) == 2:
                col = int(parts[1]) if parts[1].isdigit() else parts[1]
                get_values(col)
            else:
                print("Использование: get_values column")

        elif cmd == "get_value":
            if len(parts) == 2:
                col = int(parts[1]) if parts[1].isdigit() else parts[1]
                get_value(col)
            else:
                print("Использование: get_value column")

        elif cmd == "set_values":
            if len(parts) < 3:
                print("Использование: set_values val1,val2,... column")
                continue
            vals = parts[1].split(",")
            col = int(parts[2]) if parts[2].isdigit() else parts[2]
            set_values(vals, col)

        elif cmd == "set_value":
            if len(parts) != 3:
                print("Использование: set_value column value")
                continue
            col = int(parts[1]) if parts[1].isdigit() else parts[1]
            val = parts[2]
            set_value(val, col)

        # ------------------ СКЛЕИВАНИЕ / РАЗБИЕНИЕ ------------------
        elif cmd == "concat":
            current_table = concat(current_table, current_table)
            print("Таблицы склеены")

        elif cmd == "split":
            if len(parts) != 2:
                print("Использование: split row_number")
                continue
            row_number = int(parts[1])
            part1, part2 = split(current_table, row_number)
            print("Первая часть:")
            print(print_table(part1))
            print("Вторая часть:")
            print(print_table(part2))

        # ------------------ АРИФМЕТИКА ------------------
        elif cmd in ["add", "sub", "mul", "div"]:
            if len(parts) != 4:
                print(f"Использование: {cmd} col1 col2 result_col")
                continue
            col1, col2, result = parts[1], parts[2], parts[3]
            if cmd == "add": add(current_table, col1, col2, result)
            elif cmd == "sub": sub(current_table, col1, col2, result)
            elif cmd == "mul": mul(current_table, col1, col2, result)
            elif cmd == "div": div(current_table, col1, col2, result)
            print(f"Результат записан в столбец '{result}'")
            print_table(current_table)
        # ------------------ СРАВНЕНИЯ ------------------
        elif cmd in ["eq", "gr", "ls", "ge", "le", "ne"]:
            if len(parts) != 3:
                print(f"Использование: {cmd} col1 col2")
                continue
            col1, col2 = parts[1], parts[2]
            res = {
                "eq": eq,
                "gr": gr,
                "ls": ls,
                "ge": ge,
                "le": le,
                "ne": ne
            }[cmd](current_table, col1, col2)
            print(res.tolist())

        # ------------------ ФИЛЬТРАЦИЯ ------------------
        elif cmd == "filter_rows":
            mask_str = " ".join(parts[1:])
            mask = eval(mask_str)
            current_table = filter_rows(current_table, mask)
            print("Таблица отфильтрована")
            print_table(current_table)

        # ------------------ ОБЪЕДИНЕНИЕ ------------------
        elif cmd == "merge_tables":
            by_number = True
            if len(parts) == 2:
                by_number = parts[1].lower() in ["true", "t"]
            current_table = merge_tables(current_table, current_table, by_number)
            print("Таблицы объединены")
            print(current_table)

        else:
            print("Неизвестная команда!")

    except Exception as e:
        print("Ошибка:", e)
