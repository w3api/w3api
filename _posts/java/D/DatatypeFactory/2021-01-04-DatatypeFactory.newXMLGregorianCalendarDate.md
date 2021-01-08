---
title: DatatypeFactory.newXMLGregorianCalendarDate()
permalink: Java/DatatypeFactory/newXMLGregorianCalendarDate
date: 2021-01-04
key: JavaJava.D.DatatypeFactory
category: java
tags: ['java se', 'javax.xml.datatype', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatatypeFactory.metodos valor="newXMLGregorianCalendarDate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public XMLGregorianCalendar newXMLGregorianCalendarDate(int year, int month, int day, int timezone)
~~~

## Parámetros
* **int year**,  {% include w3api/param_description.html metodo=_data parametro="int year" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int timezone**,  {% include w3api/param_description.html metodo=_data parametro="int timezone" %}
* **int day**,  {% include w3api/param_description.html metodo=_data parametro="int day" %}

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
{%- for _ldc in site.data.Java.D.DatatypeFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
