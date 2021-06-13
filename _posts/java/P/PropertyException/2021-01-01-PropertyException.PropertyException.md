---
title: PropertyException.PropertyException()
permalink: /Java/PropertyException/PropertyException/
date: 2021-01-11
key: Java.P.PropertyException
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PropertyException.constructores valor="PropertyException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PropertyException(String message)
public PropertyException(String name, Object value)
public PropertyException(String message, String errorCode)
public PropertyException(String message, String errorCode, Throwable exception)
public PropertyException(String message, Throwable exception)
public PropertyException(Throwable exception)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String errorCode**,  {% include w3api/param_description.html metodo=_dato parametro="String errorCode" %}
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}

## Clase Padre
[PropertyException](/Java/PropertyException/)

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
