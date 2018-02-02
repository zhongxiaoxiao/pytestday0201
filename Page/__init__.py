from selenium.webdriver.common.by import By
"""
设置
"""
#点击搜索按钮
search_btn = (By.ID,"com.android.settings:id/search")
#输入内容
search_text = (By.ID,"android:id/search_src_text")
#点击返回按钮
search_return_btn = (By.CLASS_NAME,"android.widget.ImageButton")