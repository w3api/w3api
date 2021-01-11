---
title: ForkJoinPool.drainTasksTo()
permalink: Java/ForkJoinPool/drainTasksTo
date: 2021-01-11
key: JavaJava.F.ForkJoinPool
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.metodos valor="drainTasksTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected int drainTasksTo(Collection<? super ForkJoinTask<?>> c)
~~~

## Parámetros
* **Collection&lt;? super ForkJoinTask&lt;?&gt;&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? super ForkJoinTask<?>> c" %}

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

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
