---
title: CssParser.parse()
permalink: /Java/CssParser/parse/
date: 2021-01-11
key: Java.C.CssParser
category: Java
tags: ['java se', 'javafx.css', 'javafx.graphics', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CssParser.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Stylesheet parse(String stylesheetText)
public Stylesheet parse(String docbase, String stylesheetText) throws IOException
public Stylesheet parse(URL url) throws IOException
~~~

## Parámetros
* **String docbase**,  {% include w3api/param_description.html metodo=_dato parametro="String docbase" %}
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String stylesheetText**,  {% include w3api/param_description.html metodo=_dato parametro="String stylesheetText" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[CssParser](/Java/CssParser/)

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
