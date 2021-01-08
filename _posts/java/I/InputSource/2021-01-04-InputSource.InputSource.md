---
title: InputSource.InputSource()
permalink: Java/InputSource/InputSource
date: 2021-01-04
key: JavaJava.I.InputSource
category: java
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
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **InputStream byteStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream byteStream" %}
* **Reader characterStream**,  {% include w3api/param_description.html metodo=_data parametro="Reader characterStream" %}

## Clase Padre
[InputSource](/Java/InputSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InputSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
