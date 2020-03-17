# -
放入centos中的定时脚本

服务器设置定时任务
crontab -u root -e //-u规定使用者，-e表示修改
(分) （时） （日） （月） （周几） 执行命令 执行目录
举例：0 8 * * * python3 ~/pc/pc.py  含义：每天早八点执行pc.py文件
 开启定时任务：service crond start
 查看定时任务:crontab -u root -l
