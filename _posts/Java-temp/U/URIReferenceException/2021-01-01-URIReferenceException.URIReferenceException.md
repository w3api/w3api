---
title: URIReferenceException.URIReferenceException()
permalink: /Java/URIReferenceException/URIReferenceException/
date: 2021-01-11
key: Java.U.URIReferenceException
category: Java
tags: ['java se', 'javax.xml.crypto', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URIReferenceException.constructores valor="URIReferenceException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public URIReferenceException()
public URIReferenceException(String message)
public URIReferenceException(String message, Throwable cause)
public URIReferenceException(String message, Throwable cause, URIReference uriReference)
public URIReferenceException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **URIReference uriReference**,  {% include w3api/param_description.html metodo=_dato parametro="URIReference uriReference" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URIReferenceException](/Java/URIReferenceException/)

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
