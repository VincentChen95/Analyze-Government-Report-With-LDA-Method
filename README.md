# Analyze-Government-Report-With-LDA
<br>Hello guys, government working report is related with everyone's life. I want to use LDA methods to analyze it and acquire useful information.
## Data Pre-process
<br>Firstly, I coded a web crawler to collect Government Working Report from 1954 to 2018. It contains 50 documents. Then I use "jieba" package to segementate the words.
## Data Visualization
<br>I utilized the "word cloud" method to visualiza reports. I select 5 documents to compare. It shows the trend of government task.
<br>![2018](https://user-images.githubusercontent.com/36937088/50495387-a6100180-09dd-11e9-9a78-30cd884b7365.jpeg)
## Result
<br>This is the trainin result of LDA model. I select 5 topics. Because the sample size is insufficient, this model cannot show a perfect result. However, there are still something we can conclude from result. 
<br>For topic 0, it focus on "jobs". For topic 1, it is related to "development". Topic 2, it is about "revolution". For topic 3, it is "agriculture". Topic 4 concentrate on "economy".
<br>Topic 0:
<br>发展 建设 推进 经济 改革 加强 加快 实施 政府 社会 工作 提高 促进 就业 增长
<br>Topic 1:
<br>发展 建设 经济 加强 工作 继续 改革 企业 社会 积极 进一步 政府 稳定 国家 市场
<br>Topic 2:
<br>人民 社会主义 我国 国家 发展 建设 工作 必须 进行 革命 一个 中国 群众 领导 已经
<br>Topic 3:
<br>增长 工业 生产 农业 建设 增加 计划 国家 企业 发展 五年计划 完成 方面 全国 达到
<br>Topic 4:
<br>经济 发展 企业 改革 建设 我国 生产 必须 国家 工作 提高 人民 方面 增长 进行
<br>I also used pyLDAvis package, which can visualize the result of LDA model. It shows that the training result did a decent classification job.
<br>![result](https://user-images.githubusercontent.com/36937088/50495570-da37f200-09de-11e9-8270-b99e4e841a4a.png)
## Installtion
<br>sklearn 0.19.1
<br>matplotlib 2.1.2
<br>numpy 1.14.6
<br>pyLDAvis 2.1.2
<br>jieba 0.39
