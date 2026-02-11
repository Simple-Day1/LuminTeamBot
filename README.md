```markdown
<p align="center">
  <img src="https://raw.githubusercontent.com/lumin-core/.github/main/assets/lumin-logo.png" alt="LuminTeam Logo" width="120" style="border-radius: 50%;">
  <h1 align="center">✨ LuminTeamBot</h1>
  <p align="center">
    <b>Telegram‑бот, который оживляет процесс разработки игр</b><br>
    Прогресс · Концепт‑арты · Бэкстейджи · О студии
  </p>
  <p align="center">
    <a href="https://python.org">
      <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+">
    </a>
    <a href="https://docs.aiogram.dev">
      <img src="https://img.shields.io/badge/aiogram-3.4.1-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="aiogram 3.4.1">
    </a>
    <a href="LICENSE">
      <img src="https://img.shields.io/badge/license-MIT-3DA639?style=for-the-badge&logo=open-source-initiative&logoColor=white" alt="MIT License">
    </a>
  </p>
  <p align="center">
    <a href="#-возможности">Возможности</a> •
    <a href="#-демонстрация">Демо</a> •
    <a href="#-установка-и-запуск">Установка</a> •
    <a href="#-структура-проекта">Структура</a> •
    <a href="#-деплой">Деплой</a>
  </p>
</p>

<br>

---

## 🌟 Возможности

Бот закрывает четыре ключевых потребности команды разработки и комьюнити:

| Команда / Кнопка          | 🎯 Описание                                                                                       |
|---------------------------|---------------------------------------------------------------------------------------------------|
| `/progress` · 📊 Прогресс | 🖼 Отправляет **progress.jpg** с актуальными метриками готовности игры.                           |
| `/gallery` · 🎨 Галерея   | 🗂 Показывает категории концепт-артов. При выборе — **все изображения** из выбранной папки.       |
| `/backstage` · 🎬 Бэкстейдж | 🎞 То же, но с **детальным описанием** под каждым фото (имя, дата, автор).                      |
| `/info` · ℹ️ О нас        | 📄 Красивая **HTML‑визитка** студии: состав, контакты, ссылки.                                   |

✅ **Главное меню** — быстрые Reply‑кнопки под полем ввода.  
✅ **Inline‑навигация** — удобные кнопки для выбора категорий.  
✅ **Асинхронность** — молниеносный ответ даже при десятках запросов.

<br>

---

## 🎬 Демонстрация

<p align="center">
  <table>
    <tr>
      <td align="center"><b>🏠 Главное меню</b></td>
      <td align="center"><b>🗂 Категории галереи</b></td>
      <td align="center"><b>🖼 Концепт‑арт</b></td>
    </tr>
    <tr>
      <td><img src="https://via.placeholder.com/300x600?text=Main+Menu" width="250"></td>
      <td><img src="https://via.placeholder.com/300x600?text=Categories" width="250"></td>
      <td><img src="https://via.placeholder.com/300x600?text=Concept+Art" width="250"></td>
    </tr>
  </table>
  <i>⬆️ Скриншоты будут добавлены после первого релиза ⬆️</i>
</p>

<br>

---

## 🛠 Стек технологий

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="30">
  <img src="https://img.shields.io/badge/aiogram-2CA5E0?style=flat-square&logo=telegram&logoColor=white" height="30">
  <img src="https://img.shields.io/badge/python--dotenv-ECD53F?style=flat-square&logo=.env&logoColor=black" height="30">
  <img src="https://img.shields.io/badge/asyncio-0078D7?style=flat-square&logo=python&logoColor=white" height="30">
</p>

- **Python 3.9+** — современный, быстрый, асинхронный  
- **aiogram 3.4.1** — актуальная версия фреймворка для Telegram API  
- **python-dotenv** — безопасное хранение токенов  
- **asyncio** — неблокирующие операции ввода/вывода  

<br>

---

## 🚀 Установка и запуск

<details>
<summary><b>🔰 Пошаговое руководство (нажми, чтобы развернуть)</b></summary>
<br>

### 📦 1. Клонирование репозитория
```bash
git clone https://github.com/lumin-core/LuminTeamBot.git
cd LuminTeamBot
```

### 🐍 2. Виртуальное окружение и зависимости
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
# venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 🔐 3. Переменные окружения
Создай файл `.env` в корне:
```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
ADMIN_ID=123456789          # Твой Telegram ID (узнать у @userinfobot)
```

### 🖼 4. Медиафайлы (обязательно!)
Структура папки `assets` должна быть такой:
```
assets/
├── progress.jpg                # Фото прогресса
├── gallery/
│   ├── Персонажи/              # Категория 1
│   │   ├── warrior.jpg
│   │   └── mage.png
│   └── Локации/                # Категория 2
│       └── forest.webp
└── backstage/
    ├── Запись голоса/          # Категория 1
    │   └── session.jpg
    └── Съёмки/                 # Категория 2
        └── bts.jpg
```

### 🚦 5. Запуск
```bash
python bot.py
```
🎉 Всё! Бот уже отвечает в Telegram.

</details>

<br>

---

## 📁 Архитектура проекта

```
LuminTeamBot/
├── 📦 .env                     # Секреты (игнорируется Git)
├── 📦 .gitignore
├── 📦 requirements.txt
├── 🧠 bot.py                  # Точка входа, сборка роутеров
├── ⚙️ config.py               # Загрузка переменных из .env
├── 🎛 handlers/               # Обработчики событий
│   ├── start.py
│   ├── progress.py
│   ├── gallery.py
│   ├── backstage.py
│   ├── info.py
│   └── callbacks.py          # Кнопка «Назад» и общие колбэки
├── 🎚 keyboards/             # Клавиатуры
│   ├── __init__.py
│   └── main_menu.py
├── 🧰 services/              # Логика работы с файлами
│   ├── __init__.py
│   └── file_manager.py
└── 🖼 assets/                # Медиа (создаётся вручную)
```

> 💡 **Почему так?**  
> Разделение на роутеры, сервисы и клавиатуры позволяет масштабировать бота без головной боли. Хотите добавить админку или базу данных — просто положите новый модуль в нужную папку.

<br>

---

## 🕹 Использование

1. **Найди бота** в Telegram по его юзернейму.  
2. **Нажми `/start`** — появится главное меню.  
3. **Используй кнопки** или команды:

| Команда        | Действие                          |
|----------------|-----------------------------------|
| `/progress`    | Смотрим прогресс разработки       |
| `/gallery`     | Листаем концепт-арты             |
| `/backstage`   | Заглядываем за кулисы            |
| `/info`        | Читаем о студии                  |

🔄 **Навигация по категориям** — происходит через inline‑кнопки.  
🔙 **Вернуться назад** — кнопка «◀️ Назад» под любым списком.

<br>

---

## 🎨 Добавление своего контента

| Раздел         | Действие                                                                                                 |
|----------------|----------------------------------------------------------------------------------------------------------|
| **Прогресс**   | Замени `assets/progress.jpg`. Текст подписи — в `handlers/progress.py`.                                 |
| **Галерея**    | Создай подпапку в `assets/gallery/`, положи туда картинки. Бот подхватит их автоматом.                  |
| **Бэкстейдж**  | Аналогично галерее, но в `assets/backstage/`. Описание редактируй в `handlers/backstage.py`.            |
| **О нас**      | Весь текст хранится в `handlers/info.py` — меняй смело.                                                 |

> ✨ **Подсказка:** названия категорий и файлов могут быть на любом языке. Бот отобразит их «как есть».

<br>

---

## ☁️ Деплой (бесплатные варианты)

<p align="center">
  <a href="https://amvera.ru/"><img src="https://img.shields.io/badge/Amvera-бесплатно-2A6EBB?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCIgdmlld0JveD0iMCAwIDIwMCAyMDAiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHJlY3Qgd2lkdGg9IjIwMCIgaGVpZ2h0PSIyMDAiIGZpbGw9IndoaXRlIi8+PC9zdmc+" alt="Amvera"></a>
  <a href="https://railway.app/"><img src="https://img.shields.io/badge/Railway-удобно-0B0D0E?style=for-the-badge&logo=railway" alt="Railway"></a>
  <a href="https://render.com/"><img src="https://img.shields.io/badge/Render-быстро-46E3B7?style=for-the-badge&logo=render" alt="Render"></a>
  <a href="#"><img src="https://img.shields.io/badge/VPS-полный_контроль-FF6600?style=for-the-badge&logo=ubuntu" alt="VPS"></a>
</p>

**Самый простой путь — Amvera Cloud** (российский хостинг, есть вечный фриплан):

1. Залей код в **публичный/приватный Git‑репозиторий**.  
2. На [Amvera](https://amvera.ru/) создай проект, подключи репозиторий.  
3. В настройках укажи переменные `BOT_TOKEN` и `ADMIN_ID`.  
4. Запусти — бот заработает 24/7 🚀  

📘 [Подробная инструкция по вебхукам в aiogram 3.x](https://docs.aiogram.dev/en/dev-3.x/dispatcher/webhook.html)

<br>

---

## 👥 Автор и лицензия

<p align="center">
  <b>Lumin Core</b> — небольшая команда энтузиастов, влюблённых в геймдев.<br>
  ✉️ По всем вопросам: <a href="https://t.me/lumin_core">@lumin_core</a>
</p>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-3DA639?style=flat-square&logo=open-source-initiative&logoColor=white" alt="MIT">
  </a>
  <br>
  <sub>© 2026 Lumin Core. Можно использовать, форкать и дорабатывать без ограничений.</sub>
</p>

<br>

---

<p align="center">
  <a href="#-luminteambot">
    <img src="https://img.shields.io/badge/⬆️_Вернуться_наверх-2A6EBB?style=for-the-badge" alt="Back to top">
  </a>
</p>

<p align="center">
  ⭐ <b>Если бот оказался полезным, поставь звезду — это лучшая благодарность!</b><br>
  🐞 Нашёл баг? <a href="https://github.com/lumin-core/LuminTeamBot/issues">Создай Issue</a> или напиши в Telegram.
</p>
```
