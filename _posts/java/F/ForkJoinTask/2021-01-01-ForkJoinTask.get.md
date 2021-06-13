---
title: ForkJoinTask.get()
permalink: /Java/ForkJoinTask/get/
date: 2021-01-11
key: Java.F.ForkJoinTask
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinTask.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final V get() throws InterruptedException, ExecutionException
public final V get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[ExecutionException](/Java/ExecutionException/), [InterruptedException](/Java/InterruptedException/), [TimeoutException](/Java/TimeoutException/), [CancellationException](/Java/CancellationException/)

## Clase Padre
[ForkJoinTask](/Java/ForkJoinTask/)

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
