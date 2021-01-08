---
title: ScheduledThreadPoolExecutor.scheduleWithFixedDelay()
permalink: Java/ScheduledThreadPoolExecutor/scheduleWithFixedDelay
date: 2021-01-04
key: JavaJava.S.ScheduledThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledThreadPoolExecutor.metodos valor="scheduleWithFixedDelay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScheduledFuture<?> scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)
~~~

## Parámetros
* **Runnable command**,  {% include w3api/param_description.html metodo=_data parametro="Runnable command" %}
* **long initialDelay**,  {% include w3api/param_description.html metodo=_data parametro="long initialDelay" %}
* **long delay**,  {% include w3api/param_description.html metodo=_data parametro="long delay" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
