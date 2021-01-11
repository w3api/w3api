---
title: NotIdentifiableEventImpl.NotIdentifiableEventImpl()
permalink: Java/NotIdentifiableEventImpl/NotIdentifiableEventImpl
date: 2021-01-11
key: JavaJava.N.NotIdentifiableEventImpl
category: java
tags: ['java se', 'javax.xml.bind.helpers', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NotIdentifiableEventImpl.constructores valor="NotIdentifiableEventImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public NotIdentifiableEventImpl(int _severity, String _message, ValidationEventLocator _locator)
public NotIdentifiableEventImpl(int _severity, String _message, ValidationEventLocator _locator, Throwable _linkedException)
~~~

## Parámetros
* **int _severity**,  {% include w3api/param_description.html metodo=_dato parametro="int _severity" %}
* **Throwable _linkedException**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable _linkedException" %}
* **String _message**,  {% include w3api/param_description.html metodo=_dato parametro="String _message" %}
* **ValidationEventLocator _locator**,  {% include w3api/param_description.html metodo=_dato parametro="ValidationEventLocator _locator" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[NotIdentifiableEventImpl](/Java/NotIdentifiableEventImpl/)

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
