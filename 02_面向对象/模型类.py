# @Author  : liangyf
# @Time    : 2021/8/26 20:46

# ORM 模型


class FieldMetaClass(type):
    # 创建模型类的元类
    def __new__(cls, name, bases, dic, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, dic)
        # 将类名转换成小写，对应数据表的名称
        table_name = name.lower()
        # 定义一个字典，用于存放字段属性
        fields = {}
        for k, v in dic.items():
            if isinstance(v, BaseModel):
                fields[k] = v
        # 将表名属性、字段属性保存
        dic['t_name'] = table_name
        dic['fields'] = fields
        return super().__new__(cls, name, bases, dic)


# 通过元类创建模型类父类 这样就可以实现属性与表字段的映射关系
# 然后模型类父类，使用__init__方法，可以一次设置多个属性，同时也要考虑字段属性个数是不确定的，所以使用了for循环
class BaseModel(metaclass=FieldMetaClass):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            # 设置属性 传入对象、属性名、属性值
            setattr(self, k, v)

    # 保存数据，生成对应的sql
    def save(self):
        # 获取表名
        t_name = self.t_name
        # 获取字段名
        fields = self.fields
        # 获取对应的字段值
        filed_dict = {}
        for filed in fields.keys():
            value = getattr(self, filed)
            filed_dict[filed] = value

        # 生成对应的sql语句
        sql = 'insert into {table_name} values {filed_value}'.format(table_name=t_name,
                                                                     filed_value=tuple(filed_dict.values()))
        print(sql)


class CharFild(BaseModel):
    def __init__(self, max_len=10):
        self.max_len = max_len

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 判断类型进行控制
        if isinstance(value, str):
            # 长度控制
            if len(value) <= self.max_len:
                self.value = value
            else:
                raise TypeError('超出最大长度')
        else:
            raise TypeError('need a str')


class IntFild(BaseModel):
    def __init__(self, max_len=10):
        self.max_len = max_len

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 判断类型进行控制
        if isinstance(value, int):
            self.value = value

        else:
            raise TypeError('need a int')


class BoolFild(BaseModel):
    def __init__(self, max_len=10):
        self.max_len = max_len

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        # 判断类型进行控制
        if isinstance(value, bool):
            self.value = value

        else:
            raise TypeError('need a bool')

# 生成模型类：
class User(BaseModel):
    # 用户模型类 在模型类中不会重写init方法，在它的父类中写init方法 它会自动继承
    username = CharFild()
    pwd = CharFild()
    age = IntFild()
    live = BoolFild()


a = User(username='12', pwd='19', age=20, live=True)
a.save()
