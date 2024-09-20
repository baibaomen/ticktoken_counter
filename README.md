# ticktoken_counter
调用ticktoken计算openai不同模型的消息token数。  
项目意义是：openai官方的ticktoken库是python的。对于不是python编写的服务端，在找不到匹配的tocken计算库时，可以通过api访问本项目（它调用官方ticktoken库，通过vercel自动更新和发布），从而获得准确计数。  
本项目地址1（vercel自动发布）：https://ticktoken-counter.vercel.app/docs#/default/get_token_count__post。  
本项目地址2（国内访问）：https://ticktoken.52https.com/docs#/default/get_token_count__post。  
