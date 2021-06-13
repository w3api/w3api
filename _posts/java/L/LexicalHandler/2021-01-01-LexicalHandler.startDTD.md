---
title: LexicalHandler.startDTD()
permalink: /Java/LexicalHandler/startDTD/
date: 2021-01-11
key: Java.L.LexicalHandler
category: Java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0 (extensions Java 1.0)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LexicalHandler.metodos valor="startDTD" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void startDTD(String name, String publicId, String systemId) throws SAXException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[LexicalHandler](/Java/LexicalHandler/)

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
