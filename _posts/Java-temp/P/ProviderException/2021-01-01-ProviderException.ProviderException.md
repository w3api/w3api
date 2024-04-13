---
title: ProviderException.ProviderException()
permalink: /Java/ProviderException/ProviderException/
date: 2021-01-11
key: Java.P.ProviderException
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProviderException.constructores valor="ProviderException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProviderException()
public ProviderException(String s)
public ProviderException(String message, Throwable cause)
public ProviderException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}

## Clase Padre
[ProviderException](/Java/ProviderException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
