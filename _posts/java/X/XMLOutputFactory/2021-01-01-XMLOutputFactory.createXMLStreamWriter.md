---
title: XMLOutputFactory.createXMLStreamWriter()
permalink: /Java/XMLOutputFactory/createXMLStreamWriter/
date: 2021-01-11
key: Java.X.XMLOutputFactory
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLOutputFactory.metodos valor="createXMLStreamWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLStreamWriter createXMLStreamWriter(OutputStream stream) throws XMLStreamException
public abstract XMLStreamWriter createXMLStreamWriter(OutputStream stream, String encoding) throws XMLStreamException
public abstract XMLStreamWriter createXMLStreamWriter(Writer stream) throws XMLStreamException
public abstract XMLStreamWriter createXMLStreamWriter(Result result) throws XMLStreamException
~~~

## Parámetros
* **OutputStream stream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream stream" %}
* **Writer stream**,  {% include w3api/param_description.html metodo=_dato parametro="Writer stream" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}
* **Result result**,  {% include w3api/param_description.html metodo=_dato parametro="Result result" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[XMLOutputFactory](/Java/XMLOutputFactory/)

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
