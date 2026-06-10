#!/usr/bin/env python3
"""
按品类从商品名称中提取属性
参考 zach-product-research 技能的 Step 1.5 属性标注方法论
"""
import openpyxl
import json
from collections import defaultdict
import re
from datetime import datetime

class AttributeExtractor:
    def __init__(self):
        self.extraction_rules = self._build_extraction_rules()
    
    def _build_extraction_rules(self):
        """为每个一级类目构建属性提取规则"""
        return {
            '图书': {
                'attributes': [
                    {
                        'name': '图书类型',
                        'patterns': [
                            (r'小说', '小说'),
                            (r'散文', '散文'),
                            (r'诗歌', '诗歌'),
                            (r'传记', '传记'),
                            (r'历史', '历史'),
                            (r'科普', '科普'),
                            (r'育儿', '育儿'),
                            (r'儿童', '儿童'),
                            (r'绘本', '绘本'),
                            (r'教辅', '教辅'),
                            (r'漫画', '漫画'),
                            (r'励志', '励志'),
                            (r'心理', '心理'),
                            (r'管理', '管理'),
                            (r'哲学', '哲学'),
                        ]
                    },
                    {
                        'name': '适用年龄',
                        'patterns': [
                            (r'0-3岁', '0-3岁'),
                            (r'3-6岁', '3-6岁'),
                            (r'6-12岁', '6-12岁'),
                            (r'12-18岁', '12-18岁'),
                            (r'成人', '成人'),
                        ]
                    },
                    {
                        'name': '装帧形式',
                        'patterns': [
                            (r'精装', '精装'),
                            (r'平装', '平装'),
                            (r'盒装', '盒装'),
                            (r'套装', '套装'),
                            (r'单册', '单册'),
                        ]
                    },
                    {
                        'name': '出版社',
                        'patterns': [
                            (r'中信出版社', '中信出版社'),
                            (r'人民文学出版社', '人民文学出版社'),
                            (r'商务印书馆', '商务印书馆'),
                            (r'中华书局', '中华书局'),
                            (r'上海译文', '上海译文'),
                            (r'三联书店', '三联书店'),
                        ]
                    },
                ]
            },
            '休闲食品': {
                'attributes': [
                    {
                        'name': '食品类型',
                        'patterns': [
                            (r'饼干', '饼干'),
                            (r'巧克力', '巧克力'),
                            (r'糖果', '糖果'),
                            (r'坚果', '坚果'),
                            (r'膨化', '膨化'),
                            (r'蜜饯', '蜜饯'),
                            (r'肉脯', '肉脯'),
                            (r'海苔', '海苔'),
                            (r'果冻', '果冻'),
                            (r'薯片', '薯片'),
                            (r'麻花', '麻花'),
                            (r'糕点', '糕点'),
                        ]
                    },
                    {
                        'name': '口味',
                        'patterns': [
                            (r'原味', '原味'),
                            (r'辣', '辣味'),
                            (r'甜', '甜味'),
                            (r'咸', '咸味'),
                            (r'海苔', '海苔味'),
                            (r'奶油', '奶油味'),
                            (r'焦糖', '焦糖味'),
                            (r'芝士', '芝士味'),
                            (r'黄油', '黄油味'),
                            (r'五香', '五香'),
                            (r'麻辣', '麻辣'),
                        ]
                    },
                    {
                        'name': '包装规格',
                        'patterns': [
                            (r'(\d+)[g克]', 'g'),
                            (r'(\d+)[kK][g克]', 'kg'),
                            (r'盒装', '盒装'),
                            (r'袋装', '袋装'),
                            (r'独立包装', '独立包装'),
                            (r'散装', '散装'),
                        ]
                    },
                ]
            },
            '运动户外': {
                'attributes': [
                    {
                        'name': '运动类型',
                        'patterns': [
                            (r'瑜伽', '瑜伽'),
                            (r'跑步', '跑步'),
                            (r'健身', '健身'),
                            (r'骑行', '骑行'),
                            (r'游泳', '游泳'),
                            (r'登山', '登山'),
                            (r'徒步', '徒步'),
                            (r'露营', '露营'),
                            (r'滑雪', '滑雪'),
                            (r'篮球', '篮球'),
                            (r'足球', '足球'),
                            (r'羽毛球', '羽毛球'),
                            (r'乒乓球', '乒乓球'),
                        ]
                    },
                    {
                        'name': '产品类型',
                        'patterns': [
                            (r'鞋', '鞋'),
                            (r'服', '服装'),
                            (r'配件', '配件'),
                            (r'装备', '装备'),
                            (r'器械', '器械'),
                            (r'垫子', '垫子'),
                            (r'球', '球类'),
                        ]
                    },
                    {
                        'name': '性别',
                        'patterns': [
                            (r'男款', '男款'),
                            (r'女款', '女款'),
                            (r'儿童', '儿童'),
                            (r'成人', '成人'),
                            (r'通用', '通用'),
                        ]
                    },
                    {
                        'name': '尺码',
                        'patterns': [
                            (r'[Ss][Mm]', 'SM'),
                            (r'[Mm]', 'M'),
                            (r'[Ll]', 'L'),
                            (r'[Xx][Ll]', 'XL'),
                            (r'(\d+)码', '码'),
                        ]
                    },
                ]
            },
            '酒类': {
                'attributes': [
                    {
                        'name': '酒类类型',
                        'patterns': [
                            (r'白酒', '白酒'),
                            (r'红酒', '红酒'),
                            (r'啤酒', '啤酒'),
                            (r'黄酒', '黄酒'),
                            (r'果酒', '果酒'),
                            (r'起泡酒', '起泡酒'),
                            (r'威士忌', '威士忌'),
                            (r'伏特加', '伏特加'),
                            (r'白兰地', '白兰地'),
                        ]
                    },
                    {
                        'name': '酒精度',
                        'patterns': [
                            (r'(\d+)[°度]', '度'),
                        ]
                    },
                    {
                        'name': '容量',
                        'patterns': [
                            (r'(\d+)[mM][lL]', 'ml'),
                            (r'(\d+)[lL]', 'L'),
                            (r'(\d+)[kK][lL]', 'kl'),
                        ]
                    },
                    {
                        'name': '产地',
                        'patterns': [
                            (r'法国', '法国'),
                            (r'意大利', '意大利'),
                            (r'智利', '智利'),
                            (r'澳大利亚', '澳大利亚'),
                            (r'美国', '美国'),
                            (r'西班牙', '西班牙'),
                            (r'贵州', '贵州'),
                            (r'四川', '四川'),
                            (r'山西', '山西'),
                        ]
                    },
                ]
            },
            '家居饰品': {
                'attributes': [
                    {
                        'name': '饰品类型',
                        'patterns': [
                            (r'花瓶', '花瓶'),
                            (r'摆件', '摆件'),
                            (r'装饰画', '装饰画'),
                            (r'台灯', '台灯'),
                            (r'落地灯', '落地灯'),
                            (r'挂钟', '挂钟'),
                            (r'烛台', '烛台'),
                            (r'镜子', '镜子'),
                            (r'香薰', '香薰'),
                            (r'地毯', '地毯'),
                        ]
                    },
                    {
                        'name': '材质',
                        'patterns': [
                            (r'陶瓷', '陶瓷'),
                            (r'玻璃', '玻璃'),
                            (r'金属', '金属'),
                            (r'木质', '木质'),
                            (r'树脂', '树脂'),
                            (r'水晶', '水晶'),
                            (r'布艺', '布艺'),
                            (r'亚克力', '亚克力'),
                        ]
                    },
                    {
                        'name': '风格',
                        'patterns': [
                            (r'北欧', '北欧'),
                            (r'现代', '现代'),
                            (r'简约', '简约'),
                            (r'复古', '复古'),
                            (r'中式', '中式'),
                            (r'欧式', '欧式'),
                            (r'美式', '美式'),
                            (r'工业风', '工业风'),
                            (r'日式', '日式'),
                            (r'轻奢', '轻奢'),
                        ]
                    },
                    {
                        'name': '颜色',
                        'patterns': [
                            (r'金色', '金色'),
                            (r'银色', '银色'),
                            (r'黑色', '黑色'),
                            (r'白色', '白色'),
                            (r'灰色', '灰色'),
                            (r'蓝色', '蓝色'),
                            (r'绿色', '绿色'),
                            (r'红色', '红色'),
                            (r'透明', '透明'),
                        ]
                    },
                ]
            },
            '宠物生活': {
                'attributes': [
                    {
                        'name': '宠物类型',
                        'patterns': [
                            (r'猫', '猫咪'),
                            (r'狗', '狗狗'),
                            (r'犬', '狗狗'),
                            (r'通用', '通用'),
                        ]
                    },
                    {
                        'name': '用品类型',
                        'patterns': [
                            (r'猫砂', '猫砂'),
                            (r'猫粮', '猫粮'),
                            (r'狗粮', '狗粮'),
                            (r'玩具', '玩具'),
                            (r'窝', '窝/垫'),
                            (r'垫', '窝/垫'),
                            (r'牵引绳', '牵引绳'),
                            (r'项圈', '项圈'),
                            (r'碗', '食具'),
                            (r'笼子', '笼子'),
                            (r'航空箱', '航空箱'),
                            (r'衣服', '衣服'),
                        ]
                    },
                    {
                        'name': '适用阶段',
                        'patterns': [
                            (r'幼', '幼宠'),
                            (r'成', '成宠'),
                            (r'全', '全阶段'),
                            (r'老年', '老年'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)[kK][g克]', 'kg'),
                            (r'(\d+)[gG]', 'g'),
                            (r'(\d+)[lL]', 'L'),
                            (r'小号', '小号'),
                            (r'中号', '中号'),
                            (r'大号', '大号'),
                        ]
                    },
                ]
            },
            '美妆护肤': {
                'attributes': [
                    {
                        'name': '产品类型',
                        'patterns': [
                            (r'面膜', '面膜'),
                            (r'精华', '精华'),
                            (r'乳液', '乳液'),
                            (r'面霜', '面霜'),
                            (r'爽肤水', '爽肤水'),
                            (r'卸妆', '卸妆'),
                            (r'口红', '口红'),
                            (r'粉底', '粉底'),
                            (r'眼霜', '眼霜'),
                            (r'防晒', '防晒'),
                            (r'化妆水', '化妆水'),
                            (r'眼影', '眼影'),
                        ]
                    },
                    {
                        'name': '功效',
                        'patterns': [
                            (r'保湿', '保湿'),
                            (r'美白', '美白'),
                            (r'抗衰老', '抗衰老'),
                            (r'祛痘', '祛痘'),
                            (r'紧致', '紧致'),
                            (r'修护', '修护'),
                            (r'提亮', '提亮'),
                            (r'舒缓', '舒缓'),
                            (r'控油', '控油'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)[mM][lL]', 'ml'),
                            (r'(\d+)[gG]', 'g'),
                            (r'(\d+)片', '片'),
                            (r'(\d+)片装', '片装'),
                            (r'(\d+)入', '入'),
                        ]
                    },
                    {
                        'name': '适用肤质',
                        'patterns': [
                            (r'干性', '干性'),
                            (r'油性', '油性'),
                            (r'混合', '混合'),
                            (r'敏感', '敏感'),
                            (r'通用', '通用'),
                        ]
                    },
                ]
            },
            '居家布艺': {
                'attributes': [
                    {
                        'name': '布艺类型',
                        'patterns': [
                            (r'窗帘', '窗帘'),
                            (r'床单', '床单'),
                            (r'被套', '被套'),
                            (r'枕头', '枕头'),
                            (r'靠垫', '靠垫'),
                            (r'桌布', '桌布'),
                            (r'地毯', '地毯'),
                            (r'浴巾', '浴巾'),
                            (r'毛巾', '毛巾'),
                            (r'四件套', '四件套'),
                        ]
                    },
                    {
                        'name': '材质',
                        'patterns': [
                            (r'棉', '棉'),
                            (r'亚麻', '亚麻'),
                            (r'丝绸', '丝绸'),
                            (r'聚酯纤维', '聚酯纤维'),
                            (r'竹纤维', '竹纤维'),
                            (r'天丝', '天丝'),
                            (r'羊毛', '羊毛'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'1\.*5米', '1.5米床'),
                            (r'1\.*8米', '1.8米床'),
                            (r'2米', '2.0米床'),
                            (r'1\.2m', '1.2m'),
                            (r'1\.5m', '1.5m'),
                            (r'1\.8m', '1.8m'),
                            (r'2\.0m', '2.0m'),
                            (r'(\d+)[x×](\d+)', 'x'),
                        ]
                    },
                    {
                        'name': '风格',
                        'patterns': [
                            (r'北欧', '北欧'),
                            (r'简约', '简约'),
                            (r'现代', '现代'),
                            (r'中式', '中式'),
                            (r'欧式', '欧式'),
                            (r'ins', 'ins风'),
                            (r'ins风', 'ins风'),
                        ]
                    },
                ]
            },
            '水饮冲调': {
                'attributes': [
                    {
                        'name': '饮品类型',
                        'patterns': [
                            (r'冰淇淋', '冰淇淋'),
                            (r'咖啡', '咖啡'),
                            (r'茶', '茶'),
                            (r'奶茶', '奶茶'),
                            (r'果汁', '果汁'),
                            (r'牛奶', '牛奶'),
                            (r'酸奶', '酸奶'),
                            (r'豆奶', '豆奶'),
                            (r'冲泡粉', '冲泡粉'),
                        ]
                    },
                    {
                        'name': '口味',
                        'patterns': [
                            (r'原味', '原味'),
                            (r'巧克力', '巧克力味'),
                            (r'香草', '香草味'),
                            (r'草莓', '草莓味'),
                            (r'抹茶', '抹茶味'),
                            (r'焦糖', '焦糖味'),
                            (r'榛子', '榛子味'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)[mM][lL]', 'ml'),
                            (r'(\d+)[lL]', 'L'),
                            (r'(\d+)[g克]', 'g'),
                            (r'(\d+)支', '支'),
                            (r'(\d+)杯', '杯'),
                            (r'(\d+)盒', '盒'),
                        ]
                    },
                    {
                        'name': '包装',
                        'patterns': [
                            (r'盒装', '盒装'),
                            (r'袋装', '袋装'),
                            (r'瓶装', '瓶装'),
                            (r'罐装', '罐装'),
                            (r'桶装', '桶装'),
                            (r'支装', '支装'),
                            (r'独立包装', '独立包装'),
                        ]
                    },
                ]
            },
            '宠物健康': {
                'attributes': [
                    {
                        'name': '产品类型',
                        'patterns': [
                            (r'猫粮', '猫粮'),
                            (r'狗粮', '狗粮'),
                            (r'营养膏', '营养膏'),
                            (r'益生菌', '益生菌'),
                            (r'鱼油', '鱼油'),
                            (r'化毛', '化毛用品'),
                            (r'维生素', '维生素'),
                            (r'钙片', '钙片'),
                            (r'卵磷脂', '卵磷脂'),
                            (r'软骨素', '软骨素'),
                        ]
                    },
                    {
                        'name': '功效',
                        'patterns': [
                            (r'美毛', '美毛'),
                            (r'肠胃', '肠胃调理'),
                            (r'关节', '关节养护'),
                            (r'免疫力', '提高免疫力'),
                            (r'化毛', '化毛'),
                            (r'补钙', '补钙'),
                            (r'护肤', '护肤'),
                            (r'视力', '视力保护'),
                        ]
                    },
                    {
                        'name': '适用对象',
                        'patterns': [
                            (r'猫', '猫咪'),
                            (r'狗', '狗狗'),
                            (r'犬', '狗狗'),
                            (r'通用', '通用'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)[g克]', 'g'),
                            (r'(\d+)[mM][lL]', 'ml'),
                            (r'(\d+)片', '片'),
                            (r'(\d+)粒', '粒'),
                        ]
                    },
                ]
            },
            '厨具': {
                'attributes': [
                    {
                        'name': '厨具类型',
                        'patterns': [
                            (r'锅', '锅具'),
                            (r'刀具', '刀具'),
                            (r'砧板', '砧板'),
                            (r'水壶', '水壶'),
                            (r'保温杯', '保温杯'),
                            (r'碗碟', '碗碟'),
                            (r'勺子', '勺子'),
                            (r'筷子', '筷子'),
                            (r'保鲜盒', '保鲜盒'),
                            (r'置物架', '置物架'),
                        ]
                    },
                    {
                        'name': '材质',
                        'patterns': [
                            (r'不锈钢', '不锈钢'),
                            (r'陶瓷', '陶瓷'),
                            (r'玻璃', '玻璃'),
                            (r'铸铁', '铸铁'),
                            (r'铝合金', '铝合金'),
                            (r'硅胶', '硅胶'),
                            (r'木质', '木质'),
                            (r'塑料', '塑料'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)[cC][mM]', 'cm'),
                            (r'(\d+)寸', '寸'),
                            (r'(\d+)[lL]', 'L'),
                            (r'(\d+)[mM][lL]', 'ml'),
                            (r'小号', '小号'),
                            (r'中号', '中号'),
                            (r'大号', '大号'),
                        ]
                    },
                    {
                        'name': '适用场景',
                        'patterns': [
                            (r'家用', '家用'),
                            (r'商用', '商用'),
                            (r'户外', '户外'),
                            (r'露营', '露营'),
                        ]
                    },
                ]
            },
            '工业品': {
                'attributes': [
                    {
                        'name': '产品类型',
                        'patterns': [
                            (r'工具', '工具'),
                            (r'配件', '配件'),
                            (r'零件', '零件'),
                            (r'耗材', '耗材'),
                            (r'防护', '防护用品'),
                            (r'清洁', '清洁用品'),
                            (r'存储', '存储'),
                        ]
                    },
                    {
                        'name': '材质',
                        'patterns': [
                            (r'钢', '钢'),
                            (r'铁', '铁'),
                            (r'铝', '铝'),
                            (r'铜', '铜'),
                            (r'塑料', '塑料'),
                            (r'橡胶', '橡胶'),
                            (r'玻璃', '玻璃'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)[mM][mM]', 'mm'),
                            (r'(\d+)[cC][mM]', 'cm'),
                            (r'(\d+)[kK][g克]', 'kg'),
                            (r'(\d+)[gG]', 'g'),
                        ]
                    },
                ]
            },
            '文娱': {
                'attributes': [
                    {
                        'name': '产品类型',
                        'patterns': [
                            (r'文具', '文具'),
                            (r'办公用品', '办公用品'),
                            (r'玩具', '玩具'),
                            (r'乐器', '乐器'),
                            (r'游戏', '游戏'),
                            (r'文具', '文具'),
                            (r'笔', '笔'),
                            (r'本', '笔记本'),
                            (r'纸', '纸张'),
                            (r'贴纸', '贴纸'),
                        ]
                    },
                    {
                        'name': '适用年龄',
                        'patterns': [
                            (r'0-3岁', '0-3岁'),
                            (r'3-6岁', '3-6岁'),
                            (r'6-12岁', '6-12岁'),
                            (r'12-18岁', '12-18岁'),
                            (r'成人', '成人'),
                        ]
                    },
                    {
                        'name': '材质',
                        'patterns': [
                            (r'纸质', '纸质'),
                            (r'塑料', '塑料'),
                            (r'木质', '木质'),
                            (r'金属', '金属'),
                            (r'布艺', '布艺'),
                        ]
                    },
                    {
                        'name': '规格',
                        'patterns': [
                            (r'(\d+)支', '支'),
                            (r'(\d+)本', '本'),
                            (r'(\d+)[pP]装', 'P装'),
                            (r'(\d+)入', '入'),
                        ]
                    },
                ]
            },
        }
    
    def extract_attributes(self, product_name, category):
        """
        从商品名称中提取属性
        
        Args:
            product_name: 商品名称
            category: 一级类目
        
        Returns:
            dict: 提取到的属性
        """
        if category not in self.extraction_rules:
            return {'error': '未知类目'}
        
        attributes = {}
        rules = self.extraction_rules[category]['attributes']
        
        for attr_rule in rules:
            attr_name = attr_rule['name']
            attr_values = []
            
            for pattern, value in attr_rule['patterns']:
                matches = re.findall(pattern, product_name)
                if matches:
                    if isinstance(matches[0], tuple):
                        # 如果是分组匹配，需要处理
                        for match in matches:
                            if len(match) == 1:
                                attr_values.append(str(match[0]) + value)
                            else:
                                attr_values.append('x'.join(str(m) for m in match) + value)
                    else:
                        # 简单匹配
                        attr_values.extend([value] * len(matches))
            
            if attr_values:
                # 去重
                attributes[attr_name] = list(set(attr_values))
        
        return attributes

def load_excel_data(file_path):
    """加载Excel数据"""
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

def main():
    excel_path = "/Users/yinmeichao.1/Downloads/Documents/Excel/网红货盘poc-3.16（保密数据）.xlsx"
    output_path = "/Users/yinmeichao.1/Downloads/Documents/Excel/商品属性提取结果.json"
    
    print("开始提取商品属性...")
    print("Excel文件: " + excel_path)
    
    # 加载数据
    headers, data = load_excel_data(excel_path)
    print("数据行数: " + str(len(data)))
    
    # 查找列索引
    col_map = {}
    for i, h in enumerate(headers):
        h_str = str(h)
        if '商品名称' in h_str:
            col_map['product_name'] = i
        elif '一级类目' in h_str:
            col_map['category_l1'] = i
        elif '品牌' in h_str:
            col_map['brand'] = i
        elif '本周销量' in h_str:
            col_map['sales'] = i
    
    # 创建属性提取器
    extractor = AttributeExtractor()
    
    # 按类目分组
    category_results = {}
    
    for row in data:
        category = row[col_map['category_l1']] if col_map['category_l1'] < len(row) else '未知'
        product_name = row[col_map['product_name']] if col_map['product_name'] < len(row) else ''
        brand = row[col_map['brand']] if col_map['brand'] < len(row) else '未知'
        sales = row[col_map['sales']] if col_map['sales'] < len(row) else 0
        
        # 提取属性
        attributes = extractor.extract_attributes(product_name, category)
        
        if category not in category_results:
            category_results[category] = {
                'total_products': 0,
                'products': [],
                'attribute_stats': {}
            }
        
        category_results[category]['total_products'] += 1
        
        # 保存产品属性
        product_data = {
            'product_name': product_name,
            'brand': brand,
            'sales': sales,
            'attributes': attributes
        }
        category_results[category]['products'].append(product_data)
        
        # 统计属性频率
        for attr_name, attr_values in attributes.items():
            if attr_name not in category_results[category]['attribute_stats']:
                category_results[category]['attribute_stats'][attr_name] = {}
            
            for attr_value in attr_values:
                if attr_value not in category_results[category]['attribute_stats'][attr_name]:
                    category_results[category]['attribute_stats'][attr_name][attr_value] = 0
                category_results[category]['attribute_stats'][attr_name][attr_value] += 1
    
    # 生成汇总报告
    summary = {
        'extraction_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_products': len(data),
        'categories': len(category_results),
        'category_results': category_results
    }
    
    # 保存结果
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print("\n提取完成!")
    print("输出文件: " + output_path)
    print("\n类目统计:")
    for category, result in sorted(category_results.items(), key=lambda x: x[1]['total_products'], reverse=True):
        print("  " + category + ": " + str(result['total_products']) + " 个商品, " + str(len(result['attribute_stats'])) + " 个属性维度")
    
    return summary

if __name__ == '__main__':
    main()
