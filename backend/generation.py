import requests
import json
from PIL import Image
from diffusers import (
    StableDiffusionControlNetPipeline,
    ControlNetModel,
    UniPCMultistepScheduler,
    StableDiffusionImg2ImgPipeline,
)
import torch
from controlnet_aux import MLSDdetector
from diffusers.utils import load_image
import replicate
import logging

NEGATIVE_PROMPT = "(((Ugly))), low-resolution, morbid, blurry, cropped, deformed, dehydrated, text, disfigured, duplicate, error, extra arms, extra fingers, extra legs, extra limbs, fused fingers, gross proportions, jpeg artifacts, long neck, low resolution, tiling, poorly drawn feet, extra limbs, disfigured, body out of frame, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, low quality, lowres, low saturation, deformed body features, watermark, water mark"


INPUT = {
    "eta": 0,
    "image": "https://replicate.delivery/pbxt/IJZOELWrncBcjdE1s5Ko8ou35ZOxjNxDqMf0BhoRUAtv76u4/room.png",
    "scale": 9,
    "prompt": "a cheerful modernist bedroom",
    "a_prompt": "best quality, extremely detailed",
    "n_prompt": "longbody, lowres, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality",
    "ddim_steps": 20,
    "num_samples": "1",
    "value_threshold": 0.1,
    "image_resolution": "512",
    "detect_resolution": 512,
    "distance_threshold": 0.1,
}


def run_replicate(input: dict = INPUT):
    output = replicate.run(
        "jagilley/controlnet-hough:854e8727697a057c525cdb45ab037f64ecca770a1769cc52287c2e56472a247b",
        input=input,
    )

    return output


def controlled_generation(image, prompt: str):
    """Funcion to generate controlled images using the Stable Diffusion ControlNet model using M-LSD detector"""
    # start logging
    logging.basicConfig(level=logging.INFO)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        logging.info("No GPU found")
        return None
    mlsd = MLSDdetector.from_pretrained("lllyasviel/ControlNet")
    logging.info("MLSDdetector loaded")
    image = mlsd(image)
    logging.info("MLSD applied to image")

    logging.info("Loading ControlNet")
    controlnet = ControlNetModel.from_pretrained(
        "lllyasviel/sd-controlnet-mlsd", torch_dtype=torch.float16
    )
    logging.info("ControlNet loaded")

    pipe = StableDiffusionControlNetPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        controlnet=controlnet,
        safety_checker=None,
        torch_dtype=torch.float16,
    )

    pipe.scheduler = UniPCMultistepScheduler.from_config(pipe.scheduler.config)
    pipe.enable_xformers_memory_efficient_attention()
    pipe.enable_model_cpu_offload()
    image = pipe(prompt, image, num_inference_steps=40).images[0]

    return image


def non_controlled_generation(
    image,
    prompt: str,
    neg_prompt: str = NEGATIVE_PROMPT,
    guidance_scale: int = 10,
    strength: float = 0.7,
):
    """Function to generate images using the Stable Diffusion Img2Img Pipeline"""
    logging.basicConfig(level=logging.INFO)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    if device == "cpu":
        logging.info("No GPU found")
        return None
    logging.info("Loading Stable Diffusion Img2Img Pipeline")
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
    ).to(device)
    logging.info("Stable Diffusion Img2Img Pipeline loaded")

    logging.info("Generating Image")
    image_output = pipe(
        prompt,
        image,
        strength=strength,
        guidance_scale=guidance_scale,
        negative_prompt=neg_prompt,
    ).images[0]
    logging.info("Image Generated")

    return image_output
