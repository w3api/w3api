---
title: ScheduledThreadPoolExecutor.decorateTask()
permalink: Java/ScheduledThreadPoolExecutor/decorateTask
date: 2021-01-11
key: JavaJava.S.ScheduledThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledThreadPoolExecutor.metodos valor="decorateTask" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected <V> RunnableScheduledFuture<V> decorateTask(Runnable runnable, RunnableScheduledFuture<V> task)
protected <V> RunnableScheduledFuture<V> decorateTask(Callable<V> callable, RunnableScheduledFuture<V> task)
~~~

## Parámetros
* **RunnableScheduledFuture&lt;V&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="RunnableScheduledFuture<V> task" %}
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable runnable" %}
* **Callable&lt;V&gt; callable**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<V> callable" %}

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
