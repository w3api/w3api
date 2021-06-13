---
title: ForkJoinTask.adapt()
permalink: /Java/ForkJoinTask/adapt/
date: 2021-01-11
key: Java.F.ForkJoinTask
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinTask.metodos valor="adapt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ForkJoinTask<?> adapt(Runnable runnable)
static <T> ForkJoinTask<T> adapt(Runnable runnable, T result)
static <T> ForkJoinTask<T> adapt(Callable<? extends T> callable)
~~~

## Parámetros
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable runnable" %}
* **Callable&lt;? extends T&gt; callable**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<? extends T> callable" %}
* **T result**,  {% include w3api/param_description.html metodo=_dato parametro="T result" %}

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
