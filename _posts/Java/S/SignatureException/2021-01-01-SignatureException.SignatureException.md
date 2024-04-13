---
title: SignatureException.SignatureException()
permalink: /Java/SignatureException/SignatureException/
date: 2021-01-11
key: Java.S.SignatureException
category: Java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SignatureException.constructores valor="SignatureException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SignatureException()
public SignatureException(String msg)
public SignatureException(String message, Throwable cause)
public SignatureException(Throwable cause)
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}

## Clase Padre
[SignatureException](/Java/SignatureException/)

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
