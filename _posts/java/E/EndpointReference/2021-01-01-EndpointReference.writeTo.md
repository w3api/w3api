---
title: EndpointReference.writeTo()
permalink: /Java/EndpointReference/writeTo/
date: 2021-01-11
key: Java.E.EndpointReference
category: Java
tags: ['java se', 'javax.xml.ws', 'java.xml.ws', 'metodo java', 'Java 1.6', 'JAX-WS 2.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.EndpointReference.metodos valor="writeTo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void writeTo(Result result)
~~~

## Parámetros
* **Result result**,  {% include w3api/param_description.html metodo=_dato parametro="Result result" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [WebServiceException](/Java/WebServiceException/)

## Clase Padre
[EndpointReference](/Java/EndpointReference/)

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
