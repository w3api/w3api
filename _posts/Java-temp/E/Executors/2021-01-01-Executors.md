---
title: Executors
permalink: /Java/Executors/
date: 2021-01-11
key: Java.E.Executors
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'clase java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.Executors.description }}

## Sintaxis
~~~java
public class Executors extends Object
~~~

## Métodos
* [callable()](/Java/Executors/callable)
* [defaultThreadFactory()](/Java/Executors/defaultThreadFactory)
* [newCachedThreadPool()](/Java/Executors/newCachedThreadPool)
* [newFixedThreadPool()](/Java/Executors/newFixedThreadPool)
* [newScheduledThreadPool()](/Java/Executors/newScheduledThreadPool)
* [newSingleThreadExecutor()](/Java/Executors/newSingleThreadExecutor)
* [newSingleThreadScheduledExecutor()](/Java/Executors/newSingleThreadScheduledExecutor)
* [newWorkStealingPool()](/Java/Executors/newWorkStealingPool)
* [privilegedCallable()](/Java/Executors/privilegedCallable)
* [privilegedCallableUsingCurrentClassLoader()](/Java/Executors/privilegedCallableUsingCurrentClassLoader)
* [privilegedThreadFactory()](/Java/Executors/privilegedThreadFactory)
* [unconfigurableExecutorService()](/Java/Executors/unconfigurableExecutorService)
* [unconfigurableScheduledExecutorService()](/Java/Executors/unconfigurableScheduledExecutorService)

## Ejemplo
~~~java
{{ site.data.Java.E.Executors.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.Executors.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
