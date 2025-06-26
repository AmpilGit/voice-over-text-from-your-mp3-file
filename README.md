
Этот скрипт использует библиотеку `TTS` (Text-to-Speech) для генерации аудио из текста, а также применяет **шумоподавление** с помощью библиотеки `noisereduce`, чтобы улучшить качество звука.

Скрипт:
- Загружает модель `xtts_v2` (многоязычная модель)
- Генерирует аудиофайл на русском языке
- Добавляет шумоподавление
- Сохраняет результат в файл `output_clean.wav`

---

### 🛠️ Технологии

| Компонент | Версия / Использование |
|-----------|------------------------|
| Python    | 3.10+                  |
| TTS       | 0.24.0                 |
| noisereduce | 1.2.0               |
| soundfile | 0.12.1                 |

---

### 📁 Структура проекта

```
tts_script.py           # Основной скрипт
svetlana_wav.wav        # Аудио-файл для голоса
output.wav              # Сгенерированный аудио-файл без шумоподавления
output_clean.wav        # Аудио-файл после шумоподавления
```

---

### 🚀 Запуск

#### 1. Установите зависимости:

```bash
pip install TTS noisereduce soundfile
```

> ⚠️ Убедитесь, что у вас установлены все необходимые библиотеки и модели.

#### 2. Подготовьте файл с аудио для голоса (`svetlana_wav.wav`)

Файл должен быть в формате `.wav`, содержать голос, который будет использоваться как источник для синтеза речи.

#### 3. Запустите скрипт:

```bash
python tts_script.py
```

> После выполнения будут созданы файлы:
> - `output.wav` — исходный аудио-файл
> - `output_clean.wav` — аудио-файл с уменьшенным шумом

---

### 🔧 Настройки

- **Модель**: `tts_models/multilingual/multi-dataset/xtts_v2`
- **Язык**: `ru` (русский)
- **Голос**: `svetlana_wav.wav`
- **Темп**: `speed=1.2`
- **Параметры шумоподавления**:
  - `temperature=1.3`
  - `repetition_penalty=5.0`
  - `length_penalty=0.0`

---

### 🧠 Как работает

1. **Загрузка модели TTS**
   - Используется модель `xtts_v2`, которая поддерживает синтез речи на нескольких языках
   - Модель не запускается на GPU, если не указано иное

2. **Генерация аудио**
   - Входной текст: `"Привет, как дела!!!! Это мистери'рино Светлу'нино'. Хочу научится тыкать по кнопкам в гугле, помоги побра'тски"`
   - Голос: `svetlana_wav.wav`
   - Результат сохраняется в `output.wav`

3. **Шумоподавление**
   - Используется `noisereduce` для уменьшения шума
   - Результат сохраняется в `output_clean.wav`

---

### 📌 Автор

**Кудрявцев Данил**  
Системный администратор IT-отдела  
Email: mikushkinodanil4@gmail.com

---

### 📝 Лицензия

MIT License

Copyright (c) 2025 Кудрявцев Данил

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---
