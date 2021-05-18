# LearnPython
这是用来学习python的一个仓库。接触python首先为完成“现代力学分析软件概论”课程，但进度缓慢，需要课后自学，所以在以此仓库作为笔记

* ## 2021/5/11
第一节课程，介绍了pycharm编辑器，介绍了jupytor notebook文件格式。介绍了anaconda科学计算环境，numpy包，matplot包，pandas包等
完成了使用VScode进行文件夹内的环境配置
> [环境配置](关于环境配置.md "关于环境配置")

了解jupytor notebook文件格式的编辑，尤其是使用google colab在线进行简单的数据处理
> [google colab](https://colab.research.google.com/notebooks/ "google colab")

* ## 2021/5/18
第二节课程，简单的数据处理，matplot.pyplot包的简单实用
解决了“使用Matplotlib以非阻塞方式绘图”的问题
> [使用Matplotlib以非阻塞方式绘图](http://www.imooc.com/wenda/detail/590321)

解决问题的样例见文件夹2021-5-18中[test_file](/date2021-5-18/test_file.py)
为同时展示多个figure，而不是关闭其中一个以后再出现另一个，需要有如下操作
> \>>>plt.show(block = False) \n
> \>>>plt.show() 
