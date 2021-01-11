---
title: StreamResult.StreamResult()
permalink: Java/StreamResult/StreamResult
date: 2021-01-11
key: JavaJava.S.StreamResult
category: java
tags: ['java se', 'javax.xml.transform.stream', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamResult.constructores valor="StreamResult" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StreamResult()
public StreamResult(File f)
public StreamResult(OutputStream outputStream)
public StreamResult(Writer writer)
public StreamResult(String systemId)
~~~

## Parámetros
* **OutputStream outputStream**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream outputStream" %}
* **File f**,  {% include w3api/param_description.html metodo=_dato parametro="File f" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_dato parametro="Writer writer" %}

## Clase Padre
[StreamResult](/Java/StreamResult/)

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
