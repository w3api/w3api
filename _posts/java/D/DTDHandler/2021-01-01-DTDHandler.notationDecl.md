---
title: DTDHandler.notationDecl()
permalink: /Java/DTDHandler/notationDecl/
date: 2021-01-11
key: Java.D.DTDHandler
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
