---
title: Certificate.verify()
permalink: Java/Certificate-javax-security-cert/verify
date: 2021-01-04
key: JavaJava.C.Certificate-javax-security-cert
category: java
tags: ['java se', 'javax.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Certificate-javax-security-cert.metodos valor="verify" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void verify(PublicKey key) throws CertificateException, NoSuchAlgorithmException, InvalidKeyException, NoSuchProviderException, SignatureException
public abstract void verify(PublicKey key, String sigProvider) throws CertificateException, NoSuchAlgorithmException, InvalidKeyException, NoSuchProviderException, SignatureException
~~~

## Parámetros
* **String sigProvider**,  {% include w3api/param_description.html metodo=_data parametro="String sigProvider" %}
* **PublicKey key**,  {% include w3api/param_description.html metodo=_data parametro="PublicKey key" %}

## Excepciones
[CertificateException](/Java/CertificateException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [SignatureException](/Java/SignatureException/), [InvalidKeyException](/Java/InvalidKeyException/), [NoSuchProviderException](/Java/NoSuchProviderException/)

## Clase Padre
[Certificate](/Java/Certificate-javax-security-cert/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Certificate-javax-security-cert.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
