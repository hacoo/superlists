
## Required packages:
   * nginx
   * Python3
   * Git
   * Pip/Pip3
   * virtualenv

   On ubuntu:
   sudo apt-get install nginx python3 git pip3 
   pip3 install virtualenv

## Nginx config
   See nginx.template.conf
   Replace SITENAME with your site name (e.g. strixnebulosa.space)
   

## Gunicorn config
   See gunicorn-upstart.template.conf
   Replace SITENAME with your site name (e.g. strixnebulosa.space)	

## Folder structure:
   In /home/user/sites/SITENAME:
   database
   source
   static
   virtualenv