---
title: InputSource.InputSource()
permalink: /Java/InputSource/InputSource/
date: 2021-01-11
key: Java.I.InputSource
category: Java
tags: ['java se', 'org.xml.sax', 'java.xml', 'metodo java', 'Java 1.4', 'SAX Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputSource.constructores valor="InputSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputSource()
public InputSource(InputStream byteStream)
public InputSource(Reader characterStream)
public InputSource(String systemId)
~~~

## Parámetros
* **Reader characterStream**,  {% include w3api/param_description.html metodo=_dato parametro="Reader characterStream" %}
* **InputStream byteStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream byteStream" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}

## Clase Padre
[InputSource](/Java/InputSource/)

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
