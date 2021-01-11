---
title: X509TrustManager.checkClientTrusted()
permalink: Java/X509TrustManager/checkClientTrusted
date: 2021-01-11
key: JavaJava.X.X509TrustManager
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509TrustManager.metodos valor="checkClientTrusted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void checkClientTrusted(X509Certificate[] chain, String authType) throws CertificateException
~~~

## Parámetros
* **X509Certificate[] chain**,  {% include w3api/param_description.html metodo=_dato parametro="X509Certificate[] chain" %}
* **String authType**,  {% include w3api/param_description.html metodo=_dato parametro="String authType" %}

## Excepciones
[CertificateException](/Java/CertificateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[X509TrustManager](/Java/X509TrustManager/)

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
