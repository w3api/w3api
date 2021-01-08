---
title: XMLReporter.report()
permalink: Java/XMLReporter/report
date: 2021-01-04
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
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Location location**,  {% include w3api/param_description.html metodo=_data parametro="Location location" %}
* **Object relatedInformation**,  {% include w3api/param_description.html metodo=_data parametro="Object relatedInformation" %}
* **String errorType**,  {% include w3api/param_description.html metodo=_data parametro="String errorType" %}

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
{%- for _ldc in site.data.Java.X.XMLReporter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
