---
title: ForkJoinPool.ForkJoinPool()
permalink: Java/ForkJoinPool/ForkJoinPool
date: 2021-01-04
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
* **ForkJoinPool.ForkJoinWorkerThreadFactory factory**,  {% include w3api/param_description.html metodo=_data parametro="ForkJoinPool.ForkJoinWorkerThreadFactory factory" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}
* **int maximumPoolSize**,  {% include w3api/param_description.html metodo=_data parametro="int maximumPoolSize" %}
* **int parallelism**,  {% include w3api/param_description.html metodo=_data parametro="int parallelism" %}
* **int corePoolSize**,  {% include w3api/param_description.html metodo=_data parametro="int corePoolSize" %}
* **Thread.UncaughtExceptionHandler handler**,  {% include w3api/param_description.html metodo=_data parametro="Thread.UncaughtExceptionHandler handler" %}
* **int minimumRunnable**,  {% include w3api/param_description.html metodo=_data parametro="int minimumRunnable" %}
* **long keepAliveTime**,  {% include w3api/param_description.html metodo=_data parametro="long keepAliveTime" %}
* **boolean asyncMode**,  {% include w3api/param_description.html metodo=_data parametro="boolean asyncMode" %}
* **Predicate&lt;? super ForkJoinPool&gt; saturate**,  {% include w3api/param_description.html metodo=_data parametro="Predicate<? super ForkJoinPool> saturate" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForkJoinPool.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
