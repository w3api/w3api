---
title: X509Certificate.checkValidity()
permalink: Java/X509Certificate-java-security-cert/checkValidity
date: 2021-01-11
key: JavaJava.X.X509Certificate-java-security-cert
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509Certificate-java-security-cert.metodos valor="checkValidity" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void checkValidity() throws CertificateExpiredException, CertificateNotYetValidException
public abstract void checkValidity(Date date) throws CertificateExpiredException, CertificateNotYetValidException
~~~

## Parámetros
* **Date date**,  {% include w3api/param_description.html metodo=_dato parametro="Date date" %}

## Excepciones
[CertificateExpiredException](/Java/CertificateExpiredException/), [CertificateNotYetValidException](/Java/CertificateNotYetValidException/)

## Clase Padre
[X509Certificate](/Java/X509Certificate-java-security-cert/)

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
