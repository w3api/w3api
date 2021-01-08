---
title: X509ExtendedTrustManager.checkServerTrusted()
permalink: Java/X509ExtendedTrustManager/checkServerTrusted
date: 2021-01-04
key: JavaJava.X.X509ExtendedTrustManager
category: java
tags: ['java se', 'javax.net.ssl', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509ExtendedTrustManager.metodos valor="checkServerTrusted" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void checkServerTrusted(X509Certificate[] chain, String authType, Socket socket) throws CertificateException
public abstract void checkServerTrusted(X509Certificate[] chain, String authType, SSLEngine engine) throws CertificateException
~~~

## Parámetros
* **SSLEngine engine**,  {% include w3api/param_description.html metodo=_data parametro="SSLEngine engine" %}
* **X509Certificate[] chain**,  {% include w3api/param_description.html metodo=_data parametro="X509Certificate[] chain" %}
* **String authType**,  {% include w3api/param_description.html metodo=_data parametro="String authType" %}
* **Socket socket**,  {% include w3api/param_description.html metodo=_data parametro="Socket socket" %}

## Excepciones
[CertificateException](/Java/CertificateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[X509ExtendedTrustManager](/Java/X509ExtendedTrustManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.X509ExtendedTrustManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
