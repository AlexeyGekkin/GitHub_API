# Автоматический тест для работы с GitHub API

Этот проект содержит автоматический тест для базовых операций с GitHub API. Скрипт:

1. Создает публичный репозиторий на GitHub.
2. Проверяет его наличие.
3. Удаляет репозиторий с GitHub.

## Требования

Для запуска скрипта необходимо:

1. **Python**: Убедитесь, что на вашем компьютере установлен Python версии 3.6 или выше.
2. **Аккаунт на GitHub** и **персональный токен доступа GitHub** с правами на управление репозиториями.
3. Установленные библиотеки **requests** и **python-dotenv** (инструкции по установке ниже).

## Структура проекта

```bash
.
├── test_api.py        # Основной скрипт, выполняющий тест.
├── .env               # Файл с переменными окружения (пример ниже).
├── requirements.txt   # Зависимости проекта.
└── README.md          # Инструкция по установке и запуску.
## Инструкции по установке и запуску

1. **Клонируйте репозиторий**:
   - Перейдите в рабочую папку, например:
     ```bash
     cd d:\dev
     ```
   - Клонируйте репозиторий с кодом теста с GitHub и перейдите в папку проекта:
     ```bash
     git clone https://github.com/AlexeyGekkin/GitHub_API.git
     cd GitHub_API
     ```

3. **Создайте виртуальное окружение**:
   - Создайте виртуальное окружение для управления зависимостями:
     ```bash
     python -m venv venv
     ```
   - Активируйте виртуальное окружение:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/Scripts/activate
       ```

4. **Установите зависимости**:
   - Установите необходимые Python-пакеты:
     - **Windows**:
       ```bash
       venv\Scripts\python.exe -m pip install -r requirements.txt
       ```
     - **macOS/Linux**:
       ```bash
       venv/Scripts/python.exe -m pip install -r requirements.txt

       ```
5. **Заполните файл .env**:
   - **GITHUB_USERNAME** - Ваш юзернейм на гитхабе
   - **GITHUB_TOKEN** - Ваш персональный токен доступа GitHub
   - **REPO_NAME** - Название создаваемого репозитория

6. **Запустите тест**:
   - Выполните тестовый скрипт с помощью Python:
     ```bash
     python test_apy.py
     ```
