---
title: IntUnaryOperator.compose()
permalink: Java/IntUnaryOperator/compose
date: 2021-01-11
key: JavaJava.I.IntUnaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.IntUnaryOperator.metodos valor="compose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default IntUnaryOperator compose(IntUnaryOperator before)
~~~

## Parámetros
* **IntUnaryOperator before**,  {% include w3api/param_description.html metodo=_dato parametro="IntUnaryOperator before" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[IntUnaryOperator](/Java/IntUnaryOperator/)

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
