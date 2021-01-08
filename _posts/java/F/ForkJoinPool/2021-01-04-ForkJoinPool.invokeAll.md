---
title: ForkJoinPool.invokeAll()
permalink: Java/ForkJoinPool/invokeAll
date: 2021-01-04
key: JavaJava.F.ForkJoinPool
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.metodos valor="invokeAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> List<Future<T>> invokeAll(Collection<? extends Callable<T>> tasks)
~~~

## Parámetros
* **Collection&lt;? extends Callable&lt;T&gt;&gt; tasks**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends Callable<T>> tasks" %}

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.ForkJoinPool.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
