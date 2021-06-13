---
title: BigDecimal.divide()
permalink: /Java/BigDecimal/divide/
date: 2021-01-11
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="divide" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal divide(BigDecimal divisor)
@Deprecated(since="9") public BigDecimal divide(BigDecimal divisor, int roundingMode)
@Deprecated(since="9") public BigDecimal divide(BigDecimal divisor, int scale, int roundingMode)
public BigDecimal divide(BigDecimal divisor, int scale, RoundingMode roundingMode)
public BigDecimal divide(BigDecimal divisor, MathContext mc)
public BigDecimal divide(BigDecimal divisor, RoundingMode roundingMode)
~~~

## Parámetros
* **RoundingMode roundingMode**,  {% include w3api/param_description.html metodo=_dato parametro="RoundingMode roundingMode" %}
* **BigDecimal divisor**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal divisor" %}
* **int roundingMode**,  {% include w3api/param_description.html metodo=_dato parametro="int roundingMode" %}
* **MathContext mc**,  {% include w3api/param_description.html metodo=_dato parametro="MathContext mc" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArithmeticException](/Java/ArithmeticException/)

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
