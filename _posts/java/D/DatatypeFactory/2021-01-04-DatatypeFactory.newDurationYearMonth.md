---
title: DatatypeFactory.newDurationYearMonth()
permalink: Java/DatatypeFactory/newDurationYearMonth
date: 2021-01-04
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
* **BigInteger month**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger month" %}
* **BigInteger year**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger year" %}
* **boolean isPositive**,  {% include w3api/param_description.html metodo=_data parametro="boolean isPositive" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_data parametro="String lexicalRepresentation" %}
* **long durationInMilliseconds**,  {% include w3api/param_description.html metodo=_data parametro="long durationInMilliseconds" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DatatypeFactory](/Java/DatatypeFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DatatypeFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
