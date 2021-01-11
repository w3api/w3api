---
title: DoubleUnaryOperator.compose()
permalink: Java/DoubleUnaryOperator/compose
date: 2021-01-11
key: JavaJava.D.DoubleUnaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DoubleUnaryOperator.metodos valor="compose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default DoubleUnaryOperator compose(DoubleUnaryOperator before)
~~~

## Parámetros
* **DoubleUnaryOperator before**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleUnaryOperator before" %}

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
