var template = document.getElementById("test").innerHTML
var compiledTemplate = Handlebars.compile(template)
data = {
    picture : [
        {name:"3x3 Gradient Threshold"},
        {name:"5x5 Gradient Threshold"},
        {name:"3x3 Gradient"},
        {name: "5x5 Gradient"},
        {name:"3x3 Vertical"},
        {name:"3x3 Horizontal"},
        {name:"5x5 Vertical"},
        {name:"5x5 Horizontal"}
    ]
}
document.getElementById("template-container").innerHTML += compiledTemplate(data)
