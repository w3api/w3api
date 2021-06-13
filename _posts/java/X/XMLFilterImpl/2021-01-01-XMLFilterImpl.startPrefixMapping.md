---
title: XMLFilterImpl.startPrefixMapping()
permalink: /Java/XMLFilterImpl/startPrefixMapping/
date: 2021-01-11
key: Java.X.XMLFilterImpl
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLFilterImpl.metodos valor="startPrefixMapping" %}

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
[XMLFilterImpl](/Java/XMLFilterImpl/)

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
