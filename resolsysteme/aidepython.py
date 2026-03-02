import sympy as sy
CoeffAa,CoeffAb,CoeffAc,CoeffAd,CoeffAe,CoeffAf,CoeffAg,CoeffAh=sy.symbols("CoeffAa,CoeffAb,CoeffAc,CoeffAd,CoeffAe,CoeffAf,CoeffAg,CoeffAh")
CoeffAi,CoeffAj,CoeffAk,CoeffAl,CoeffAm,CoeffAn,CoeffAo,CoeffAp=sy.symbols("CoeffAi,CoeffAj,CoeffAk,CoeffAl,CoeffAm,CoeffAn,CoeffAo,CoeffAp")

CoeffBa,CoeffBb,CoeffBc,CoeffBd,CoeffBe,CoeffBf,CoeffBg,CoeffBh=sy.symbols("CoeffBa,CoeffBb,CoeffBc,CoeffBd,CoeffBe,CoeffBf,CoeffBg,CoeffBh")
CoeffBi,CoeffBj,CoeffBk,CoeffBl,CoeffBm,CoeffBn,CoeffBo,CoeffBp=sy.symbols("CoeffBi,CoeffBj,CoeffBk,CoeffBl,CoeffBm,CoeffBn,CoeffBo,CoeffBp")

MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH=sy.symbols("MatA,MatB,MatC,MatD,MatE,MatF,MatG,MatH")
MatI,MatJ,MatK,MatL,MatM,MatN,MatO,MatP=sy.symbols("MatI,MatJ,MatK,MatL,MatM,MatN,MatO,MatP")

# M = sy.Matrix(([MatA,MatB],[MatC,MatD]))
# N = M**3
# print("Coefficients de M au cube avec dim(M)=2x2")
# for i in range(len(N)) :
#     tmp = str(N[i])
#     tmp = tmp.replace("Mat", "\Mat")
#     tmp = tmp.replace(" ", "")
#     print(tmp)
# 
# P = sy.Matrix(([MatA,MatB,MatC],[MatD,MatE,MatF],[MatG,MatH,MatI]))
# Q = P**3
# print("Coefficients de M au cube avec dim(M)=3x3")
# for i in range(len(Q)) :
#     tmp = str(Q[i])
#     tmp = tmp.replace("Mat", "\Mat")
#     tmp = tmp.replace(" ", "")
#     print(tmp)
# 
# R = sy.Matrix(([MatA,MatB,MatC,MatD],[MatE,MatF,MatG,MatH],[MatI,MatJ,MatK,MatL],[MatM,MatN,MatO,MatP]))
# S = R**3
# print("Coefficients de M au cube avec dim(M)=4x4")
# for i in range(len(S)) :
#     tmp = str(S[i])
#     tmp = tmp.replace("Mat", "\Mat")
#     tmp = tmp.replace(" ", "")
#     print(tmp)
# 
# T = R.inv()
# print("Coefficients de l'inverse de M avec dim(M)=4x4")
# for i in range(len(T)) :
#     tmp = str(T[i])
#     tmp = tmp.replace("Mat", "\Mat")
#     tmp = tmp.replace(" ", "")
#     print(tmp)