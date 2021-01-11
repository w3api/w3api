---
title: XMLStreamReader.getAttributeValue()
permalink: Java/XMLStreamReader/getAttributeValue
date: 2021-01-11
key: JavaJava.X.XMLStreamReader
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamReader.metodos valor="getAttributeValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getAttributeValue(int index)
String getAttributeValue(String namespaceURI, String localName)
~~~

## Parámetros
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[XMLStreamReader](/Java/XMLStreamReader/)

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
