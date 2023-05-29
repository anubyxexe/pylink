import replicate
import time
from colorama import Fore
import os

#commande a executer au lancement de votre terminal
#export REPLICATE_API_TOKEN=r8_0uNeY60EH2eyun4PL57uyt17zmsWk8R00yPPE


model = replicate.models.get("prompthero/openjourney")
version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")
os.system('cls' if os.name=='nt' else 'clear')
print(Fore.GREEN + "_____  ___.__. ____  ____   ____  ")
time.sleep(0.1)
print("\__  \<   |  |/ ___\/  _ \ /    \ ")
time.sleep(0.1)
print(" / __ \\___  \  \__(  <_> )   |  \ ")
time.sleep(0.1)
print("(____  / ____|\___  >____/|___|  /")
time.sleep(0.1)
print("     \/\/         \/           \/")
time.sleep(0.1)
print("corrige par un bg d'erreur d'un fdp")
time.sleep(0.1)
print()

p = input(Fore.LIGHTGREEN_EX + "aycon-> ")
print("chargement...")

inputs = {
        
    # Input prompt
    'prompt': p + ", 8k",

    # Width of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'width': 512,

    # Height of output image. Maximum size is 1024x768 or 768x1024 because
    # of memory limits
    'height': 512,

    # Number of images to output
    'num_outputs': 1,

    # Number of denoising steps
    # Range: 1 to 500
    'num_inference_steps': 50,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 6,

    # Random seed. Leave blank to randomize the seed
    # 'seed': ...,
}

# https://replicate.com/prompthero/openjourney/versions/9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb#output-schema

output = version.predict(**inputs)
print("chargement fini")
print(Fore.CYAN)
print(output)
