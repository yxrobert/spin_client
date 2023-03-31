server_name=pkcp
conf_file=server_config.yaml
awk '/"'"$server_name"'"/{print NR}' $conf_file
