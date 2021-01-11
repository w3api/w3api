---
title: IntStream.anyMatch()
permalink: Java/IntStream/anyMatch
date: 2021-01-11
key: JavaJava.I.IntStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntStream.metodos valor="anyMatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean anyMatch(IntPredicate predicate)
~~~

## Parámetros
* **IntPredicate predicate**,  {% include w3api/param_description.html metodo=_dato parametro="IntPredicate predicate" %}

## Clase Padre
[IntStream](/Java/IntStream/)

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
