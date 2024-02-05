import requests
import json
import replicate

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
