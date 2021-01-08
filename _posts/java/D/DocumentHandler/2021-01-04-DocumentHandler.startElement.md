---
title: DocumentHandler.startElement()
permalink: Java/DocumentHandler/startElement
date: 2021-01-04
key: JavaJava.D.DocumentHandler
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentHandler.metodos valor="startElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void startElement(String name, AttributeList atts) throws SAXException
~~~

## Parámetros
* **AttributeList atts**,  {% include w3api/param_description.html metodo=_data parametro="AttributeList atts" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DocumentHandler](/Java/DocumentHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocumentHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
