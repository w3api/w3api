---
title: SAXParseException.SAXParseException()
permalink: /Java/SAXParseException/SAXParseException/
date: 2021-01-11
key: Java.S.SAXParseException
category: Java
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
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **Locator locator**,  {% include w3api/param_description.html metodo=_dato parametro="Locator locator" %}
* **int lineNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int lineNumber" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **int columnNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int columnNumber" %}
* **Exception e**,  {% include w3api/param_description.html metodo=_dato parametro="Exception e" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

## Clase Padre
[SAXParseException](/Java/SAXParseException/)

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
