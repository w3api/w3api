---
title: XMLEventFactory.createStartElement()
permalink: Java/XMLEventFactory/createStartElement
date: 2021-01-04
key: JavaJava.X.XMLEventFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="createStartElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract StartElement createStartElement(String prefix, String namespaceUri, String localName)
public abstract StartElement createStartElement(String prefix, String namespaceUri, String localName, Iterator<? extends Attribute> attributes, Iterator<? extends Namespace> namespaces)
public abstract StartElement createStartElement(String prefix, String namespaceUri, String localName, Iterator<? extends Attribute> attributes, Iterator<? extends Namespace> namespaces, NamespaceContext context)
public abstract StartElement createStartElement(QName name, Iterator<? extends Attribute> attributes, Iterator<? extends Namespace> namespaces)
~~~

## Parámetros
* **QName name**,  {% include w3api/param_description.html metodo=_data parametro="QName name" %}
* **NamespaceContext context**,  {% include w3api/param_description.html metodo=_data parametro="NamespaceContext context" %}
* **String localName**,  {% include w3api/param_description.html metodo=_data parametro="String localName" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_data parametro="String prefix" %}
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_data parametro="String namespaceUri" %}
* **Iterator&lt;? extends Attribute&gt; attributes**,  {% include w3api/param_description.html metodo=_data parametro="Iterator<? extends Attribute> attributes" %}
* **Iterator&lt;? extends Namespace&gt; namespaces**,  {% include w3api/param_description.html metodo=_data parametro="Iterator<? extends Namespace> namespaces" %}

## Clase Padre
[XMLEventFactory](/Java/XMLEventFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLEventFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
