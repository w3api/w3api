---
title: XMLEventFactory.createNamespace()
permalink: /Java/XMLEventFactory/createNamespace/
date: 2021-01-11
key: Java.X.XMLEventFactory
category: Java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEventFactory.metodos valor="createNamespace" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Namespace createNamespace(String namespaceURI)
public abstract Namespace createNamespace(String prefix, String namespaceUri)
~~~

## Parámetros
* **String namespaceUri**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceUri" %}
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}

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
