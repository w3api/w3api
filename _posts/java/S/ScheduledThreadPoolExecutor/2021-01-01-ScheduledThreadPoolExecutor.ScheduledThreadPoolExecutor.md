---
title: ScheduledThreadPoolExecutor.ScheduledThreadPoolExecutor()
permalink: Java/ScheduledThreadPoolExecutor/ScheduledThreadPoolExecutor
date: 2021-01-11
key: JavaJava.S.ScheduledThreadPoolExecutor
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScheduledThreadPoolExecutor.constructores valor="ScheduledThreadPoolExecutor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScheduledThreadPoolExecutor(int corePoolSize)
public ScheduledThreadPoolExecutor(int corePoolSize, RejectedExecutionHandler handler)
public ScheduledThreadPoolExecutor(int corePoolSize, ThreadFactory threadFactory)
public ScheduledThreadPoolExecutor(int corePoolSize, ThreadFactory threadFactory, RejectedExecutionHandler handler)
~~~

## Parámetros
* **int corePoolSize**,  {% include w3api/param_description.html metodo=_dato parametro="int corePoolSize" %}
* **ThreadFactory threadFactory**,  {% include w3api/param_description.html metodo=_dato parametro="ThreadFactory threadFactory" %}
* **RejectedExecutionHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="RejectedExecutionHandler handler" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
