---
title: Certificate.verify()
permalink: Java/Certificate-java-security-cert/verify
date: 2021-01-11
key: JavaJava.C.Certificate-java-security-cert
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Certificate-java-security-cert.metodos valor="verify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void verify(PublicKey key) throws CertificateException, NoSuchAlgorithmException, InvalidKeyException, NoSuchProviderException, SignatureException
public abstract void verify(PublicKey key, String sigProvider) throws CertificateException, NoSuchAlgorithmException, InvalidKeyException, NoSuchProviderException, SignatureException
public void verify(PublicKey key, Provider sigProvider) throws CertificateException, NoSuchAlgorithmException, InvalidKeyException, SignatureException
~~~

## Parámetros
* **String sigProvider**,  {% include w3api/param_description.html metodo=_dato parametro="String sigProvider" %}
* **PublicKey key**,  {% include w3api/param_description.html metodo=_dato parametro="PublicKey key" %}
* **Provider sigProvider**,  {% include w3api/param_description.html metodo=_dato parametro="Provider sigProvider" %}

## Excepciones
[NoSuchProviderException](/Java/NoSuchProviderException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [CertificateException](/Java/CertificateException/), [SignatureException](/Java/SignatureException/), [InvalidKeyException](/Java/InvalidKeyException/)

## Clase Padre
[Certificate](/Java/Certificate-java-security-cert/)

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
