#!/usr/bin/env python
# coding: utf-8

# In[ ]:


作業1:Data Science for Good:Center for Policing Equity
        1.你選的這組資料為何重要
            對單一市中心治安進行分析，如果成功並且其他市中心擁有差不多數據，可以藉此套用並且解決此案需要的其他問題
        2.資料從何而來:
            美國司法資料庫，由警察單位
        3.蒐集而來的資料型態為何
            有csv、dbf.cpg、prj等不同來源資料，資料內文字、數字等資料型態眾多
        4.這組資料想解決的問題如何評估
            首先需要將不同來源的資料整合成一份，並且將其歸類，每份資料有meta data可以藉由此合併或連結，但是資料混亂需要不少時間整理，之後進行分析並以圖形化顯示


# In[ ]:


作業2:
        1.核心問題為何(tips:如何定義「提升業績&你的假設」)
            如果是一個自由載客車隊，提升業績可能有兩個曾面，一是每小時平均載客量或是載客距離，與整日載客距離，如果要提升業績應該朝向司機載客途中皆沒有中斷為最多
        2.資料從何而來
            對於這些可以於司機車上裝置GPS追蹤，並將載客點與下客點匯集成圖
        3.蒐集來的資料型態應該為座標數字，並有array
        4.如果資料蒐集完成並分析完成，可以將一部份司機投放於載客點及下客點重複區域，看是否業績有所成長


# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


w = 3
b = 0.5

x_lin = np.linspace(0, 100, 101)

y = (x_lin + np.random.randn(101) * 5) * w + b

plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[5]:


y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[17]:


def mean_absolute_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    mae = MAE = sum(abs(y - yp)) / len(y)
    return mae

MAE = mean_absolute_error(y, y_hat)
print("The Mean absolute error is %.3f" % (MAE))


# In[ ]:


請寫一個函式用來計算Mean Square Error


# In[32]:


def mean_square_error(y, yp):
    """
    計算 MAE
    Args:
        - y: 實際值
        - yp: 預測值
    Return:
        - mae: MAE
    """
    mse = MSE = sum((y - yp)**2) / len(y)
    return mse

MSE = mean_square_error(y, y_hat)
print("The Mean square error is %.3f" % (MSE))

