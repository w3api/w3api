---
title: LongUnaryOperator.compose()
permalink: Java/LongUnaryOperator/compose
date: 2021-01-04
key: JavaJava.L.LongUnaryOperator
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongUnaryOperator.metodos valor="compose" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default LongUnaryOperator compose(LongUnaryOperator before)
~~~

## Parámetros
* **LongUnaryOperator before**,  {% include w3api/param_description.html metodo=_data parametro="LongUnaryOperator before" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LongUnaryOperator](/Java/LongUnaryOperator/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LongUnaryOperator.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
