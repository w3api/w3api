---
title: ExecutorService.invokeAny()
permalink: Java/ExecutorService/invokeAny
date: 2021-01-04
key: JavaJava.E.ExecutorService
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutorService.metodos valor="invokeAny" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T invokeAny(Collection<? extends Callable<T>> tasks)
<T> T invokeAny(Collection<? extends Callable<T>> tasks, long timeout, TimeUnit unit)
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}
* **Collection&lt;? extends Callable&lt;T&gt;&gt; tasks**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends Callable<T>> tasks" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TimeUnit unit" %}

## Clase Padre
[ExecutorService](/Java/ExecutorService/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutorService.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
