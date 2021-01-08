---
title: XMLResolver.resolveEntity()
permalink: Java/XMLResolver/resolveEntity
date: 2021-01-04
key: JavaJava.X.XMLResolver
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLResolver.metodos valor="resolveEntity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object resolveEntity(String publicID, String systemID, String baseURI, String namespace) throws XMLStreamException
~~~

## Parámetros
* **String namespace**,  {% include w3api/param_description.html metodo=_data parametro="String namespace" %}
* **String publicID**,  {% include w3api/param_description.html metodo=_data parametro="String publicID" %}
* **String baseURI**,  {% include w3api/param_description.html metodo=_data parametro="String baseURI" %}
* **String systemID**,  {% include w3api/param_description.html metodo=_data parametro="String systemID" %}

## Excepciones
[XMLStreamException](/Java/XMLStreamException/)

## Clase Padre
[XMLResolver](/Java/XMLResolver/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLResolver.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
