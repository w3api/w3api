---
title: IntPredicate.or()
permalink: Java/IntPredicate/or
date: 2021-01-11
key: JavaJava.I.IntPredicate
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntPredicate.metodos valor="or" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default IntPredicate or(IntPredicate other)
~~~

## Parámetros
* **IntPredicate other**,  {% include w3api/param_description.html metodo=_dato parametro="IntPredicate other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IntPredicate](/Java/IntPredicate/)

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
