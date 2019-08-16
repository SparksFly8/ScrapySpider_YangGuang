# 实战Scrapy之阳光政务平台爬虫项目
![](https://img.shields.io/badge/license-MIT-success.svg)
[![](https://img.shields.io/badge/Blog-SL_World-orange.svg)](https://blog.csdn.net/SL_World/article/details/90728386)
> 本项目用于爬取「东莞阳光热线问政平台」中的投诉标题、申诉部门、处理状态、发布时间、详情页面中的投诉文本内容以及图片并存储到MongoDB中。

【本文博客】：https://blog.csdn.net/SL_World/article/details/99096210

【项目描述】：爬取「东莞阳光热线问政平台」中的投诉标题、申诉部门、处理状态、发布时间、详情页面中的投诉文本内容以及图片。

【网站地址】：[东莞阳光热线问政平台](http://wz.sun0769.com/index.php/question/questionType?type=4&page=0)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190816231310964.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190816223316312.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)

【爬取结果】：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190816225817282.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L1NMX1dvcmxk,size_16,color_FFFFFF,t_70)

爬虫文件位于：`YangGuang/spiders/yg.py`

管道文件位于：`YangGuang/pipelines.py`

项目文件位于：`YangGuang/items.py`

本项目的主要模块代码，已在必要的地方做了详细注释
