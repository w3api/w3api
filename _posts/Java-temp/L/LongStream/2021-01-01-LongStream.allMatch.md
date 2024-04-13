---
title: LongStream.allMatch()
permalink: /Java/LongStream/allMatch/
date: 2021-01-11
key: Java.L.LongStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="allMatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean allMatch(LongPredicate predicate)
~~~

## Parámetros
* **LongPredicate predicate**,  {% include w3api/param_description.html metodo=_dato parametro="LongPredicate predicate" %}

## Clase Padre
[LongStream](/Java/LongStream/)

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
