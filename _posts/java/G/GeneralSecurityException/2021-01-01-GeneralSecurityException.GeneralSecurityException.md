---
title: GeneralSecurityException.GeneralSecurityException()
permalink: Java/GeneralSecurityException/GeneralSecurityException
date: 2021-01-11
key: JavaJava.G.GeneralSecurityException
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GeneralSecurityException.constructores valor="GeneralSecurityException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GeneralSecurityException()
public GeneralSecurityException(String msg)
public GeneralSecurityException(String message, Throwable cause)
public GeneralSecurityException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}

## Clase Padre
[GeneralSecurityException](/Java/GeneralSecurityException/)

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
