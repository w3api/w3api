---
title: X509Certificate.getInstance()
permalink: Java/X509Certificate-javax-security-cert/getInstance
date: 2021-01-04
key: JavaJava.X.X509Certificate-javax-security-cert
category: java
tags: ['java se', 'javax.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509Certificate-javax-security-cert.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static X509Certificate getInstance(byte[] certData)
static X509Certificate getInstance(InputStream inStream)
~~~

## Parámetros
* **byte[] certData**,  {% include w3api/param_description.html metodo=_data parametro="byte[] certData" %}
* **InputStream inStream**,  {% include w3api/param_description.html metodo=_data parametro="InputStream inStream" %}

## Clase Padre
[X509Certificate](/Java/X509Certificate-javax-security-cert/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.X509Certificate-javax-security-cert.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
