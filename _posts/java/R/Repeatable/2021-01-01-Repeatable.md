---
title: Repeatable
permalink: Java/Repeatable
date: 2021-01-11
key: JavaJava.R.Repeatable
category: java
tags: ['java se', 'java.lang.annotation', 'java.base', 'anotacion java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Repeatable.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(ANNOTATION_TYPE) public @interface Repeatable
~~~

## Ejemplo
~~~java
{{ site.data.Java.R.Repeatable.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Repeatable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
