def sumatoria(num1, num2):
    ans = num1+num2
    if ans%2==0:
        print("es par, y su suma y mitad es ",int(ans/2))
    else:
        print("no es par, y su suma es ",ans)

sumatoria(2,2)