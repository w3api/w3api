---
title: X509Certificate.verify()
permalink: Java/X509Certificate-java-security-cert/verify
date: 2021-01-04
key: JavaJava.X.X509Certificate-java-security-cert
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.X509Certificate-java-security-cert.metodos valor="verify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void verify(PublicKey key, Provider sigProvider) throws CertificateException, NoSuchAlgorithmException, InvalidKeyException, SignatureException
~~~

## Parámetros
* **Provider sigProvider**,  {% include w3api/param_description.html metodo=_data parametro="Provider sigProvider" %}
* **PublicKey key**,  {% include w3api/param_description.html metodo=_data parametro="PublicKey key" %}

## Excepciones
[CertificateException](/Java/CertificateException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [SignatureException](/Java/SignatureException/), [InvalidKeyException](/Java/InvalidKeyException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[X509Certificate](/Java/X509Certificate-java-security-cert/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.X.X509Certificate-java-security-cert.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
