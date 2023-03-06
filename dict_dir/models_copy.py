models = {
    "员工管理": {
        "type": {
            "interface_setting": {},
            "web_client": {}
        },
        "quote": {
            "组织管理": [
                "data"
            ]
        },
        "quoted": {
            "工单配置-流程节点": []
        },
        "interface": [
            "akjsgdfjhg"
        ],
        "special": [
            "特征测试点1",
            "特征测试点2"
        ]
    },
    "工单配置-流程节点": {
        "type": {
            "server_side_logic": {
                "outside_server": [
                    "创建工单外部服务"
                ],
                "script": [
                    "创建工单脚本"
                ],
                "own_logic": [
                    "创建工单自身逻辑重点"
                ]
            },
            "interface_setting": {
                "create": {
                    "custom_field": [],
                    "required_field": [],
                    "unique_field": [],
                    "lead": []
                },
                "update": {
                    "custom_field": [],
                    "required_field": [],
                    "unique_field": []
                },
                "delete": {
                    "delete_limit": []
                },
                "list": {
                    "screening_field": [],
                    "sort_field": [],
                    "lead_out": []
                }
            },
            "web_client": {
                "pages": {
                    "工单配置页面": {
                        "js": [
                            "树组件点击链接",
                            "配置解析"
                        ],
                        "css": [
                            "div遮挡"
                        ],
                        "html": [
                            "单位"
                        ]
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "切换配置清空表单",
                        "切换节点不清空表单"
                    ],
                    "id_link": [
                        "流程节点拥有单独id"
                    ]
                },
                "data_receive": {
                    "params": [],
                    "data_type": [
                        "配置字段节点支持解析为json"
                    ]
                }
            },
            "app_client": {
                "pages": {
                    "工单配置": {
                        "app_view": [
                            "*注意产品列表名称与web不一致"
                        ],
                        "app_model": [],
                        "app_presenter": []
                    }
                }
            }
        },
        "quote": {
            "员工管理": [
                "data"
            ]
        },
        "quoted": {
            "工单流程-创建工单": [
                "节点配置写入工单"
            ]
        },
        "interface": [
            "asfgasdjfghj"
        ],
        "special": [
            "特征测试点1",
            "特征测试点2"
        ]
    },
    "工单流程-创建工单": {
        "type": {
            "server_side_logic": {
                "outside_server": [
                    "通知服务"
                ],
                "script": [
                    "日统计脚本"
                ],
                "own_logic": [
                    "写入时检查"
                ]
            },
            "interface_setting": {},
            "web_client": {},
            "app_client": {}
        },
        "quote": {
            "工单配置-流程节点": []
        },
        "quoted": {
            "工单流程-指派工单": []
        },
        "interface": [
            "kasjdhkjh"
        ],
        "special": [
            "特征测试点1",
            "特征测试点2"
        ]
    },
    "个人使用记录": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "锁定数量剩余可用数量",
                    "变化区分正负"
                ]
            },
            "interface_setting": {
                "list": {
                    "screening_field": [
                        "备件编码",
                        "备件名称",
                        "备件类别",
                        "关联方",
                        "关联单号",
                        "日期",
                        "*关注仅列出登录账号相关记录"
                    ],
                    "sort_field": [
                        "默认日期"
                    ]
                },
                "exec": {
                    "示例：内部执行\r\n注*同级节点需要加list备注": []
                }
            },
            "web_client": {
                "pages": {
                    "个人备件库-个人使用情况": {
                        "js": [
                            "备件类别筛选-树勾选事件"
                        ],
                        "css": [
                            "备件类别树省略展示hover效果"
                        ],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "组合筛选"
                    ],
                    "id_link": [
                        "备件类别id筛选结果"
                    ]
                },
                "data_receive": {
                    "params": [
                        "备件类别"
                    ],
                    "data_type": [
                        "无特殊数据解析"
                    ]
                }
            },
            "app_client": {
                "pages": {
                    "个人备件库-个人使用情况": {
                        "app_presenter": [
                            "单号查询",
                            "状态筛选",
                            "类型筛选"
                        ]
                    },
                    "个人使用记录详情": {
                        "app_presenter": [
                            "id获取记录准确",
                            "备件图片准确"
                        ],
                        "app_view": [
                            "备件图片展示"
                        ]
                    }
                }
            },
            "iot_data_collect": {},
            "iot_data_issue": {}
        },
        "quote": {
            "个人备件操作": [
                "申领、退回、调拨、工单消耗均会记录",
                "调拨双方同时记录",
                "操作发起时生成记录",
                "单次操作多备件生成多条记录"
            ],
            "备件类型": [
                "备件类型数量及名称长度"
            ]
        },
        "quoted": {},
        "interface": [],
        "module_special_check": []
    },
    "备件出库": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "生成审批单时录入审批人，变更审批配置不下发已生成单",
                    "出库审批列表过滤审批通过的审批单",
                    "出入库记录记录所有审批单",
                    "审批不通过时锁定数量回退，修改实际为重新提交一次审批",
                    "审批操作时，查询配置，若为二次审批，不执行数量变更，生成二次审批单",
                    "调拨时先走出库审批，再走入库审批"
                ]
            },
            "interface_setting": {
                "list": {
                    "出库审批": {
                        "screening_field": {
                            "出库单号": {},
                            "申请人": {},
                            "审批人": {},
                            "出库视角": {
                                "检查多种视角可靠": {}
                            },
                            "时间": {}
                        },
                        "sort_field": {
                            "默认时间": {}
                        }
                    },
                    "出库单记录": {
                        "同入库审批": {},
                        "出库类型筛选": {},
                        "出库单状态筛选": {}
                    },
                    "出库备件记录": {
                        "同出库审批": {},
                        "出库类型筛选": {},
                        "出库单状态筛选": {},
                        "多一个备件名称/编码复合字段筛选": {}
                    }
                },
                "exec": {
                    "出库审批": [
                        "审批可编辑数量，验证数量不可大于申请数，且变更后结果正确"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件管理-入库审批": {
                        "js": [],
                        "css": [
                            "审批单下数量超过一页时展示"
                        ],
                        "html": []
                    },
                    "备件管理-出入库记录": {
                        "js": [],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "多条库位数据提交",
                        "二次审批单数据与一次审批单修改后一致"
                    ],
                    "id_link": []
                },
                "data_receive": {
                    "params": [],
                    "data_type": []
                }
            }
        },
        "quote": {
            "个人备件操作": [
                "生成审批单内容一致"
            ],
            "备件配置": {}
        },
        "quoted": {
            "库位管理及库存": {
                "锁定数量及可用数量变化": {}
            },
            "个人备件使用情况": {
                "数量记录": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "仓库管理": {
        "type": {
            "server_side_logic": {
                "own_logic": []
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "仓库编号由系统生成",
                        "仓库名称",
                        "仓库管理员"
                    ],
                    "unique_field": [
                        "仓库名称"
                    ]
                },
                "update": {
                    "required_field": [
                        "同新增",
                        "上级仓库不可变更"
                    ],
                    "unique_field": [
                        "同新增"
                    ]
                },
                "delete": {
                    "delete_limit": [
                        "仓库无下级仓库",
                        "仓库下无仓位"
                    ]
                },
                "list": {
                    "screening_field": [
                        "树结构，一次性返回，前端筛选仓库名称"
                    ],
                    "sort_field": [
                        "按树结构sortnum排序"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件仓库管理": {
                        "js": [],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [],
                    "id_link": []
                },
                "data_receive": {
                    "params": [
                        "仓库类型字典"
                    ],
                    "data_type": []
                }
            }
        },
        "quote": {
            "员工管理": [
                "示例：关注工单配置写入",
                "示例：关注工单配置读取"
            ]
        },
        "quoted": {
            "个人备件操作": {
                "仓库下无库位时无法进行操作": {},
                "审批人为仓库管理员时，仅审批人可查看对应审批单": {}
            },
            "库位管理及库存": {
                "备件详情仓库名称同步": {}
            },
            "备件出库": {
                "仓库下无库位时无法进行操作": {},
                "审批人为仓库管理员时，仅审批人可查看对应审批单": {}
            },
            "备件入库": {
                "仓库下无库位时无法进行操作": {},
                "审批人为仓库管理员时，仅审批人可查看对应审批单": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "备件类型管理": {
        "type": {
            "server_side_logic": {
                "own_logic": []
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "备件类别编码",
                        "备件类别名称",
                        "父类别"
                    ],
                    "unique_field": [
                        "备件类别编码",
                        "备件类别名称"
                    ]
                },
                "update": {
                    "required_field": [
                        "同新增"
                    ],
                    "unique_field": [
                        "同新增"
                    ]
                },
                "delete": {
                    "delete_limit": [
                        "类别下存在子类别无法删除",
                        "类别下存在备件无法删除"
                    ]
                },
                "list": {
                    "screening_field": [
                        "前端名称筛选"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件管理-备件档案": {
                        "js": [
                            "树结构列表"
                        ],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            }
        },
        "quote": {},
        "quoted": {
            "备件入库": {
                "筛选": {}
            },
            "备件出库": {
                "筛选": {}
            },
            "个人备件清单": {
                "筛选": {}
            },
            "工单服务记录": {
                "筛选": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "备件管理": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "备件有仓库库存或个人库存时，无法停用",
                    "停用备件无法进行入库操作，无法被工单服务记录选取"
                ]
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "系统编码",
                        "备件编码",
                        "备件名称",
                        "备件类别"
                    ],
                    "unique_field": [
                        "备件编码",
                        "备件名称"
                    ],
                    "lead": [
                        "备件名称*\t备件编码*\t备件关键程度\t型号\t品牌\t单位\t销售指导价\t备件简介"
                    ]
                },
                "update": {
                    "required_field": [
                        "同新增"
                    ],
                    "unique_field": [
                        "同新增"
                    ]
                },
                "delete": {
                    "delete_limit": [
                        "备件有仓库库存或个人库存时，无法删除"
                    ]
                },
                "list": {
                    "screening_field": [
                        "备件编码",
                        "备件名称",
                        "品牌"
                    ],
                    "sort_field": [
                        "默认日期"
                    ],
                    "lead_out": [
                        "备件名称*\t备件编码*\t备件关键程度\t型号\t品牌\t单位\t销售指导价\t备件简介"
                    ]
                },
                "exec": {
                    "启停用": [
                        "批量操作"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件管理-备件档案": {
                        "js": [
                            "示例：分页切换不重置筛选条件"
                        ],
                        "css": [
                            "示例：主题切换"
                        ],
                        "html": [
                            "示例：筛选条件错误时提示文案为:xxxxx"
                        ]
                    }
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            },
            "app_client": {
                "pages": {
                    "工作台-备件信息": {}
                }
            }
        },
        "quote": {
            "备件类别管理": []
        },
        "quoted": {
            "备件入库": {},
            "工单服务记录": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "备件入库": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "采购入库时，备件需存在",
                    "生成审批单时录入审批人，变更审批配置不下发已生成单",
                    "入库审批列表过滤审批通过的审批单",
                    "出入库记录记录所有审批单",
                    "审批不通过时锁定数量回退，修改实际为重新提交一次审批",
                    "审批操作时，查询配置，若为二次审批，不执行数量变更，生成二次审批单"
                ]
            },
            "interface_setting": {
                "list": {
                    "入库审批": {
                        "screening_field": {
                            "入库单号": {},
                            "申请人": {},
                            "审批人": {},
                            "入库视角": {
                                "检查多种视角可靠": {}
                            },
                            "时间": {}
                        },
                        "sort_field": {
                            "默认时间": {}
                        }
                    },
                    "入库单记录": {
                        "同入库审批": {},
                        "入库类型筛选": {},
                        "入库单状态筛选": {}
                    },
                    "入库备件记录": {
                        "同入库审批": {},
                        "入库类型筛选": {},
                        "入库单状态筛选": {},
                        "多一个备件名称/编码复合字段筛选": {}
                    }
                },
                "exec": {
                    "入库审批": [
                        "审批可编辑数量，验证数量不可大于申请数，且变更后结果正确",
                        "审批可编辑库位，验证多库位汇聚结果正确"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件管理-入库审批": {
                        "js": [
                            "审批时批量修改仓位，数量整合正确"
                        ],
                        "css": [
                            "审批单下数量超过一页时展示"
                        ],
                        "html": []
                    },
                    "备件管理-出入库记录": {
                        "js": [],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "多条库位数据提交"
                    ],
                    "id_link": []
                },
                "data_receive": {
                    "params": [],
                    "data_type": []
                }
            }
        },
        "quote": {
            "个人备件操作": [
                "生成审批单内容一致"
            ],
            "备件配置": {}
        },
        "quoted": {
            "库位管理及库存": {},
            "个人备件使用情况": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "备件配置": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "关闭调拨出库审批时，调拨默认无出库审批",
                    "角色审批时，变更角色对应人员，不影响已生成的审批",
                    "配置字段格式传输需可解析",
                    "工单来源选择个人备件库时，数量受个人备件数量影响"
                ]
            },
            "interface_setting": {
                "update": {
                    "选项组合配置json，json转换成字符串": {}
                },
                "list": {}
            },
            "web_client": {
                "pages": {
                    "系统配置-备件设置": {
                        "js": [
                            "关闭出库审批时，隐藏对应人员选择"
                        ],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "配置json构成"
                    ],
                    "id_link": [
                        "出库审批、入库审批、调拨审批、工单来源分别对应一个id"
                    ]
                },
                "data_receive": {
                    "params": [],
                    "data_type": [
                        "配置json解析"
                    ]
                }
            }
        },
        "quote": {
            "员工管理": [
                "停用人员可选"
            ]
        },
        "quoted": {
            "备件入库": {},
            "备件出库": {},
            "工单服务记录": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "个人备件操作": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "回退、调拨操作审批完成前锁定数量",
                    "申领走出库审批逻辑，回退走入库审批逻辑",
                    "调拨生成调拨单，走员工备件审批逻辑",
                    "工单消耗走个人备件需开启对应配置"
                ]
            },
            "interface_setting": {
                "list": {
                    "screening_field": [
                        "单号",
                        "查询人员为申请人、被调拨人、备件接收人复合字段",
                        "时间段",
                        "接受状态"
                    ],
                    "sort_field": [
                        "默认日期"
                    ]
                },
                "exec": {
                    "操作撤销": [
                        "撤销锁定数量变为可用"
                    ],
                    "审核不通过修改": [
                        "不通过锁定数量变可用，修改后重新计算"
                    ],
                    "调拨接受": [
                        "被调拨人锁定减少，接收人可用变多"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件库存": {
                        "js": [
                            "添加库位、备件相同项时提示",
                            "数量限制小于获取的库存",
                            "超过分页数量时可分页"
                        ],
                        "css": [],
                        "html": []
                    },
                    "个人备件库": {
                        "js": [
                            "添加库位、备件相同项时提示",
                            "数量限制小于获取的库存",
                            "超过分页数量时可分页"
                        ],
                        "css": [],
                        "html": []
                    },
                    "个人调拨记录": {
                        "js": [
                            "添加库位、备件相同项时提示",
                            "数量限制小于获取的库存",
                            "超过分页数量时可分页"
                        ],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "单次操作选择多备件提交数据准确"
                    ],
                    "id_link": [
                        "查看审批单时，数据无丢失"
                    ]
                },
                "data_receive": {
                    "params": [
                        "接收人视角、发起人视角区分角色"
                    ],
                    "data_type": [
                        "审批单备件列表解析"
                    ]
                }
            },
            "app_client": {
                "pages": {
                    "个人备件库-调拨、申领、退回": {
                        "app_presenter": [
                            "多备件数据提交"
                        ],
                        "app_model": [
                            "撤销、接受操作"
                        ],
                        "app_view": [
                            "超过页面高度展示"
                        ]
                    },
                    "个人使用记录-记录详情": {
                        "app_presenter": [
                            "多备件数据解析"
                        ],
                        "app_model": [
                            "撤销、接受操作"
                        ],
                        "app_view": [
                            "超过页面高度展示"
                        ]
                    }
                }
            }
        },
        "quote": {
            "员工管理": [
                "启停用状态影响",
                "区分公司"
            ],
            "仓库管理及库存": [
                "无可用数量不展示",
                "后端检查可用数量"
            ],
            "库位管理及库存": [
                "无可用数量不展示",
                "后端检查可用数量"
            ],
            "个人备件清单": {
                "无可用数量不展示": {},
                "后端检查可用数量": {}
            }
        },
        "quoted": {
            "个人备件使用情况": [
                "记录数量"
            ],
            "工单服务记录": [
                "多个工单同时添加数量总和不超过可用"
            ],
            "入库审批": [
                "开启二次审批，一次审批不变更数量"
            ],
            "出库审批": [
                "开启二次审批，一次审批不变更数量"
            ]
        },
        "interface": [
            "工单个人消耗数量的修改与准确性"
        ],
        "module_special_check": []
    },
    "个人备件清单": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "操作不通过时，对应锁定数量变为可用数量",
                    "操作发起时，对应可用数量变为锁定数量",
                    "根据登录账号信息筛选清单",
                    "可用与锁定均为0时，不会列出"
                ]
            },
            "interface_setting": {
                "list": {
                    "screening_field": [
                        "备件编码",
                        "备件名称",
                        "备件类别筛选父级不会筛选到子级"
                    ],
                    "sort_field": [
                        "默认日期"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "个人备件库-个人备件清单": {
                        "js": [],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "组合筛选"
                    ],
                    "id_link": [
                        "备件类别id"
                    ]
                },
                "data_receive": {
                    "params": [],
                    "data_type": []
                }
            },
            "app_client": {
                "pages": {
                    "我的-个人备件库": {
                        "app_presenter": [
                            "备件名称/备件编码组合筛选字段"
                        ],
                        "app_model": [],
                        "app_view": [
                            "备件图片"
                        ]
                    }
                }
            },
            "iot_data_collect": {},
            "iot_data_issue": {}
        },
        "quote": {
            "个人备件操作": [
                "发起时，目标清单可用及锁定数量不变更",
                "单次操作多备件记录正确"
            ],
            "备件类型管理": []
        },
        "quoted": {
            "工单服务记录": {
                "备件配置工单备件来源为个人备件库时消耗个人备件": {},
                "工单完成前，选中数量为锁定状态": {},
                "工单取消时，锁定数量变为可用数量": {}
            },
            "个人备件操作": {
                "调拨锁定数量": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "工单超时配置": {
        "type": {
            "server_side_logic": {
                "outside_server": {
                    "外部通知平台": {
                        "验证通知有效": {},
                        "多人员类型通知有效": {}
                    }
                },
                "script": [
                    "进入节点状态时生成定时任务，到点进行通知",
                    "变更配置不影响已生成的定时任务"
                ],
                "own_logic": [
                    "定时任务触发后，查询是否循环",
                    "开始计时节点为进入流程状态的事件",
                    "开始计时时间+超时时间=定时任务触发通知时间"
                ]
            },
            "interface_setting": {
                "update": {
                    "开始计时节点": [
                        "对应节点前的状态，无法写入节点或节点后状态"
                    ],
                    "超时时间设置": {},
                    "超时通知方式": {
                        "单次通知": {},
                        "循环通知": {}
                    },
                    "提醒对象": {
                        "对象非人员时，在其他模块变更，通知同步": {}
                    }
                },
                "查询": {}
            },
            "web_client": {
                "pages": {
                    "系统设置-工单设置": {}
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "变更选择的节点不影响已写入表单"
                    ],
                    "id_link": []
                },
                "data_receive": {
                    "params": [],
                    "data_type": []
                }
            }
        },
        "quote": {
            "员工管理": [],
            "客户管理": {},
            "工单审批": {}
        },
        "quoted": {
            "工单创建": {
                "工单取消/关闭停止任务": {},
                "审批通过前均计时": {}
            },
            "工单指派": {
                "工单取消/关闭停止任务": {},
                "审批通过前均计时": {}
            },
            "工单转派&拒绝&接受&开始": {
                "工单取消/关闭停止任务": {},
                "转派变更通知对象": {},
                "审批通过前均计时": {},
                "拒绝通过停止开始节点计时，进入指派节点计时": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "工单池工单": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "工单池转派不走审批流程",
                    "列表筛选不在待派工状态的工单"
                ]
            },
            "interface_setting": {
                "list": {
                    "screening_field": [
                        "工单编号",
                        "人员",
                        "客户名称",
                        "时间",
                        "工单类型"
                    ],
                    "sort_field": [
                        "默认时间",
                        "期望服务时间"
                    ]
                },
                "exec": {
                    "转派": [
                        "可对所有员工进行转派，转派后工单状态变更，责任人变更"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "工单管理-工单池管理": {
                        "js": [],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "协助人提交结构与app同步"
                    ],
                    "id_link": []
                },
                "data_receive": {
                    "params": [],
                    "data_type": []
                }
            },
            "app_client": {
                "pages": {
                    "工单池": {
                        "app_presenter": [
                            "拉取登录账号所在工单池下所有工单"
                        ],
                        "app_model": [],
                        "app_view": []
                    }
                }
            },
            "iot_data_collect": {},
            "iot_data_issue": {}
        },
        "quote": {
            "工单指派": {
                "指派多个工单池": {}
            },
            "工单创建": {
                "创建同时指派工单池": {}
            }
        },
        "quoted": {
            "工单转派&拒绝&接受&开始": {
                "拒绝通过时，工单返回工单池": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "工单池管理": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "一级工单池不支持指派工单",
                    "一级工单池不支持管理人员",
                    "接单后，责任人变更",
                    "工单池内指派时仅支持选择工单池下人员"
                ]
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "上级工单池名称",
                        "工单池名称"
                    ],
                    "unique_field": [
                        "工单池名称"
                    ]
                },
                "update": {
                    "同新增": {},
                    "上级工单池无法变更": {}
                },
                "delete": {
                    "delete_limit": [
                        "存在下级工单池时无法删除",
                        "存在人员时无法删除",
                        "存在未指派到人员工单时无法删除"
                    ]
                },
                "list": {
                    "screening_field": [
                        "前端名称筛选"
                    ],
                    "sort_field": [
                        "后端sortnum控制排序"
                    ]
                },
                "exec": {
                    "上移下移": [
                        "变更排序sortnum"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "工单管理-工单池管理": {
                        "js": [
                            "树结构列表"
                        ],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            },
            "app_client": {
                "pages": {
                    "工单池": {
                        "app_presenter": [
                            "拉取登录账号所在工单池下的所有工单",
                            "工单编号及客户名称组合筛选字段"
                        ],
                        "app_model": [],
                        "app_view": []
                    }
                }
            }
        },
        "quote": {},
        "quoted": {
            "工单指派": {
                "指派到工单池时，实际工单状态未流转": {}
            },
            "工单池员工管理": {},
            "工单池工单": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "工单池员工管理": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "添加时可选所有人员，包括停用状态员工",
                    "接单时不走审批逻辑"
                ]
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "所选员工信息"
                    ],
                    "unique_field": [
                        "员工id"
                    ]
                },
                "update": {
                    "同新增": {}
                },
                "delete": {
                    "delete_limit": [
                        "无移除限制"
                    ]
                },
                "list": {
                    "screening_field": [
                        "员工姓名"
                    ],
                    "sort_field": [
                        "默认时间"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "工单管理-工单池管理": {
                        "js": [],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            }
        },
        "quote": {
            "工单池管理": [],
            "员工管理": {}
        },
        "quoted": {
            "工单池工单": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "工单节点配置": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "与超时共用同一字段构成json",
                    "流程节点关闭时，跳过对应流程",
                    "流程节点开关不影响已生成工单",
                    "节点设置操作及审批人员为实时数据，影响已生成工单",
                    "操作开启、审批关闭时，执行对应操作自动流转",
                    "操作关闭时，对应流程节点无法进行对应操作",
                    "签到设置为，接受节点实时获取配置",
                    "需要签到，未签到时无法对工单进行其他操作"
                ]
            },
            "interface_setting": {
                "update": {
                    "指派工单": [
                        "取消开关",
                        "指派审批"
                    ],
                    "接受工单": [
                        "取消开关",
                        "转派开关",
                        "拒绝开关"
                    ],
                    "开始工单": {
                        "取消开关": {
                            "涉及审批": {}
                        },
                        "转派开关": {
                            "涉及审批": {}
                        },
                        "签到设置": {}
                    },
                    "关闭工单": {
                        "涉及审批": {}
                    }
                },
                "查询": {},
                "exec": {
                    "启停用": {}
                }
            },
            "web_client": {
                "pages": {
                    "工单设置-工单流程配置": {
                        "js": [
                            "流程字段解析展示"
                        ],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "切换节点不影响其他表单数据"
                    ],
                    "id_link": [
                        "每个节点对应一个id"
                    ]
                },
                "data_receive": {
                    "params": [],
                    "data_type": {}
                }
            }
        },
        "quote": {
            "员工管理": [
                "示例：关注工单配置写入",
                "示例：关注工单配置读取"
            ]
        },
        "quoted": {
            "工单创建": {},
            "工单指派": {},
            "工单转派&拒绝&接受&开始": {
                "接受节点关闭时跳过节点": {}
            },
            "工单取消": {},
            "工单关闭": {},
            "工单完工回执及提交验收": {},
            "客户验收": {
                "验收节点关闭时，提交验收直接完成": {}
            },
            "客户评价": {
                "客户评价节点关闭时，无评价环节": {}
            },
            "工单支付": {
                "结算节点关闭时，无支付流程": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "工单类型管理": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "复制时，同步复制",
                    "启停用仅影响是否可创建，不影响搜索展示等功能",
                    "新增有操作锁，关系为客户+名称"
                ]
            },
            "interface_setting": {
                "复制": {
                    "required_field": [
                        "工单类型名称",
                        "源类型"
                    ],
                    "unique_field": [
                        "工单类型名称"
                    ]
                },
                "update": {
                    "required_field": [
                        "同新增"
                    ],
                    "unique_field": [
                        "同新增"
                    ]
                },
                "list": {
                    "screening_field": [
                        "前端名称筛选"
                    ],
                    "sort_field": [
                        "默认启停用，第二字段时间"
                    ]
                },
                "exec": {
                    "启停用": []
                }
            },
            "web_client": {
                "pages": {
                    "系统设置-工单设置": {}
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            }
        },
        "quote": {},
        "quoted": {
            "回访配置": {},
            "工单节点配置": {},
            "工单超时配置": {},
            "工单预警配置": {},
            "工单流转规则": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "工单流转规则": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "create和update接口增加筛选逻辑，按触发条件顺序进行与筛选，对满足条件的工单进行自动流转",
                    "优先级一样时，按修改时间进行流转",
                    "优先流转指派人，有流转人时，不进行流转责任人流程",
                    "未流转指派人，进行流转负责人流程，都未流转时无影响",
                    "开启审批时进入审批"
                ]
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "规则名称",
                        "优先级",
                        "触发时机",
                        "触发条件",
                        "流转员工"
                    ],
                    "unique_field": [],
                    "数量上限20": {}
                },
                "update": {
                    "同新增": {}
                },
                "delete": {
                    "delete_limit": [
                        "无喊出限制"
                    ]
                },
                "list": {},
                "exec": {
                    "启停用": [],
                    "复制建档": {}
                }
            },
            "web_client": {
                "pages": {
                    "系统设置-工单设置": {
                        "js": [
                            "添加规则触发条件增删"
                        ]
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [
                        "多触发条件提交"
                    ]
                },
                "data_receive": {}
            }
        },
        "quote": {
            "员工管理": [
                "触发条件"
            ],
            "客户管理": {
                "触发条件": {}
            },
            "产品管理": {
                "触发条件": {}
            }
        },
        "quoted": {
            "工单指派": {
                "当有指派人时，仅指派可派工": {}
            },
            "工单创建": {
                "创建和编辑时命中规则": {},
                "维保任务创建及诉求关联创建亦走规则流程": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "工单预警配置": {
        "type": {
            "server_side_logic": {
                "outside_server": [
                    "外部通知平台"
                ],
                "script": [
                    "工单状态流转时生成定时任务，对应时间后生成通知平台消息队列任务"
                ],
                "own_logic": [
                    "节点流转会取消之前的任务",
                    "生成通知队列消息后会查询是否循环",
                    "循环次数为实时查询",
                    "触发时间变更不影响已生成的任务",
                    "提醒标题为app收到的通知"
                ]
            },
            "interface_setting": {
                "create": {
                    "提醒标题": {},
                    "触发条件": {},
                    "通知方式": {},
                    "预警对象": {
                        "对象动态变更时同步": {}
                    }
                },
                "update": {
                    "同新增": {},
                    "变更触发条件不影响已生成的任务": {},
                    "变更触发条件影响循环的下次任务": {}
                },
                "delete": {
                    "delete_limit": [
                        "无删除限制"
                    ]
                },
                "list": {
                    "screening_field": [
                        "提醒标题"
                    ],
                    "sort_field": [
                        "默认启停用，第二字段修改时间"
                    ]
                },
                "exec": {
                    "启停用": [
                        "停用后预警不生效"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "系统设置-工单设置-工单预警": {}
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            },
            "app_client": {
                "pages": {
                    "消息": {
                        "app_presenter": [
                            "接受消息正确"
                        ],
                        "app_model": [],
                        "app_view": [
                            "通知栏展示"
                        ]
                    }
                }
            }
        },
        "quote": {
            "客户管理": [
                "通知人员"
            ],
            "员工管理": {
                "通知人员": {}
            },
            "工单创建": {
                "通知人员": {}
            }
        },
        "quoted": {
            "工单创建": {},
            "工单指派": {},
            "工单转派&拒绝&接受&开始": {},
            "工单取消": {},
            "工单关闭": {},
            "工单完工回执及提交验收": {},
            "客户验收": {},
            "客户评价": {},
            "工单回访": {},
            "工单审批": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "供应商管理": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "单备件可绑定多供应商"
                ]
            },
            "interface_setting": {
                "create": {
                    "required_field": [
                        "系统编码由系统生成",
                        "供应商编码",
                        "供应商名称",
                        "联系人",
                        "联系人电话",
                        "供应商类别"
                    ],
                    "unique_field": [
                        "供应商编码",
                        "供应商名称"
                    ],
                    "lead": [
                        "供应商编码*\t供应商名称*\t联系人*\t联系电话*\t供应商地址\t电子邮箱\t供应商简介"
                    ]
                },
                "update": {
                    "required_field": [
                        "同新增"
                    ],
                    "unique_field": [
                        "同新增"
                    ],
                    "支持变更供应商类别": {}
                },
                "delete": {
                    "delete_limit": [
                        "有备件绑定关系时无法删除",
                        "类别存在下级供应商类别无法删除",
                        "类别下存在供应商无法删除"
                    ]
                },
                "list": {
                    "screening_field": [
                        "供应商编码：模糊",
                        "供应商名称：模糊",
                        "联系人：模糊",
                        "联系电话：模糊"
                    ],
                    "sort_field": [
                        "默认日期"
                    ],
                    "lead_out": [
                        "默认导出条件为查询条件",
                        "供应商编码*\t供应商名称*\t联系人*\t联系电话*\t供应商地址\t电子邮箱\t供应商类别\t供应商简介",
                        "所有筛选条件作用时，导出正常"
                    ]
                },
                "exec": {
                    "类型树id排序": [
                        "上移、下移正常"
                    ]
                }
            },
            "web_client": {
                "pages": {
                    "备件管理-供应商录入": {
                        "js": [
                            "翻页不重置查询条件",
                            "供应商类别搜索为前端功能"
                        ],
                        "css": [],
                        "html": []
                    },
                    "备件管理-备件档案-备件详情-供应商": {
                        "绑定窗口复用供应商录入页面": {},
                        "绑定时后端检查是否存在": {}
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [],
                    "id_link": []
                },
                "data_receive": {
                    "params": [],
                    "data_type": [
                        "供应商类型树最多支持3层"
                    ]
                }
            },
            "app_client": {
                "pages": {
                    "示例：工单列表": {
                        "app_presenter": [
                            "示例：app协助人解析中person字段下对象需为json"
                        ],
                        "app_model": [],
                        "app_view": []
                    }
                }
            }
        },
        "quote": {},
        "quoted": {
            "备件管理": {
                "暂未设置绑定上限": {}
            }
        },
        "interface": [],
        "module_special_check": []
    },
    "回访配置": {
        "type": {
            "server_side_logic": {
                "own_logic": [
                    "任务生成时间",
                    "已有回访单时，定时任务不再生成",
                    "待回访工单范围",
                    "计划回访时间为生成时间+回访计划完成时间",
                    "停用时无效果"
                ],
                "script": [
                    "每日定时筛选工单类型下x天内完成的工单",
                    "工单完成定时任务生成回访",
                    "每日任务扫描工单类型下是否有回访任务需要执行逾期前提醒",
                    "每日任务扫描工单类型下是否有回访任务需要执行逾期后提醒"
                ]
            },
            "interface_setting": {
                "update": {
                    "required_field": {
                        "任务生成时间": {
                            "待回访工单范围": {}
                        },
                        "回访计划完成时间": {}
                    },
                    "unique_field": [
                        "回访计划完成时间"
                    ],
                    "其他字段": {
                        "逾期前提醒日期": {},
                        "逾期前提醒对象": {},
                        "逾期后提醒日期": {},
                        "逾期后提醒对象": {}
                    }
                },
                "查询": {}
            },
            "web_client": {
                "pages": {
                    "系统设置-工单设置-回访设置": {}
                }
            },
            "client_serve": {
                "data_commit": {},
                "data_receive": {}
            }
        },
        "quote": {
            "员工管理": []
        },
        "quoted": {
            "工单回访": {},
            "客户验收": {}
        },
        "interface": [],
        "module_special_check": []
    },
    "库位管理及库存": {
        "type": {
            "server_side_logic": {
                "own_logic": {
                    "库位下存在备件时不可停用": {},
                    "停用后不可被出入库操作选取": {},
                    "新增生成规则区分": {
                        "名称+序号总数需小于1000": {},
                        "货架数+层数+位置总数需小于1000": {},
                        "单次生成": {}
                    }
                }
            },
            "interface_setting": {
                "create": {
                    "required_field": {
                        "库位名称": {},
                        "是否批量": {
                            "批量": {
                                "生成规则": {
                                    "货架数+层数+位置": {},
                                    "序号：生成数量": {}
                                }
                            },
                            "单次": {}
                        }
                    },
                    "unique_field": {
                        "名称": {
                            "批量生成中名称重复时，会忽略，检查重复时库位状态是否重置": {}
                        }
                    }
                },
                "update": {
                    "required_field": {
                        "库位编号，由系统生成": {},
                        "库位名称": {}
                    },
                    "unique_field": {
                        "名称": {}
                    }
                },
                "delete": {
                    "delete_limit": [
                        "库位下有备件时无法删除"
                    ]
                },
                "list": {
                    "库位管理": {
                        "screening_field": [
                            "库位名称",
                            "库位状态",
                            "库位类型"
                        ],
                        "sort_field": [
                            "默认启停用，第二排序字段为时间"
                        ]
                    },
                    "库存管理": {
                        "screening_field": [
                            "备件编码",
                            "备件名称"
                        ],
                        "sort_field": [
                            "默认时间"
                        ],
                        "明细": {
                            "多库位数量检查": {}
                        }
                    }
                },
                "exec": {
                    "设置安全库存": [
                        "多库位验证"
                    ],
                    "启停用": {
                        "库位下有备件时无法停用": {},
                        "库位下有审批单时，无法停用": {}
                    }
                }
            },
            "web_client": {
                "pages": {
                    "备件管理-备件仓库管理": {
                        "js": [],
                        "css": [],
                        "html": []
                    },
                    "备件管理-备件库存": {
                        "js": [
                            "备件类别树"
                        ],
                        "css": [],
                        "html": []
                    }
                }
            },
            "client_serve": {
                "data_commit": {
                    "form": [],
                    "id_link": []
                },
                "data_receive": {
                    "params": [],
                    "data_type": []
                }
            }
        },
        "quote": {
            "仓库管理": {}
        },
        "quoted": {
            "个人备件操作": {
                "停用库位": {}
            },
            "备件入库": {},
            "备件出库": {}
        },
        "interface": [],
        "module_special_check": []
    }
}