#!/usr/bin/env python3
import openpyxl
from datetime import datetime
import subprocess

def load_excel_data(file_path):
    wb = openpyxl.load_workbook(file_path)
    ws = wb['Sheet5']
    
    data = []
    headers = None
    for i, row in enumerate(ws.iter_rows(values_only=True)):
        if i == 0:
            headers = row
            continue
        data.append(row)
    
    return headers, data

def analyze_data(headers, data):
    col_map = {}
    for i, h in enumerate(headers):
        h_str = str(h)
        if '品牌' in h_str:
            col_map['brand'] = i
        elif '本周销量' in h_str:
            col_map['this_week_sales'] = i
        elif '上周销量' in h_str:
            col_map['last_week_sales'] = i
        elif '本周GMV' in h_str:
            col_map['this_week_gmv'] = i
        elif '本周客单价' in h_str:
            col_map['this_week_atv'] = i
        elif '上周客单价' in h_str:
            col_map['last_week_atv'] = i
        elif '商品名称' in h_str:
            col_map['product_name'] = i
        elif '综合动能得分' in h_str:
            col_map['momentum_score'] = i
        elif '一级类目' in h_str:
            col_map['category_l1'] = i
    
    total_this_week = 0
    total_last_week = 0
    total_gmv = 0
    valid_rows = 0
    
    brand_stats = {}
    category_l1_stats = {}
    
    for row in data:
        try:
            this_week_sales = float(row[col_map['this_week_sales']]) if col_map['this_week_sales'] < len(row) else 0
            last_week_sales = float(row[col_map['last_week_sales']]) if col_map['last_week_sales'] < len(row) else 0
            this_week_gmv = float(row[col_map['this_week_gmv']]) if col_map['this_week_gmv'] < len(row) else 0
            
            if col_map['brand'] < len(row):
                brand = row[col_map['brand']]
            else:
                brand = '未知'
            
            if col_map['category_l1'] < len(row):
                category = row[col_map['category_l1']]
            else:
                category = '未知'
            
            if this_week_sales > 0:
                valid_rows += 1
                total_this_week += this_week_sales
                total_last_week += last_week_sales
                total_gmv += this_week_gmv
                
                if brand not in brand_stats:
                    brand_stats[brand] = {'sales': 0, 'gmv': 0, 'count': 0}
                brand_stats[brand]['sales'] += this_week_sales
                brand_stats[brand]['gmv'] += this_week_gmv
                brand_stats[brand]['count'] += 1
                
                if category not in category_l1_stats:
                    category_l1_stats[category] = {'sales': 0, 'count': 0}
                category_l1_stats[category]['sales'] += this_week_sales
                category_l1_stats[category]['count'] += 1
                    
        except:
            continue
    
    top_brands = sorted(brand_stats.items(), key=lambda x: x[1]['sales'], reverse=True)[:10]
    top_categories = sorted(category_l1_stats.items(), key=lambda x: x[1]['sales'], reverse=True)[:10]
    
    growth = 0
    if total_last_week > 0:
        growth = ((total_this_week - total_last_week) / total_last_week) * 100
    
    return {
        'total_this_week': total_this_week,
        'total_last_week': total_last_week,
        'growth': growth,
        'total_gmv': total_gmv,
        'valid_rows': valid_rows,
        'top_brands': top_brands,
        'top_categories': top_categories,
        'brand_stats': brand_stats,
        'category_l1_stats': category_l1_stats
    }

def generate_html(analysis):
    metrics = analysis
    
    lines = []
    lines.append('<!doctype html>')
    lines.append('<html lang="zh-CN">')
    lines.append('<head>')
    lines.append('<meta charset="utf-8">')
    lines.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    lines.append('<title>网红货盘数据Dashboard</title>')
    lines.append('<style>')
    lines.append('    :root {')
    lines.append('      --bg: #f4efe6;')
    lines.append('      --ink: #14212b;')
    lines.append('      --muted: #5f6970;')
    lines.append('      --card: rgba(255, 250, 241, 0.88);')
    lines.append('      --accent: #cb5b2f;')
    lines.append('      --accent-2: #1f7a8c;')
    lines.append('      --accent-3: #8a9447;')
    lines.append('      --accent-4: #7c5c46;')
    lines.append('      --shadow: 0 16px 40px rgba(20, 33, 43, 0.08);')
    lines.append('      --line: #e0e0e0;')
    lines.append('    }')
    lines.append('    * { box-sizing: border-box; }')
    lines.append('    html { scroll-behavior: smooth; }')
    lines.append('    body {')
    lines.append('      margin: 0;')
    lines.append('      font-family: "IBM Plex Sans", "PingFang SC", sans-serif;')
    lines.append('      color: var(--ink);')
    lines.append('      background:')
    lines.append('        radial-gradient(circle at 15% 10%, rgba(203, 91, 47, 0.10), transparent 28%),')
    lines.append('        radial-gradient(circle at 88% 16%, rgba(31, 122, 140, 0.10), transparent 24%),')
    lines.append('        linear-gradient(180deg, #f3eee5 0%, #e8f0ef 52%, #f1eadf 100%);')
    lines.append('      min-height: 100vh;')
    lines.append('    }')
    lines.append('    .page { max-width: 1380px; margin: 0 auto; padding: 28px 22px 56px; }')
    lines.append('    .hero {')
    lines.append('      position: relative;')
    lines.append('      overflow: hidden;')
    lines.append('      background:')
    lines.append('        linear-gradient(135deg, rgba(255,255,255,0.82), rgba(246, 235, 220, 0.92)),')
    lines.append('        radial-gradient(circle at top left, rgba(255,255,255,0.75), transparent 48%);')
    lines.append('        border: 1px solid rgba(187, 168, 143, 0.45);')
    lines.append('      border-radius: 32px;')
    lines.append('      box-shadow: var(--shadow);')
    lines.append('      padding: 30px;')
    lines.append('    }')
    lines.append('    .hero h1 {')
    lines.append('        font-size: 32px; font-weight: 700; margin: 0 20px 0; color: var(--accent-2); }')
    lines.append('    .hero p {')
    lines.append('        font-size: 16px; color: var(--muted); margin: 0;')
    lines.append('    }')
    lines.append('    .metrics { display: grid; grid-template-columns: repeat(2, 1fr); gap: 22px; align-items: start; }')
    lines.append('    .metric-card {')
    lines.append('      background: rgba(255,255,255,0.95);')
    lines.append('      border-radius: 20px;')
    lines.append('      padding: 24px;')
    lines.append('      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.06); }')
    lines.append('    .metric-label { font-size: 14px; color: var(--muted); margin-bottom: 8px; }')
    lines.append('    .metric-value { font-size: 36px; font-weight: 700; color: var(--accent-2); }')
    lines.append('    .trend-up { color: #8a9447; }')
    lines.append('    .trend-down { color: #cb5b2f; }')
    lines.append('    .section { margin: 40px 0; }')
    lines.append('    .section-title {')
    lines.append('      font-size: 24px; font-weight: 700;')
    lines.append('      color: var(--ink);')
    lines.append('      margin-bottom: 24px;')
    lines.append('      display: flex;')
    lines.append('      align-items: center;')
    lines.append('      gap: 12px;')
    lines.append('    }')
    lines.append('    .section-title::after {')
    lines.append('      content: "";')
    lines.append('      flex: 1;')
    lines.append('      height: 3px;')
    lines.append('      background: var(--accent);')
    lines.append('      border-radius: 2px;')
    lines.append('    }')
    lines.append('    .card-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px; margin: 24px 0; }')
    lines.append('    .card {')
    lines.append('      background: var(--card);')
    lines.append('      border-radius: 20px;')
    lines.append('      padding: 24px;')
    lines.append('      transition: transform 0.3s;')
    lines.append('    }')
    lines.append('    .card:hover { transform: translateY(-4px); }')
    lines.append('    .card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }')
    lines.append('    .card-rank { font-size: 14px; color: var(--muted); }')
    lines.append('    .card-title { font-size: 18px; font-weight: 600; }')
    lines.append('    .card-body { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }')
    lines.append('    .card-label { font-size: 14px; color: var(--muted); }')
    lines.append('    .card-value { font-size: 20px; font-weight: 600; color: var(--ink); }')
    lines.append('    .chart-container {')
    lines.append('      background: var(--card);')
    lines.append('      border-radius: 20px;')
    lines.append('      padding: 30px;')
    lines.append('      margin: 24px 0;')
    lines.append('      height: 400px;')
    lines.append('      display: flex;')
    lines.append('      align-items: center;')
    lines.append('      justify-content: center;')
    lines.append('    }')
    lines.append('    </style>')
    lines.append('</head>')
    lines.append('<body>')
    lines.append('<div class="page">')
    
    # Hero
    lines.append('  <div class="hero">')
    lines.append('    <h1 style="font-size: 32px; font-weight: 700; margin: 0 20px 0; color: var(--accent-2);">')
    lines.append('      网红货盘数据Dashboard')
    lines.append('    </h1>')
    lines.append('    <p style="font-size: 16px; color: var(--muted); margin: 0;">')
    lines.append('      数据来源: 潮红货盘POC-3.16 | 生成时间: ' + datetime.now().strftime('%Y-%m-%d %H:%M'))
    lines.append('    </p>')
    lines.append('  </div>')
    
    # 总体指标
    lines.append('  <div class="section">')
    lines.append('    <div class="section-title">总体指标</div>')
    lines.append('    <div class="metrics">')
    
    sales_growth = metrics['growth']
    growth_class = 'trend-up' if sales_growth >= 0 else 'trend-down'
    growth_symbol = '+' if sales_growth >= 0 else ''
    
    lines.append('      <div class="metric-card">')
    lines.append('          <div class="metric-label">本周销量</div>')
    lines.append('          <div class="metric-value">' + str(int(metrics['total_this_week'])) + '</div>')
    lines.append('      </div>')
    lines.append('      <div class="metric-card">')
    lines.append('          <div class="metric-label">上周销量</div>')
    lines.append('          <div class="metric-value">' + str(int(metrics['total_last_week'])) + '</div>')
    lines.append('      </div>')
    lines.append('      <div class="metric-card">')
    lines.append('          <div class="metric-label">环比增长</div>')
    lines.append('          <div class="metric-value ' + growth_class + '">')
    lines.append('          ' + growth_symbol + '{:.1f}%</div>'.format(abs(sales_growth)))
    lines.append('      </div>')
    lines.append('      <div class="metric-card">')
    lines.append('          <div class="metric-label">本周GMV</div>')
    lines.append('          <div class="metric-value">¥' + str(int(metrics['total_gmv'])) + '</div>')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('  </div>')
    
    # Top 10 品牌
    lines.append('  <div class="section">')
    lines.append('    <div class="section-title">TOP 10 品牌</div>')
    lines.append('    <div class="card-grid">')
    
    for idx, (brand, stats) in enumerate(metrics['top_brands']):
        lines.append('      <div class="card">')
        lines.append('        <div class="card-header">')
        lines.append('          <div class="card-rank">#' + str(idx + 1) + '</div>')
        lines.append('          <div class="card-title">' + brand + '</div>')
        lines.append('        </div>')
        lines.append('        <div class="card-body">')
        lines.append('          <div class="card-label">本周销量</div>')
        lines.append('          <div class="card-value">' + str(int(stats['sales'])) + '</div>')
        lines.append('          <div class="card-label">GMV</div>')
        lines.append('          <div class="card-value">¥' + str(int(stats['gmv'])) + '</div>')
        lines.append('        </div>')
        lines.append('      </div>')
    
    lines.append('    </div>')
    lines.append('  </div>')
    
    # Top 10 类目
    lines.append('  <div class="section">')
    lines.append('    <div class="section-title">TOP 10 类目</div>')
    lines.append('    <div class="card-grid">')
    
    for idx, (category, stats) in enumerate(metrics['top_categories']):
        lines.append('      <div class="card">')
        lines.append('        <div class="card-header">')
        lines.append('          <div class="card-rank">#' + str(idx + 1) + '</div>')
        lines.append('          <div class="card-title">' + category + '</div>')
        lines.append('        </div>')
        lines.append('        <div class="card-body">')
        lines.append('          <div class="card-label">本周销量</div>')
        lines.append('          <div class="card-value">' + str(int(stats['sales'])) + '</div>')
        lines.append('          <div class="card-label">商品数</div>')
        lines.append('          <div class="card-value">' + str(stats['count']) + '</div>')
        lines.append('        </div>')
        lines.append('      </div>')
    
    lines.append('    </div>')
    lines.append('  </div>')
    
    # 数据概览
    lines.append('  <div class="section">')
    lines.append('    <div class="section-title">数据概览</div>')
    lines.append('    <div class="chart-container">')
    lines.append('      <div style="text-align: center; color: var(--muted);">')
    lines.append('        <div style="font-size: 20px; margin-bottom: 20px;">使用Excel原始数据生成图表</div>')
    lines.append('        <div style="font-size: 14px; margin-top: 20px;">' + str(metrics['valid_rows']) + ' 行有效数据</div>')
    lines.append('        <div style="font-size: 14px; margin-top: 10px;">' + str(len(metrics['top_brands'])) + ' 个品牌</div>')
    lines.append('      </div>')
    lines.append('    </div>')
    lines.append('  </div>')
    
    lines.append('    <div style="text-align: center; padding: 40px; color: var(--muted);">')
    lines.append('      <p>数据分析 Dashboard - 潮红货盘POC-3.16</p>')
    lines.append('      <p>生成时间: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '</p>')
    lines.append('    </div>')
    lines.append('</div>')
    lines.append('</body>')
    lines.append('</html>')
    
    return '\n'.join(lines)

def main():
    excel_path = "/Users/yinmeichao.1/Downloads/Documents/Excel/网红货盘poc-3.16（保密数据）.xlsx"
    output_path = "/Users/yinmeichao.1/Downloads/Documents/Excel/网红货盘Dashboard.html"
    
    print("开始生成Dashboard...")
    print("Excel文件: " + excel_path)
    
    headers, data = load_excel_data(excel_path)
    print("数据行数: " + str(len(data)))
    
    analysis = analyze_data(headers, data)
    
    print("\n总体指标:")
    print("  本周销量: " + str(int(analysis['total_this_week'])))
    print("  上周销量: " + str(int(analysis['total_last_week'])))
    print("  环比增长: " + "{:.1f}".format(analysis['growth']) + "%")
    print("  本周GMV: ¥" + str(int(analysis['total_gmv'])))
    print("  有效数据: " + str(analysis['valid_rows']) + " 行")
    
    print("\nTOP 10 品牌:")
    for i, (brand, stats) in enumerate(analysis['top_brands']):
        print("  " + str(i+1) + ". " + brand + ": " + str(stats['sales']) + " 销量")
    
    print("\n生成HTML...")
    html = generate_html(analysis)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print("已完成!")
    print("输出文件: " + output_path)
    
    subprocess.run(['open', output_path])

if __name__ == '__main__':
    main()
