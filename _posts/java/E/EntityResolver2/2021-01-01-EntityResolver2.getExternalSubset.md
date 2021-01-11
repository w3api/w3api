---
title: EntityResolver2.getExternalSubset()
permalink: Java/EntityResolver2/getExternalSubset
date: 2021-01-11
key: JavaJava.E.EntityResolver2
category: java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.5', 'SAX 2.0 (extensions Java 1.1 alpha)']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EntityResolver2.metodos valor="getExternalSubset" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
InputSource getExternalSubset(String name, String baseURI) throws SAXException, IOException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String baseURI**,  {% include w3api/param_description.html metodo=_dato parametro="String baseURI" %}

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
