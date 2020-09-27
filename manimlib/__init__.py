#!/usr/bin/env python
import manimlib.config
import manimlib.constants
import manimlib.extract_scene


def main():
    # 通过argparse模块，获得输入参数
    args = manimlib.config.parse_cli()
    # 从arg参数中获得config配置
    config = manimlib.config.get_configuration(args)
    # 初始化配置
    manimlib.constants.initialize_directories(config)
    # 应用配置
    manimlib.extract_scene.main(config)

