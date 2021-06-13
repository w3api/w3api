---
title: DatatypeFactory.newXMLGregorianCalendarTime()
permalink: /Java/DatatypeFactory/newXMLGregorianCalendarTime/
date: 2021-01-11
key: Java.D.DatatypeFactory
category: Java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newXMLGregorianCalendarTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public XMLGregorianCalendar newXMLGregorianCalendarTime(int hours, int minutes, int seconds, int timezone)
public XMLGregorianCalendar newXMLGregorianCalendarTime(int hours, int minutes, int seconds, int milliseconds, int timezone)
public XMLGregorianCalendar newXMLGregorianCalendarTime(int hours, int minutes, int seconds, BigDecimal fractionalSecond, int timezone)
~~~

## Parámetros
* **int seconds**,  {% include w3api/param_description.html metodo=_dato parametro="int seconds" %}
* **int minutes**,  {% include w3api/param_description.html metodo=_dato parametro="int minutes" %}
* **int timezone**,  {% include w3api/param_description.html metodo=_dato parametro="int timezone" %}
* **BigDecimal fractionalSecond**,  {% include w3api/param_description.html metodo=_dato parametro="BigDecimal fractionalSecond" %}
* **int hours**,  {% include w3api/param_description.html metodo=_dato parametro="int hours" %}
* **int milliseconds**,  {% include w3api/param_description.html metodo=_dato parametro="int milliseconds" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
