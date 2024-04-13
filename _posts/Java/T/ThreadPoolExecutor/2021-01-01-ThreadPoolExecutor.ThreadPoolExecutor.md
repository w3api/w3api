---
title: ThreadPoolExecutor.ThreadPoolExecutor()
permalink: /Java/ThreadPoolExecutor/ThreadPoolExecutor/
date: 2021-01-11
key: Java.T.ThreadPoolExecutor
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadPoolExecutor.constructores valor="ThreadPoolExecutor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ThreadPoolExecutor(int corePoolSize, int maximumPoolSize, long keepAliveTime, TimeUnit unit, BlockingQueue<Runnable> workQueue)
public ThreadPoolExecutor(int corePoolSize, int maximumPoolSize, long keepAliveTime, TimeUnit unit, BlockingQueue<Runnable> workQueue, RejectedExecutionHandler handler)
public ThreadPoolExecutor(int corePoolSize, int maximumPoolSize, long keepAliveTime, TimeUnit unit, BlockingQueue<Runnable> workQueue, ThreadFactory threadFactory)
public ThreadPoolExecutor(int corePoolSize, int maximumPoolSize, long keepAliveTime, TimeUnit unit, BlockingQueue<Runnable> workQueue, ThreadFactory threadFactory, RejectedExecutionHandler handler)
~~~

## Parámetros
* **RejectedExecutionHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="RejectedExecutionHandler handler" %}
* **int maximumPoolSize**,  {% include w3api/param_description.html metodo=_dato parametro="int maximumPoolSize" %}
* **int corePoolSize**,  {% include w3api/param_description.html metodo=_dato parametro="int corePoolSize" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}
* **long keepAliveTime**,  {% include w3api/param_description.html metodo=_dato parametro="long keepAliveTime" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadFactory threadFactory" %}
* **BlockingQueue&lt;Runnable&gt; workQueue**,  {% include w3api/param_description.html metodo=_dato parametro="BlockingQueue<Runnable> workQueue" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ThreadPoolExecutor](/Java/ThreadPoolExecutor/)

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
