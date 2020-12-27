import json 


para_1 = {
    "hello" : "I am interested in the Associate Product Manager (APM) position at Company. My education and experience have given me the intuition and technical skills required to understand users' needs, prevailing market forces, and the constraints of design and engineering teams. Also, my letter states that I reside in Baton Rouge, but I intend to move to Austin."
}

para_2 = {
    "hello2" : "Product management is critical in maintaining existing customer relationships and obtaining new customers, as it keeps the needs and wants of the user at the center of the development process. In my graduate studies and as a research associate at the Economics and Policy Research Group (EPRG), I acquired knowledge and skills an APM would use every day. "
}

bullets = {
    "Experiment and Analysis" : "•  *Experiment and Analysis:* At EPRG, I worked on a team whose entire product revolved around analyzing economic series and testing hypotheses. As a member of the product team, this would translate into carefully designed metrics and the ability to track product success with an eye for continual improvement. ", 
    "Crafting a Product" : "•   Crafting a Product: During my economics masters, I studied optimization theory, and the concept of maximizing a goal under constraints is an ideal framework for thinking about a product. For instance, creating a product involves a customer, a budget, and an engineering team. A great APM must masterfully balance the needs and wants of the customer with the constraints of the design and the engineering teams. Every question in economics starts with something or someone who needs to maximize within the bounds of constraints, and I have become an expert in confronting and solving such problems. ",
    "Collaboration" : "•    Collaboration: This is the most valuable skill I have acquired, and I learned it through my time at EPRG and in my studies. At EPRG, I worked on a team answering complex questions that required us to brainstorm and to set strategies for how best to tackle projects. Also, my elective in graduate school included a case study component I found invaluable in teaching me to work with people of different backgrounds, as my group of five spanned four nationalities. Even more importantly, I encountered frictions in my team's productivity, which gave me experience in improving the cohesion among a diverse group of people. "
}

para_final = {
    "final" : "Company is a place where talented people have come together to insert something nice company accomplishes. I hope you will consider my application, as I would be a valuable and eager member of a team working towards such a purpose. "
}


contents = {
    "para_1" : para_1,
    "para_2" : para_2,
    "bullets" : bullets,
    "para_final" : para_final
}

print(contents)

print('skip')
print('skip')
print('skip')

print(json.dumps(contents, indent = 4))

with open('contents.json', 'w') as json_file: 
	json.dump(contents, json_file, indent = 4)