---
title: PKCS12Attribute.PKCS12Attribute()
permalink: Java/PKCS12Attribute/PKCS12Attribute
date: 2021-01-11
key: JavaJava.P.PKCS12Attribute
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PKCS12Attribute.constructores valor="PKCS12Attribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PKCS12Attribute(byte[] encoded)
public PKCS12Attribute(String name, String value)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **byte[] encoded**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] encoded" %}
* **String value**,  {% include w3api/param_description.html metodo=_dato parametro="String value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PKCS12Attribute](/Java/PKCS12Attribute/)

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
