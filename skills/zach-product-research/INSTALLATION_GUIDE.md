# zach-product-research 技能安装指南

## ✅ 已完成的安装步骤

### 1. ✅ 克隆仓库
```bash
cd ~/.agents/skills
git clone https://github.com/zach22-1999/amazon-skills.git
```

### 2. ✅ 复制Skill到全局目录
```bash
cp -r ~/.agents/skills/amazon-skills/zach-product-research ~/.claude/skills/
```

### 3. ✅ 创建MCP配置模板
```bash
# 已创建 ~/.mcp.json
```

---

## ⚠️ 需要手动完成的步骤

### 1. 配置Sorftime API Key

**注册Sorftime（新用户有3天免费试用）：**
- 访问：https://www.sorftime.com/
- 注册账号（首次注册有免费额度）
- 在个人中心获取API Key

**配置MCP：**
编辑 `~/.mcp.json`，将 `YOUR_API_KEY` 替换为实际的API Key：

```json
{
  "mcpServers": {
    "sorftime": {
      "type": "sse",
      "url": "https://mcp.sorftime.com/sse?key=你的实际API_KEY"
    }
  }
}
```

### 2. 验证Python依赖

主要依赖：
- `openpyxl` - ✅ 已安装
- `html` - Python标准库
- `json` - Python标准库
- `pathlib` - Python标准库

如需安装：
```bash
pip3 install openpyxl
```

---

## 🚀 使用方法

### 方式1：Skill命令
在Claude Code中输入：
```
/zach-product-research [产品关键词] [站点]

示例：
/zach-product-research bluetooth speaker US
/zach-product-research yoga mat UK
```

### 方式2：自然语言
```
帮我用Sorftime分析一下美国站蓝牙音箱选品机会
```

### 方式3：带约束条件
```
找美国站月销1000+、价格$15-30、评论门槛低的潜力产品
```

---

## 📁 文件结构

```
~/.claude/skills/zach-product-research/
├── SKILL.md                    # 核心技能说明
├── README.md                   # 项目说明
├── scripts/
│   ├── render_deliverables.py  # 交付生成脚本
│   ├── cross_analysis.py       # 交叉分析
│   └── parse_top100_dimensions.py
├── agents/
│   ├── data_pipeline.md         # 数据管道Agent
│   └── insight_writer.md       # 洞察撰写Agent
├── assets/
│   ├── html_report_template.html  # HTML报告模板
│   └── dashboard_template.html    # Dashboard模板
├── references/
│   ├── payload_schema_v2.md      # v2数据包结构
│   └── analysis_patterns.md     # 分析模式参考
└── evals/
    └── evals.json              # 最小自测套件
```

---

## 🔧 脚本使用

### 生成交付物
```bash
cd ~/.claude/skills/zach-product-research/skills/zach-product-research/scripts
python3 render_deliverables.py generate --input payload.json
python3 render_deliverables.py validate --input payload.json
python3 render_deliverables.py all --input payload.json
```

### 解析Top100维度
```bash
python3 parse_top100_dimensions.py
```

### 交叉分析
```bash
python3 cross_analysis.py
```

---

## 📊 输出交付物

### 1. 市场调研报告（Markdown）
- 完整的10章节结构化报告
- 约800行，包含所有分析维度
- 适合详细阅读和存档

### 2. 精简报告（HTML）
- 浏览器直接打开
- 快速浏览关键结论
- 可视化友好

### 3. Dashboard（HTML）
- 交互式数据看板
- 图表 + 评分卡 + 热力图
- 数据可视化分析

### 4. Excel数据文件
- 多Sheet数据表格
- 供逐条核对
- 适合Excel深度分析

### 5. 原始数据包（JSON）
- unified_payload.json
- 可重新生成全部交付物
- v2格式支持chapters结构

---

## ❓ 常见问题

### Q: Claude Code不识别/zach-product-research命令？
**A:** 
1. 确认skill在 `~/.claude/skills/` 目录下
2. 检查文件名：`zach-product-research/SKILL.md`
3. 重启Claude Code让它重新加载技能

### Q: MCP连接不上Sorftime？
**A:**
1. 确认 `.mcp.json` 在正确的位置：
   - 项目根目录（和 `.claude/` 同级）或
   - `~/.claude/` 目录下
2. 检查API Key格式（无多余空格或换行）
3. 重启Claude Code

### Q: 报错找不到Python模块？
**A:**
```bash
pip3 install openpyxl
```

### Q: 没有Claude Code，能用吗？
**A:** 可以。在Coze或Cursor中手动粘贴skill内容，配置MCP后使用降级版。

---

## 📚 学习资源

### 项目文档
- [GitHub仓库](https://github.com/zach22-1999/amazon-skills/tree/main/zach-product-research)
- [项目README](~/.claude/skills/zach-product-research/README.md)
- [技能说明](~/.claude/skills/zach-product-research/SKILL.md)

### Sorftime
- 官网：https://www.sorftime.com/
- 新用户福利：注册后3天免费试用
- 数据源：跨境电商市场数据

---

## 🎯 下一步

### 配置完成后的第一次使用
1. 配置Sorftime API Key到 `~/.mcp.json`
2. 重启Claude Code
3. 测试MCP连接：`你能看到sorftime的工具吗？`
4. 使用skill：`/zach-product-research bluetooth speaker US`

---

## 📞 技术支持

### 遇到问题？
- 查看GitHub Issues：https://github.com/zach22-1999/amazon-skills/issues
- 公众号： Zach的进化笔记
- 交流群：扫描README中的二维码

---

**安装日期**: 2026-04-02
**技能版本**: v2.0
**作者**: Zach22-1999
**许可证**: MIT