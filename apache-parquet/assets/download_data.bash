# download data
wget -i urls.txt

# unzip data and remove zips
 unzip "*.zip" -d ./data  && rm -rf *.zip