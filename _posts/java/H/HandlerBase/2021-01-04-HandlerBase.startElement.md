---
title: HandlerBase.startElement()
permalink: Java/HandlerBase/startElement
date: 2021-01-04
key: JavaJava.H.HandlerBase
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandlerBase.metodos valor="startElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void startElement(String name, AttributeList attributes) throws SAXException
~~~

## Parámetros
* **AttributeList attributes**,  {% include w3api/param_description.html metodo=_data parametro="AttributeList attributes" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[HandlerBase](/Java/HandlerBase/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.H.HandlerBase.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
