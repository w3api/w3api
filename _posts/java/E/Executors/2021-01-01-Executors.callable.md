---
title: Executors.callable()
permalink: Java/Executors/callable
date: 2021-01-11
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="callable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Callable<Object> callable(Runnable task)
static <T> Callable<T> callable(Runnable task, T result)
public static Callable<Object> callable(PrivilegedAction<?> action)
public static Callable<Object> callable(PrivilegedExceptionAction<?> action)
~~~

## Parámetros
* **PrivilegedAction&lt;?&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="PrivilegedAction<?> action" %}
* **PrivilegedExceptionAction&lt;?&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="PrivilegedExceptionAction<?> action" %}
* **Runnable task**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable task" %}
* **T result**,  {% include w3api/param_description.html metodo=_dato parametro="T result" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Executors](/Java/Executors/)

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
