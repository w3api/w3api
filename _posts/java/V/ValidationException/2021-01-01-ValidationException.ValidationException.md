---
title: ValidationException.ValidationException()
permalink: Java/ValidationException/ValidationException
date: 2021-01-11
key: JavaJava.V.ValidationException
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValidationException.constructores valor="ValidationException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ValidationException(String message)
public ValidationException(String message, String errorCode)
public ValidationException(String message, String errorCode, Throwable exception)
public ValidationException(String message, Throwable exception)
public ValidationException(Throwable exception)
~~~

## Parámetros
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}
* **String errorCode**,  {% include w3api/param_description.html metodo=_dato parametro="String errorCode" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[ValidationException](/Java/ValidationException/)

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
