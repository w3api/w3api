---
title: Marshaller.marshal()
permalink: Java/Marshaller/marshal
date: 2021-01-11
key: JavaJava.M.Marshaller
category: Java
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
* **Result result**,  {% include w3api/param_description.html metodo=_dato parametro="Result result" %}
* **XMLEventWriter writer**,  {% include w3api/param_description.html metodo=_dato parametro="XMLEventWriter writer" %}
* **Object jaxbElement**,  {% include w3api/param_description.html metodo=_dato parametro="Object jaxbElement" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_dato parametro="Writer writer" %}
* **Node node**,  {% include w3api/param_description.html metodo=_dato parametro="Node node" %}
* **File output**,  {% include w3api/param_description.html metodo=_dato parametro="File output" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}
* **ContentHandler handler**,  {% include w3api/param_description.html metodo=_dato parametro="ContentHandler handler" %}
* **XMLStreamWriter writer**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStreamWriter writer" %}

## Excepciones
[MarshalException](/Java/MarshalException/), [JAXBException](/Java/JAXBException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Marshaller](/Java/Marshaller/)

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
