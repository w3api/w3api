---
title: autofocus
permalink: /HTML/autofocus/
date: 2021-07-15 00:30:12.395494 +0200
key: HTML.a.autofocus
category: HTML
tags: ['atributo html']
sidebar: 
  nav: html
---

## Descripción
{{site.data.HTML.a.autofocus.description }}

## Sintaxis
~~~html
<elemento autofous></elemento>
~~~

## Ejemplo
~~~java
{{ site.data.HTML.a.autofocus.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.HTML.a.autofocus.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
