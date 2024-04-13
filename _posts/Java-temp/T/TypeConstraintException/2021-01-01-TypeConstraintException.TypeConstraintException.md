---
title: TypeConstraintException.TypeConstraintException()
permalink: /Java/TypeConstraintException/TypeConstraintException/
date: 2021-01-11
key: Java.T.TypeConstraintException
category: Java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeConstraintException.constructores valor="TypeConstraintException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TypeConstraintException(String message)
public TypeConstraintException(String message, String errorCode)
public TypeConstraintException(String message, String errorCode, Throwable exception)
public TypeConstraintException(String message, Throwable exception)
public TypeConstraintException(Throwable exception)
~~~

## Parámetros
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}
* **String errorCode**,  {% include w3api/param_description.html metodo=_dato parametro="String errorCode" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[TypeConstraintException](/Java/TypeConstraintException/)

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
