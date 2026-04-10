import os


class PopulationAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []

    def read_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл {self.file_path} не знайдено.")

        def sort_by_area(self, reverse=False):
            return sorted(self.data, key=lambda x: x['area'], reverse=reverse)

        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    name, area, population = line.split(',')

                    self.data.append({
                        'name': name.strip(),
                        'area': float(area.strip()),
                        'population': int(population.strip())
                    })
        return self.data