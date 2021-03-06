---
title: ValidationEventImpl.ValidationEventImpl()
permalink: /Java/ValidationEventImpl/ValidationEventImpl/
date: 2021-01-11
key: Java.V.ValidationEventImpl
category: Java
tags: ['java se', 'javax.xml.bind.helpers', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.ValidationEventImpl.constructores valor="ValidationEventImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ValidationEventImpl(int _severity, String _message, ValidationEventLocator _locator)
public ValidationEventImpl(int _severity, String _message, ValidationEventLocator _locator, Throwable _linkedException)
~~~

## Parámetros
* **int _severity**,  {% include w3api/param_description.html metodo=_dato parametro="int _severity" %}
* **Throwable _linkedException**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable _linkedException" %}
* **String _message**,  {% include w3api/param_description.html metodo=_dato parametro="String _message" %}
* **ValidationEventLocator _locator**,  {% include w3api/param_description.html metodo=_dato parametro="ValidationEventLocator _locator" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ValidationEventImpl](/Java/ValidationEventImpl/)

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
