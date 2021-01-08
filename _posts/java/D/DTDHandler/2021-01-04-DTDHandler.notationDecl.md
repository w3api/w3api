---
title: DTDHandler.notationDecl()
permalink: Java/DTDHandler/notationDecl
date: 2021-01-04
key: JavaJava.D.DTDHandler
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DTDHandler.metodos valor="notationDecl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void notationDecl(String name, String publicId, String systemId) throws SAXException
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_data parametro="String publicId" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DTDHandler](/Java/DTDHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DTDHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
