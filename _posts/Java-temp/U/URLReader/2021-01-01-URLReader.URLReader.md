---
title: URLReader.URLReader()
permalink: /Java/URLReader/URLReader/
date: 2021-01-11
key: Java.U.URLReader
category: Java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLReader.constructores valor="URLReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public URLReader(URL url)
public URLReader(URL url, String charsetName)
public URLReader(URL url, Charset cs)
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}
* **String charsetName**,  {% include w3api/param_description.html metodo=_dato parametro="String charsetName" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_dato parametro="Charset cs" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URLReader](/Java/URLReader/)

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
