---
title: CertPathValidatorException.CertPathValidatorException()
permalink: Java/CertPathValidatorException/CertPathValidatorException
date: 2021-01-11
key: JavaJava.C.CertPathValidatorException
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertPathValidatorException.constructores valor="CertPathValidatorException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CertPathValidatorException()
public CertPathValidatorException(String msg)
public CertPathValidatorException(String msg, Throwable cause)
public CertPathValidatorException(String msg, Throwable cause, CertPath certPath, int index)
public CertPathValidatorException(String msg, Throwable cause, CertPath certPath, int index, CertPathValidatorException.Reason reason)
public CertPathValidatorException(Throwable cause)
~~~

## Parámetros
* **CertPathValidatorException.Reason reason**,  {% include w3api/param_description.html metodo=_dato parametro="CertPathValidatorException.Reason reason" %}
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_dato parametro="CertPath certPath" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CertPathValidatorException](/Java/CertPathValidatorException/)

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
