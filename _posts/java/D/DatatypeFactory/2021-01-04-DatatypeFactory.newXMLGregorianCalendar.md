---
title: DatatypeFactory.newXMLGregorianCalendar()
permalink: Java/DatatypeFactory/newXMLGregorianCalendar
date: 2021-01-04
key: JavaJava.D.DatatypeFactory
category: java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newXMLGregorianCalendar" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLGregorianCalendar newXMLGregorianCalendar()
public XMLGregorianCalendar newXMLGregorianCalendar(int year, int month, int day, int hour, int minute, int second, int millisecond, int timezone)
public abstract XMLGregorianCalendar newXMLGregorianCalendar(String lexicalRepresentation)
public abstract XMLGregorianCalendar newXMLGregorianCalendar(BigInteger year, int month, int day, int hour, int minute, int second, BigDecimal fractionalSecond, int timezone)
public abstract XMLGregorianCalendar newXMLGregorianCalendar(GregorianCalendar cal)
~~~

## Parámetros
* **BigInteger year**,  {% include w3api/param_description.html metodo=_data parametro="BigInteger year" %}
* **int minute**,  {% include w3api/param_description.html metodo=_data parametro="int minute" %}
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int timezone**,  {% include w3api/param_description.html metodo=_data parametro="int timezone" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int day**,  {% include w3api/param_description.html metodo=_data parametro="int day" %}
* **BigDecimal fractionalSecond**,  {% include w3api/param_description.html metodo=_data parametro="BigDecimal fractionalSecond" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_data parametro="String lexicalRepresentation" %}
* **int millisecond**,  {% include w3api/param_description.html metodo=_data parametro="int millisecond" %}
* **GregorianCalendar cal**,  {% include w3api/param_description.html metodo=_data parametro="GregorianCalendar cal" %}
* **int hour**,  {% include w3api/param_description.html metodo=_data parametro="int hour" %}
* **int second**,  {% include w3api/param_description.html metodo=_data parametro="int second" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
