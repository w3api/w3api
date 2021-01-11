---
title: JAXBException.JAXBException()
permalink: Java/JAXBException/JAXBException
date: 2021-01-11
key: JavaJava.J.JAXBException
category: java
tags: ['java se', 'javax.xml.bind', 'java.xml.bind', 'metodo java', 'Java 1.6', 'JAXB Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JAXBException.constructores valor="JAXBException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JAXBException(String message)
public JAXBException(String message, String errorCode)
public JAXBException(String message, String errorCode, Throwable exception)
public JAXBException(String message, Throwable exception)
public JAXBException(Throwable exception)
~~~

## Parámetros
* **Throwable exception**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable exception" %}
* **String errorCode**,  {% include w3api/param_description.html metodo=_dato parametro="String errorCode" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}

## Clase Padre
[JAXBException](/Java/JAXBException/)

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
