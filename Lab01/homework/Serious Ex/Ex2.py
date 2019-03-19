from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
# 1. Create connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

# 1.1 Download page
raw_data = conn.read()
html_content = raw_data.decode('utf-8')

# with open("ctysua.html", "wb") as f:
#     f.write(raw_data)

# 2. Find ROI
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", id="tableContent")

tr_list = table.find_all("tr")

table_info = []
for i in range(len(tr_list)):
    td_list = tr_list[i].find_all("td")

    info_list = OrderedDict({})

    for j in range(len(td_list)):
        if td_list[j].string != None:
            if j == 0:
                info_list["Danh mục"] = td_list[j].string.strip()
            elif j == 1:
                info_list["Quý 4-2016"] = td_list[j].string.strip()
            elif j == 2:
                info_list["Quý 1-2017"] = td_list[j].string.strip()
            elif j == 3:
                info_list["Quý 2-2017"] = td_list[j].string.strip()
            elif j == 4:
                info_list["Quý 3-2017"] = td_list[j].string.strip()
    if info_list != {}:
        table_info.append(info_list)

pyexcel.save_as(records = table_info, dest_file_name = "thống_kê_cty_sữa.xlsx")
# for i in range(len(td_list)):
