---
title: XMLFilterImpl.startElement()
permalink: Java/XMLFilterImpl/startElement
date: 2021-01-04
key: JavaJava.X.XMLFilterImpl
category: java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLFilterImpl.metodos valor="startElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void startElement(String uri, String localName, String qName, Attributes atts) throws SAXException
~~~

## Parámetros
* **Attributes atts**,  {% include w3api/param_description.html metodo=_data parametro="Attributes atts" %}
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String qName**,  {% include w3api/param_description.html metodo=_data parametro="String qName" %}
* **String uri**,  {% include w3api/param_description.html metodo=_data parametro="String uri" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[XMLFilterImpl](/Java/XMLFilterImpl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLFilterImpl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
