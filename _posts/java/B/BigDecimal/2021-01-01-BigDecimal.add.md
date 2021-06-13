---
title: BigDecimal.add()
permalink: /Java/BigDecimal/add/
date: 2021-01-11
key: JavaJava.B.BigDecimal
category: java
tags: ['java se', 'java.math', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BigDecimal.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public BigDecimal add(BigDecimal augend)
public BigDecimal add(BigDecimal augend, MathContext mc)
~~~

## Parámetros
* **BigDecimal augend**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal augend" %}
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
