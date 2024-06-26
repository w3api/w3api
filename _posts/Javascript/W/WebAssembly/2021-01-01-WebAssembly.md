---
title: WebAssembly
permalink: /Javascript/WebAssembly/
date: 2021-01-11
key: Javascript.W.WebAssembly
category: Javascript
tags: ['objeto javascript']
sidebar: 
  nav: javascript
---

## Descripción
{{site.data.Javascript.W.WebAssembly.description }}

## Sintaxis
~~~javascript
WebAssembly
~~~

## Métodos
* [instantiate()](/Javascript/WebAssembly/instantiate/)
* [instantiateStreaming()](/Javascript/WebAssembly/instantiateStreaming/)
* [compile()](/Javascript/WebAssembly/compile/)
* [compileStreaming()](/Javascript/WebAssembly/compileStreaming/)
* [validate()](/Javascript/WebAssembly/validate/)

## Ejemplo
~~~java
{{ site.data.Javascript.W.WebAssembly.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Javascript.W.WebAssembly.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
