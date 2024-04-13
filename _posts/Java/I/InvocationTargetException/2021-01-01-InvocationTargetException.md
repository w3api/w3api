---
title: InvocationTargetException
permalink: /Java/InvocationTargetException/
date: 2021-01-11
key: Java.I.InvocationTargetException
category: Java
tags: ['java se', 'java.lang.reflect', 'java.base', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.InvocationTargetException.description }}

## Sintaxis
~~~java
public class InvocationTargetException extends ReflectiveOperationException
~~~

## Constructores
* [InvocationTargetException()](/Java/InvocationTargetException/InvocationTargetException/)

## Métodos
* [getCause()](/Java/InvocationTargetException/getCause)
* [getTargetException()](/Java/InvocationTargetException/getTargetException)

## Ejemplo
~~~java
{{ site.data.Java.I.InvocationTargetException.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.I.InvocationTargetException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
