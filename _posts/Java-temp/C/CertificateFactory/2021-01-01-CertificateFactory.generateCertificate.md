---
title: CertificateFactory.generateCertificate()
permalink: /Java/CertificateFactory/generateCertificate/
date: 2021-01-11
key: Java.C.CertificateFactory
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactory.metodos valor="generateCertificate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final Certificate generateCertificate(InputStream inStream) throws CertificateException
~~~

## Parámetros
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inStream" %}

## Excepciones
[CertificateException](/Java/CertificateException/)

## Clase Padre
[CertificateFactory](/Java/CertificateFactory/)

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
