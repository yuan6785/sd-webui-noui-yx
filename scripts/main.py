# This helper script scans folders for wildcards and embeddings and writes them
# to a temporary file to expose it to the javascript side

import glob
from pathlib import Path

import gradio as gr
import yaml
from modules import script_callbacks, scripts, sd_hijack, shared

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

# Register autocomplete options
def on_ui_settings():
    # 启动时候动态设置配置项
    shared.opts.set("outdir_samples", "yxtest6666")

script_callbacks.on_ui_settings(on_ui_settings)
