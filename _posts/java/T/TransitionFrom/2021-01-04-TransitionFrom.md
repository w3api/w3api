---
title: TransitionFrom
permalink: Java/TransitionFrom
date: 2021-01-04
key: JavaJava.T.TransitionFrom
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.TransitionFrom.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(FIELD) public @interface TransitionFrom
~~~

## Ejemplo
~~~java
{{ site.data.Java.T.TransitionFrom.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TransitionFrom.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
