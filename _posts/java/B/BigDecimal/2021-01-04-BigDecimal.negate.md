---
title: BigDecimal.negate()
permalink: Java/BigDecimal/negate
date: 2021-01-04
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="negate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal negate()
public BigDecimal negate(MathContext mc)
~~~

## Parámetros
* **MathContext mc**,  {% include w3api/param_description.html metodo=_data parametro="MathContext mc" %}

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
