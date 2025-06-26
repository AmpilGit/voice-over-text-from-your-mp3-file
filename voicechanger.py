
import torch
from TTS.api import TTS
import warnings
warnings.filterwarnings("ignore")
import noisereduce as nr
import soundfile as sf
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

sf.write("output_clean.wav", reduced_noise, sr)

print("✅ Готово!")
