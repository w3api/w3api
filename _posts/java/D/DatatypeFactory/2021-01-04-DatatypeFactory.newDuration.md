---
title: DatatypeFactory.newDuration()
permalink: Java/DatatypeFactory/newDuration
date: 2021-01-04
key: JavaJava.D.DatatypeFactory
category: java
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
* **BigInteger minutes**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger minutes" %}
* **BigInteger years**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger years" %}
* **int hours**,  {% include w3api/param_description.html metodo=_data parametro="int hours" %}
* **boolean isPositive**,  {% include w3api/param_description.html metodo=_data parametro="boolean isPositive" %}
* **int seconds**,  {% include w3api/param_description.html metodo=_data parametro="int seconds" %}
* **int days**,  {% include w3api/param_description.html metodo=_data parametro="int days" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_data parametro="String lexicalRepresentation" %}
* **BigInteger months**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger months" %}
* **int months**,  {% include w3api/param_description.html metodo=_data parametro="int months" %}
* **int minutes**,  {% include w3api/param_description.html metodo=_data parametro="int minutes" %}
* **BigInteger hours**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger hours" %}
* **int years**,  {% include w3api/param_description.html metodo=_data parametro="int years" %}
* **BigDecimal seconds**,  {% include w3api/param_description.html metodo=_data parametro="BigDecimal seconds" %}
* **long durationInMilliSeconds**,  {% include w3api/param_description.html metodo=_data parametro="long durationInMilliSeconds" %}
* **BigInteger days**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger days" %}

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
