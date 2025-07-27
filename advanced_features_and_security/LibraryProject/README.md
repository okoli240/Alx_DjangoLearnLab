# Deployment Configuration: Enabling HTTPS with Nginx

1. Obtain SSL Certificate:
   - Use Let's Encrypt:
     ```bash
     sudo apt install certbot python3-certbot-nginx
     sudo certbot --nginx -d yourdomain.com
     ```

2. Configure Nginx:
   ```nginx
   server {
       listen 80;
       server_name yourdomain.com www.yourdomain.com;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name yourdomain.com www.yourdomain.com;

       ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

       location = /favicon.ico { access_log off; log_not_found off; }
       location / {
           include proxy_params;
           proxy_pass http://unix:/path/to/your/app.sock;
       }
   }

