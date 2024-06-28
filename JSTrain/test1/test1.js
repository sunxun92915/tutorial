console.log('hello world');

// function声明の方法
// 1
var functionName1 = function(parameters){
    console.log('function1');
};

// 2
// javaと違い、パラメータが違いがあっても、functionNameが同じなら、同一functionと見なされるので、同一命名注意
function functionName2(parameter1,parameter2){
    // return がないなら、undefinedがreturnされる
    return ('function2')
}