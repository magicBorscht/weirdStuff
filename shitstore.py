for i, _a in enumerate(strategies):
    P_M[i] = {}
    for j, _p in enumerate(needlist):
        if _a == _p:
            P_M[i][j] = _a[0] * d_prft[0] + _a[1] * j_prft[0]
        elif _a[0] > _p[0] and _a[1] == _p[1]:
            P_M[i][j] = (_p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[1]) + _a[1] * j_prft[
                0]  # p * prices[1] + (_a - _p) * prices[0]
        elif _a[0] == _p[0] and _a[1] > _p[1]:
            P_M[i][j] = (_p[1] * j_prft[0] + (_a[1] - _p[1]) * j_prft[1]) + _a[0] * d_prft[0]
        elif _a[0] > _p[0] and _a[1] > _p[1]:
            P_M[i][j] = (_p[1] * j_prft[0] + (_a[1] - _p[1]) * j_prft[1]) + (
            _p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[1])
        elif _a[0] < _p[0] and _a[1] == _p[1]:
            P_M[i][j] = (_p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[2]) + _a[1] * j_prft[0]
        elif _a[0] == _p[0] and _a[1] < _p[1]:
            P_M[i][j] = _a[0] * d_prft[0] + (_p[1] * j_prft[0] + (_a[1] - _p[1]) * j_prft[2])
        elif _a[0] < _p[0] and _a[1] < _p[1]:
            P_M[i][j] = (_p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[2]) + (
            _p[1] * j_prft[0] + (_a[1] - _p[1]) * j_prft[2])
        # Мне реально стыдно на этом моменте.
        elif _a[0] > _p[0] and _a[1] < _p[1]:
            P_M[i][j] = (_p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[1]) + (
            _p[1] * j_prft[0] + (_a[1] - _p[1]) * j_prft[2])
        elif _a[0] < _p[0] and _a[1] > _p[1]:
            P_M[i][j] = (_p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[2]) + (
            _p[0] * d_prft[0] + (_a[0] - _p[0]) * d_prft[1])
        else:
            print("that should not happen")  # P_M[i][j] = _a * prices[1] + (_p - _a) * prices[2]
            print(_a, _p)