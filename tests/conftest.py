import pytest


@pytest.fixture
def input_test_operations_with_vacancies():
    return [{'id': '110134917', 'premium': False, 'name': 'Python/Django Junior Backend-разработчик', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 60000, 'to': 90000, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': 'улица Ленинская Слобода', 'building': '26с15', 'lat': 55.70882, 'lng': 37.651475, 'description': None, 'raw': 'Москва, улица Ленинская Слобода, 26с15', 'metro': {'station_name': 'Автозаводская', 'line_name': 'Замоскворецкая', 'station_id': '2.2', 'line_id': '2', 'lat': 55.706634, 'lng': 37.657008}, 'metro_stations': [{'station_name': 'Автозаводская', 'line_name': 'Замоскворецкая', 'station_id': '2.2', 'line_id': '2', 'lat': 55.706634, 'lng': 37.657008}, {'station_name': 'Автозаводская', 'line_name': 'МЦК', 'station_id': '95.530', 'line_id': '95', 'lat': 55.70631, 'lng': 37.66314}], 'id': '877439'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T15:15:55+0300', 'created_at': '2024-11-11T15:15:55+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110134917', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110134917?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110134917', 'relations': [], 'employer': {'id': '3008614', 'name': 'Placebo/25', 'url': 'https://api.hh.ru/employers/3008614', 'alternate_url': 'https://hh.ru/employer/3008614', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/4102916.png', '90': 'https://img.hhcdn.ru/employer-logo/4102915.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/915559.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3008614', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.', 'responsibility': 'Участвовать в проектировании базы данных. Создавать интеграции с внешними сервисами. Дорабатывать существующие скрипты. Писать SQL-запросы. Разрабатывать админку и REST...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}, {'id': '110429201', 'premium': False, 'name': 'Junior Java Developer', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': 'улица Правды', 'building': '24с2', 'lat': 55.78729, 'lng': 37.583167, 'description': None, 'raw': 'Москва, улица Правды, 24с2', 'metro': {'station_name': 'Белорусская', 'line_name': 'Замоскворецкая', 'station_id': '2.19', 'line_id': '2', 'lat': 55.777439, 'lng': 37.582107}, 'metro_stations': [{'station_name': 'Белорусская', 'line_name': 'Замоскворецкая', 'station_id': '2.19', 'line_id': '2', 'lat': 55.777439, 'lng': 37.582107}, {'station_name': 'Савёловская', 'line_name': 'Серпуховско-Тимирязевская', 'station_id': '9.128', 'line_id': '9', 'lat': 55.794054, 'lng': 37.587163}], 'id': '264168'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T15:38:31+0300', 'created_at': '2024-11-11T15:38:31+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110429201', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110429201?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110429201', 'relations': [], 'employer': {'id': '1260189', 'name': 'Trend Soft, студия', 'url': 'https://api.hh.ru/employers/1260189', 'alternate_url': 'https://hh.ru/employer/1260189', 'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/1555621.png', '240': 'https://img.hhcdn.ru/employer-logo/1555622.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/278281.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1260189', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Знание основных шаблонов проектирования. Умение читать чужой код. Знание Spring, Hibernate. Опыт программирования на языках PHP, Ruby или <highlighttext>Python</highlighttext>. Ответственность. ', 'responsibility': 'Разработка нового и поддержка существующего функционала сервиса. Участие в разработке мобильных приложений сервиса.'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}, {'id': '110451384', 'premium': False, 'name': 'Младший продуктовый аналитик / Junior Product Analyst', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T18:32:37+0300', 'created_at': '2024-11-11T18:32:37+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110451384', 'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110451384?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110451384', 'relations': [], 'employer': {'id': '9009067', 'name': 'ЕГЭLand', 'url': 'https://api.hh.ru/employers/9009067', 'alternate_url': 'https://hh.ru/employer/9009067', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1200644.jpeg', '240': 'https://img.hhcdn.ru/employer-logo/6423026.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/6423025.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9009067', 'accredited_it_employer': True, 'trusted': True}, 'snippet': {'requirement': 'Опыт создания интерактивных дашбордов и визуализации данных в DataLens. Владение <highlighttext>Python</highlighttext> для анализа данных, разработки ETL-скриптов и автоматизации задач. ', 'responsibility': 'Подготовка и автоматизация выгрузок из баз данных для повышения эффективности операционных процессов компании. Создание интерактивных дашбордов и визуализаций, помогающих принимать...'}, 'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '164', 'name': 'Продуктовый аналитик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]



@pytest.fixture
def return_test_avg():
    return [{'id': '110134917', 'premium': False, 'name': 'Python/Django Junior Backend-разработчик', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 60000, 'to': 90000, 'currency': 'RUR', 'gross': False, 'avg': 75000.0}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': 'улица Ленинская Слобода', 'building': '26с15', 'lat': 55.70882, 'lng': 37.651475, 'description': None, 'raw': 'Москва, улица Ленинская Слобода, 26с15', 'metro': {'station_name': 'Автозаводская', 'line_name': 'Замоскворецкая', 'station_id': '2.2', 'line_id': '2', 'lat': 55.706634, 'lng': 37.657008}, 'metro_stations': [{'station_name': 'Автозаводская', 'line_name': 'Замоскворецкая', 'station_id': '2.2', 'line_id': '2', 'lat': 55.706634, 'lng': 37.657008}, {'station_name': 'Автозаводская', 'line_name': 'МЦК', 'station_id': '95.530', 'line_id': '95', 'lat': 55.70631, 'lng': 37.66314}], 'id': '877439'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T15:15:55+0300', 'created_at': '2024-11-11T15:15:55+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110134917', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110134917?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110134917', 'relations': [], 'employer': {'id': '3008614', 'name': 'Placebo/25', 'url': 'https://api.hh.ru/employers/3008614', 'alternate_url': 'https://hh.ru/employer/3008614', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/4102916.png', '90': 'https://img.hhcdn.ru/employer-logo/4102915.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/915559.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3008614', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.', 'responsibility': 'Участвовать в проектировании базы данных. Создавать интеграции с внешними сервисами. Дорабатывать существующие скрипты. Писать SQL-запросы. Разрабатывать админку и REST...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}, {'id': '110429201', 'premium': False, 'name': 'Junior Java Developer', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR', 'gross': False, 'avg': 60000.0}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': 'улица Правды', 'building': '24с2', 'lat': 55.78729, 'lng': 37.583167, 'description': None, 'raw': 'Москва, улица Правды, 24с2', 'metro': {'station_name': 'Белорусская', 'line_name': 'Замоскворецкая', 'station_id': '2.19', 'line_id': '2', 'lat': 55.777439, 'lng': 37.582107}, 'metro_stations': [{'station_name': 'Белорусская', 'line_name': 'Замоскворецкая', 'station_id': '2.19', 'line_id': '2', 'lat': 55.777439, 'lng': 37.582107}, {'station_name': 'Савёловская', 'line_name': 'Серпуховско-Тимирязевская', 'station_id': '9.128', 'line_id': '9', 'lat': 55.794054, 'lng': 37.587163}], 'id': '264168'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T15:38:31+0300', 'created_at': '2024-11-11T15:38:31+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110429201', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110429201?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110429201', 'relations': [], 'employer': {'id': '1260189', 'name': 'Trend Soft, студия', 'url': 'https://api.hh.ru/employers/1260189', 'alternate_url': 'https://hh.ru/employer/1260189', 'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/1555621.png', '240': 'https://img.hhcdn.ru/employer-logo/1555622.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/278281.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1260189', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Знание основных шаблонов проектирования. Умение читать чужой код. Знание Spring, Hibernate. Опыт программирования на языках PHP, Ruby или <highlighttext>Python</highlighttext>. Ответственность. ', 'responsibility': 'Разработка нового и поддержка существующего функционала сервиса. Участие в разработке мобильных приложений сервиса.'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}, {'id': '110451384', 'premium': False, 'name': 'Младший продуктовый аналитик / Junior Product Analyst', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR', 'gross': False, 'avg': 70000.0}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T18:32:37+0300', 'created_at': '2024-11-11T18:32:37+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110451384', 'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110451384?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110451384', 'relations': [], 'employer': {'id': '9009067', 'name': 'ЕГЭLand', 'url': 'https://api.hh.ru/employers/9009067', 'alternate_url': 'https://hh.ru/employer/9009067', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1200644.jpeg', '240': 'https://img.hhcdn.ru/employer-logo/6423026.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/6423025.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9009067', 'accredited_it_employer': True, 'trusted': True}, 'snippet': {'requirement': 'Опыт создания интерактивных дашбордов и визуализации данных в DataLens. Владение <highlighttext>Python</highlighttext> для анализа данных, разработки ETL-скриптов и автоматизации задач. ', 'responsibility': 'Подготовка и автоматизация выгрузок из баз данных для повышения эффективности операционных процессов компании. Создание интерактивных дашбордов и визуализаций, помогающих принимать...'}, 'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '164', 'name': 'Продуктовый аналитик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]


@pytest.fixture
def return_test_comparison():
    return [{'id': '110134917', 'premium': False, 'name': 'Python/Django Junior Backend-разработчик', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 60000, 'to': 90000, 'currency': 'RUR', 'gross': False, 'avg': 75000.0}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': 'улица Ленинская Слобода', 'building': '26с15', 'lat': 55.70882, 'lng': 37.651475, 'description': None, 'raw': 'Москва, улица Ленинская Слобода, 26с15', 'metro': {'station_name': 'Автозаводская', 'line_name': 'Замоскворецкая', 'station_id': '2.2', 'line_id': '2', 'lat': 55.706634, 'lng': 37.657008}, 'metro_stations': [{'station_name': 'Автозаводская', 'line_name': 'Замоскворецкая', 'station_id': '2.2', 'line_id': '2', 'lat': 55.706634, 'lng': 37.657008}, {'station_name': 'Автозаводская', 'line_name': 'МЦК', 'station_id': '95.530', 'line_id': '95', 'lat': 55.70631, 'lng': 37.66314}], 'id': '877439'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T15:15:55+0300', 'created_at': '2024-11-11T15:15:55+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110134917', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110134917?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110134917', 'relations': [], 'employer': {'id': '3008614', 'name': 'Placebo/25', 'url': 'https://api.hh.ru/employers/3008614', 'alternate_url': 'https://hh.ru/employer/3008614', 'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/4102916.png', '90': 'https://img.hhcdn.ru/employer-logo/4102915.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/915559.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3008614', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.', 'responsibility': 'Участвовать в проектировании базы данных. Создавать интеграции с внешними сервисами. Дорабатывать существующие скрипты. Писать SQL-запросы. Разрабатывать админку и REST...'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}, {'id': '110451384', 'premium': False, 'name': 'Младший продуктовый аналитик / Junior Product Analyst', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 60000, 'to': 80000, 'currency': 'RUR', 'gross': False, 'avg': 70000.0}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T18:32:37+0300', 'created_at': '2024-11-11T18:32:37+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110451384', 'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110451384?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110451384', 'relations': [], 'employer': {'id': '9009067', 'name': 'ЕГЭLand', 'url': 'https://api.hh.ru/employers/9009067', 'alternate_url': 'https://hh.ru/employer/9009067', 'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1200644.jpeg', '240': 'https://img.hhcdn.ru/employer-logo/6423026.jpeg', '90': 'https://img.hhcdn.ru/employer-logo/6423025.jpeg'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9009067', 'accredited_it_employer': True, 'trusted': True}, 'snippet': {'requirement': 'Опыт создания интерактивных дашбордов и визуализации данных в DataLens. Владение <highlighttext>Python</highlighttext> для анализа данных, разработки ETL-скриптов и автоматизации задач. ', 'responsibility': 'Подготовка и автоматизация выгрузок из баз данных для повышения эффективности операционных процессов компании. Создание интерактивных дашбордов и визуализаций, помогающих принимать...'}, 'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '164', 'name': 'Продуктовый аналитик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}, {'id': '110429201', 'premium': False, 'name': 'Junior Java Developer', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'}, 'salary': {'from': 50000, 'to': 70000, 'currency': 'RUR', 'gross': False, 'avg': 60000.0}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': 'улица Правды', 'building': '24с2', 'lat': 55.78729, 'lng': 37.583167, 'description': None, 'raw': 'Москва, улица Правды, 24с2', 'metro': {'station_name': 'Белорусская', 'line_name': 'Замоскворецкая', 'station_id': '2.19', 'line_id': '2', 'lat': 55.777439, 'lng': 37.582107}, 'metro_stations': [{'station_name': 'Белорусская', 'line_name': 'Замоскворецкая', 'station_id': '2.19', 'line_id': '2', 'lat': 55.777439, 'lng': 37.582107}, {'station_name': 'Савёловская', 'line_name': 'Серпуховско-Тимирязевская', 'station_id': '9.128', 'line_id': '9', 'lat': 55.794054, 'lng': 37.587163}], 'id': '264168'}, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-11-11T15:38:31+0300', 'created_at': '2024-11-11T15:38:31+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=110429201', 'show_logo_in_search': None, 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/110429201?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/110429201', 'relations': [], 'employer': {'id': '1260189', 'name': 'Trend Soft, студия', 'url': 'https://api.hh.ru/employers/1260189', 'alternate_url': 'https://hh.ru/employer/1260189', 'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/1555621.png', '240': 'https://img.hhcdn.ru/employer-logo/1555622.png', 'original': 'https://img.hhcdn.ru/employer-logo-original/278281.png'}, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=1260189', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Знание основных шаблонов проектирования. Умение читать чужой код. Знание Spring, Hibernate. Опыт программирования на языках PHP, Ruby или <highlighttext>Python</highlighttext>. Ответственность. ', 'responsibility': 'Разработка нового и поддержка существующего функционала сервиса. Участие в разработке мобильных приложений сервиса.'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'noExperience', 'name': 'Нет опыта'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}]



@pytest.fixture
def return_test_high():
    return {
        "id": "110134917",
        "premium": False,
        "name": "Python/Django Junior Backend-разработчик",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
        "salary": {"from": 60000, "to": 90000, "currency": "RUR", "gross": False, "avg": 75000.0},
        "type": {"id": "open", "name": "Открытая"},
        "address": {
            "city": "Москва",
            "street": "улица Ленинская Слобода",
            "building": "26с15",
            "lat": 55.70882,
            "lng": 37.651475,
            "description": None,
            "raw": "Москва, улица Ленинская Слобода, 26с15",
            "metro": {
                "station_name": "Автозаводская",
                "line_name": "Замоскворецкая",
                "station_id": "2.2",
                "line_id": "2",
                "lat": 55.706634,
                "lng": 37.657008,
            },
            "metro_stations": [
                {
                    "station_name": "Автозаводская",
                    "line_name": "Замоскворецкая",
                    "station_id": "2.2",
                    "line_id": "2",
                    "lat": 55.706634,
                    "lng": 37.657008,
                },
                {
                    "station_name": "Автозаводская",
                    "line_name": "МЦК",
                    "station_id": "95.530",
                    "line_id": "95",
                    "lat": 55.70631,
                    "lng": 37.66314,
                },
            ],
            "id": "877439",
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-11-11T15:15:55+0300",
        "created_at": "2024-11-11T15:15:55+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=110134917",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/110134917?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/110134917",
        "relations": [],
        "employer": {
            "id": "3008614",
            "name": "Placebo/25",
            "url": "https://api.hh.ru/employers/3008614",
            "alternate_url": "https://hh.ru/employer/3008614",
            "logo_urls": {
                "240": "https://img.hhcdn.ru/employer-logo/4102916.png",
                "90": "https://img.hhcdn.ru/employer-logo/4102915.png",
                "original": "https://img.hhcdn.ru/employer-logo-original/915559.png",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3008614",
            "accredited_it_employer": False,
            "trusted": True,
        },
        "snippet": {
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.",
            "responsibility": "Участвовать в проектировании базы данных. Создавать интеграции с внешними сервисами. Дорабатывать существующие скрипты. Писать SQL-запросы. Разрабатывать админку и REST...",
        },
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "noExperience", "name": "Нет опыта"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }


@pytest.fixture
def return_test_lowest_pay():
    return {
        "id": "110134917",
        "premium": False,
        "name": "Python/Django Junior Backend-разработчик",
        "department": None,
        "has_test": False,
        "response_letter_required": False,
        "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
        "salary": {"from": 60000, "to": 90000, "currency": "RUR", "gross": False, "avg": 75000.0},
        "type": {"id": "open", "name": "Открытая"},
        "address": {
            "city": "Москва",
            "street": "улица Ленинская Слобода",
            "building": "26с15",
            "lat": 55.70882,
            "lng": 37.651475,
            "description": None,
            "raw": "Москва, улица Ленинская Слобода, 26с15",
            "metro": {
                "station_name": "Автозаводская",
                "line_name": "Замоскворецкая",
                "station_id": "2.2",
                "line_id": "2",
                "lat": 55.706634,
                "lng": 37.657008,
            },
            "metro_stations": [
                {
                    "station_name": "Автозаводская",
                    "line_name": "Замоскворецкая",
                    "station_id": "2.2",
                    "line_id": "2",
                    "lat": 55.706634,
                    "lng": 37.657008,
                },
                {
                    "station_name": "Автозаводская",
                    "line_name": "МЦК",
                    "station_id": "95.530",
                    "line_id": "95",
                    "lat": 55.70631,
                    "lng": 37.66314,
                },
            ],
            "id": "877439",
        },
        "response_url": None,
        "sort_point_distance": None,
        "published_at": "2024-11-11T15:15:55+0300",
        "created_at": "2024-11-11T15:15:55+0300",
        "archived": False,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=110134917",
        "show_logo_in_search": None,
        "insider_interview": None,
        "url": "https://api.hh.ru/vacancies/110134917?host=hh.ru",
        "alternate_url": "https://hh.ru/vacancy/110134917",
        "relations": [],
        "employer": {
            "id": "3008614",
            "name": "Placebo/25",
            "url": "https://api.hh.ru/employers/3008614",
            "alternate_url": "https://hh.ru/employer/3008614",
            "logo_urls": {
                "240": "https://img.hhcdn.ru/employer-logo/4102916.png",
                "90": "https://img.hhcdn.ru/employer-logo/4102915.png",
                "original": "https://img.hhcdn.ru/employer-logo-original/915559.png",
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3008614",
            "accredited_it_employer": False,
            "trusted": True,
        },
        "snippet": {
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.",
            "responsibility": "Участвовать в проектировании базы данных. Создавать интеграции с внешними сервисами. Дорабатывать существующие скрипты. Писать SQL-запросы. Разрабатывать админку и REST...",
        },
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "noExperience", "name": "Нет опыта"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }


@pytest.fixture
def return_test_get_max_avg_salary():
    return 75000.0

@pytest.fixture
def return_search():
    return ['Имя вакансии - Junior Java разработчик,месторасположение - Москва,средняя зарплата - 80000.0,валюта - RUR,url - https://hh.ru/vacancy/109788485', 'Имя вакансии - Junior Java Developer,месторасположение - Москва,средняя зарплата - 60000.0,валюта - RUR,url - https://hh.ru/vacancy/110429201']