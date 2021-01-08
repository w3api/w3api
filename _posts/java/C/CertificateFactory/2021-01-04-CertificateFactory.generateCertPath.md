---
title: CertificateFactory.generateCertPath()
permalink: Java/CertificateFactory/generateCertPath
date: 2021-01-04
key: JavaJava.C.CertificateFactory
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactory.metodos valor="generateCertPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final CertPath generateCertPath(InputStream inStream) throws CertificateException
public final CertPath generateCertPath(InputStream inStream, String encoding) throws CertificateException
public final CertPath generateCertPath(List<? extends Certificate> certificates) throws CertificateException
~~~

## Parámetros
* **List&lt;? extends Certificate&gt; certificates**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends Certificate> certificates" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_data parametro="String encoding" %}
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inStream" %}

## Excepciones
[CertificateException](/Java/CertificateException/)

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
