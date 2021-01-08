---
title: ThreadLocal
permalink: Java/ThreadLocal
date: 2021-01-04
key: JavaJava.T.ThreadLocal
category: java
tags: ['java se', 'java.lang', 'java.base', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThreadLocal.description }}

## Sintaxis
~~~java
public class ThreadLocal<T> extends Object
~~~

## Constructores
* [ThreadLocal()](/Java/ThreadLocal/ThreadLocal/)

## Métodos
* [get()](/Java/ThreadLocal/get)
* [initialValue()](/Java/ThreadLocal/initialValue)
* [remove()](/Java/ThreadLocal/remove)
* [set()](/Java/ThreadLocal/set)
* [withInitial()](/Java/ThreadLocal/withInitial)

## Ejemplo
~~~java
{{ site.data.Java.T.ThreadLocal.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadLocal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
