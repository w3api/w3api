---
title: DeclHandler.internalEntityDecl()
permalink: /Java/DeclHandler/internalEntityDecl/
date: 2021-01-11
key: Java.D.DeclHandler
category: Java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DeclHandler.metodos valor="internalEntityDecl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void internalEntityDecl(String name, String value) throws SAXException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

## Excepciones
[SAXException](/Java/SAXException/)

## Clase Padre
[DeclHandler](/Java/DeclHandler/)

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
