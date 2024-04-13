---
title: XMLEventFactory.createStartElement()
permalink: /Java/XMLEventFactory/createStartElement/
date: 2021-01-11
key: Java.X.XMLEventFactory
category: Java
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
* **QName name**,  {% include w3api/param_description.html metodo=_dato parametro="QName name" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceUri" %}
* **Iterator&lt;? extends Namespace&gt; namespaces**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<? extends Namespace> namespaces" %}
* **NamespaceContext context**,  {% include w3api/param_description.html metodo=_dato parametro="NamespaceContext context" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **Iterator&lt;? extends Attribute&gt; attributes**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<? extends Attribute> attributes" %}

## Clase Padre
[XMLEventFactory](/Java/XMLEventFactory/)

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
