---
title: ExecutorService.invokeAll()
permalink: /Java/ExecutorService/invokeAll/
date: 2021-01-11
key: Java.E.ExecutorService
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutorService.metodos valor="invokeAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks)
<T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks, long timeout, TimeUnit unit)
~~~

## Parámetros
* **Collection&lt;? extends Callable&lt;T&gt;&gt; tasks**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends Callable<T>> tasks" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Clase Padre
[ExecutorService](/Java/ExecutorService/)

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
