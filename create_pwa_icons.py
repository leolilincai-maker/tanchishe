#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PWA图标生成脚本
为贪吃蛇游戏创建各种尺寸的图标
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_snake_icon(size):
    """创建贪吃蛇图标"""
    # 创建画布
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # 计算缩放比例
    scale = size / 512
    
    # 背景 - 绿色渐变
    bg_color1 = (39, 174, 96)  # 深绿色
    bg_color2 = (46, 204, 113)  # 浅绿色
    
    # 绘制圆形背景
    margin = int(20 * scale)
    draw.ellipse([margin, margin, size - margin, size - margin], 
                 fill=bg_color1, outline=bg_color2, width=int(3 * scale))
    
    # 蛇头 - 黄色/橙色
    head_size = int(80 * scale)
    head_x = size // 2 - head_size // 2
    head_y = size // 2 - head_size // 2
    
    # 蛇头主体
    draw.ellipse([head_x, head_y, head_x + head_size, head_y + head_size], 
                 fill=(255, 255, 0), outline=(255, 165, 0), width=int(2 * scale))
    
    # 蛇头眼睛
    eye_size = max(2, int(8 * scale))
    eye_color = (255, 255, 255)
    pupil_color = (0, 0, 0)
    
    # 左眼
    left_eye_x = head_x + int(25 * scale)
    left_eye_y = head_y + int(25 * scale)
    if left_eye_x + eye_size > left_eye_x and left_eye_y + eye_size > left_eye_y:
        draw.ellipse([left_eye_x, left_eye_y, left_eye_x + eye_size, left_eye_y + eye_size], 
                     fill=eye_color, outline=(0, 0, 0), width=1)
        pupil_size = max(1, eye_size - 2)
        if left_eye_x + 1 + pupil_size > left_eye_x + 1 and left_eye_y + 1 + pupil_size > left_eye_y + 1:
            draw.ellipse([left_eye_x + 1, left_eye_y + 1, left_eye_x + 1 + pupil_size, left_eye_y + 1 + pupil_size], 
                         fill=pupil_color)
    
    # 右眼
    right_eye_x = head_x + int(47 * scale)
    right_eye_y = head_y + int(25 * scale)
    if right_eye_x + eye_size > right_eye_x and right_eye_y + eye_size > right_eye_y:
        draw.ellipse([right_eye_x, right_eye_y, right_eye_x + eye_size, right_eye_y + eye_size], 
                     fill=eye_color, outline=(0, 0, 0), width=1)
        pupil_size = max(1, eye_size - 2)
        if right_eye_x + 1 + pupil_size > right_eye_x + 1 and right_eye_y + 1 + pupil_size > right_eye_y + 1:
            draw.ellipse([right_eye_x + 1, right_eye_y + 1, right_eye_x + 1 + pupil_size, right_eye_y + 1 + pupil_size], 
                         fill=pupil_color)
    
    # 蛇身 - 黄色圆形
    body_size = int(60 * scale)
    body_x = head_x + int(90 * scale)
    body_y = head_y + int(10 * scale)
    draw.ellipse([body_x, body_y, body_x + body_size, body_y + body_size], 
                 fill=(255, 255, 0), outline=(255, 165, 0), width=int(2 * scale))
    
    # 蛇身装饰点
    dot_size = int(4 * scale)
    dot_color = (0, 100, 0)
    for i in range(3):
        dot_x = body_x + int(15 * scale) + i * int(15 * scale)
        dot_y = body_y + int(20 * scale) + (i % 2) * int(20 * scale)
        draw.ellipse([dot_x, dot_y, dot_x + dot_size, dot_y + dot_size], fill=dot_color)
    
    # 食物 - 红色苹果
    food_size = int(40 * scale)
    food_x = head_x + int(120 * scale)
    food_y = head_y + int(20 * scale)
    
    # 苹果主体
    draw.ellipse([food_x, food_y, food_x + food_size, food_y + food_size], 
                 fill=(231, 76, 60), outline=(192, 57, 43), width=int(2 * scale))
    
    # 苹果高光
    highlight_size = int(12 * scale)
    highlight_x = food_x + int(8 * scale)
    highlight_y = food_y + int(8 * scale)
    draw.ellipse([highlight_x, highlight_y, highlight_x + highlight_size, highlight_y + highlight_size], 
                 fill=(255, 102, 102))
    
    # 苹果柄
    stem_color = (139, 69, 19)
    stem_width = int(3 * scale)
    stem_height = int(8 * scale)
    stem_x = food_x + food_size // 2 - stem_width // 2
    stem_y = food_y - stem_height
    draw.rectangle([stem_x, stem_y, stem_x + stem_width, stem_y + stem_height], fill=stem_color)
    
    # 苹果叶子
    leaf_color = (0, 128, 0)
    leaf_size = int(8 * scale)
    leaf_x = food_x + food_size // 2 + int(5 * scale)
    leaf_y = food_y - int(5 * scale)
    draw.ellipse([leaf_x, leaf_y, leaf_x + leaf_size, leaf_y + leaf_size], fill=leaf_color)
    
    return img

def main():
    """主函数"""
    print("开始生成PWA图标...")
    
    # 创建icons目录
    icons_dir = "icons"
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir)
        print(f"创建目录: {icons_dir}")
    
    # 需要生成的图标尺寸
    sizes = [
        16, 32, 48, 72, 96, 128, 144, 152, 167, 180, 192, 256, 384, 512
    ]
    
    # 生成各种尺寸的图标
    for size in sizes:
        try:
            icon = create_snake_icon(size)
            filename = f"icon-{size}x{size}.png"
            filepath = os.path.join(icons_dir, filename)
            icon.save(filepath, "PNG")
            print(f"✓ 生成图标: {filename}")
        except Exception as e:
            print(f"✗ 生成图标失败 {size}x{size}: {e}")
    
    print("\n所有图标生成完成！")
    print(f"图标保存在: {os.path.abspath(icons_dir)}")
    
    # 显示文件列表
    print("\n生成的文件:")
    for filename in sorted(os.listdir(icons_dir)):
        if filename.endswith('.png'):
            filepath = os.path.join(icons_dir, filename)
            filesize = os.path.getsize(filepath)
            print(f"  {filename} ({filesize} bytes)")

if __name__ == "__main__":
    main() 