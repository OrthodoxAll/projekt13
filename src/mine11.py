import json

def get_avg_for_city(path: str, city: str) -> bool:
    '''Получение средней температцры для города'''
    try:
        with open(path) as city_file:
            try:
                city_data = json.load(city_file)
            except json.decoder.JSONDecodeError:
                print('Ошибка декодирования файлв')
                return False
    except FileNotFoundError:
        print('Файл не найден')
        return False
    avg_temp = round(sum(city_data[city].values()) / len(city_data[city].keys()),2)
    out_data = {
        city: {
            'Averege temoerature' : avg_temp
        }
    }

    with open('out.json', 'w') as out_file:
        json.dump(out_data, out_file)



    return True


get_avg_for_city('data.json', 'Moscow')


