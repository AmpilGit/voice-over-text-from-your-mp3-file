# import torch
# from TTS.api import TTS

# # Имитируем старое поведение torch.load (для совместимости)
# old_torch_load = torch.load
# def _new_torch_load(*args, **kwargs):
#     if "weights_only" not in kwargs:
#         kwargs["weights_only"] = False
#     return old_torch_load(*args, **kwargs)

# torch.load = _new_torch_load

# # Теперь загружаем модель
# tts = TTS(
#     model_name="tts_models/multilingual/multi-dataset/xtts_v2",
#     progress_bar=True,
#     gpu=False
# )

# # Пути к файлам
# REFERENCE_WAV = "nekopara.wav"  # WAV-файл с голосом для клонирования
# TEXT_TO_SYNTHESIZE =  "Podozhdite, Chocola edva li mozhet chitat detskie knigi! Ona ne smozhet prochitat recept!"
# OUTPUT_PATH = "output_cloned_voice.wav"

# print("🔊 Генерация речи...")
# tts.tts_to_file(
#     text=TEXT_TO_SYNTHESIZE,
#     speaker_wav=REFERENCE_WAV,
#     file_path=OUTPUT_PATH,
#     split_sentences=True
# )

# print(f"✅ Переозвученный файл сохранён как {os.path.abspath(OUTPUT_PATH)}")
import torch
from TTS.api import TTS
import warnings
warnings.filterwarnings("ignore")
import noisereduce as nr
import soundfile as sf
# Обход ошибки с weights_only
# from rwkv_cpp import RwkvCpp

# # Путь к модели
# model_path = "rwkv-4-ru-petro-79M-q8_0.gguf"

# # Загрузка модели
# model = RwkvCpp(model_path=model_path)

# def generate_insult():
#     prompt = "Скажи что-нибудь постироничное про человека, который спрашивает глупые вопросы:"
#     output = model.generate(
#         prompt=prompt,
#         max_tokens=50,
#         temperature=0.8,
#         top_k=50,
#         top_p=0.95,
#         repetition_penalty=1.1
#     )
#     return output.strip()
old_torch_load = torch.load
def _new_torch_load(*args, **kwargs):
    if "weights_only" not in kwargs:
        kwargs["weights_only"] = False
    return old_torch_load(*args, **kwargs)
torch.load = _new_torch_load

# Загрузка модели
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True, gpu=False,
          vocoder_path="vocoder_models/universal/libri_tts/univnet")

# Генерация речи
tts.tts_to_file(
    text=" Привет, как дела!!!! Это мистери'рино Светлу'нино'. Хочу научится тыкать по кнопкам в гугле, помоги побра'тски",
    file_path="output.wav", 
    speaker_wav="svetlana_wav.wav",
    speed=1.2,
    language="ru",
    temperature=1.3,
    repetition_penalty=5.0,
    length_penalty=0.0,
)
data, sr = sf.read("output.wav")

# Удаление шума
reduced_noise = nr.reduce_noise(y=data, sr=sr)


# Сохраняем обратно
sf.write("output_clean.wav", reduced_noise, sr)

print("✅ Готово!")