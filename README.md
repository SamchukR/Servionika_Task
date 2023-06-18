# Тестовое задание 
## задания 2.1 и 2.2 находятся в ветке main
## задания 1.1 и 2.1 находятся в ветке master
## При запуске 2.2 необходибо задать параметр virtual_ip пример: ansible-playbook -i inventory servs_conf.yml -e "virtual_ip=192.168.1.100"
Задание 2.1
Создать 2 WEB сервера с выводом страницы «Hello Word! \n Server 1» (аналогично для второго Server 2). Сделать балансировку нагрузки (HA + keepalived), чтобы при обновлении страницы мы попадали на любой из WEB серверов(Для балансировки можно сделать 2 отдельных сервера, в сумме 4).
Будет плюсом использование Docker.
Работу стенда продемонстрировать в отчёте.
Задание 2.2(усложненное)
Написать роль на Ansible по развёртыванию стенда из Задание 2.1. Должен быть описан файл инвентори с серверами по примеру:
[loadbalancers]
ha1 ansible_host=10.10.1.1
ha2 ansible_host=10.10.1.2
[webservers]
web1 ansible_host=10.10.1.1
web2 ansible_host=10.10.1.2
Можно написать 1 большую роль, либо 3 роли и потом вызвать их поочёрдно.
Роль Nginx – устанавливает и конфигурирует Nginx на группе хостов [webservers].
Роль HA Proxy – устанавливает и конфигурирует HA Proxy на группе хостов [loadbalancers].
Роль Keepalived – устанавливает и конфигурирует Keepalived на группе хостов [loadbalancers].
Конфиги nginx, HA proxy, keepalived оформить, используя шаблоны Jinja2(язык шаблонов).
Пример использования шаблонов Jinja2:
В каталоге /roles/nginx/templates создаётся конфиг nginx.conf, далее в роле мы используем данный конфиг
- name: Add nginx config
	  template:
	     src=template/nginx.conf
     dest=/etc/nginx/nginx.conf

Итоговый playbook объединяющий три роли может выглядеть следующим образом.
- hosts: webservers
become: yes
roles:
- nginx
- hosts: loadbalancers
become: yes
roles:
- ha-proxy
- hosts: loadbalancers
become: yes
roles:
- keepalived
Запуск итогового playbook примерно выглядит так
Ansible-playbook –i <inventory_file>  nginx_haproxy_ha.yml

Прислать файлы на проверку, работу стенда продемонстрировать в отчёте.
Для 2.2 используйте OS Ubuntu от 20.04 для всех нод.
