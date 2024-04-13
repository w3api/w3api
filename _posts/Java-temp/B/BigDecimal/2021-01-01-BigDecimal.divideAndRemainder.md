---
title: BigDecimal.divideAndRemainder()
permalink: /Java/BigDecimal/divideAndRemainder/
date: 2021-01-11
key: Java.B.BigDecimal
category: Java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="divideAndRemainder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal[] divideAndRemainder(BigDecimal divisor)
public BigDecimal[] divideAndRemainder(BigDecimal divisor, MathContext mc)
~~~

## Parámetros
* **BigDecimal divisor**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal divisor" %}
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
