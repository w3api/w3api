---
title: StreamSource.StreamSource()
permalink: Java/StreamSource/StreamSource
date: 2021-01-11
key: JavaJava.S.StreamSource
category: java
tags: ['java se', 'javax.xml.transform.stream', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StreamSource.constructores valor="StreamSource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StreamSource()
public StreamSource(File f)
public StreamSource(InputStream inputStream)
public StreamSource(InputStream inputStream, String systemId)
public StreamSource(Reader reader)
public StreamSource(Reader reader, String systemId)
public StreamSource(String systemId)
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **File f**,  {% include w3api/param_description.html metodo=_dato parametro="File f" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **InputStream inputStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inputStream" %}

## Clase Padre
[StreamSource](/Java/StreamSource/)

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
