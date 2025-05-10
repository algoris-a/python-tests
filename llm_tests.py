# Need to install hugging face:
# conda install -c conda-forge huggingface_hub
# conda install transformers
# Also need to install torch (pytorch)
#  pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
#  pip3 install sentencepiece
#  pip3 install sacremoses

from transformers import pipeline

spanish_text = "Este curso sobre LLMs se está poniendo muy interesante"

# Define the pipeline
translator = pipeline(task="translation_es_to_en", model="Helsinki-NLP/opus-mt-es-en")

# Translate the Spanish text
translations = translator(spanish_text, clean_up_tokenization_spaces=True)

print(translations[0]["translation_text"]) 