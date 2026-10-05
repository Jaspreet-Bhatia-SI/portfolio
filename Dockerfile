FROM nginx:alpine
COPY portfolio.html /usr/share/nginx/html/index.html
COPY profile.jpg /usr/share/nginx/html/profile.jpg
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
