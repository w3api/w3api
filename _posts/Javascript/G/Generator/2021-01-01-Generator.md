---
title: Generator
permalink: /Javascript/Generator/
date: 2021-01-11
key: Javascript.G.Generator
category: Javascript
tags: ['objeto javascript']
sidebar: 
  nav: javascript
---

## Descripción
{{site.data.Javascript.G.Generator.description }}

## Sintaxis
~~~javascript
Generator
~~~

## Métodos
* [next()](/Javascript/Generator/next/)
* [return()](/Javascript/Generator/return/)
* [throw()](/Javascript/Generator/throw/)

## Ejemplo
~~~java
{{ site.data.Javascript.G.Generator.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Javascript.G.Generator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
