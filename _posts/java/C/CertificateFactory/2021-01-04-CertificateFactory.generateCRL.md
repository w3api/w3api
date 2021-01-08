---
title: CertificateFactory.generateCRL()
permalink: Java/CertificateFactory/generateCRL
date: 2021-01-04
key: JavaJava.C.CertificateFactory
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactory.metodos valor="generateCRL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CRL generateCRL(InputStream inStream) throws CRLException
~~~

## Parámetros
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inStream" %}

## Excepciones
[CRLException](/Java/CRLException/)

## Clase Padre
[CertificateFactory](/Java/CertificateFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertificateFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
