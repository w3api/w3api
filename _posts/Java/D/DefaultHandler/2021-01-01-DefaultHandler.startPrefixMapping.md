---
title: DefaultHandler.startPrefixMapping()
permalink: /Java/DefaultHandler/startPrefixMapping/
date: 2021-01-11
key: Java.D.DefaultHandler
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultHandler.metodos valor="startPrefixMapping" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void startPrefixMapping(String prefix, String uri) throws SAXException
~~~

## Parámetros
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DefaultHandler](/Java/DefaultHandler/)

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
