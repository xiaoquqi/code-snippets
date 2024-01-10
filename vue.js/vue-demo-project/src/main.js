import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

// 每个 Vue 应用都是通过 createApp 函数创建一个新的 应用实例
// 应用实例必须在调用了 .mount() 方法后才会渲染出来。该方法接收一个“容器”参数，
// 可以是一个实际的 DOM 元素或是一个 CSS 选择器字符串：
createApp(App).mount('#app')

// 应用实例并不只限于一个。createApp API 允许你在同一个页面中创建多个共存的 Vue 应用，
// 而且每个应用都拥有自己的用于配置和全局资源的作用域。

// 组件注册(全局)
// import { createApp } from 'vue'
//
// const app = createApp({})
// 
// app.component(
//   // 注册的名字
//   'MyComponent',
//   // 组件的实现
//   {
//     /* ... */
//   }
// )
//
// 如果组件是从文件引入
// import MyComponent from './App.vue'

// app.component('MyComponent', MyComponent)

// 全局注册，但并没有被使用的组件无法在生产打包时被自动移除 (也叫“tree-shaking”)。
// 如果你全局注册了一个组件，即使它并没有被实际使用，它仍然会出现在打包后的 JS 文件中。
//
// 全局注册在大型项目中使项目的依赖关系变得不那么明确。在父组件中使用子组件时，
// 不太容易定位子组件的实现。和使用过多的全局变量一样，这可能会影响应用长期的可维护性。