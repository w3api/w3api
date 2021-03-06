---
title: XMLEventFactory.createEndElement()
permalink: /Java/XMLEventFactory/createEndElement/
date: 2021-01-11
key: Java.X.XMLEventFactory
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="createEndElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract EndElement createEndElement(String prefix, String namespaceUri, String localName)
public abstract EndElement createEndElement(String prefix, String namespaceUri, String localName, Iterator<? extends Namespace> namespaces)
public abstract EndElement createEndElement(QName name, Iterator<? extends Namespace> namespaces)
~~~

## Parámetros
* **QName name**,  {% include w3api/param_description.html metodo=_dato parametro="QName name" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceUri" %}
* **Iterator&lt;? extends Namespace&gt; namespaces**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<? extends Namespace> namespaces" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}

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
