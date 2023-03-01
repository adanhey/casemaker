models = {
    "员工管理": {
        "type": {"interface_setting": {}, "web_client": {}},
        "quote": {
            "组织管理": ["data"],
        },
        "quoted": {
            "工单配置-流程节点": []
        },
        "interface": {
            "create": {"自定义字段": []}, "update": {}, "delete": {}, "list": {}},
        "special": ["特征测试点1", "特征测试点2"]
    },
    "工单配置-流程节点": {
        "type": {
            "server_side_logic": {
                "outside_server": ["创建工单外部服务"],
                "script": ["创建工单脚本"],
                "own_logic": ["创建工单自身逻辑重点"]
            },
            "interface_setting": {},
            "web_client": {}
        },
        "quote": {
            "员工管理": ["data"],
        },
        "quoted": {
            "工单流程-创建工单": []
        },
        "interface": {
            "create": {}, "update": {}, "delete": {}, "list": {}},
        "special": ["特征测试点1", "特征测试点2"]
    },
    "工单流程-创建工单": {
        "type": {
            "server_side_logic": {
                "outside_server": ["通知服务"],
                "script": ["日统计脚本"],
                "own_logic": ["写入时检查"]
            },
            "interface_setting": {},
            "web_client": {},
            "app_client": {}},
        "quote": {
            "工单配置-流程节点": [],
        },
        "quoted": {
            "工单流程-指派工单": []
        },
        "interface": {
            "create": {}, "update": {}, "delete": {}, "list": {}},
        "special": ["特征测试点1", "特征测试点2"]
    },
}
