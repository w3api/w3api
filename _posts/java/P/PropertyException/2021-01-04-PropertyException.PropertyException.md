---
title: PropertyException.PropertyException()
permalink: Java/PropertyException/PropertyException
date: 2021-01-04
key: JavaJava.P.PropertyException
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
* **Throwable exception**,  {% include w3api/param_description.html metodo=_data parametro="Throwable exception" %}
* **String message**,  {% include w3api/param_description.html metodo=_data parametro="String message" %}
* **String errorCode**,  {% include w3api/param_description.html metodo=_data parametro="String errorCode" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **Object value**,  {% include w3api/param_description.html metodo=_data parametro="Object value" %}

## Clase Padre
[PropertyException](/Java/PropertyException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PropertyException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
