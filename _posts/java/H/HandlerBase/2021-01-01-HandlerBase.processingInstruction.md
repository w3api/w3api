---
title: HandlerBase.processingInstruction()
permalink: Java/HandlerBase/processingInstruction
date: 2021-01-11
key: JavaJava.H.HandlerBase
category: java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandlerBase.metodos valor="processingInstruction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void processingInstruction(String target, String data) throws SAXException
~~~

## Parámetros
* **String data**,  {% include w3api/param_description.html metodo=_dato parametro="String data" %}
* **String target**,  {% include w3api/param_description.html metodo=_dato parametro="String target" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
