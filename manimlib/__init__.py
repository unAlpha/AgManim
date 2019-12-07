#!/usr/bin/env python
import manimlib.config
import manimlib.constants
import manimlib.extract_scene
import manimlib.stream_starter


def main():
    # 通过argparse模块，获得输入参数
    args = manimlib.config.parse_cli()
    if not args.livestream:
        # 从arg参数中获得config配置
        config = manimlib.config.get_configuration(args)
        # 初始化配置
        manimlib.constants.initialize_directories(config)
        # 应用配置
        manimlib.extract_scene.main(config)
    else:
        manimlib.stream_starter.start_livestream(
            to_twitch=args.to_twitch,
            twitch_key=args.twitch_key,
        )
