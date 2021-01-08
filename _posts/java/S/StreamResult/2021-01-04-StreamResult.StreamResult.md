---
title: StreamResult.StreamResult()
permalink: Java/StreamResult/StreamResult
date: 2021-01-04
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
* **String systemId**,  {% include w3api/param_description.html metodo=_data parametro="String systemId" %}
* **File f**,  {% include w3api/param_description.html metodo=_data parametro="File f" %}
* **Writer writer**,  {% include w3api/param_description.html metodo=_data parametro="Writer writer" %}
* **OutputStream outputStream**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream outputStream" %}

## Clase Padre
[StreamResult](/Java/StreamResult/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StreamResult.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
