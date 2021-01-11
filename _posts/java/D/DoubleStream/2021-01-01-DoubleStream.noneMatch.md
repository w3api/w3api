---
title: DoubleStream.noneMatch()
permalink: Java/DoubleStream/noneMatch
date: 2021-01-11
key: JavaJava.D.DoubleStream
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleStream.metodos valor="noneMatch" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean noneMatch(DoublePredicate predicate)
~~~

## Parámetros
* **DoublePredicate predicate**,  {% include w3api/param_description.html metodo=_dato parametro="DoublePredicate predicate" %}

## Clase Padre
[DoubleStream](/Java/DoubleStream/)

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
