---
title: DOMImplementationLS.createLSParser()
permalink: Java/DOMImplementationLS/createLSParser
date: 2021-01-11
key: JavaJava.D.DOMImplementationLS
category: java
tags: ['java se', 'org.w3c.dom.ls', 'java.xml', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DOMImplementationLS.metodos valor="createLSParser" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LSParser createLSParser(short mode, String schemaType) throws DOMException
~~~

## Parámetros
* **short mode**,  {% include w3api/param_description.html metodo=_dato parametro="short mode" %}
* **String schemaType**,  {% include w3api/param_description.html metodo=_dato parametro="String schemaType" %}

## Excepciones
[DOMException](/Java/DOMException/)

## Clase Padre
[DOMImplementationLS](/Java/DOMImplementationLS/)

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
