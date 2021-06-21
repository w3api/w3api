---
title: IntStream.allMatch()
permalink: /Java/IntStream/allMatch/
date: 2021-01-11
key: Java.I.IntStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="allMatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean allMatch(IntPredicate predicate)
~~~

## Parámetros
* **IntPredicate predicate**,  {% include w3api/param_description.html metodo=_dato parametro="IntPredicate predicate" %}

## Clase Padre
[IntStream](/Java/IntStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
