---
title: DocumentBuilder.parse()
permalink: /Java/DocumentBuilder/parse/
date: 2021-01-11
key: Java.D.DocumentBuilder
category: Java
tags: ['java se', 'javax.xml.parsers', 'java.xml', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocumentBuilder.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Document parse(File f) throws SAXException, IOException
public Document parse(InputStream is) throws SAXException, IOException
public Document parse(InputStream is, String systemId) throws SAXException, IOException
public Document parse(String uri) throws SAXException, IOException
public abstract Document parse(InputSource is) throws SAXException, IOException
~~~

## Parámetros
* **File f**,  {% include w3api/param_description.html metodo=_dato parametro="File f" %}
* **String uri**,  {% include w3api/param_description.html metodo=_dato parametro="String uri" %}
* **InputStream is**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream is" %}
* **InputSource is**,  {% include w3api/param_description.html metodo=_dato parametro="InputSource is" %}
* **String systemId**,  {% include w3api/param_description.html metodo=_dato parametro="String systemId" %}

## Excepciones
[SAXException](/Java/SAXException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/)

## Clase Padre
[DocumentBuilder](/Java/DocumentBuilder/)

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
