# from unstructured.partition.auto import partition

# # PDF文件路径
# pdf_path = "../../data/C2/pdf/rag.pdf"

# # 使用Unstructured加载并解析PDF文档
# elements = partition(
#     filename=pdf_path,
#     content_type="application/pdf"
# )

# # 打印解析结果
# print(f"解析完成: {len(elements)} 个元素, {sum(len(str(e)) for e in elements)} 字符")

# # 统计元素类型
# from collections import Counter
# types = Counter(e.category for e in elements)
# print(f"元素类型: {dict(types)}")

# # 显示所有元素
# print("\n所有元素:")
# for i, element in enumerate(elements, 1):
#     print(f"Element {i} ({element.category}):")
#     print(element)
#     print("=" * 60)


from unstructured.partition.pdf import partition_pdf  # 替换原来的partition
from collections import Counter

# PDF文件路径（保持和你原来一致）
pdf_path = "../../data/C2/pdf/rag.pdf"

# ==================== 1. 测试 hi_res 策略（高分辨率布局分析） ====================
print("="*80)
print("【策略1：hi_res - 高分辨率布局分析】")
print("="*80)
# 使用hi_res策略解析（unstructured默认策略，依赖OpenCV做布局分析）
elements_hi_res = partition_pdf(
    filename=pdf_path,
    strategy="hi_res"  # 核心：指定hi_res策略
)

# 打印hi_res解析结果
print(f"hi_res 解析结果：")
print(f"- 元素总数：{len(elements_hi_res)}")
print(f"- 总字符数：{sum(len(str(e)) for e in elements_hi_res)}")
# 统计元素类型（如Title、NarrativeText、ListItem等）
types_hi_res = Counter(e.category for e in elements_hi_res)
print(f"- 元素类型分布：{dict(types_hi_res)}")
# 打印前2个元素示例（方便观察）
print(f"- 前2个元素内容示例：")
for i, e in enumerate(elements_hi_res[:2], 1):
    print(f"  元素{i}（{e.category}）：{str(e)[:200]}...")  # 只显示前200字符
print("\n")

# ==================== 2. 测试 ocr_only 策略（纯OCR解析） ====================
print("="*80)
print("【策略2：ocr_only - 纯OCR文本提取】")
print("="*80)
# 使用ocr_only策略解析（纯光学字符识别，适合扫描版/图片型PDF）
elements_ocr_only = partition_pdf(
    filename=pdf_path,
    strategy="ocr_only"  # 核心：指定ocr_only策略
)

# 打印ocr_only解析结果
print(f"ocr_only 解析结果：")
print(f"- 元素总数：{len(elements_ocr_only)}")
print(f"- 总字符数：{sum(len(str(e)) for e in elements_ocr_only)}")
# 统计元素类型（ocr_only通常只有NarrativeText）
types_ocr_only = Counter(e.category for e in elements_ocr_only)
print(f"- 元素类型分布：{dict(types_ocr_only)}")
# 打印前2个元素示例
print(f"- 前2个元素内容示例：")
for i, e in enumerate(elements_ocr_only[:2], 1):
    print(f"  元素{i}（{e.category}）：{str(e)[:200]}...")
print("\n")

# ==================== 3. 对比总结 ====================
print("="*80)
print("【两种策略对比总结】")
print("="*80)
print(f"- 元素数量差异：hi_res({len(elements_hi_res)}) vs ocr_only({len(elements_ocr_only)})")
print(f"- 元素类型差异：hi_res有{len(types_hi_res)}种类型，ocr_only有{len(types_ocr_only)}种类型")
print(f"- 字符数差异：hi_res({sum(len(str(e)) for e in elements_hi_res)}) vs ocr_only({sum(len(str(e)) for e in elements_ocr_only)})")
