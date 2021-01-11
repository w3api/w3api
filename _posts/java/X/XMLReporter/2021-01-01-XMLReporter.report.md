---
title: XMLReporter.report()
permalink: Java/XMLReporter/report
date: 2021-01-11
key: JavaJava.X.XMLReporter
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReporter.metodos valor="report" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void report(String message, String errorType, Object relatedInformation, Location location) throws XMLStreamException
~~~

## Parámetros
* **Location location**,  {% include w3api/param_description.html metodo=_dato parametro="Location location" %}
* **String errorType**,  {% include w3api/param_description.html metodo=_dato parametro="String errorType" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **Object relatedInformation**,  {% include w3api/param_description.html metodo=_dato parametro="Object relatedInformation" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLReporter](/Java/XMLReporter/)

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
