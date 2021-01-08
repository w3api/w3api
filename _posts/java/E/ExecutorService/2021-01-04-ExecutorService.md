---
title: ExecutorService
permalink: Java/ExecutorService
date: 2021-01-04
key: JavaJava.E.ExecutorService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'interface java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.E.ExecutorService.description }}

## Sintaxis
~~~java
public interface ExecutorService extends Executor
~~~

## Métodos
* [awaitTermination()](/Java/ExecutorService/awaitTermination)
* [invokeAll()](/Java/ExecutorService/invokeAll)
* [invokeAny()](/Java/ExecutorService/invokeAny)
* [isShutdown()](/Java/ExecutorService/isShutdown)
* [isTerminated()](/Java/ExecutorService/isTerminated)
* [shutdown()](/Java/ExecutorService/shutdown)
* [shutdownNow()](/Java/ExecutorService/shutdownNow)
* [submit()](/Java/ExecutorService/submit)

## Ejemplo
~~~java
{{ site.data.Java.E.ExecutorService.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutorService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
