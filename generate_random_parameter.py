#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
__author__ = 'wei.zhang'
import sys

sys.path.append("..")

"""
创建随机参数
"""


class generateRandomParameter:
    import random
    def generateName(self):
        """
        创建一个随机的名字
        :return:
        """
        FAMILY_NAME = ["赵", "钱", "孙", "李", "周", "吴", "郑", "王", "冯", "陈", "楮", "卫", "蒋", "沈", "韩", "杨", "朱", "秦", "尤",
                       "许", "何", "吕", "施", "张", "孔", "曹", "严", "华", "金", "魏", "陶", "姜", "戚", "谢", "邹", "喻", "柏", "水",
                       "窦", "章", "云", "苏", "潘", "葛", "奚", "范", "彭", "郎", "鲁", "韦", "昌", "马", "苗", "凤", "花", "方", "俞",
                       "任", "袁", "柳", "酆", "鲍", "史", "唐", "费", "廉", "岑", "薛", "雷", "贺", "倪", "汤", "滕", "殷", "罗", "毕",
                       "郝", "邬", "安", "常", "乐", "于", "时", "傅", "皮", "卞", "齐", "康", "伍", "余", "元", "卜", "顾", "孟", "平",
                       "黄", "和", "穆", "萧", "尹", "姚", "邵", "湛", "汪", "祁", "毛", "禹", "狄", "米", "贝", "明", "臧", "计", "伏",
                       "成", "戴", "谈", "宋", "茅", "庞", "熊", "纪", "舒", "屈", "项", "祝", "董", "梁", "杜", "阮", "蓝", "闽", "席",
                       "季", "麻", "强", "贾", "路", "娄", "危", "江", "童", "颜", "郭", "梅", "盛", "林", "刁", "锺", "徐", "丘", "骆",
                       "高", "夏", "蔡", "田", "樊", "胡", "凌", "霍", "虞", "万", "支", "柯", "昝", "管", "卢", "莫", "经", "房", "裘",
                       "缪", "干", "解", "应", "宗", "丁", "宣", "贲", "邓", "郁", "单", "杭", "洪", "包", "诸", "左", "石", "崔", "吉",
                       "钮", "龚", "程", "嵇", "邢", "滑", "裴", "陆", "荣", "翁", "荀", "羊", "於", "惠", "甄", "麹", "家", "封", "芮",
                       "羿", "储", "靳", "汲", "邴", "糜", "松", "井", "段", "富", "巫", "乌", "焦", "巴", "弓", "牧", "隗", "山", "谷",
                       "车", "侯", "宓", "蓬", "全", "郗", "班", "仰", "秋", "仲", "伊", "宫", "宁", "仇", "栾", "暴", "甘", "斜", "厉",
                       "戎", "祖", "武", "符", "刘", "景", "詹", "束", "龙", "叶", "幸", "司", "韶", "郜", "黎", "蓟", "薄", "印", "宿",
                       "白", "怀", "蒲", "邰", "从", "鄂", "索", "咸", "籍", "赖", "卓", "蔺", "屠", "蒙", "池", "乔", "阴", "郁", "胥",
                       "能", "苍", "双", "闻", "莘", "党", "翟", "谭", "贡", "劳", "逄", "姬", "申", "扶", "堵", "冉", "宰", "郦", "雍",
                       "郤", "璩", "桑", "桂", "濮", "牛", "寿", "通", "边", "扈", "燕", "冀", "郏", "浦", "尚", "农", "温", "别", "庄",
                       "晏", "柴", "瞿", "阎", "充", "慕", "连", "茹", "习", "宦", "艾", "鱼", "容", "向", "古", "易", "慎", "戈", "廖",
                       "庾", "终", "暨", "居", "衡", "步", "都", "耿", "满", "弘", "匡", "国", "文", "寇", "广", "禄", "阙", "东", "欧",
                       "殳", "沃", "利", "蔚", "越", "夔", "隆", "师", "巩", "厍", "聂", "晁", "勾", "敖", "融", "冷", "訾", "辛", "阚",
                       "那", "简", "饶", "空", "曾", "毋", "沙", "乜", "养", "鞠", "须", "丰", "巢", "关", "蒯", "相", "查", "后", "荆",
                       "红", "游", "竺", "权", "逑", "盖", "益", "桓", "公", "万俟", "司马", "上官", "欧阳", "夏侯", "诸葛", "闻人", "东方",
                       "赫连", "皇甫", "尉迟", "公羊", "澹台", "公冶", "宗政", "濮阳", "淳于", "单于", "太叔", "申屠", "公孙", "仲孙", "轩辕", "令狐",
                       "锺离", "宇文", "长孙", "慕容", "鲜于", "闾丘", "司徒", "司空", "丌官", "司寇", "仉", "督", "子车", "颛孙", "端木", "巫马",
                       "公西", "漆雕", "乐正", "壤驷", "公良", "拓拔", "夹谷", "宰父", "谷梁", "晋", "楚", "阎", "法", "汝", "鄢", "涂", "钦",
                       "段干", "百里", "东郭", "南门", "呼延", "归", "海", "羊舌", "微生", "岳", "帅", "缑", "亢", "况", "后", "有", "琴", "梁丘",
                       "左丘", "东门", "西门", "商", "牟", "佘", "佴", "伯", "赏", "南宫", "墨", "哈", "谯", "笪", "年", "爱", "阳", "佟"]
        LAST_NAME = ["资", "屋", "击", "速", "顾", "泪", "洲", "团", "圣", "旁", "堂", "兵", "七", "露", "园", "牛", "哭", "旅", "街", "劳",
                     "型", "烈", "姑", "陈", "莫", "鱼", "异", "抱", "宝", "权", "鲁", "简", "态", "级", "票", "怪", "寻", "杀", "律", "胜",
                     "份", "汽", "右", "洋", "范", "床", "舞", "秘", "午", "登", "楼", "贵", "吸", "责", "例", "追", "较", "职", "属", "渐",
                     "左", "录", "丝", "牙", "党", "继", "托", "赶", "章", "智", "冲", "叶", "胡", "吉", "卖", "坚", "喝", "肉", "遗", "救",
                     "修", "松", "临", "藏", "担", "戏", "善", "卫", "药", "悲", "敢", "靠", "伊", "村", "戴", "词", "森", "耳", "差", "短",
                     "祖", "云", "规", "窗", "散", "迷", "油", "旧", "适", "乡", "架", "恩", "投", "弹", "铁", "博", "雷", "府", "压", "超",
                     "负", "勒", "杂", "醒", "洗", "采", "毫", "嘴", "毕", "九", "冰", "既", "状", "乱", "景", "席", "珍", "童", "顶", "派",
                     "素", "脱", "农", "疑", "练", "野", "按", "犯", "拍", "征", "坏", "骨", "余", "承", "置", "臓", "彩", "灯", "巨", "琴",
                     "免", "环", "姆", "暗", "换", "技", "翻", "束", "增", "忍", "餐", "洛", "塞", "缺", "忆", "判", "欧", "层", "付", "退",
                     "摇", "弄", "桌", "熟", "诺", "宣", "银", "势", "奖", "宫", "忽", "套", "康", "供", "优", "课", "鸟", "喊", "降", "夏",
                     "困", "刘", "罪", "亡", "鞋", "健", "模", "败", "伴", "守", "挥", "鲜", "财", "孤", "枪", "禁", "恐", "伙", "杰", "迹",
                     "妹", "藸", "遍", "盖", "副", "坦", "牌", "江", "顺", "秋", "萨", "菜", "划", "授", "归", "浪", "听", "凡", "预", "奶",
                     "雄", "升", "碃", "编", "典", "袋", "莱", "含", "盛", "济", "蒙", "棋", "端", "腿", "招", "释", "介", "烧", "误", "乾",
                     "坤"]
        familyName = self.random.choice(FAMILY_NAME)
        lastName = self.random.sample(LAST_NAME, self.random.randint(1, 2))
        return familyName + "".join(lastName)

    def generatePhoneNumber(self):
        """
        创建一个随机的手机号
        :return:
        """
        THEM_ROUGHLY = ["147", "157", "150", "151", "152", "153", "155", "156", "157", "158", "159", "130", "131",
                        "132", "133", "134", "135", "136", "137", "138", "139", "180", "182", "185", "186", "187",
                        "188", "189 "]
        themRoughly = self.random.choice(THEM_ROUGHLY)
        number = self.random.sample([str(i) for i in range(10)], 8)
        return themRoughly + "".join(number)

    def calculateIdCardTailNumber(self, idCard):
        """
        计算身份证号最后一位数
        :param idCard:
        :return:
        """
        coefficient = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # idCardNumber = map(lambda a: a[0] * a[1],[i for i in zip(coefficient, [int(i) for i in idCard])])
        idCardNumber = [a*b for a,b in zip(coefficient, [int(i) for i in idCard])]
        endNumber = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        idCardSun = 0
        for i in idCardNumber: idCardSun += i
        return endNumber[idCardSun % 11]

    def generateIdCard(self):
        """
        创建一个随机的身份证
        :return:
        """
        AdministrativeCode = open('AdministrativeCode.txt', 'r')
        ACode = self.random.choice(AdministrativeCode.read().split(','))
        randomYear = self.random.randint(1950, 2010)
        randomMonth = str(self.random.randint(1, 12))
        if randomMonth in ["1", "3", "5", "7", "8", "10", "12"]:
            randomDay = self.random.randint(1, 31)
        elif randomMonth in '2':
            randomDay = self.random.randint(1, 29) if (randomYear % 4 == 0 and randomYear % 100 != 0) \
                                                      or randomYear % 400 == 0 else self.random.randint(1, 28)
        else:
            randomDay = self.random.randint(1, 30)

        randomMonth = "0" + randomMonth if int(randomMonth) < 10 else randomMonth
        randomDay = "0" + str(randomDay) if randomDay < 10 else str(randomDay)

        sequenceCodes = self.random.randint(0, 999)
        if sequenceCodes < 100:
            sequenceCodes = "0" + str(sequenceCodes)
        elif sequenceCodes < 10:
            sequenceCodes = "0" + str(sequenceCodes)
        else:
            sequenceCodes = str(sequenceCodes)
        diCardNumber = ACode + str(randomYear) + randomMonth + randomDay + sequenceCodes
        return diCardNumber + self.calculateIdCardTailNumber(diCardNumber)

    def getListElement(self, elementList):
        return self.random.choice(elementList)

    def randomrepaymentMethod(self, allow, term):
        """
        随机一个还款方式
        :param allow: 获取还款方式接口返回数据
        :param term: 期数
        :return:
        """
        repaymentMethod = {
            "allowAverageCapitalPlusInterest": ("1001", "一次还清"),
            "allowMonthPayInterest": ("1002", "按月付息"),
            "allowMonthSamePay": ("1003", "等本等息"),
            "allowSettle": ("1004", "等额本息")
        }
        allowlist = []
        for allowkey in repaymentMethod.keys():
            if allow.get(allowkey) == "1":
                allowlist.append(repaymentMethod.get(allowkey))
        if term != "1" and ("1001", "一次还清") in allowlist:
            allowlist.remove(("1001", "一次还清"))
        return self.getListElement(allowlist)
