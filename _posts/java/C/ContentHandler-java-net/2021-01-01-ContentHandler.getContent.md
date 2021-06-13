---
title: ContentHandler.getContent()
permalink: /Java/ContentHandler-java-net/getContent/
date: 2021-01-11
key: Java.C.ContentHandler-java-net
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ContentHandler-java-net.metodos valor="getContent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Object getContent(URLConnection urlc) throws IOException
public Object getContent(URLConnection urlc, Class[] classes) throws IOException
~~~

## Parámetros
* **Class[] classes**,  {% include w3api/param_description.html metodo=_dato parametro="Class[] classes" %}
* **URLConnection urlc**,  {% include w3api/param_description.html metodo=_dato parametro="URLConnection urlc" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[ContentHandler](/Java/ContentHandler-java-net/)

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
