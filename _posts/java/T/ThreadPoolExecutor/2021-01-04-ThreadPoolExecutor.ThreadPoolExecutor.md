---
title: ThreadPoolExecutor.ThreadPoolExecutor()
permalink: Java/ThreadPoolExecutor/ThreadPoolExecutor
date: 2021-01-04
key: JavaJava.T.ThreadPoolExecutor
category: java
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
* **RejectedExecutionHandler handler**,  {% include w3api/param_description.html metodo=_data parametro="RejectedExecutionHandler handler" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}
* **int maximumPoolSize**,  {% include w3api/param_description.html metodo=_data parametro="int maximumPoolSize" %}
* **long keepAliveTime**,  {% include w3api/param_description.html metodo=_data parametro="long keepAliveTime" %}
* **int corePoolSize**,  {% include w3api/param_description.html metodo=_data parametro="int corePoolSize" %}
* **BlockingQueue&lt;Runnable&gt; workQueue**,  {% include w3api/param_description.html metodo=_data parametro="BlockingQueue<Runnable> workQueue" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_data parametro="ThreadFactory threadFactory" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ThreadPoolExecutor](/Java/ThreadPoolExecutor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadPoolExecutor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
