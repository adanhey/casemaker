models = {"员工管理": {"type": {"interface_setting": {}, "web_client": {}}, "quote": {"组织管理": ["data"]},
                       "quoted": {"工单配置-流程节点": []}, "interface": ["akjsgdfjhg"],
                       "special": ["特征测试点1", "特征测试点2"]}, "工单配置-流程节点": {"type": {
    "server_side_logic": {"outside_server": ["创建工单外部服务"], "script": ["创建工单脚本"],
                          "own_logic": ["创建工单自身逻辑重点"]},
    "interface_setting": {"create": {"custom_field": [], "required_field": [], "unique_field": [], "lead": []},
                          "update": {"custom_field": [], "required_field": [], "unique_field": []},
                          "delete": {"delete_limit": []},
                          "list": {"screening_field": [], "sort_field": [], "lead_out": []}}, "web_client": {
        "pages": {"工单配置页面": {"js": ["树组件点击链接", "配置解析"], "css": ["div遮挡"], "html": ["单位"]}}},
    "client_serve": {
        "data_commit": {"form": ["切换配置清空表单", "切换节点不清空表单"], "id_link": ["流程节点拥有单独id"]},
        "data_receive": {"params": [], "data_type": ["配置字段节点支持解析为json"]}}, "app_client": {
        "pages": {"工单配置": {"app_view": ["*注意产品列表名称与web不一致"], "app_model": [], "app_presenter": []}}}},
                                                                                         "quote": {
                                                                                             "员工管理": ["data"]},
                                                                                         "quoted": {
                                                                                             "工单流程-创建工单": [
                                                                                                 "节点配置写入工单"]},
                                                                                         "interface": ["asfgasdjfghj"],
                                                                                         "special": ["特征测试点1",
                                                                                                     "特征测试点2"]},
          "工单流程-创建工单": {"type": {"server_side_logic": {"outside_server": ["通知服务"], "script": ["日统计脚本"],
                                                               "own_logic": ["写入时检查"]}, "interface_setting": {},
                                         "web_client": {}, "app_client": {}}, "quote": {"工单配置-流程节点": []},
                                "quoted": {"工单流程-指派工单": []}, "interface": ["kasjdhkjh"],
                                "special": ["特征测试点1", "特征测试点2"]}, "个人使用记录": {
        "type": {"server_side_logic": {"own_logic": ["锁定数量剩余可用数量", "变化区分正负"]}, "interface_setting": {
            "list": {"screening_field": ["备件编码", "备件名称", "备件类别", "关联方", "关联单号", "日期",
                                         "*关注仅列出登录账号相关记录"], "sort_field": ["默认日期"]},
            "exec": {"示例：内部执行\r\n注*同级节点需要加list备注": []}}, "web_client": {"pages": {
            "个人备件库-个人使用情况": {"js": ["备件类别筛选-树勾选事件"], "css": ["备件类别树省略展示hover效果"],
                                        "html": []}}},
                 "client_serve": {"data_commit": {"form": ["组合筛选"], "id_link": ["备件类别id筛选结果"]},
                                  "data_receive": {"params": ["备件类别"], "data_type": ["无特殊数据解析"]}},
                 "app_client": {
                     "pages": {"个人备件库-个人使用情况": {"app_presenter": ["单号查询", "状态筛选", "类型筛选"]},
                               "个人使用记录详情": {"app_presenter": ["id获取记录准确", "备件图片准确"],
                                                    "app_view": ["备件图片展示"]}}}, "iot_data_collect": {},
                 "iot_data_issue": {}}, "quote": {
            "个人备件操作": ["申领、退回、调拨、工单消耗均会记录", "调拨双方同时记录", "操作发起时生成记录",
                             "单次操作多备件生成多条记录"], "备件类型": ["备件类型数量及名称长度"]}, "quoted": {},
        "interface": [], "module_special_check": []}}
