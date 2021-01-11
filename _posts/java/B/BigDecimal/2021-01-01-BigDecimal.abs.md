---
title: BigDecimal.abs()
permalink: Java/BigDecimal/abs
date: 2021-01-11
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="abs" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal abs()
public BigDecimal abs(MathContext mc)
~~~

## Parámetros
* **MathContext mc**,  {% include w3api/param_description.html metodo=_dato parametro="MathContext mc" %}

## Excepciones
[ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[BigDecimal](/Java/BigDecimal/)

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