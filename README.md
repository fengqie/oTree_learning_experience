# oTree_Learning_Experience

This project will share **my experience** with people who want to learn oTree. It aims to help those who cannot find their way in learning the oTree package. 

Learning oTree is **difficult**, so before starting, ask yourself “Must I study it to achieve my goal?” If yes, go on. Otherwise, turn off this experience post. 

> [!IMPORTANT]
>
> Please pay attention! The official guidelines and forum are so important that if you encounter problems, go back and read them carefully.

This post contains the following sections: S1 Simple Introduction to oTree; S2 Knowledge and Materials Preparations before Learning; S3 Learning Path and Some Details; S4 My Experimental program Case.

## S1 Simple Introduction

> ​	“The most powerful platform for behavioral research and experiments”  [oTree: Behavioral research platform](https://www.otree.org/).

The most important thing here is that oTree is developed based on Python.  You can see other introductions on its homepage.

##  S2 Knowledge and Materials Preparations Before learning

### s2.1 Knowledge

First, **get enough knowledge of experimental theory**. Before programming your experiment or program, you must have a clear idea of what you need, especially for those who use it to program their experiments. You should guarantee the experiment design is OK, otherwise you may go far away. Which one do you need, a computer experiment or a real effort experiment? (But if you just want to have fun, please ignore what I have just said and go ahead.)

Second, **get enough knowledge about Python**. As I have just introduced, the oTree is based on Python, not to mention its grammar. I have passed the National Computer Rank Examination and achieved level 2. It may be a conference point for you to assess your position.

Third, given the complexity of your experiment (like a multiplayer game, just as the case in this post’s end), you also need knowledge about 1)**web design**; 2)**simple database operation**( like SQL series); 3) **Front-end and back-end interactions**. Next section I will introduce you to some videos for a quick start.

### s2.2 Materials

In this section, I will introduce some materials you should prepare before programming your program.

#### s.2.2.1 Technology

As a package designed by (Daniel L. Chen et al., 2016), you should get ready for the scientific network (**V/P/N**). Otherwise, you cannot get to the forum which is so important that you must not ignore it. Besides, the **LLM** is essential for a layman to program, it can help you to understand the function of codes(when you read the official guidelines & encounter errors when you run the program etc.). 

But remember that you are the owner of the experiment and hold your own opinion about the answers from the LLM! Try to use the LLM as an advisor not the  Book of Answers. It just helps you not replace you.

#### s2.2.2 Video

As you can see in the next videos, oTree could be used as an attachment package or use its online Hub. The latter is easier , correspondingly, it has fewer features. I recommend the **text editor** more, such as  *Pycharm* (you can apply the professional edition for students freely, but I do not know whether the community edition is enough). So if you want to use Pycharm, learn it simply by 【2024 PyCharm保姆级基础】 https://www.bilibili.com/video/BV1nhmqYPEgm/?share_source=copy_web&vd_source=aed3a55177b263933b97c84e9ac20051.

Sometimes you are just like a full-stack engineer who needs to note many things. But the good news is you can learn all of these through Django(【最新Python的web开发全家桶（django+前端+数据库）】 https://www.bilibili.com/video/BV1rT4y1v7uQ/?share_source=copy_web&vd_source=aed3a55177b263933b97c84e9ac20051). 

Here is another web [菜鸟教程 - 学的不仅是技术，更是梦想！](https://www.runoob.com/) . You can treat it as a textbook

> [!NOTE]
>
> ***Attention!***  This does not mean to be an expert in programming, choose what you need. Treat it as a pre-knowledge, which will not decide whether you can develop a good experiment, but may help you to get farther down the road.

Next are some videos that might help you to get an intuitive understanding of oTree programming. 

【oTree简介-上手版】 https://www.bilibili.com/video/BV1h34y1x7i9/?share_source=copy_web&vd_source=aed3a55177b263933b97c84e9ac20051

【经济学家的python编程】 https://www.bilibili.com/video/BV1JE411W7bR/?share_source=copy_web&vd_source=aed3a55177b263933b97c84e9ac20051

【Otree Hub创建猜数字博弈】 https://www.bilibili.com/video/BV14a411a7aP/?share_source=copy_web&vd_source=aed3a55177b263933b97c84e9ac20051

【oTree复刻-JEBO-剑前盟约】 https://www.bilibili.com/video/BV1bT4y1s77c/?share_source=copy_web&vd_source=aed3a55177b263933b97c84e9ac20051

Finally, here are the official instructional videos:[oTree tutorials - YouTube](https://www.youtube.com/@otreetutorials)

#### s.2.2.3 Document

You may need some supporting documents, I will share them and tell you how to get them.

Official guidelines: [oTree — oTree documentation](https://otree.readthedocs.io/en/latest/)

> [!IMPORTANT]
>
> **Forum**: [Public Projects](https://www.otreehub.com/projects/?featured=1). You can also enter this page from the **document web**. You can express your confusion or help others in the forum.
>
> Find the example code, and use it as the tool book. (You can save the code as a PDF so that you can make it a code case manual) 

> [!NOTE]
>
> Recently, the browser will break down when you click the **example code**, I prepared the PDF for you (not the newest, https://pan.baidu.com/s/1z27pXnR8Utp08AuFeYsnGA?pwd=1114 ).

## S3 Learning Path and Some Details

### s3.1 Learning Path

Given you have basic knowledge about Python, here is my learning path:

Browse the **document page** of oTree,  and take a brief look at what oTree can accomplish.

—->Recall what your experiment wants to achieve, and pay attention to these functions.

—->Study the django3 and prepare the package you may use.

—–>Prepare the computer environment [that means to download the software/package you may need]

—-> Watch the videos about oTree programming(especially those based on the Pycharm)

—->Start to program.

> [!TIP]
>
> ==Starting is ***vital***, **remember that practice makes perfect!**==
>
> Don't be afraid to make mistakes, there are a lot of opportunities to try. 
>
> 



### s3.2 Details

In this section, I will tell you some code which may save you time to find.

1. Commonly, we install the oTree package by `pip install -U otree` in the **command shell**. But sometimes you need to add the Mirror site(i.e. install -U otree -i mirror site). Here is the relevant experience post [pip 下载安装时使用清华大学镜像（各种国内源配置）_pip清华镜像网址-CSDN博客](https://blog.csdn.net/sjjsaaaa/article/details/110096059)

2. ````shell
   cd folders(where you create your program)
   otree startproject your_project_name
   #Above is how to start your otree project
   ````

3. After you have deployed your interpreter environment (that means you have installed all the packages you need and deployed them correctly), open your otree project folder using Pycharm, and program your project step by step.

4. ```shell
   # You can start the experiment in the command shell. 
   cd your_project_path # i.e.where your otree program is
   otree devserver
   # Open your browser to http://localhost:8000/. You should see the oTree demo site.
   # pay attention please, this is a debugging command.
   # for running your experiment formally
   cd your_project_path # i.e.where your otree program is
   otree prodserver 端口号(e.g. 8000, 80, 70 etc.)
   ```

5. If you've gotten this far in deploying the experiment, please refer to **Document_Server setup_Windows Server (advanced)**. If you still have problems, ask the ChatGPT. 
## S4 My Case

Please refer to the file.

