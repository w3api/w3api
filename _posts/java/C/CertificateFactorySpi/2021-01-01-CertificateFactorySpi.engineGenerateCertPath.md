---
title: CertificateFactorySpi.engineGenerateCertPath()
permalink: /Java/CertificateFactorySpi/engineGenerateCertPath/
date: 2021-01-11
key: Java.C.CertificateFactorySpi
category: Java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertificateFactorySpi.metodos valor="engineGenerateCertPath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CertPath engineGenerateCertPath(InputStream inStream) throws CertificateException
public CertPath engineGenerateCertPath(InputStream inStream, String encoding) throws CertificateException
public CertPath engineGenerateCertPath(List<? extends Certificate> certificates) throws CertificateException
~~~

## Parámetros
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream inStream" %}
* **List&lt;? extends Certificate&gt; certificates**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends Certificate> certificates" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}

## Excepciones
[CertificateException](/Java/CertificateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[CertificateFactorySpi](/Java/CertificateFactorySpi/)

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
