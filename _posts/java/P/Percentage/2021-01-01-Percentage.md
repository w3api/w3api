---
title: Percentage
permalink: /Java/Percentage/
date: 2021-01-11
key: Java.P.Percentage
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.Percentage.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,TYPE,METHOD}) public @interface Percentage
~~~

## Ejemplo
~~~java
{{ site.data.Java.P.Percentage.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.Percentage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
