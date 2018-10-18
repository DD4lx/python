## 学习使用ajax
>首先需要找到一个数据接口；在这里使用的是天行数据网站的一些免费接口；

>API - 应用程序编程接口

>Ajax:

-Asynchronous: 异步；异步请求（没有中断浏览器的用户体验）从服务器获取数据;

-Javascript

-and

XML - eXtensible Markup Language:可扩展的标记语言；传数据，被json替代；

json --- 通过DOM操作对页面进行局部刷新，异步加载数据，局部刷新页面；

>注意：URL中中文字符要转换成百分号编码；将字符串转换成百分号编码：encodeURIComponent(str,"utf-8")；将百分号编码解码：decodeURIComponent(str,"utf-8")；


>通过接口在页面上加载图片
```
<body>
		<button id="load">加载</button>
		<ul id="imgs"></ul>
		<script src="js/jquery.min.js"></script>
		<script>
			$(function(){
				$("#load").on("click",function(){
					var url = "http://api.tianapi.com/meinv/?key=e80eea975e6f45127c62a6f7da4da47b&num=100";
					// 发一个get请求，拿到json文件； 
					$.getJSON(url, function(jsonObj){
						$("#imgs").empty();
						// 处理数据，做DOM操作
						for (var i = 0; i < jsonObj.newslist.length; i += 1){
							$("#imgs").append(
								$("<li>").append(
									$("<a target='_blank'>").text(jsonObj.newslist[i].title).attr("href", jsonObj.newslist[i].picUrl)
								)	
							);
						}
					});
				});
			});
			
		</script>
	</body>
```
>通过接口数据实现周公解梦的功能
```
<body>
		<input type="text" id="word"/>
		<button id="search">搜索</button>
		<div id="result">
			
		</div>
		
		<script src="js/jquery.min.js"></script>
		<script>
			$(function(){
				
				$("#search").on("click",function(){
					var word = $("#word").val().trim();
					//var word = encodeURIComponent($("#word").val().trim(),"utf-8");
					var url = "http://api.tianapi.com/txapi/dream/";
//					var url = "http://api.tianapi.com/txapi/dream/?key=e80eea975e6f45127c62a6f7da4da47b&word=" + word;
//					$.getJSON(url,function(jsonObj){
//						if (jsonObj.code == 250){
//							$("#result").append($("<p>").text(jsonObj.msg));
//						}else{
//							$("#result").append($("<p>").text(jsonObj.newslist[0].result));
//						}
//						
//						
//					});
					$.ajax({
						"url": url,
						"type": "get",
						"data": {
							"key":"e80eea975e6f45127c62a6f7da4da47b",
							"word":word
						},
						"dataType": "json",
						"success": function(jsonObj){
							if (jsonObj.code == 250){
							$("#result").append($("<p>").text(jsonObj.msg));
							}else{
							$("#result").append($("<p>").text(jsonObj.newslist[0].result));
							}
						}
					});
					
					
				});
			});
			
		</script>
		
	</body>
```

>了解Bootstrip响应式布局；

>通过自学Git jekell Hexo:先安装node.js;进而完善自己的博客；