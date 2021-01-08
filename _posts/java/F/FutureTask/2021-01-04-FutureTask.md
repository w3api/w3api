---
title: FutureTask
permalink: Java/FutureTask
date: 2021-01-04
key: JavaJava.F.FutureTask
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FutureTask.description }}

## Sintaxis
~~~java
public class FutureTask<V> extends Object implements RunnableFuture<V>
~~~

## Constructores
* [FutureTask()](/Java/FutureTask/FutureTask/)

## Métodos
* [done()](/Java/FutureTask/done)
* [get()](/Java/FutureTask/get)
* [runAndReset()](/Java/FutureTask/runAndReset)
* [set()](/Java/FutureTask/set)
* [setException()](/Java/FutureTask/setException)
* [toString()](/Java/FutureTask/toString)

## Ejemplo
~~~java
{{ site.data.Java.F.FutureTask.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FutureTask.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
