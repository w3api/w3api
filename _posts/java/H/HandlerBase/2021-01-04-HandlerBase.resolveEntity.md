---
title: HandlerBase.resolveEntity()
permalink: Java/HandlerBase/resolveEntity
date: 2021-01-04
key: JavaJava.H.HandlerBase
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandlerBase.metodos valor="resolveEntity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputSource resolveEntity(String publicId, String systemId) throws SAXException
~~~

## Parámetros
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_data parametro="String publicId" %}

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
