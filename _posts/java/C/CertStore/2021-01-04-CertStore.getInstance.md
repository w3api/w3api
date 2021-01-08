---
title: CertStore.getInstance()
permalink: Java/CertStore/getInstance
date: 2021-01-04
key: JavaJava.C.CertStore
category: java
tags: ['java se', 'java.security.cert', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CertStore.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static CertStore getInstance(String type, CertStoreParameters params) throws InvalidAlgorithmParameterException, NoSuchAlgorithmException
public static CertStore getInstance(String type, CertStoreParameters params, String provider) throws InvalidAlgorithmParameterException, NoSuchAlgorithmException, NoSuchProviderException
public static CertStore getInstance(String type, CertStoreParameters params, Provider provider) throws NoSuchAlgorithmException, InvalidAlgorithmParameterException
~~~

## Parámetros
* **Provider provider**,  {% include w3api/param_description.html metodo=_data parametro="Provider provider" %}
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}
* **CertStoreParameters params**,  {% include w3api/param_description.html metodo=_data parametro="CertStoreParameters params" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [InvalidAlgorithmParameterException](/Java/InvalidAlgorithmParameterException/), [NullPointerException](/Java/NullPointerException/), [NoSuchProviderException](/Java/NoSuchProviderException/)

## Clase Padre
[CertStore](/Java/CertStore/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CertStore.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
