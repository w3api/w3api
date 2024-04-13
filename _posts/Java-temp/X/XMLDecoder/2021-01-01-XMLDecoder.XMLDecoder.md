---
title: XMLDecoder.XMLDecoder()
permalink: /Java/XMLDecoder/XMLDecoder/
date: 2021-01-11
key: Java.X.XMLDecoder
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLDecoder.constructores valor="XMLDecoder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public XMLDecoder(InputStream in)
public XMLDecoder(InputStream in, Object owner)
public XMLDecoder(InputStream in, Object owner, ExceptionListener exceptionListener)
public XMLDecoder(InputStream in, Object owner, ExceptionListener exceptionListener, ClassLoader cl)
public XMLDecoder(InputSource is)
~~~

## Parámetros
* **Object owner**,  {% include w3api/param_description.html metodo=_dato parametro="Object owner" %}
* **ClassLoader cl**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader cl" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **ExceptionListener exceptionListener**,  {% include w3api/param_description.html metodo=_dato parametro="ExceptionListener exceptionListener" %}
* **InputSource is**,  {% include w3api/param_description.html metodo=_dato parametro="InputSource is" %}

## Clase Padre
[XMLDecoder](/Java/XMLDecoder/)

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
