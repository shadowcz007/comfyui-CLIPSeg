from .nodes.Clipseg import CLIPSeg,CombineMasks

# 要导出的所有节点及其名称的字典
# 注意：名称应全局唯一
NODE_CLASS_MAPPINGS = {
    "CLIPSeg_":CLIPSeg,
    "CombineMasks_":CombineMasks
}
