---
title: XMLDecoder.createHandler()
permalink: Java/XMLDecoder/createHandler
date: 2021-01-11
key: JavaJava.X.XMLDecoder
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLDecoder.metodos valor="createHandler" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DefaultHandler createHandler(Object owner, ExceptionListener el, ClassLoader cl)
~~~

## Parámetros
* **Object owner**,  {% include w3api/param_description.html metodo=_dato parametro="Object owner" %}
* **ExceptionListener el**,  {% include w3api/param_description.html metodo=_dato parametro="ExceptionListener el" %}
* **ClassLoader cl**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader cl" %}

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
