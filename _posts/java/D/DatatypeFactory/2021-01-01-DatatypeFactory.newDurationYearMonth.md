---
title: DatatypeFactory.newDurationYearMonth()
permalink: Java/DatatypeFactory/newDurationYearMonth
date: 2021-01-11
key: JavaJava.D.DatatypeFactory
category: java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newDurationYearMonth" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Duration newDurationYearMonth(boolean isPositive, int year, int month)
public Duration newDurationYearMonth(boolean isPositive, BigInteger year, BigInteger month)
public Duration newDurationYearMonth(long durationInMilliseconds)
public Duration newDurationYearMonth(String lexicalRepresentation)
~~~

## Parámetros
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalRepresentation" %}
* **BigInteger month**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger month" %}
* **long durationInMilliseconds**,  {% include w3api/param_description.html metodo=_dato parametro="long durationInMilliseconds" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **BigInteger year**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger year" %}
* **boolean isPositive**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isPositive" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}

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
