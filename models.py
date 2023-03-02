list_index = ['type']


models = {
    '员工管理': {
        'type': {'interface_setting': {}, 'web_client': {}},
        'quote': {
            '组织管理': ['data'],
        },
        'quoted': {
            '工单配置-流程节点': []
        },
        'interface': {
            'create': {'custom_field': []}, 'update': {}, 'delete': {}, 'list': {}},
        'special': ['特征测试点1', '特征测试点2']
    },
    '工单配置-流程节点': {
        'type': {
            'server_side_logic': {
                'outside_server': ['创建工单外部服务'],
                'script': ['创建工单脚本'],
                'own_logic': ['创建工单自身逻辑重点']
            },
            'interface_setting': {
                'create': {
                    'custom_field': [],
                    'required_field': [],
                    'unique_field': [],
                    'lead': []
                },
                'update': {
                    'custom_field': [],
                    'required_field': [],
                    'unique_field': [],
                },
                'delete': {
                    'delete_limit': []
                },
                'list': {
                    'screening_field': [],
                    'sort_field': [],
                    'lead_out': []
                }
            },
            'web_client': {
                'pages': {
                    '工单配置页面': {
                        'js': ['树组件点击链接', '配置解析'],
                        'css': ['div遮挡'],
                        'html': ['单位']
                    }
                }
            },
            'client_serve': {
                'data_commit': {
                    'form': ['切换配置清空表单', '切换节点不清空表单'],
                    'id_link': ['流程节点拥有单独id']
                },
                'data_receive': {
                    'params': [],
                    'data_type': ['配置字段节点支持解析为json']
                },
            },
            'app_client': {
                'pages': {
                    '工单配置': {
                        'app_view': [],
                        'app_model': [],
                        'app_presenter': []
                    }
                }
            }
        },
        'quote': {
            '员工管理': ['data'],
        },
        'quoted': {
            '工单流程-创建工单': ['节点配置写入工单']
        },
        'interface': {
            'create': {}, 'update': {}, 'delete': {}, 'list': {}},
        'special': ['特征测试点1', '特征测试点2']
    },
    '工单流程-创建工单': {
        'type': {
            'server_side_logic': {
                'outside_server': ['通知服务'],
                'script': ['日统计脚本'],
                'own_logic': ['写入时检查']
            },
            'interface_setting': {},
            'web_client': {},
            'app_client': {}},
        'quote': {
            '工单配置-流程节点': [],
        },
        'quoted': {
            '工单流程-指派工单': []
        },
        'interface': {
            'create': {}, 'update': {}, 'delete': {}, 'list': {}},
        'special': ['特征测试点1', '特征测试点2']
    },
}
