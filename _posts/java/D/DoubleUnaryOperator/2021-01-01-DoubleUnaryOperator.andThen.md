---
title: DoubleUnaryOperator.andThen()
permalink: Java/DoubleUnaryOperator/andThen
date: 2021-01-11
key: JavaJava.D.DoubleUnaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleUnaryOperator.metodos valor="andThen" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default DoubleUnaryOperator andThen(DoubleUnaryOperator after)
~~~

## Parámetros
* **DoubleUnaryOperator after**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleUnaryOperator after" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DoubleUnaryOperator](/Java/DoubleUnaryOperator/)

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
