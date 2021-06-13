---
title: XMLEncoder.XMLEncoder()
permalink: /Java/XMLEncoder/XMLEncoder/
date: 2021-01-11
key: Java.X.XMLEncoder
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLEncoder.constructores valor="XMLEncoder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public XMLEncoder(OutputStream out)
public XMLEncoder(OutputStream out, String charset, boolean declaration, int indentation)
~~~

## Parámetros
* **String charset**,  {% include w3api/param_description.html metodo=_dato parametro="String charset" %}
* **int indentation**,  {% include w3api/param_description.html metodo=_dato parametro="int indentation" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **boolean declaration**,  {% include w3api/param_description.html metodo=_dato parametro="boolean declaration" %}

## Excepciones
[IllegalCharsetNameException](/Java/IllegalCharsetNameException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedCharsetException](/Java/UnsupportedCharsetException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[XMLEncoder](/Java/XMLEncoder/)

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
