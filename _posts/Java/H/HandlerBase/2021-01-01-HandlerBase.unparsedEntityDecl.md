---
title: HandlerBase.unparsedEntityDecl()
permalink: /Java/HandlerBase/unparsedEntityDecl/
date: 2021-01-11
key: Java.H.HandlerBase
category: Java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.H.HandlerBase.metodos valor="unparsedEntityDecl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void unparsedEntityDecl(String name, String publicId, String systemId, String notationName)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **String publicId**,  {% include w3api/param_description.html metodo=_dato parametro="String publicId" %}
* **String notationName**,  {% include w3api/param_description.html metodo=_dato parametro="String notationName" %}

## Clase Padre
[HandlerBase](/Java/HandlerBase/)

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
