---
title: MarshalException.MarshalException()
permalink: Java/MarshalException-javax-xml-bind/MarshalException
date: 2021-01-11
key: JavaJava.M.MarshalException-javax-xml-bind
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MarshalException-javax-xml-bind.constructores valor="MarshalException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MarshalException(String message)
public MarshalException(String message, String errorCode)
public MarshalException(String message, String errorCode, Throwable exception)
public MarshalException(String message, Throwable exception)
public MarshalException(Throwable exception)
~~~

## Parámetros
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}
* **String errorCode**,  {% include w3api/param_description.html metodo=_dato parametro="String errorCode" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[MarshalException](/Java/MarshalException-javax-xml-bind/)

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
