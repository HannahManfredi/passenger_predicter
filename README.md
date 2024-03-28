# human speech emotion classifier

Using the RAVDESS dataset, we intend to fine-tune an existing (likely Wav2Vec) model to classify audio into 7 “core” categories, 'angry', 'calm', 'disgust', 'fearful', 'happy', 'neutral', 'sad', and 'surprised'.

## Things to Explore

## Objectives

- Have learned about this problem so that our next work sesh is dope/productive

## Resources

- [Audio Classification](https://huggingface.co/docs/transformers/en/tasks/audio_classification)
- [Search Audio Emotion Classification Models - Hugging Face](https://huggingface.co/models?pipeline_tag=audio-classification&sort=downloads&search=emotion)

### Model

- [Wav2Vec](https://ai.meta.com/research/impact/wav2vec/#how-it-works)
- [Wav2Vec2 Model on Hugging Face](https://huggingface.co/docs/transformers/en/model_doc/wav2vec2)
  - [facebook/wav2vec2-base-960h · Hugging Face](https://huggingface.co/facebook/wav2vec2-base-960h)
- [ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition · Hugging Face](https://huggingface.co/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition)

### Dataset

- [ravdess Dataset - Hugging Face](https://huggingface.co/datasets/narad/ravdess)
- [Toronto emotional speech set (TESS) - Kaggle](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)
- [RAVDESS Emotional speech audio - Kaggle](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)

### Tutorials

- Linked from hugging face task doc: [Audio Classification on Keyword Spotting - Colab](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/audio_classification.ipynb)
  - [transformers/examples/pytorch/audio-classification at main · huggingface/transformers](https://github.com/huggingface/transformers/tree/main/examples/pytorch/audio-classification)
- Linked from model card: [Fine-Tune Wav2Vec2 for English ASR Notebook - Colaboratory](https://colab.research.google.com/drive/1FjTsqbYKphl9kL-eILgUc-bl4zVThL8F?usp=sharing)
  - [Fine-Tune Wav2Vec2 for English ASR in Hugging Face with 🤗 Transformers](https://huggingface.co/blog/fine-tune-wav2vec2-english)
- [Speech Recognition with Wav2Vec2 — Torchaudio 2.2.0 documentation](https://pytorch.org/audio/stable/tutorials/speech_recognition_pipeline_tutorial.html)
- [Greek Emotion Recogntion Wav2Vec2](https://colab.research.google.com/github/m3hrdadfi/soxan/blob/main/notebooks/Emotion_recognition_in_Greek_speech_using_Wav2Vec2.ipynb)

#### Deployment

- [Deploy Automatic Speech Recogntion with Hugging Face's Transformers & Amazon SageMaker](https://www.philschmid.de/automatic-speech-recognition-sagemaker)

## Plan

- Everyone is going to read and absorb all of the resources and become enlightened (~1.5 hrs of prep)
  - Get a high level understanding of how the Wav2Vec works
  - Scan the dataset and understand what we're working with
  - [Audio-Classification-on-Keyword-Spotting.ipynb - Colaboratory](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/audio_classification.ipynb)
  - Review [Audio Classification Guide](https://huggingface.co/docs/transformers/en/tasks/audio_classification)
  - If you're feeling spicy and have more time, complete [Speech Recognition with Wav2Vec2 — Torchaudio 2.2.0 documentation](https://pytorch.org/audio/stable/tutorials/speech_recognition_pipeline_tutorial.html)
  - This is overkill: [Google Colab](https://colab.research.google.com/github/m3hrdadfi/soxan/blob/main/notebooks/Emotion_recognition_in_Greek_speech_using_Wav2Vec2.ipynb)
- We're tentatively meeting on Saturday afternoon, 3/30
