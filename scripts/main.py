# This helper script scans folders for wildcards and embeddings and writes them
# to a temporary file to expose it to the javascript side

import glob
from pathlib import Path

import gradio as gr
import yaml
from modules import script_callbacks, scripts, sd_hijack, shared
import requests
from gradio import Blocks
from fastapi import FastAPI
from typing import Optional, Dict, Any

try:
    from modules.paths import extensions_dir, script_path

    # Webui root path
    FILE_DIR = Path(script_path)

    # The extension base path
    EXT_PATH = Path(extensions_dir)
except ImportError:
    # Webui root path
    FILE_DIR = Path().absolute()
    # The extension base path
    EXT_PATH = FILE_DIR.joinpath('extensions')

# 插件物理路径
EXT_INNER_PATH = Path(scripts.basedir())


def on_ui_settings():
    """
    @des: 启动时候动态设置配置项
    参考:
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/shared.py
    参考
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/script_callbacks.py
    """
    if 1:
        # 添加自定义配置项
        shared.opts.add_option("playdayyconfig", shared.OptionInfo(default=None, label="天天玩家额外配置"))
        # 启动时候动态设置配置项---这里是有效果的------
        shared.opts.set("outdir_samples", "yxtest6666")
        # print("动态设置输出路径配置项完成-------by yx")
        

def on_app_started(demo: Optional[Blocks], app: FastAPI):
    """
    @des: 启动完成后的回调函数
    参考
    /Users/yuanxiao/workspace/0yxgithub/stable-diffusion-webui/modules/script_callbacks.py
    """
    if 0:
        base_output_dir = "outputs"
        res = requests.get("http://localhost:9965/servermanageyx/version", timeout=(5,5))
        print('', res.text)
    pass

            

script_callbacks.on_ui_settings(on_ui_settings)
script_callbacks.on_app_started(on_app_started)