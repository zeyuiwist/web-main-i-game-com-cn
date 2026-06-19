import json

DEFAULT_SITES = [
    {
        "platform": "爱游戏",
        "url": "https://web-main-i-game.com.cn",
        "tags": ["游戏", "娱乐", "在线平台"],
        "description": "一个专注于提供丰富在线游戏体验的综合平台。"
    },
    {
        "platform": "示例站A",
        "url": "https://example-a.com",
        "tags": ["测试", "演示"],
        "description": "用于展示结构化信息的示例站点。"
    },
    {
        "platform": "示例站B",
        "url": "https://example-b.org",
        "tags": ["案例", "参考"],
        "description": "另一个包含模拟数据的参考站点。"
    }
]

def load_sites(source=None):
    if source:
        with open(source, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_SITES

def generate_summary(site):
    tags_str = ", ".join(site["tags"])
    lines = [
        f"平台名称: {site['platform']}",
        f"访问地址: {site['url']}",
        f"关键词标签: {tags_str}",
        f"简短说明: {site['description']}",
        "---"
    ]
    return "\n".join(lines)

def build_full_summary(sites):
    header = "内置站点结构化摘要\n====================\n"
    body_parts = [generate_summary(s) for s in sites]
    return header + "\n".join(body_parts)

def save_summary(summary_text, output_path="summary_output.txt"):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary_text)

def main():
    sites = load_sites()
    summary = build_full_summary(sites)
    print(summary)
    save_summary(summary)

if __name__ == "__main__":
    main()