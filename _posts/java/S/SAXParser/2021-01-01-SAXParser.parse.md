---
title: SAXParser.parse()
permalink: Java/SAXParser/parse
date: 2021-01-11
key: JavaJava.S.SAXParser
category: java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SAXParser.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void parse(File f, HandlerBase hb) throws SAXException, IOException
public void parse(File f, DefaultHandler dh) throws SAXException, IOException
public void parse(InputStream is, HandlerBase hb) throws SAXException, IOException
public void parse(InputStream is, HandlerBase hb, String systemId) throws SAXException, IOException
public void parse(InputStream is, DefaultHandler dh) throws SAXException, IOException
public void parse(InputStream is, DefaultHandler dh, String systemId) throws SAXException, IOException
public void parse(String uri, HandlerBase hb) throws SAXException, IOException
public void parse(String uri, DefaultHandler dh) throws SAXException, IOException
public void parse(InputSource is, HandlerBase hb) throws SAXException, IOException
public void parse(InputSource is, DefaultHandler dh) throws SAXException, IOException
~~~

## Parámetros
* **File f**,  {% include w3api/param_description.html metodo=_dato parametro="File f" %}
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **InputStream is**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream is" %}
* **InputSource is**,  {% include w3api/param_description.html metodo=_dato parametro="InputSource is" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}
* **DefaultHandler dh**,  {% include w3api/param_description.html metodo=_dato parametro="DefaultHandler dh" %}
* **HandlerBase hb**,  {% include w3api/param_description.html metodo=_dato parametro="HandlerBase hb" %}

## Excepciones
[SAXException](/Java/SAXException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[SAXParser](/Java/SAXParser/)

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
