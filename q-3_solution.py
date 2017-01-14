import re

def find_sub_string(full_string):
    st = re.search(
        r'([A-Z]{2}[0-9]{3}/[0-9]{2}[A-Z]{1}[0-9]{2}/[0-9]{1}\s{1}[0-9]{3}[A-Z]{1}\s{1}[A-Z]{2})|([0-9]{3}/[0-9]{2}[A-Z]{1}[0-9]{2}\s{1}[0-9]{3}[A-Z]{1}\s{1}[A-Z]{2})|([A-Z]{1}[0-9]{3}/[0-9]{2}[A-Z]{1}[0-9]{2}\s{1}[0-9]{2}[A-Z]{1})|([A-Z]{2}[0-9]{3}/[0-9]{2}[A-Z]{1}[0-9]{2}/[0-9]{2})|([0-9]{3}/[0-9]{2}[A-Z]{1}[0-9]{2}/[A-Z]{1}\s{1})|([0-9]{3}/[0-9]{2}[A-Z]{2}[0-9]{2}/[A-Z]{2})|([0-9]{3}/[0-9]{2}[A-Z]{1}[0-9]{2}\s{1})|([0-9]{3}/[0-9]{2}-[0-9]{2}\s{1})',
        full_string)
    if st:
        return st.group(0)
    else:
        return None


full_string = "Continental ExtremeWinterContact Tire LT285/70R17/8 118Q BW"
sub_string = find_sub_string(full_string)
print("Match Sub String  = ", sub_string)