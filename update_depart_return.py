from locale import currency
import xml.etree.ElementTree as ET
import datetime

def update_depart_return(X, Y):
    tree = ET.parse("test_payload1.xml")
    root = tree.getroot()
    for d_date in root.iter('DEPART'):
        depart_date = d_date.text
        formatted_date = datetime.datetime.strptime(depart_date[0:4] + "/" + depart_date[4:6] + "/" + depart_date[6:8], "%Y/%m/%d")
        modified_date = formatted_date + datetime.timedelta(days = 120)
        d_date.text = "".join(str(modified_date).split(' ')[0].split("-"))

    for r_date in root.iter('RETURN'):
        return_date = r_date.text
        formatted_date = datetime.datetime.strptime(return_date[0:4] + "/" + return_date[4:6] + "/" + return_date[6:8], "%Y/%m/%d")
        modified_date = formatted_date + datetime.timedelta(days = 120)
        r_date.text = "".join(str(modified_date).split(' ')[0].split("-"))
    
    tree.write("updated_dates.xml")

update_depart_return(12, 12)
