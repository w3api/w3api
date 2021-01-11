---
title: LSResourceResolver.resolveResource()
permalink: Java/LSResourceResolver/resolveResource
date: 2021-01-11
key: JavaJava.L.LSResourceResolver
category: java
tags: ['java se', 'org.w3c.dom.ls', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LSResourceResolver.metodos valor="resolveResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LSInput resolveResource(String type, String namespaceURI, String publicId, String systemId, String baseURI)
~~~

## Parámetros
* **String baseURI**,  {% include w3api/param_description.html metodo=_dato parametro="String baseURI" %}
* **String namespaceURI**,  {% include w3api/param_description.html metodo=_dato parametro="String namespaceURI" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String type**,  {% include w3api/param_description.html metodo=_dato parametro="String type" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}

## Clase Padre
[LSResourceResolver](/Java/LSResourceResolver/)

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
