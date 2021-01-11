---
title: XMLStreamException.XMLStreamException()
permalink: Java/XMLStreamException/XMLStreamException
date: 2021-01-11
key: JavaJava.X.XMLStreamException
category: java
tags: ['java se', 'javax.xml.stream', 'java.xml', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XMLStreamException.constructores valor="XMLStreamException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public XMLStreamException()
public XMLStreamException(String msg)
public XMLStreamException(String msg, Throwable th)
public XMLStreamException(String msg, Location location)
public XMLStreamException(String msg, Location location, Throwable th)
public XMLStreamException(Throwable th)
~~~

## Parámetros
* **Location location**,  {% include w3api/param_description.html metodo=_dato parametro="Location location" %}
* **Throwable th**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable th" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}

## Clase Padre
[XMLStreamException](/Java/XMLStreamException/)

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
