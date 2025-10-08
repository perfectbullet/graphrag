import os
import re
import sys
from pathlib import Path


def split_markdown_by_chapters(file_path):
    """
    按一级标题（# 标题）切分markdown文件并保存到以文件名命名的文件夹中

    Args:
        file_path: markdown文件路径
    """

    # 读取文件
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        return
    except Exception as e:
        print(f"错误：读取文件失败 - {e}")
        return

    # 获取文件名（不包含扩展名）
    file_stem = Path(file_path).stem

    # 创建输出文件夹
    output_dir = Path(file_stem)
    output_dir.mkdir(exist_ok=True)

    # 使用正则表达式按一级标题切分
    # 匹配以 # 开头的行（一级标题）
    chapters = re.split(r'^# ', content, flags=re.MULTILINE)

    # 第一个元素通常是标题前的内容（如果有的话）
    if chapters[0].strip() == '':
        chapters = chapters[1:]  # 移除空的第一个元素
    else:
        # 如果第一个元素不是空的，说明文件开头有内容但没有一级标题
        # 保存为前言或序言
        if chapters[0].strip():
            save_chapter(output_dir, "00_前言", chapters[0].strip())
        chapters = chapters[1:]

    # 处理每个章节
    for i, chapter_content in enumerate(chapters, 1):
        if not chapter_content.strip():
            continue

        # 提取标题（第一行）和内容
        lines = chapter_content.split('\n', 1)
        title = lines[0].strip()
        content_body = lines[1] if len(lines) > 1 else ""

        # 清理标题，移除不适合文件名的字符
        safe_title = clean_filename(title)

        # 生成文件名
        filename = f"{i:02d}_{safe_title}"

        # 重新组装完整内容（包含标题）
        full_content = f"# {title}\n{content_body}"

        # 保存章节
        save_chapter(output_dir, filename, full_content)

    print(f"切分完成！共生成 {len(chapters)} 个章节文件，保存在 '{output_dir}' 文件夹中")


def clean_filename(filename):
    """
    清理文件名，移除不适合的字符
    """
    # 移除或替换不适合文件名的字符
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = filename.replace(' ', '_')

    # 限制长度
    if len(filename) > 50:
        filename = filename[:50]

    return filename


def save_chapter(output_dir, filename, content):
    """
    保存章节内容到文件
    """
    file_path = output_dir / f"{filename}.md"
    file_path2 = output_dir / f"{filename}.txt"
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        with open(file_path2, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"已保存：{file_path}")
        print(f"已保存：{file_path2}")
    except Exception as e:
        print(f"错误：保存文件 {file_path} 失败 - {e}")


def main():
    """
    主函数，处理命令行参数
    """
    if len(sys.argv) != 2:
        print("用法: python split_markdown.py <markdown文件路径>")
        print("例如: python split_markdown.py book.md")
        return

    file_path = sys.argv[1]

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        return

    # 检查是否是markdown文件
    if not file_path.lower().endswith(('.md', '.markdown')):
        print("警告：输入文件可能不是markdown格式")

    split_markdown_by_chapters(file_path)


if __name__ == "__main__":
    main()