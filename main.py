import json

from ai_model import get_prompt, send_request_to_model
from process_sewagger import get_data_from_file, get_server_url, group_by_tag, process_componts, process_tag_map, \
    write_result_to_file

if __name__ == '__main__':
    #  处理swagger文档
    data = get_data_from_file('default_OpenAPI.json')
    server_url = get_server_url(data)
    # 输出 JSON 对象
    print(server_url)

    tag_map = group_by_tag(data)

    schemas = process_componts(data)

    result = process_tag_map(tag_map, schemas)

    for key, value in result.items():
        write_result_to_file(f"postman/{key}.json", value)

    #    调用AI大模型回复内容
    postman_map = {
        "info": {
            "name": "API Collection",
            "description": "Generated from swagger spec",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/"
        }
    }
    for key, value in result.items():
        prompt = get_prompt(server_url,value)
        response = send_request_to_model(prompt)
        json = json.loads(response)
        item = json['item']
