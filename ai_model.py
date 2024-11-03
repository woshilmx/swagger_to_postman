import os

from volcenginesdkarkruntime import Ark

api_key="ceda1a86-e69a-4069-a02c-7e63a6699757"
os.environ['ARK_API_KEY']=api_key
def get_prompt(server_url, swagger_json):
    """获取提示prompt"""
    param= {"current": 1, "pageSize": 10}
    prompt_format = f"""
    你是一名软件测试人员，现在我给你如下经过处理的 swagger 规范的json，你需要根据这段json，生成postman支持的collection.json 文件，要求
1. 你需要根据接口的参数生成测试的参数；
2. 接口的 base_url 使用 postman 提供的变量来表示,base_url 的值为 {{server_url}}
3. 请直接给出我最终完整版本的collection.json 内容
4. 每个接口的名字使用 summary 的内容来命名，如果 summary中的内容为空，那么你自己来进行推断
5. 分析的过程，不需要给出，请只给出我最终的结果；
6. 如果requestBody/content 中是 application/json类型，那么你生成的 collection.json文档的请求参数也是json格式类型
7. raw 参数请直接给出 字符串类型的json格式，并且你要根据请求参数的含义，帮我给出实际的参数值,例如 {{param}}等
8. 请确保你编写的json格式，可以被 postman 正确解析
请帮我一步步推理并最终完善它
swagger规范的json结构如下：
{{swagger_json}}
    """

    return prompt_format.format(server_url=server_url, swagger_json=swagger_json,param=param)


def send_request_to_model(prompt):
    """发送prompt"""
    client = Ark(api_key=os.environ.get("ARK_API_KEY"))

    print("----- standard request -----")
    completion = client.chat.completions.create(
        model="ep-20240901231439-5qrmr",
        messages=[
            {"role": "system", "content": prompt},
        ],
    )
    print(completion)
    return completion.choices[0].message.content

if __name__ == '__main__':
    prompt=get_prompt("http://127.0.0.1:8976",[
    {
        "api_path": "/locations/add",
        "api_detail": {
            "post": {
                "tags": [
                    "地点表"
                ],
                "summary": "新增",
                "operationId": "addUsingPOST_11",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "LocationsVO",
                                "type": "object",
                                "properties": {
                                    "andFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "city": {
                                        "type": "string",
                                        "description": "市"
                                    },
                                    "createTime": {
                                        "type": "string",
                                        "description": "创建时间",
                                        "format": "date-time"
                                    },
                                    "current": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "district": {
                                        "type": "string",
                                        "description": "区"
                                    },
                                    "isDeleted": {
                                        "type": "integer",
                                        "description": "是否删除",
                                        "format": "int32"
                                    },
                                    "locationId": {
                                        "type": "integer",
                                        "description": "主键，自增",
                                        "format": "int64"
                                    },
                                    "orFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "orderConditions": {
                                        "type": "array",
                                        "items": {
                                            "title": "OrderCondition",
                                            "type": "object",
                                            "properties": {
                                                "name": {
                                                    "type": "string"
                                                },
                                                "sort": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "other_search_condition": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "pageSize": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "province": {
                                        "type": "string",
                                        "description": "省"
                                    },
                                    "street": {
                                        "type": "string",
                                        "description": "街道"
                                    },
                                    "updateTime": {
                                        "type": "string",
                                        "description": "修改时间",
                                        "format": "date-time"
                                    }
                                },
                                "description": "地点表-vo"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "title": "BaseResponse",
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "integer",
                                            "format": "int32"
                                        },
                                        "data": {
                                            "type": "object"
                                        },
                                        "message": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                },
                "extensions": {
                    "x-order": "2147483647"
                }
            }
        }
    },
    {
        "api_path": "/locations/delete/{id}",
        "api_detail": {
            "delete": {
                "tags": [
                    "地点表"
                ],
                "summary": "删除",
                "operationId": "deleteUsingDELETE_11",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "id",
                        "required": True,
                        "style": "simple",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "title": "BaseResponse",
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "integer",
                                            "format": "int32"
                                        },
                                        "data": {
                                            "type": "object"
                                        },
                                        "message": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "204": {
                        "description": "No Content"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    }
                },
                "extensions": {
                    "x-order": "2147483647"
                }
            }
        }
    },
    {
        "api_path": "/locations/get/{id}",
        "api_detail": {
            "get": {
                "tags": [
                    "地点表"
                ],
                "summary": "根据Id查询",
                "operationId": "getUsingGET_18",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "description": "id",
                        "required": True,
                        "style": "simple",
                        "schema": {
                            "type": "integer",
                            "format": "int64"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "title": "BaseResponse",
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "integer",
                                            "format": "int32"
                                        },
                                        "data": {
                                            "type": "object"
                                        },
                                        "message": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                },
                "extensions": {
                    "x-order": "2147483647"
                }
            }
        }
    },
    {
        "api_path": "/locations/list",
        "api_detail": {
            "post": {
                "tags": [
                    "地点表"
                ],
                "summary": "列表",
                "operationId": "listUsingPOST_18",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "LocationsVO",
                                "type": "object",
                                "properties": {
                                    "andFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "city": {
                                        "type": "string",
                                        "description": "市"
                                    },
                                    "createTime": {
                                        "type": "string",
                                        "description": "创建时间",
                                        "format": "date-time"
                                    },
                                    "current": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "district": {
                                        "type": "string",
                                        "description": "区"
                                    },
                                    "isDeleted": {
                                        "type": "integer",
                                        "description": "是否删除",
                                        "format": "int32"
                                    },
                                    "locationId": {
                                        "type": "integer",
                                        "description": "主键，自增",
                                        "format": "int64"
                                    },
                                    "orFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "orderConditions": {
                                        "type": "array",
                                        "items": {
                                            "title": "OrderCondition",
                                            "type": "object",
                                            "properties": {
                                                "name": {
                                                    "type": "string"
                                                },
                                                "sort": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "other_search_condition": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "pageSize": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "province": {
                                        "type": "string",
                                        "description": "省"
                                    },
                                    "street": {
                                        "type": "string",
                                        "description": "街道"
                                    },
                                    "updateTime": {
                                        "type": "string",
                                        "description": "修改时间",
                                        "format": "date-time"
                                    }
                                },
                                "description": "地点表-vo"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "title": "BaseResponse",
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "integer",
                                            "format": "int32"
                                        },
                                        "data": {
                                            "type": "object"
                                        },
                                        "message": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                },
                "extensions": {
                    "x-order": "2147483647"
                }
            }
        }
    },
    {
        "api_path": "/locations/page",
        "api_detail": {
            "post": {
                "tags": [
                    "地点表"
                ],
                "summary": "分页",
                "operationId": "pageUsingPOST_18",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "LocationsPageVO",
                                "type": "object",
                                "properties": {
                                    "andFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "city": {
                                        "type": "string",
                                        "description": "市"
                                    },
                                    "createTime": {
                                        "type": "string",
                                        "description": "创建时间",
                                        "format": "date-time"
                                    },
                                    "current": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "district": {
                                        "type": "string",
                                        "description": "区"
                                    },
                                    "isDeleted": {
                                        "type": "integer",
                                        "description": "是否删除",
                                        "format": "int32"
                                    },
                                    "locationId": {
                                        "type": "integer",
                                        "description": "主键，自增",
                                        "format": "int64"
                                    },
                                    "orFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "orderConditions": {
                                        "type": "array",
                                        "items": {
                                            "title": "OrderCondition",
                                            "type": "object",
                                            "properties": {
                                                "name": {
                                                    "type": "string"
                                                },
                                                "sort": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "other_search_condition": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "pageSize": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "province": {
                                        "type": "string",
                                        "description": "省"
                                    },
                                    "street": {
                                        "type": "string",
                                        "description": "街道"
                                    },
                                    "updateTime": {
                                        "type": "string",
                                        "description": "修改时间",
                                        "format": "date-time"
                                    }
                                },
                                "description": "地点表-分页列表-响应参数"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "title": "BaseResponse",
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "integer",
                                            "format": "int32"
                                        },
                                        "data": {
                                            "type": "object"
                                        },
                                        "message": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                },
                "extensions": {
                    "x-order": "2147483647"
                }
            }
        }
    },
    {
        "api_path": "/locations/update",
        "api_detail": {
            "put": {
                "tags": [
                    "地点表"
                ],
                "summary": "更新",
                "operationId": "updateUsingPUT_11",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "LocationsVO",
                                "type": "object",
                                "properties": {
                                    "andFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "city": {
                                        "type": "string",
                                        "description": "市"
                                    },
                                    "createTime": {
                                        "type": "string",
                                        "description": "创建时间",
                                        "format": "date-time"
                                    },
                                    "current": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "district": {
                                        "type": "string",
                                        "description": "区"
                                    },
                                    "isDeleted": {
                                        "type": "integer",
                                        "description": "是否删除",
                                        "format": "int32"
                                    },
                                    "locationId": {
                                        "type": "integer",
                                        "description": "主键，自增",
                                        "format": "int64"
                                    },
                                    "orFilter": {
                                        "type": "array",
                                        "items": {
                                            "title": "Filter",
                                            "type": "object",
                                            "properties": {
                                                "eq": {
                                                    "type": "object"
                                                },
                                                "ge": {
                                                    "type": "object"
                                                },
                                                "gt": {
                                                    "type": "object"
                                                },
                                                "in": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "isNotNull": {
                                                    "type": "boolean"
                                                },
                                                "isNull": {
                                                    "type": "boolean"
                                                },
                                                "le": {
                                                    "type": "object"
                                                },
                                                "leftLike": {
                                                    "type": "string"
                                                },
                                                "like": {
                                                    "type": "string"
                                                },
                                                "lt": {
                                                    "type": "object"
                                                },
                                                "name": {
                                                    "type": "string"
                                                },
                                                "ne": {
                                                    "type": "object"
                                                },
                                                "notIn": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "string"
                                                    }
                                                },
                                                "rightLike": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "orderConditions": {
                                        "type": "array",
                                        "items": {
                                            "title": "OrderCondition",
                                            "type": "object",
                                            "properties": {
                                                "name": {
                                                    "type": "string"
                                                },
                                                "sort": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    },
                                    "other_search_condition": {
                                        "type": "array",
                                        "items": {
                                            "type": "string"
                                        }
                                    },
                                    "pageSize": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "province": {
                                        "type": "string",
                                        "description": "省"
                                    },
                                    "street": {
                                        "type": "string",
                                        "description": "街道"
                                    },
                                    "updateTime": {
                                        "type": "string",
                                        "description": "修改时间",
                                        "format": "date-time"
                                    }
                                },
                                "description": "地点表-vo"
                            }
                        }
                    }
                },
                "responses": {
                    "200": {
                        "description": "OK",
                        "content": {
                            "*/*": {
                                "schema": {
                                    "title": "BaseResponse",
                                    "type": "object",
                                    "properties": {
                                        "code": {
                                            "type": "integer",
                                            "format": "int32"
                                        },
                                        "data": {
                                            "type": "object"
                                        },
                                        "message": {
                                            "type": "string"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "201": {
                        "description": "Created"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "403": {
                        "description": "Forbidden"
                    },
                    "404": {
                        "description": "Not Found"
                    }
                },
                "extensions": {
                    "x-order": "2147483647"
                }
            }
        }
    }
])
    print(send_request_to_model(prompt=prompt))
