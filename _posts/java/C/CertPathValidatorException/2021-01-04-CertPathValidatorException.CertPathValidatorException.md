---
title: CertPathValidatorException.CertPathValidatorException()
permalink: Java/CertPathValidatorException/CertPathValidatorException
date: 2021-01-04
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
* **CertPath certPath**,  {% include w3api/param_description.html metodo=_data parametro="CertPath certPath" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}
* **CertPathValidatorException.Reason reason**,  {% include w3api/param_description.html metodo=_data parametro="CertPathValidatorException.Reason reason" %}
* **String msg**,  {% include w3api/param_description.html metodo=_data parametro="String msg" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CertPathValidatorException](/Java/CertPathValidatorException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertPathValidatorException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
