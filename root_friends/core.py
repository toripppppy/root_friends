import math

### レベル
# 初項
i = 10
# 公比
a = 1.5

class Core:
    def calc_lv(self, count) -> int:
        # 等比数列の公式から逆算
        lv = math.floor( math.log((count / i) * (a - 1) + 1, a) )
        return lv