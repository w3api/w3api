---
title: XMLOutputFactory.createXMLEventWriter()
permalink: Java/XMLOutputFactory/createXMLEventWriter
date: 2021-01-04
key: JavaJava.X.XMLOutputFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLOutputFactory.metodos valor="createXMLEventWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLEventWriter createXMLEventWriter(OutputStream stream) throws XMLStreamException
public abstract XMLEventWriter createXMLEventWriter(OutputStream stream, String encoding) throws XMLStreamException
public abstract XMLEventWriter createXMLEventWriter(Writer stream) throws XMLStreamException
public abstract XMLEventWriter createXMLEventWriter(Result result) throws XMLStreamException
~~~

## Parámetros
* **OutputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream stream" %}
* **Writer stream**,  {% include w3api/param_description.html metodo=_data parametro="Writer stream" %}
* **Result result**,  {% include w3api/param_description.html metodo=_data parametro="Result result" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_data parametro="String encoding" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLOutputFactory](/Java/XMLOutputFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLOutputFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
