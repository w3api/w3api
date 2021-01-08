---
title: SAXParseException.SAXParseException()
permalink: Java/SAXParseException/SAXParseException
date: 2021-01-04
key: JavaJava.S.SAXParseException
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXParseException.constructores valor="SAXParseException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SAXParseException(String message, String publicId, String systemId, int lineNumber, int columnNumber)
public SAXParseException(String message, String publicId, String systemId, int lineNumber, int columnNumber, Exception e)
public SAXParseException(String message, Locator locator)
public SAXParseException(String message, Locator locator, Exception e)
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **Locator locator**,  {% include w3api/param_description.html metodo=_data parametro="Locator locator" %}
* **int lineNumber**,  {% include w3api/param_description.html metodo=_data parametro="int lineNumber" %}
* **int columnNumber**,  {% include w3api/param_description.html metodo=_data parametro="int columnNumber" %}
* **Exception e**,  {% include w3api/param_description.html metodo=_data parametro="Exception e" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_data parametro="String publicId" %}

## Clase Padre
[SAXParseException](/Java/SAXParseException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SAXParseException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
