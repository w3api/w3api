---
title: XMLEncoder.XMLEncoder()
permalink: Java/XMLEncoder/XMLEncoder
date: 2021-01-04
key: JavaJava.X.XMLEncoder
category: java
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
* **String charset**,  {% include w3api/param_description.html metodo=_data parametro="String charset" %}
* **boolean declaration**,  {% include w3api/param_description.html metodo=_data parametro="boolean declaration" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}
* **int indentation**,  {% include w3api/param_description.html metodo=_data parametro="int indentation" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [UnsupportedCharsetException](/Java/UnsupportedCharsetException/), [IllegalCharsetNameException](/Java/IllegalCharsetNameException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[XMLEncoder](/Java/XMLEncoder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.XMLEncoder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
