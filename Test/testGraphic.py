import matplotlib.pyplot as plt
import datetime

# Тестовые значения цен биткоина (замените их на реальные данные)
prices = [5000000, 5020000, 4980000, 5050000, 5075000, 5100000, 5095000, 5120000, 5150000, 5145000, 5160000, 5200000, 5225000, 5250000, 5270000, 5300000, 5325000, 5340000, 5360000, 5380000, 5400000, 5420000, 5440000, 5460000, 5480000, 5500000, 5520000, 5540000, 5560000, 5580000, 5600000, 5620000, 5640000, 5660000, 5680000, 5700000, 5720000, 5740000, 5760000, 5780000, 5800000, 5820000, 5840000, 5860000, 5880000, 5900000, 5920000, 5940000, 5960000, 5980000, 6000000, 6020000, 6040000, 6060000, 6080000, 6100000, 6120000, 6140000, 6160000, 6180000, 6200000, 6220000, 6240000, 6260000, 6280000, 6300000, 6320000, 6340000, 6360000, 6380000, 6400000, 6420000, 6440000, 6460000, 6480000, 6500000, 6520000, 6540000, 6560000, 6580000, 6600000, 6620000, 6640000, 6660000, 6680000, 6700000, 6720000, 6740000, 6760000, 6780000, 6800000, 6820000, 6840000, 6860000, 6880000, 6900000, 6920000, 6940000, 6960000, 6980000, 7000000, 7020000, 7040000, 7060000, 7080000, 7100000, 7120000, 7140000, 7160000, 7180000, 7200000, 7220000, 7240000, 7260000, 7280000, 7300000, 7320000, 7340000, 7360000, 7380000, 7400000, 7420000, 7440000, 7460000, 7480000, 7500000, 7520000, 7540000, 7560000, 7580000, 7600000, 7620000, 7640000, 7660000, 7680000, 7700000, 7720000, 7740000, 7760000, 7780000, 7800000, 7820000, 7840000, 7860000, 7880000, 7900000, 7920000, 7940000, 7960000, 7980000, 8000000, 8020000, 8040000, 8060000, 8080000, 8100000, 8120000, 8140000, 8160000, 8180000, 8200000, 8220000, 8240000, 8260000, 8280000, 8300000, 8320000, 8340000, 8360000, 8380000, 8400000, 8420000, 8440000, 8460000, 8480000, 8500000, 8520000, 8540000, 8560000, 8580000, 8600000, 8620000, 8640000, 8660000, 8680000, 8700000, 8720000, 8740000, 8760000, 8780000, 8800000, 8820000, 8840000, 8860000, 8880000, 8900000, 8920000, 8940000, 8960000, 8980000, 9000000, 9020000, 9040000, 9060000, 9080000, 9100000, 9120000, 9140000, 9160000, 9180000, 9200000, 9220000, 9240000, 9260000, 9280000, 9300000, 9320000, 9340000, 9360000, 9380000, 9400000, 9420000, 9440000, 9460000, 9480000, 9500000, 9520000, 9540000, 9560000, 9580000, 9600000, 9620000, 9640000, 9660000, 9680000, 9700000, 9720000, 9740000, 9760000, 9780000, 9800000, 9820000, 9840000, 9860000, 9880000, 9900000, 9920000, 9940000, 9960000, 9980000, 10000000, 10020000, 10040000, 10060000, 10080000, 10100000, 10120000, 10140000, 10160000, 10180000, 10200000, 10220000, 10240000, 10260000, 10280000, 10300000, 10320000, 10340000, 10360000, 10380000, 10400000, 10420000, 10440000, 10460000, 10480000, 10500000, 10520000, 10540000, 10560000, 10580000, 10600000, 10620000, 10640000, 10660000, 10680000, 10700000, 10720000, 10740000, 10760000, 10780000, 10800000, 10820000, 10840000, 10860000, 10880000, 10900000, 10920000, 10940000, 10960000, 10980000, 11000000, 11020000, 11040000, 11060000, 11080000, 11100000, 11120000, 11140000, 11160000, 11180000, 11200000, 11220000, 11240000, 11260000, 11280000, 11300000, 11320000, 11340000, 11360000, 11380000, 11400000, 11420000, 11440000, 11460000, 11480000, 11500000, 11520000, 11540000, 11560000, 11580000, 11600000, 11620000, 11640000, 11660000, 11680000, 11700000, 11720000, 11740000, 11760000, 11780000, 11800000, 11820000, 11840000, 11860000, 11880000, 11900000, 11920000, 11940000, 11960000, 11980000, 12000000, 12020000, 12040000, 12060000, 12080000, 12100000, 12120000, 12140000, 12160000, 12180000, 12200000, 12220000, 12240000, 12260000]

# Создание списка временных меток для оси x
timestamps = []
current_time = datetime.datetime.now()
for i in range(len(prices)):
    timestamps.append(current_time - datetime.timedelta(minutes=i*10))

# Построение графика
plt.plot(timestamps, prices)
plt.xlabel('Время')
plt.ylabel('Цена биткоина')
plt.title('График цен биткоина за 24 часа')
plt.xticks(rotation=45)
plt.grid(True)



# Отображение графика
plt.show()