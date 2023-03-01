models = {
    "工单配置-流程节点": {
        "type": ["interface_setting", "web_client"],
        "quote": {
            "员工管理": [],
        },
        "quoted": {
            "工单流程-创建工单": []
        },
        "interface": ["create", "update", "delete", "list"]
    },
    "工单流程-创建工单": {
        "type": ["interface_setting", "web_client", "app_client"],
        "quote": {
            "工单配置-流程节点": [],
        },
        "quoted": {
            "工单流程-指派工单": []
        },
        "interface": ["create", "update", "list"]
    },
}
