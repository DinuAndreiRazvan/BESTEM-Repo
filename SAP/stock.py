from main import Stock
def stock_check(stocks):
    previousId = stocks[0].product_ID
    sales_sum = 0
    k = 0

    for i in range(1, len(stocks)):
        p = stocks[i]
        if (p.product_ID != previousId):
            if(k >= 5):
                start = stocks[i-k].date
                end = stocks[i-1].date
                dif = (end - start).days / 30
                medie = sales_sum / dif
                print(previousId, medie, dif)
            sales_sum = 0
            k = 0

        sales_sum += p.sales
        k += 1
        previousId = p.product_ID

    if(k >= 5):
        start = stocks[i-k].date
        end = stocks[i-1].date
        dif = (end - start).days / 30
        medie = sales_sum / dif
        print(previousId, medie, dif)