from django.db import models


class ConsumerTrialApply(models.Model):
    """
    用户测试申请
    """
    username = models.CharField(max_length=64, blank=True, unique=True, verbose_name='用户账号', help_text='唯一标识对该用户授权访问的一个访问通道编码。编码规则：机构中文全拼缩写（小写 ）+ 4位16进制随机编码，由业务输入系统 （系统应具备验证用户名唯一性功能）。用户账号由业务生成，生成的过程中，能够校验账号的唯一性')
    oa_number = models.CharField(max_length=128, blank=True, verbose_name='协议OA审批编号', help_text='用户申请测试，如果测试连接第三方生产环境，有费用发生，需要走OA流程，知会财务；如果是自己数据源，小宇100条免费，可以不用走OA，大于100条需要走OA流程审批')
    category = models.IntegerField(default=0, verbose_name='用户类型', help_text='1 内部用户； 2 外部用户')
    org_name_zh = models.CharField(max_length=256, blank=True, verbose_name='机构中文名称', help_text='可以为空，但是中英文单位名称必须填一个')
    org_name_en = models.CharField(max_length=256, blank=True, verbose_name='机构英文名称', help_text='可以为空，但是中英文单位名称必须填一个')
    org_number = models.CharField(max_length=128, blank=True, verbose_name='社会统一信用代码（组织机构代码）', help_text='用于客户业务校核，客户的中英文名称应该与社会统一信用代码一致')
    org_address = models.CharField(max_length=256, blank=True, verbose_name='机构地址', help_text='可以为空')
    user_department = models.CharField(max_length=128, blank=True, verbose_name='用户部门', help_text='主要是配置必要的辅助信息，用于对账，内部用户必填')
    user_project = models.CharField(max_length=128, blank=True, verbose_name='用户项目', help_text='内部用户必填')
    user_product = models.CharField(max_length=128, blank=True, verbose_name='用户产品', help_text='内部用户必填')
    test_count = models.IntegerField(default=100, verbose_name='测试条数', help_text='默认测试100条')
    server_ips = models.CharField(max_length=128, blank=True, verbose_name='服务器IP', help_text='用于配置白名单，多个IP以逗号分隔')
    contact_person = models.CharField(max_length=64, blank=True, verbose_name='联系人', help_text='必填')
    contact_mobile = models.CharField(max_length=64, blank=True, verbose_name='联系人手机号码', help_text='必填')
    contact_email = models.CharField(max_length=64, blank=True, verbose_name='联系人邮箱', help_text='必填')
    related_products = models.CharField(max_length=256, blank=True, verbose_name='用户关联产品', help_text='多个产品以逗号分隔')
    creator = models.CharField(max_length=64, blank=True, verbose_name='创建人', help_text='必填')
    creator_mobile = models.CharField(max_length=64, blank=True, verbose_name='创建人手机号码', help_text='必填')
    creator_email = models.CharField(max_length=64, blank=True, verbose_name='创建人邮箱', help_text='必填')
    description = models.TextField(blank=True, verbose_name='描述', help_text='可以描述附加的客户需求')


class ConsumerLaunchApply(models.Model):
    """
    用户上线申请
    """
    username = models.CharField(max_length=64, blank=True, unique=True, verbose_name='用户账号', help_text='唯一标识对该用户授权访问的一个访问通道编码。编码规则：机构中文全拼缩写（小写 ）+ 4位16进制随机编码，由业务输入系统 （系统应具备验证用户名唯一性功能）。用户账号由业务生成，生成的过程中，能够校验账号的唯一性')
    oa_number = models.CharField(max_length=128, blank=True, verbose_name='协议OA审批编号', help_text='用户申请使用生产系统的产品，需要先签订合同，并OA审批通过')
    category = models.IntegerField(default=0, verbose_name='用户类型', help_text='1 内部用户； 2 外部用户')
    org_name_zh = models.CharField(max_length=256, blank=True, verbose_name='机构中文名称', help_text='可以为空，但是中英文单位名称必须填一个')
    org_name_en = models.CharField(max_length=256, blank=True, verbose_name='机构英文名称', help_text='可以为空，但是中英文单位名称必须填一个')
    org_number = models.CharField(max_length=128, blank=True, verbose_name='社会统一信用代码（组织机构代码）', help_text='用于客户业务校核，客户的中英文名称应该与社会统一信用代码一致')
    org_address = models.CharField(max_length=256, blank=True, verbose_name='机构地址', help_text='可以为空')
    user_department = models.CharField(max_length=128, blank=True, verbose_name='用户部门', help_text='主要是配置必要的辅助信息，用于对账，内部用户必填')
    user_project = models.CharField(max_length=128, blank=True, verbose_name='用户项目', help_text='内部用户必填')
    user_product = models.CharField(max_length=128, blank=True, verbose_name='用户产品', help_text='内部用户必填')
    server_ips = models.CharField(max_length=128, blank=True, verbose_name='服务器IP', help_text='用于配置白名单，多个IP以逗号分隔')
    contact_person = models.CharField(max_length=64, blank=True, verbose_name='联系人', help_text='必填')
    contact_mobile = models.CharField(max_length=64, blank=True, verbose_name='联系人手机号码', help_text='必填')
    contact_email = models.CharField(max_length=64, blank=True, verbose_name='联系人邮箱', help_text='必填')
    related_products = models.CharField(max_length=256, blank=True, verbose_name='用户关联产品', help_text='多个产品以逗号分隔')
    creator = models.CharField(max_length=64, blank=True, verbose_name='创建人', help_text='必填')
    creator_mobile = models.CharField(max_length=64, blank=True, verbose_name='创建人手机号码', help_text='必填')
    creator_email = models.CharField(max_length=64, blank=True, verbose_name='创建人邮箱', help_text='必填')
    description = models.TextField(blank=True, verbose_name='描述', help_text='可以描述附加的客户需求')


class ProductLaunchApply(models.Model):
    """
    产品上线申请
    """
    product_number = models.CharField(max_length=64, blank=True, unique=True, verbose_name='产品编号', help_text='唯一标识')
    product_name = models.CharField(max_length=128, blank=True, verbose_name='产品名称', help_text='必填')
    source_numbers = models.CharField(max_length=256, blank=True, verbose_name='数据源编码', help_text='必填，来自第三方API接入或者内部开发数据源，多个数据源以逗号分隔')
    manager_name = models.CharField(max_length=64, blank=True, verbose_name='产品经理姓名', help_text='必填')
    manager_mobile = models.CharField(max_length=64, blank=True, verbose_name='产品经理手机号码', help_text='必填')
    manager_email = models.CharField(max_length=64, blank=True, verbose_name='产品经理邮箱', help_text='必填')
    use_cache = models.BooleanField(default=False, verbose_name='是否缓存', help_text='必填，是否使用缓存热数据返回用户')
    cache_ms = models.IntegerField(default=0, verbose_name='缓存时间（毫秒）', help_text='必填')
    timeout_ms = models.IntegerField(default=0, verbose_name='超时时间（毫秒）', help_text='必填')
    alarm_total_count = models.IntegerField(default=0, verbose_name='报警总观测次数', help_text='必填，报警累计次数')
    alarm_fail_count = models.IntegerField(default=0, verbose_name='失败数报警阀值', help_text='必填，失败几次开始报警')
    alarm_timeout_count = models.IntegerField(default=0, verbose_name='超时报警阀值', help_text='必填')
    params_in = models.TextField(blank=True, verbose_name='入参', help_text='必填')
    params_in_sensitive = models.TextField(blank=True, verbose_name='入参敏感字段', help_text='必填')
    params_out_sensitive = models.TextField(blank=True, verbose_name='出参敏感字段', help_text='必填')
    remark = models.TextField(blank=True, verbose_name='备注', help_text='可以为空，补充信息')


class VendorApply(models.Model):
    """
    第三方供应商注册申请
    """
    org_code = models.CharField(max_length=64, blank=True, unique=True, verbose_name='机构编码', help_text='供应商的唯一标识。编码规则：机构中文全拼缩写（小写 ）+ 4位16进制随机编码，由业务输入系统 （系统应具备验证用户名唯一性功能）。用户账号由业务生成，生成的过程中，能够校验账号的唯一性。该账号也是供应商访问日志的登录账号')
    org_name_zh = models.CharField(max_length=64, blank=True, verbose_name='机构中文名称', help_text='如：白骑士，机构名称全局唯一，如果系统有多个相同名称，应该以序号自动区分。')
    org_number = models.CharField(max_length=64, blank=True, verbose_name='机构社会统一信用编码', help_text='必须，用于客户业务校核，客户的中文名称应该与社会统一信用代码一致 ')
    contact_person = models.CharField(max_length=64, blank=True, verbose_name='联系人', help_text='必填')
    contact_mobile = models.CharField(max_length=64, blank=True, verbose_name='联系人手机号码', help_text='必填')
    contact_email = models.CharField(max_length=64, blank=True, verbose_name='联系人邮箱', help_text='必填')
    org_address = models.CharField(max_length=256, blank=True, verbose_name='机构地址', help_text='可以为空')
    creator = models.CharField(max_length=64, blank=True, verbose_name='创建人', help_text='必填')
    creator_mobile = models.CharField(max_length=64, blank=True, verbose_name='创建人手机号码', help_text='必填')
    creator_email = models.CharField(max_length=64, blank=True, verbose_name='创建人邮箱', help_text='必填')
    score = models.IntegerField(default=0, verbose_name='评分', help_text='评分分为1~5分，最开始进入系统都为0分')
    risk = models.IntegerField(default=0, verbose_name='风险', help_text='风险分为1~5级，最开始进入系统都为0级，没有风险')
    communication = models.TextField(blank=True, verbose_name='沟通记录', help_text='与供应商沟通后，特别需要关注的问题')
    industry = models.CharField(max_length=64, blank=True, verbose_name='所属行业', help_text='必填')
    description = models.TextField(blank=True, verbose_name='描述', help_text='可以描述附加的客户需求')


class VendorApiApply(models.Model):
    """
    第三方供应商API接入申请
    """
    org_code = models.CharField(max_length=64, blank=True, verbose_name='机构账编码', help_text='供应商的唯一标识。编码规则：机构中文全拼缩写（小写 ）+ 4位16进制随机编码，由业务输入系统 （系统应具备验证用户名唯一性功能）。用户账号由业务生成，生成的过程中，能够校验账号的唯一性。该账号也是供应商访问日志的登录账号')
    product_name = models.CharField(max_length=64, blank=True, verbose_name='产品名称', help_text='必填')
    api_code = models.CharField(max_length=64, blank=True, verbose_name='API编码', help_text='必填，满足数据源编码规范，参考《数据产品编码规范》')
    product_description = models.CharField(max_length=64, blank=True, verbose_name='产品定义', help_text='必填，产品描述')
    api_url = models.CharField(max_length=64, blank=True, verbose_name='API访问URL', help_text='必填')
    params_in = models.TextField(blank=True, verbose_name='入参', help_text='必填')
    params_in_sensitive = models.TextField(blank=True, verbose_name='入参敏感字段', help_text='必填')
    params_out_sensitive = models.TextField(blank=True, verbose_name='出参敏感字段', help_text='必填')
    use_cache = models.BooleanField(default=False, verbose_name='是否缓存', help_text='必填，是否使用缓存热数据返回用户')
    cache_ms = models.IntegerField(default=0, verbose_name='缓存时间（毫秒）', help_text='必填')
    timeout_ms = models.IntegerField(default=0, verbose_name='超时时间（毫秒）', help_text='必填')
    field = models.CharField(max_length=64, blank=True, verbose_name='使用领域', help_text='必填')
    alarm_total_count = models.IntegerField(default=0, verbose_name='报警总观测次数', help_text='必填，报警累计次数')
    alarm_fail_count = models.IntegerField(default=0, verbose_name='失败数报警阀值', help_text='必填，失败几次开始报警')
    alarm_timeout_count = models.IntegerField(default=0, verbose_name='超时报警阀值', help_text='必填')
    start = models.CharField(max_length=64, blank=True, verbose_name='开始时间', help_text='API合同生效时间')
    send = models.CharField(max_length=64, blank=True, verbose_name='结束时间', help_text='API合同结束时间')
    version = models.CharField(max_length=64, blank=True, verbose_name='版本号', help_text='必填，API目前注册版本号')
    remark = models.TextField(blank=True, verbose_name='备注', help_text='可以为空，补充信息')


