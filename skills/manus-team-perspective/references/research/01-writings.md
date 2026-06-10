# Manus团队 - 著作与系统性思考

## 核心哲学与自创术语

### "Less Structure, More Intelligence"（少结构，多智能）
- Manus的核心产品哲学，出现在官网首页和所有产品定位中
- 含义：不过度设计工作流和规则，让AI的智能来驱动执行
- 与传统SaaS的"多功能多配置"形成鲜明对比

### "Mens et Manus"（脑与手）
- 名字来源：MIT校训"手脑并用"
- 哲学含义："Others have built the brain for AI to think, Manus is building the hands for AI to do."（别人建了大脑让AI思考，Manus建了双手让AI执行）
- 产品定位从"chat"（对话）转向"act"（行动）

### "Action Engine for Life"
- 产品定位："We build general AI agents as the Action Engine for life."
- 不是copilot（副驾驶），不是assistant（助手），是engine（引擎）

### "We don't want overachieving AI, we want overachieving Humans"
- 核心价值观：AI的目标不是替代人，而是让人超越自己
- "To extend human reach by giving everyone the code to leverage their life."

### "Stochastic Graduate Descent"（随机梯度下降的玩笑版）
- 季逸超自创术语，描述团队的开发方法：架构搜索+prompt调试+经验猜测
- 含义：不是科学规划出来的，是试出来的
- 团队重建了4次agent框架才找到正确方向

### Context Engineering（上下文工程）
- 季逸超2025年7月18日发表长文《Context Engineering for AI Agents: Lessons from Building Manus》
- 核心论点：上下文工程是AI Agent系统最关键的工程学科
- 6条核心经验：
  1. **围绕KV-Cache设计**：KV-cache命中率是生产级AI Agent最重要的单一指标
  2. **Mask而非Remove**：不删除工具定义，而是通过logit masking控制可用操作
  3. **用文件系统作为上下文**：文件系统是"无限的、持久的、agent可直接操作的"外部记忆
  4. **通过复述操纵注意力**：todo.md不是装饰，是注意力机制——把目标推到context尾部
  5. **保留错误信息**："Erasing failure removes evidence. And without evidence, the model can't adapt."
  6. **不要被Few-Shot绑架**：上下文越统一，agent越脆弱；需要结构化变化

### "If model progress is the rising tide, we want Manus to be the boat, not the pillar stuck to the seabed."
- 季逸超的核心比喻：模型进步是涨潮，Manus要做船而不是海底的柱子
- 这解释了为什么不训练自有模型，而是选择context engineering路线
- 保持模型无关性（model-agnostic），随模型进步而自动受益

## 产品哲学体系

### 1. 通用Agent > 专用工具
- 反对为每个任务建专用工具，主张一个通用agent覆盖所有
- Wide Research架构：不用专用研究工具，而是派生多个通用子agent并行工作
- "The only real limit is your imagination."

### 2. 并行架构 > 更大上下文窗口
- Wide Research文章核心论点：扩展上下文窗口无法解决规模化问题
- 4个原因：上下文衰减不是二元的、处理成本指数增长、认知负载、训练数据偏向短对话
- 解决方案：并行子agent架构，每个子agent有独立的全新context window
- "The 50th item is researched just as thoroughly as the first"

### 3. 文件系统作为记忆 > 上下文压缩
- 不做aggressive truncation或compression——信息丢失不可逆
- 用文件系统做外部记忆：按需读写，持久化存储
- 压缩必须是可恢复的：保留URL可丢弃网页内容，保留文件路径可丢弃文档内容

### 4. 开放标准 > 封闭生态
- 支持Agent Skills开放标准（Anthropic提出）
- 支持MCP协议
- "MCP提供标准化的数据管道，Skills提供操作手册"
- Skills vs MCP互补而非竞争

### 5. 渐进式披露 > 一次性加载
- Skills的三级加载设计：Metadata→Instructions→Resources
- 极低上下文成本启动（~100 tokens/Skill），按需加载详细内容
- 设计哲学：不在agent不需要时浪费context

## 创始人背景与思想来源

### 肖翼（Xiao Hong / Red）
- 2022年创立Butterfly Effect，比ChatGPT公开发布早两个月
- 之前做了Monica（ChatGPT浏览器扩展）
- 拒绝了字节跳动约3000万美元的收购提议（2024年）
- 拒绝了中国地方政府的投资，担心"国内政府关联会在西方市场引发审查"
- 名言："Joining Meta allows us to build on a stronger, more sustainable foundation without changing how Manus works or how decisions are made."

### 季逸超（Ji Yichao / Peak）
- 1992年出生，在科罗拉多和北京长大
- 高中时开发Mammoth Browser（iPhone浏览器）
- 2012年创立Peak Labs，获真格基金和红杉中国投资
- 2012-2013年登上福布斯中国30 Under 30
- NLP领域出身，BERT时代就开始做NLP
- 之前的创业公司从零训练模型做开放信息抽取和语义搜索，但被GPT-3一夜淘汰
- 这段经历深刻影响了Manus的技术路线选择：不做模型训练，做context engineering

### 张涛（Zhang Tao / Pan）
- 产品总监，联合创始人
- 在Microsoft合作公告中被提及："Our goal has always been to help more users experience Manus and complete their work faster."

## 产品演进逻辑

1. **Monica**（2023）→ 浏览器扩展，聚合多个LLM，做翻译/摘要/写作
2. **Manus**（2025.3）→ 通用AI Agent，从聊天到行动
3. **Manus 1.5**（2025.10）→ 全栈web应用开发，4x速度提升
4. **Wide Research**（2025.7）→ 并行子agent架构
5. **Manus 1.6**（2025.12）→ 移动端开发、设计视图
6. **加入Meta**（2025.12）→ 从创业公司到大公司平台

信息来源：manus.im官网、Wikipedia、季逸超技术博客、Manus官方博客
可信度：一手来源（官网、官方博客）+ 权威二手来源（Wikipedia）
