---
title: DeclHandler.elementDecl()
permalink: /Java/DeclHandler/elementDecl/
date: 2021-01-11
key: Java.D.DeclHandler
category: Java
tags: ['java se', 'org.xml.sax.ext', 'java.xml', 'metodo java', 'Java 1.4', 'SAX 2.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DeclHandler.metodos valor="elementDecl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void elementDecl(String name, String model) throws SAXException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String model**,  {% include w3api/param_description.html metodo=_dato parametro="String model" %}

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
