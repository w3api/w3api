---
title: ForkJoinPool.invoke()
permalink: /Java/ForkJoinPool/invoke/
date: 2021-01-11
key: Java.F.ForkJoinPool
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
<T> T invoke(ForkJoinTask<T> task)
~~~

## Parámetros
* **ForkJoinTask&lt;T&gt; task**,  {% include w3api/param_description.html metodo=_dato parametro="ForkJoinTask<T> task" %}

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
