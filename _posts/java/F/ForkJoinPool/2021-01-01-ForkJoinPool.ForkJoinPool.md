---
title: ForkJoinPool.ForkJoinPool()
permalink: Java/ForkJoinPool/ForkJoinPool
date: 2021-01-11
key: JavaJava.F.ForkJoinPool
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.constructores valor="ForkJoinPool" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ForkJoinPool()
public ForkJoinPool(int parallelism)
public ForkJoinPool(int parallelism, ForkJoinPool.ForkJoinWorkerThreadFactory factory, Thread.UncaughtExceptionHandler handler, boolean asyncMode)
public ForkJoinPool(int parallelism, ForkJoinPool.ForkJoinWorkerThreadFactory factory, Thread.UncaughtExceptionHandler handler, boolean asyncMode, int corePoolSize, int maximumPoolSize, int minimumRunnable, Predicate<? super ForkJoinPool> saturate, long keepAliveTime, TimeUnit unit)
~~~

## Parámetros
* **ForkJoinPool.ForkJoinWorkerThreadFactory factory**,  {% include w3api/param_description.html metodo=_dato parametro="ForkJoinPool.ForkJoinWorkerThreadFactory factory" %}
* **Predicate&lt;? super ForkJoinPool&gt; saturate**,  {% include w3api/param_description.html metodo=_dato parametro="Predicate<? super ForkJoinPool> saturate" %}
* **int maximumPoolSize**,  {% include w3api/param_description.html metodo=_dato parametro="int maximumPoolSize" %}
* **int corePoolSize**,  {% include w3api/param_description.html metodo=_dato parametro="int corePoolSize" %}
* **int minimumRunnable**,  {% include w3api/param_description.html metodo=_dato parametro="int minimumRunnable" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}
* **int parallelism**,  {% include w3api/param_description.html metodo=_dato parametro="int parallelism" %}
* **boolean asyncMode**,  {% include w3api/param_description.html metodo=_dato parametro="boolean asyncMode" %}
* **long keepAliveTime**,  {% include w3api/param_description.html metodo=_dato parametro="long keepAliveTime" %}
* **Thread.UncaughtExceptionHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="Thread.UncaughtExceptionHandler handler" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
