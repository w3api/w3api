---
title: XMLEventFactory.createAttribute()
permalink: Java/XMLEventFactory/createAttribute
date: 2021-01-11
key: JavaJava.X.XMLEventFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="createAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Attribute createAttribute(String localName, String value)
public abstract Attribute createAttribute(String prefix, String namespaceURI, String localName, String value)
public abstract Attribute createAttribute(QName name, String value)
~~~

## Parámetros
* **QName name**,  {% include w3api/param_description.html metodo=_dato parametro="QName name" %}
* **String localName**,  {% include w3api/param_description.html metodo=_dato parametro="String localName" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}
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
