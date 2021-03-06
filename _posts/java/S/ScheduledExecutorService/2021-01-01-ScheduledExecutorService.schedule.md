---
title: ScheduledExecutorService.schedule()
permalink: /Java/ScheduledExecutorService/schedule/
date: 2021-01-11
key: Java.S.ScheduledExecutorService
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledExecutorService.metodos valor="schedule" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ScheduledFuture<?> schedule(Runnable command, long delay, TimeUnit unit)
<V> ScheduledFuture<V> schedule(Callable<V> callable, long delay, TimeUnit unit)
~~~

## Parámetros
* **long delay**,  {% include w3api/param_description.html metodo=_dato parametro="long delay" %}
* **Callable&lt;V&gt; callable**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<V> callable" %}
* **Runnable command**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable command" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [RejectedExecutionException](/Java/RejectedExecutionException/)

## Clase Padre
[ScheduledExecutorService](/Java/ScheduledExecutorService/)

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
