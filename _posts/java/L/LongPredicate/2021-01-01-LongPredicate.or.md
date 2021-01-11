---
title: LongPredicate.or()
permalink: Java/LongPredicate/or
date: 2021-01-11
key: JavaJava.L.LongPredicate
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongPredicate.metodos valor="or" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default LongPredicate or(LongPredicate other)
~~~

## Parámetros
* **LongPredicate other**,  {% include w3api/param_description.html metodo=_dato parametro="LongPredicate other" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LongPredicate](/Java/LongPredicate/)

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
