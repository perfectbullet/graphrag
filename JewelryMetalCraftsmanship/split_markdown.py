import os
import re
import sys
from pathlib import Path


def split_markdown_by_chapters(file_path):
    """
    按 '# 第X章' 格式切分markdown文件并保存到以文件名命名的文件夹中

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

    # 使用正则表达式按 '# 第X章' 格式切分
    # 匹配 # 第数字章 或 # 第数字+中文数字章
    chapter_pattern = r'^# 第\d+章'
    chapters = re.split(chapter_pattern, content, flags=re.MULTILINE)

    # 查找所有章节标题
    chapter_titles = re.findall(chapter_pattern, content, flags=re.MULTILINE)

    # 处理第一部分（章节前的内容）
    if chapters[0].strip():
        save_chapter(output_dir, "00_前言", chapters[0].strip())
        chapters = chapters[1:]  # 移除第一个元素
    else:
        chapters = chapters[1:]  # 移除空的第一个元素

    # 检查章节数量是否匹配
    if len(chapters) != len(chapter_titles):
        print(f"警告：章节内容数量({len(chapters)}) 与标题数量({len(chapter_titles)}) 不匹配")

    # 处理每个章节
    for i, (title, chapter_content) in enumerate(zip(chapter_titles, chapters)):
        if not chapter_content.strip():
            continue

        # 提取章节号
        chapter_num_match = re.search(r'第(\d+)章', title)
        if chapter_num_match:
            chapter_num = chapter_num_match.group(1)
        else:
            chapter_num = str(i + 1).zfill(2)

        # 生成文件名
        filename = f"{chapter_num.zfill(2)}_{title.replace('# ', '')}"

        # 重新组装完整内容（包含标题）
        full_content = f"{title}\n{chapter_content}"

        # 保存章节
        save_chapter(output_dir, filename, full_content)

    print(f"切分完成！共生成 {len(chapter_titles)} 个章节文件，保存在 '{output_dir}' 文件夹中")


def save_chapter(output_dir, filename, content):
    """
    保存章节内容到文件
    """
    # 清理文件名
    filename = clean_filename(filename)
    file_path = output_dir / f"{filename}.txt"

    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        print(f"已保存：{file_path}")
    except Exception as e:
        print(f"错误：保存文件 {file_path} 失败 - {e}")


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


def preview_chapters(file_path):
    """
    预览将要切分的章节
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return

    # 查找所有章节标题
    chapter_pattern = r'^# 第\d+章.*?$'
    chapter_titles = re.findall(chapter_pattern, content, flags=re.MULTILINE)

    print(f"找到 {len(chapter_titles)} 个章节：")
    for i, title in enumerate(chapter_titles, 1):
        print(f"  {i}. {title}")
    print()


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

    # 预览章节
    preview_chapters(file_path)

    # 确认是否继续
    response = input("是否继续切分文件？(y/n): ").lower()
    if response != 'y' and response != 'yes':
        print("操作已取消")
        return

    split_markdown_by_chapters(file_path)


if __name__ == "__main__":
    main()