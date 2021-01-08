---
title: XMLInputFactory.createXMLStreamReader()
permalink: Java/XMLInputFactory/createXMLStreamReader
date: 2021-01-04
key: JavaJava.X.XMLInputFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLInputFactory.metodos valor="createXMLStreamReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract XMLStreamReader createXMLStreamReader(InputStream stream) throws XMLStreamException
public abstract XMLStreamReader createXMLStreamReader(InputStream stream, String encoding) throws XMLStreamException
public abstract XMLStreamReader createXMLStreamReader(Reader reader) throws XMLStreamException
public abstract XMLStreamReader createXMLStreamReader(String systemId, InputStream stream) throws XMLStreamException
public abstract XMLStreamReader createXMLStreamReader(String systemId, Reader reader) throws XMLStreamException
public abstract XMLStreamReader createXMLStreamReader(Source source) throws XMLStreamException
~~~

## Parámetros
* **InputStream stream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream stream" %}
* **Source source**,  {% include w3api/param_description.html metodo=_data parametro="Source source" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_data parametro="String encoding" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLInputFactory](/Java/XMLInputFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLInputFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
