---
title: XMLFilterImpl.getProperty()
permalink: /Java/XMLFilterImpl/getProperty/
date: 2021-01-11
key: Java.X.XMLFilterImpl
category: Java
tags: ['java se', 'org.xml.sax.helpers', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLFilterImpl.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getProperty(String name) throws SAXNotRecognizedException, SAXNotSupportedException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[SAXNotRecognizedException](/Java/SAXNotRecognizedException/), [SAXNotSupportedException](/Java/SAXNotSupportedException/)

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
