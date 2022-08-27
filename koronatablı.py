import matplotlib.pyplot as plt
plt.title("13 AĞUSTOS KORONA VİRÜS GRAFİĞİ")
plt.figure(figsize=(12,8))
xeksen=["hasta sayısı","iyileşen kişi sayısı","aşı olan kişi sayısı","temaslı kişi sayısı"]
yeksen=[5000,3000,4500,10000]
plt.bar(xeksen,yeksen,color="pink",edgecolor="purple")

