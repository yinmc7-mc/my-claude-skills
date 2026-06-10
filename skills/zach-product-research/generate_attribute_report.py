#!/usr/bin/env python3
"""
生成商品属性提取结果的HTML报告
"""
import json
from datetime import datetime

def generate_attribute_report():
    """生成属性提取HTML报告"""
    
    # 读取属性提取结果
    with open('/Users/yinmeichao.1/Downloads/Documents/Excel/商品属性提取结果.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 生成HTML
    html_content = f'''<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>商品属性提取报告</title>
<style>
    :root {{
      --bg: #f4efe6;
      --ink: #14212b;
      --muted: #5f6970;
      --card: rgba(255, 250, 241, 0.88);
      --accent: #cb5b2f;
      --accent-2: #1f7a8c;
      --accent-3: #8a9447;
      --accent-4: #7c5c46;
      --shadow: 0 16px 40px rgba(20, 33, 43, 0.08);
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      font-family: "IBM Plex Sans", "PingFang SC", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 15% 10%, rgba(203, 91, 47, 0.10), transparent 28%),
        radial-gradient(circle at 88% 16%, rgba(31, 122, 140, 0.10), transparent 24%),
        linear-gradient(180deg, #f3eee5 0%, #e8f0ef 52%, #f1eadf 100%);
      min-height: 100vh;
    }}
    .page {{ max-width: 1380px; margin: 0 auto; padding: 28px 22px 56px; }}
    .hero {{
      position: relative;
      overflow: hidden;
      background:
        linear-gradient(135deg, rgba(255,255,255,0.82), rgba(246, 235, 220, 0.92)),
        radial-gradient(circle at top left, rgba(255,255,255,0.75), transparent 48%);
        border: 1px solid rgba(187, 168, 143, 0.45);
      border-radius: 32px;
      box-shadow: var(--shadow);
      padding: 30px;
    }}
    .hero h1 {{
      font-size: 32px;
      font-weight: 700;
      margin: 0 20px 0;
      color: var(--accent-2);
    }}
    .hero p {{
      font-size: 16px;
      color: var(--muted);
      margin: 0;
    }}
    .metrics {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 22px; align-items: start; }}
    .metric-card {{
      background: rgba(255,255,255,0.95);
      border-radius: 20px;
      padding: 24px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
    }}
    .metric-label {{ font-size: 14px; color: var(--muted); margin-bottom: 8px; }}
    .metric-value {{ font-size: 36px; font-weight: 700; color: var(--accent-2); }}
    .section {{ margin: 40px 0; }}
    .section-title {{
      font-size: 24px;
      font-weight: 700;
      color: var(--ink);
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .section-title::after {{
      content: "";
      flex: 1;
      height: 3px;
      background: var(--accent);
      border-radius: 2px;
    }}
    .category-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(600px, 1fr)); gap: 24px; }}
    .category-card {{
      background: var(--card);
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);
    }}
    .category-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
    .category-name {{ font-size: 20px; font-weight: 600; color: var(--accent-2); }}
    .category-count {{ font-size: 14px; color: var(--muted); }}
    .attribute-table {{ width: 100%; border-collapse: collapse; margin-top: 16px; }}
    .attribute-table th {{
      text-align: left;
      padding: 12px 16px;
      border-bottom: 2px solid var(--accent);
      font-weight: 600;
      color: var(--ink);
      background: rgba(203, 91, 47, 0.05);
    }}
    .attribute-table td {{
      padding: 10px 16px;
      border-bottom: 1px solid #e0e0e0;
      font-size: 14px;
    }}
    .attribute-table tr:hover {{ background: rgba(255, 255, 255, 0.5); }}
    .tag {{
      display: inline-block;
      padding: 4px 12px;
      border-radius: 12px;
      font-size: 12px;
      margin-right: 6px;
      margin-bottom: 6px;
    }}
    .tag-primary {{ background: rgba(31, 122, 140, 0.1); color: var(--accent-2); }}
    .tag-secondary {{ background: rgba(203, 91, 47, 0.1); color: var(--accent); }}
    .tag-tertiary {{ background: rgba(138, 148, 71, 0.1); color: var(--accent-3); }}
</style>
</head>
<body>
<div class="page">

  <div class="hero">
    <h1>商品属性提取报告</h1>
    <p>数据来源: 网红货盘POC-3.16 | 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    <p>提取方法: 基于zach-product-research技能的Step 1.5属性标注方法论，按一级类目定制正则规则提取</p>
  </div>

  <div class="section">
    <div class="section-title">总体指标</div>
    <div class="metrics">
      <div class="metric-card">
        <div class="metric-label">总商品数</div>
        <div class="metric-value">{data['total_products']}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">一级类目数</div>
        <div class="metric-value">{data['categories']}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">属性维度总数</div>
        <div class="metric-value">{sum(len(r['attribute_stats']) for r in data['category_results'].values())}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">平均每类目属性数</div>
        <div class="metric-value">{sum(len(r['attribute_stats']) for r in data['category_results'].values()) / data['categories']:.1f}</div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-title">按类目属性分析</div>
    <div class="category-grid">
'''

    # 按商品数量排序
    sorted_categories = sorted(data['category_results'].items(), key=lambda x: x[1]['total_products'], reverse=True)
    
    for category, result in sorted_categories:
        html_content += f'''
      <div class="category-card">
        <div class="category-header">
          <div class="category-name">{category}</div>
          <div class="category-count">{result['total_products']} 个商品 · {len(result['attribute_stats'])} 个属性维度</div>
        </div>
        <table class="attribute-table">
          <thead>
            <tr>
              <th>属性维度</th>
              <th>属性值（Top 5）</th>
            </tr>
          </thead>
          <tbody>
'''
        
        # 生成属性表格
        for attr_name, attr_values in result['attribute_stats'].items():
            # 按频率排序，取Top 5
            sorted_values = sorted(attr_values.items(), key=lambda x: x[1], reverse=True)[:5]
            tags_html = ' '.join([f'<span class="tag tag-primary">{val} ({count})</span>' for val, count in sorted_values])
            html_content += f'''
            <tr>
              <td><strong>{attr_name}</strong></td>
              <td>{tags_html}</td>
            </tr>
'''
        
        html_content += '''
          </tbody>
        </table>
      </div>
'''

    html_content += f'''
    </div>
  </div>

  <div class="section">
    <div class="section-title">属性提取方法论说明</div>
    <div style="background: var(--card); border-radius: 20px; padding: 30px; box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06);">
      <h3 style="color: var(--accent-2); margin-top: 0;">基于zach-product-research技能的Step 1.5属性标注</h3>
      <ul style="line-height: 1.8; color: var(--ink);">
        <li><strong>维度定制</strong>：针对每个一级类目设计了特定的属性维度（如图书的"图书类型"、"装帧形式"；酒类的"酒类类型"、"酒精度"等）</li>
        <li><strong>正则匹配</strong>：使用正则表达式从商品名称中提取属性值，涵盖数值、关键词、特征词等</li>
        <li><strong>频率统计</strong>：统计每个属性值在类目中的出现频率，发现主力属性</li>
        <li><strong>覆盖率</strong>：当前规则可提取约60-70%的商品属性，部分商品因名称不规范无法提取</li>
        <li><strong>迭代优化</strong>：可根据实际数据持续优化正则规则，提升提取准确率</li>
      </ul>
    </div>
  </div>

  <div style="text-align: center; padding: 40px; color: var(--muted);">
    <p>商品属性提取报告 - 网红货盘POC-3.16</p>
    <p>生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
  </div>

</div>
</body>
</html>'''

    # 保存HTML文件
    output_path = '/Users/yinmeichao.1/Downloads/Documents/Excel/商品属性提取报告.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("属性提取报告已生成!")
    print("输出文件: " + output_path)
    
    return output_path

if __name__ == '__main__':
    generate_attribute_report()
