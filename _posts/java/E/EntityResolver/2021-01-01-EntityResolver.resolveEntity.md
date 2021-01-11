---
title: EntityResolver.resolveEntity()
permalink: Java/EntityResolver/resolveEntity
date: 2021-01-11
key: JavaJava.E.EntityResolver
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EntityResolver.metodos valor="resolveEntity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
InputSource resolveEntity(String publicId, String systemId) throws SAXException, IOException
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

## Excepciones
[SAXException](/Java/SAXException/), [IOException](/Java/IOException/)

## Clase Padre
[EntityResolver](/Java/EntityResolver/)

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
