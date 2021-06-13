---
title: AbstractExecutorService.newTaskFor()
permalink: /Java/AbstractExecutorService/newTaskFor/
date: 2021-01-11
key: Java.A.AbstractExecutorService
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractExecutorService.metodos valor="newTaskFor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected <T> RunnableFuture<T> newTaskFor(Runnable runnable, T value)
protected <T> RunnableFuture<T> newTaskFor(Callable<T> callable)
~~~

## Parámetros
* **Callable&lt;T&gt; callable**,  {% include w3api/param_description.html metodo=_dato parametro="Callable<T> callable" %}
* **Runnable runnable**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable runnable" %}
* **T value**,  {% include w3api/param_description.html metodo=_dato parametro="T value" %}

## Clase Padre
[AbstractExecutorService](/Java/AbstractExecutorService/)

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
