---
title: DatatypeFactory.newDuration()
permalink: /Java/DatatypeFactory/newDuration/
date: 2021-01-11
key: Java.D.DatatypeFactory
category: Java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newDuration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Duration newDuration(boolean isPositive, int years, int months, int days, int hours, int minutes, int seconds)
public abstract Duration newDuration(boolean isPositive, BigInteger years, BigInteger months, BigInteger days, BigInteger hours, BigInteger minutes, BigDecimal seconds)
public abstract Duration newDuration(long durationInMilliSeconds)
public abstract Duration newDuration(String lexicalRepresentation)
~~~

## Parámetros
* **int seconds**,  {% include w3api/param_description.html metodo=_dato parametro="int seconds" %}
* **BigInteger months**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger months" %}
* **long durationInMilliSeconds**,  {% include w3api/param_description.html metodo=_dato parametro="long durationInMilliSeconds" %}
* **int minutes**,  {% include w3api/param_description.html metodo=_dato parametro="int minutes" %}
* **int days**,  {% include w3api/param_description.html metodo=_dato parametro="int days" %}
* **int months**,  {% include w3api/param_description.html metodo=_dato parametro="int months" %}
* **BigInteger hours**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger hours" %}
* **BigInteger years**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger years" %}
* **boolean isPositive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isPositive" %}
* **BigInteger days**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger days" %}
* **int years**,  {% include w3api/param_description.html metodo=_dato parametro="int years" %}
* **BigDecimal seconds**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal seconds" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalRepresentation" %}
* **BigInteger minutes**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger minutes" %}
* **int hours**,  {% include w3api/param_description.html metodo=_dato parametro="int hours" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[DatatypeFactory](/Java/DatatypeFactory/)

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
