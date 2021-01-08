---
title: BigDecimal.divideToIntegralValue()
permalink: Java/BigDecimal/divideToIntegralValue
date: 2021-01-04
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="divideToIntegralValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal divideToIntegralValue(BigDecimal divisor)
public BigDecimal divideToIntegralValue(BigDecimal divisor, MathContext mc)
~~~

## Parámetros
* **MathContext mc**,  {% include w3api/param_description.html metodo=_data parametro="MathContext mc" %}
* **BigDecimal divisor**,  {% include w3api/param_description.html metodo=_data parametro="BigDecimal divisor" %}

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
{%- for _ldc in site.data.Java.B.BigDecimal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
