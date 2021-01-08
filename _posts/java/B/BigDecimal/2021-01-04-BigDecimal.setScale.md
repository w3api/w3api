---
title: BigDecimal.setScale()
permalink: Java/BigDecimal/setScale
date: 2021-01-04
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="setScale" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal setScale(int newScale)
@Deprecated(since="9") public BigDecimal setScale(int newScale, int roundingMode)
public BigDecimal setScale(int newScale, RoundingMode roundingMode)
~~~

## Parámetros
* **int roundingMode**,  {% include w3api/param_description.html metodo=_data parametro="int roundingMode" %}
* **int newScale**,  {% include w3api/param_description.html metodo=_data parametro="int newScale" %}
* **RoundingMode roundingMode**,  {% include w3api/param_description.html metodo=_data parametro="RoundingMode roundingMode" %}

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
{%- for _ldc in site.data.Java.B.BigDecimal.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
