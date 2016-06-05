// 发送一次请求
var ajaxGet = function(url, backFun, errFun) {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', url)
    xhr.send(null)
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {

                backFun(xhr.responseText)
            } else {

                errFun(xhr.responseText)
            }
        }
    }

}

// // 创建表格内容
// var createTable = function() {
//     var url = '/api/1.0/course/info?page=0'
//     var backFun = function(responseText) {
//         var jsonObject = JSON.parse(responseText)

//         // 使用Vue实现数据绑定
//         new Vue({
//             el: '#main-table',
//             data: jsonObject
//         })
//     }

//     ajaxGet(url, backFun)
// }

// 创建表格头部
var createTitle = function() {

    // 一个很简单的Vue例子
    new Vue({
        el: '#head-title', // 这是通过id来获取元素
        data: {
            message: 'Course Table' // 这里定义了数据
        }
    })
}

// js加载到这里就自动执行
createTitle()
    // createTable()


var createTable = function() {
    var jsonObject
    if (jsonObject===undefined){
        var jsonObject = {
            courses: [{
                id: 'loading',
                classify: 'loading',
                form: 'loadiing',
                dispass: 'loading',
                frequency: 'loading',
                introduction: 'loading',
                teacher: 'loading',
                topic: 'loading'
            }]
        }
    }
    

    var vm = new Vue({
        el: '#main-table',
        data: jsonObject
    })

    var url = '/api/1.0/course/info'
    var backFun = function(responseText) {
        var jsonObject = JSON.parse(responseText)
        vm.courses = jsonObject.courses
    }

    ajaxGet(url, backFun)
}


createTable()
