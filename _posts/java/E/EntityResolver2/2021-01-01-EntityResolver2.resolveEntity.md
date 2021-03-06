---
title: EntityResolver2.resolveEntity()
permalink: /Java/EntityResolver2/resolveEntity/
date: 2021-01-11
key: Java.E.EntityResolver2
category: Java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.5', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EntityResolver2.metodos valor="resolveEntity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
InputSource resolveEntity(String name, String publicId, String baseURI, String systemId) throws SAXException, IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String baseURI**,  {% include w3api/param_description.html metodo=_dato parametro="String baseURI" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

## Excepciones
[SAXException](/Java/SAXException/), [IOException](/Java/IOException/)

## Clase Padre
[EntityResolver2](/Java/EntityResolver2/)

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
