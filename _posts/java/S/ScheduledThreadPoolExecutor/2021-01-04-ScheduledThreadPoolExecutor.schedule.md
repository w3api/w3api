---
title: ScheduledThreadPoolExecutor.schedule()
permalink: Java/ScheduledThreadPoolExecutor/schedule
date: 2021-01-04
key: JavaJava.S.ScheduledThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledThreadPoolExecutor.metodos valor="schedule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScheduledFuture<?> schedule(Runnable command, long delay, TimeUnit unit)
<V> ScheduledFuture<V> schedule(Callable<V> callable, long delay, TimeUnit unit)
~~~

## Parámetros
* **Runnable command**,  {% include w3api/param_description.html metodo=_data parametro="Runnable command" %}
* **Callable&lt;V&gt; callable**,  {% include w3api/param_description.html metodo=_data parametro="Callable<V> callable" %}
* **long delay**,  {% include w3api/param_description.html metodo=_data parametro="long delay" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ScheduledThreadPoolExecutor](/Java/ScheduledThreadPoolExecutor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScheduledThreadPoolExecutor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
