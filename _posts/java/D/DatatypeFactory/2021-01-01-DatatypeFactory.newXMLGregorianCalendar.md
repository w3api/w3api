---
title: DatatypeFactory.newXMLGregorianCalendar()
permalink: /Java/DatatypeFactory/newXMLGregorianCalendar/
date: 2021-01-11
key: Java.D.DatatypeFactory
category: Java
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
* **GregorianCalendar cal**,  {% include w3api/param_description.html metodo=_dato parametro="GregorianCalendar cal" %}
* **String lexicalRepresentation**,  {% include w3api/param_description.html metodo=_dato parametro="String lexicalRepresentation" %}
* **int day**,  {% include w3api/param_description.html metodo=_dato parametro="int day" %}
* **int millisecond**,  {% include w3api/param_description.html metodo=_dato parametro="int millisecond" %}
* **int timezone**,  {% include w3api/param_description.html metodo=_dato parametro="int timezone" %}
* **int month**,  {% include w3api/param_description.html metodo=_dato parametro="int month" %}
* **BigInteger year**,  {% include w3api/param_description.html metodo=_dato parametro="BigInteger year" %}
* **int minute**,  {% include w3api/param_description.html metodo=_dato parametro="int minute" %}
* **int second**,  {% include w3api/param_description.html metodo=_dato parametro="int second" %}
* **int year**,  {% include w3api/param_description.html metodo=_dato parametro="int year" %}
* **BigDecimal fractionalSecond**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal fractionalSecond" %}
* **int hour**,  {% include w3api/param_description.html metodo=_dato parametro="int hour" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

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
