---
title: XMLEventFactory.createStartDocument()
permalink: Java/XMLEventFactory/createStartDocument
date: 2021-01-11
key: JavaJava.X.XMLEventFactory
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="createStartDocument" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract StartDocument createStartDocument()
public abstract StartDocument createStartDocument(String encoding)
public abstract StartDocument createStartDocument(String encoding, String version)
public abstract StartDocument createStartDocument(String encoding, String version, boolean standalone)
~~~

## Parámetros
* **boolean standalone**,  {% include w3api/param_description.html metodo=_dato parametro="boolean standalone" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}
* **String version**,  {% include w3api/param_description.html metodo=_dato parametro="String version" %}

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
