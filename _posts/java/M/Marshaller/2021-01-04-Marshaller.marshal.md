---
title: Marshaller.marshal()
permalink: Java/Marshaller/marshal
date: 2021-01-04
key: JavaJava.M.Marshaller
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.Marshaller.metodos valor="marshal" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void marshal(Object jaxbElement, File output) throws JAXBException
void marshal(Object jaxbElement, OutputStream os) throws JAXBException
void marshal(Object jaxbElement, Writer writer) throws JAXBException
void marshal(Object jaxbElement, XMLEventWriter writer) throws JAXBException
void marshal(Object jaxbElement, XMLStreamWriter writer) throws JAXBException
void marshal(Object jaxbElement, Result result) throws JAXBException
void marshal(Object jaxbElement, Node node) throws JAXBException
void marshal(Object jaxbElement, ContentHandler handler) throws JAXBException
~~~

## Parámetros
* **XMLEventWriter writer**,  {% include w3api/param_description.html metodo=_data parametro="XMLEventWriter writer" %}
* **File output**,  {% include w3api/param_description.html metodo=_data parametro="File output" %}
* **Object jaxbElement**,  {% include w3api/param_description.html metodo=_data parametro="Object jaxbElement" %}
* **XMLStreamWriter writer**,  {% include w3api/param_description.html metodo=_data parametro="XMLStreamWriter writer" %}
* **Node node**,  {% include w3api/param_description.html metodo=_data parametro="Node node" %}
* **ContentHandler handler**,  {% include w3api/param_description.html metodo=_data parametro="ContentHandler handler" %}
* **Result result**,  {% include w3api/param_description.html metodo=_data parametro="Result result" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream os" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_data parametro="Writer writer" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [MarshalException](/Java/MarshalException/), [JAXBException](/Java/JAXBException/)

## Clase Padre
[Marshaller](/Java/Marshaller/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.Marshaller.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
