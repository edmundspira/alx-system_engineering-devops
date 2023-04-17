# Puppet commands to configure Nginx web server

exec {'install':
  command  => 'sudo apt update ; sudo apt -y install nginx ; echo "Holberton School" | sudo tee /var/www/html/index.html',
  provider => shell,
}
exec {'default':
  command  => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4 permanent;/" /etc/nginx/sites-available/default ; sudo service nginx restart',
  provider => shell,
}
