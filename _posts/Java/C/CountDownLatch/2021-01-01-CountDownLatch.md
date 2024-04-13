---
title: CountDownLatch
permalink: /Java/CountDownLatch/
date: 2021-01-11
key: Java.C.CountDownLatch
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.CountDownLatch.description }}

## Sintaxis
~~~java
public class CountDownLatch extends Object
~~~

## Constructores
* [CountDownLatch()](/Java/CountDownLatch/CountDownLatch/)

## Métodos
* [await()](/Java/CountDownLatch/await)
* [countDown()](/Java/CountDownLatch/countDown)
* [getCount()](/Java/CountDownLatch/getCount)
* [toString()](/Java/CountDownLatch/toString)

## Ejemplo
~~~java
{{ site.data.Java.C.CountDownLatch.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.CountDownLatch.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
