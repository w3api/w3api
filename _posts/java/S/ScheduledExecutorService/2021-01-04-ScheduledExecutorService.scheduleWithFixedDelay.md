---
title: ScheduledExecutorService.scheduleWithFixedDelay()
permalink: Java/ScheduledExecutorService/scheduleWithFixedDelay
date: 2021-01-04
key: JavaJava.S.ScheduledExecutorService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledExecutorService.metodos valor="scheduleWithFixedDelay" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ScheduledFuture<?> scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)
~~~

## Parámetros
* **Runnable command**,  {% include w3api/param_description.html metodo=_data parametro="Runnable command" %}
* **long initialDelay**,  {% include w3api/param_description.html metodo=_data parametro="long initialDelay" %}
* **long delay**,  {% include w3api/param_description.html metodo=_data parametro="long delay" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Excepciones
[RejectedExecutionException](/Java/RejectedExecutionException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ScheduledExecutorService](/Java/ScheduledExecutorService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScheduledExecutorService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
