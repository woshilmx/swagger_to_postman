import json
import os


def get_data_from_file(path):
    """ 获取swagger文档的json结构 """
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_server_url(data):
    """获取base url地址"""
    return data['servers'][0]['url']


def group_by_tag(data):
    """根据tag进行循环分组"""
    tags = data['tags']
    tag_map = {}
    for item in tags:
        name = item['name']
        tag_map[name] = []

    paths = data['paths']
    for key, value in paths.items():
        api_detail_ = value.values()
        for item in api_detail_:  # 可能只有一个
            tags = item['tags']
            for tag in tags:
                path_item = {
                    "api_path": key,
                    "api_detail": value
                }
                tag_map[tag].append(path_item)
    return tag_map


def process_componts(data):
    schemas = data['components']['schemas']
    schemas_map = {}
    for item in schemas.values():
        obj = expand_refs(item, schemas)
        schemas_map[obj['title']] = obj
    return schemas_map


# 递归展开 $ref 函数
def expand_refs(obj, schemas):
    if isinstance(obj, dict):
        # 检查并处理 $ref 字段
        if "$ref" in obj:
            # 取得引用的名字
            ref_path = obj["$ref"].split("/")[-1]
            # 从 schemas 中找到引用对象
            if ref_path in schemas:
                return expand_refs(schemas[ref_path], schemas)
            else:
                raise ValueError(f"Reference {ref_path} not found in schemas.")

        # 递归地处理每个键值对
        return {k: expand_refs(v, schemas) for k, v in obj.items()}

    elif isinstance(obj, list):
        # 如果是列表，递归处理每个元素
        return [expand_refs(item, schemas) for item in obj]

    return obj  # 返回基本类型值


def write_result_to_file(path, tag_map):
    """将字典写入文件"""
    # 获取目录路径
    directory = os.path.dirname(path)

    # 判断目录是否存在，不存在则创建
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(tag_map, file, ensure_ascii=False, indent=4)


def process_tag_map(tag_map, schemas):
    """"
    将 tag_map的数据中的 $ref 进行展开
    """
    result_map = {}
    for key, value in tag_map.items():
        result_map[key]=[]
        for item in value:
            result = expand_refs(item, schemas)
            result_map[key].append(result)
    return result_map