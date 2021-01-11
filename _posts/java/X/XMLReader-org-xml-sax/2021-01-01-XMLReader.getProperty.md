---
title: XMLReader.getProperty()
permalink: Java/XMLReader-org-xml-sax/getProperty
date: 2021-01-11
key: JavaJava.X.XMLReader-org-xml-sax
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLReader-org-xml-sax.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getProperty(String name) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/)

## Clase Padre
[XMLReader](/Java/XMLReader-org-xml-sax/)

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
