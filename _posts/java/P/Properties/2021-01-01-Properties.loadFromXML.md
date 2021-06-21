---
title: Properties.loadFromXML()
permalink: /Java/Properties/loadFromXML/
date: 2021-01-11
key: Java.P.Properties
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.Properties.metodos valor="loadFromXML" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void loadFromXML(InputStream in) throws IOException, InvalidPropertiesFormatException
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [InvalidPropertiesFormatException](/Java/InvalidPropertiesFormatException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[Properties](/Java/Properties/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
