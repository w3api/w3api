---
title: ScheduledThreadPoolExecutor.scheduleWithFixedDelay()
permalink: /Java/ScheduledThreadPoolExecutor/scheduleWithFixedDelay/
date: 2021-01-11
key: Java.S.ScheduledThreadPoolExecutor
category: Java
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
* **long delay**,  {% include w3api/param_description.html metodo=_dato parametro="long delay" %}
* **long initialDelay**,  {% include w3api/param_description.html metodo=_dato parametro="long initialDelay" %}
* **Runnable command**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable command" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [RejectedExecutionException](/Java/RejectedExecutionException/)

## Clase Padre
[ScheduledThreadPoolExecutor](/Java/ScheduledThreadPoolExecutor/)

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
